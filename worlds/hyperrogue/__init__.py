from copy import deepcopy
from typing import Callable, Dict, List

from BaseClasses import CollectionState, Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.hyperrogue.Webinterface import HyperrogueWebWorld
from .Options import HyperrogueOptions
from .Lands import landtable, landlist
from .Regions import *
from .Rules import *

hyperrogue_base_id = 0xCBA000

# Contains every suffix for the type of location and its corresponding base id
location_suffixes: Dict[str,int] = {
        "Unlock":       0x000, 
        "10 Treasures": 0x100, 
        "25 Treasures": 0x200, 
        "50 Treasures": 0x300
}

class HyperrogueWorld(World):
    """A tactical puzzle/roguelike on a hyperbolic plane."""

    options_dataclass = HyperrogueOptions
    options: HyperrogueOptions

    game = "Hyperrogue"

    item_name_to_id = {**{land_name : land_id + hyperrogue_base_id
                       for land_name, land_id in landtable.items()},
                       **{"Crossroads" : hyperrogue_base_id - 1}}
    
    # Assigns to each land the number of already created items for that land:
    # This is relevant, as (except for R'Lyeh + Temple of Cthulhu) exactly the first check
    # in each land is relevant for progression.
    item_creation_progress: Dict[str,int] = {land_name : 0
                                             for land_name in landlist}
    
    location_name_to_id = {f"{land_name} {suff}" : land_id + hyperrogue_base_id + suff_id
                                    for land_name, land_id in landtable.items()
                                    for suff, suff_id in location_suffixes.items()}
    
    web = HyperrogueWebWorld()

    def generate_early(self) -> None:
        # Exclude high treasure locations from the game depending on settings
        if self.options.treasure_requirements<50:
            del location_suffixes["50 Treasures"]
        if self.options.treasure_requirements<25:
            del location_suffixes["25 Treasures"]
        pass

    def create_regions(self) -> None:
        # Create regions and add them to the multiworld
        self.multiworld.regions.extend(Region(region_name, self.player, self.multiworld) 
                                       for region_name in regionlist)
        
        # Add progress locations to land regions
        for land_name in landlist:
            land: Region =  self.multiworld.get_region(land_name,self.player)
            land.add_locations({
                f"{land_name} {suff}" : self.location_name_to_id[f"{land_name} {suff}"]
                for suff in location_suffixes.keys()
                if not suff == "Unlock" # "Unlock" locations belong to the menu region instead
            })
        
        # Add unlock locations to the menu region
        menu: Region = self.multiworld.get_region("Menu", self.player)
        menu.add_locations({
            f"{land_name} Unlock" : self.location_name_to_id[f"{land_name} Unlock"]
            for land_name in landlist
        })

        # Add a crossroads location for initialization purposes
        menu.add_locations({
            "Crossroads" : hyperrogue_base_id - 1
        })

        # Add connections according to the region_connections dictionary
        for region_name, connecting_regions in region_connections.items():
            region = self.multiworld.get_region(region_name,self.player)
            for target_region_name in connecting_regions:
                target_region = self.multiworld.get_region(target_region_name,self.player)
                region.connect(target_region,None,get_basic_access_rule(target_region_name,self.player))
                # Add reverse direction for connections to "Non-Sea Great Wall",
                # as these are not listed in region_connections
                if target_region_name == "Non-Sea Great Wall":
                    target_region.connect(region,None,get_basic_access_rule(region_name,self.player))
        
        # R'Lyeh completion allows R'Lyeh to spawn on land
        rLyeh = self.multiworld.get_region("R'Lyeh",self.player)
        nSGW = self.multiworld.get_region("Non-Sea Great Wall",self.player)
        rLyeh.connect(nSGW, None, lambda state: 
                      state.has("R'Lyeh", self.player, 2) or state.has("Temple of Cthulhu", self.player, 2))
        nSGW.connect(rLyeh, None, lambda state: 
                     state.has("R'Lyeh", self.player, 2) or state.has("Temple of Cthulhu", self.player, 2)
                     and get_basic_access_rule("R'Lyeh",self.player))
        

    
    def create_item(self, name: str) -> Item:
        # R'Lyeh 10 Treasures and Temple of Cthulhu 10 Treasures are progression relevant,
        # as they allow R'Lyeh to spawn on land
        relevant_progress = 2 if name in ["R'Lyeh", "Temple of Cthulhu"] else 1
        self.item_creation_progress[name] += 1
        if self.item_creation_progress[name] <= relevant_progress:
            return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        else:
            return Item(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        self.multiworld.itempool += [self.create_item(land_name)
                                     for land_name in landlist
                                     for suff in location_suffixes.keys()]
        # Add Crossroads item and lock it into Crossroads location for initialization purposes
        cr : Item = Item("Crossroads", ItemClassification.progression_skip_balancing, hyperrogue_base_id - 1, self.player)
        self.get_location("Crossroads").place_locked_item(cr)
        self.multiworld.push_precollected(cr)
        
    def set_rules(self) -> None:
        # Add Location Rules
        unlock_locations: Dict[str, Location] = {land_name : self.get_location(f"{land_name} Unlock")
                                                 for land_name in landlist}
        for land_name, loc in unlock_locations.items():
            loc.access_rule = get_location_unlock_rule(land_name, self.player)
        
        # Add Goal Rule
        self.multiworld.completion_condition[self.player] = get_completion_rule(self.player)

    def fill_slot_data(self):
        return {
            "death_link": self.options.death_link.value,
            "goal": self.options.goal.value,
            "starting_land": self.options.starting_land.value
        }


        
        

    

    


