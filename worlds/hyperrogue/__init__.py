from random import choice
from math import ceil
from copy import deepcopy
from typing import Callable, Dict, List

from BaseClasses import CollectionState, Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Webinterface import HyperrogueWebWorld
from .Options import HyperrogueOptions
from .Names import landtable, landlist, orbtable, orblist
from .Regions import *
from .Rules import *

hyperrogue_base_id = 0xCBA000

# Contains every suffix for the type of location and its corresponding base id
location_suffixes: Dict[str,int] = {
        "Unlock":               0x000, 
        "10 Treasures":         0x100, 
        "25 Treasures":         0x200, 
        "50 Treasures":         0x300,
        "10 Treasures Extra":   0x400,
        "25 Treasures Extra":   0x500,
        "50 Treasures Extra":   0x600,
}


class HyperrogueItem(Item):
    game="Hyperrogue"

class HyperrogueWorld(World):
    """A tactical puzzle/roguelike on a hyperbolic plane."""

    options_dataclass = HyperrogueOptions
    options: HyperrogueOptions

    game = "Hyperrogue"

    item_name_to_id = {**{land_name : land_id + hyperrogue_base_id
                    for land_name, land_id in landtable.items()},
                    **{"Crossroads" : hyperrogue_base_id - 1},
                    **{"Nothing" : hyperrogue_base_id - 2},
                    **{orb_name : orb_id + hyperrogue_base_id + 0x1000
                       for orb_name, orb_id in orbtable.items()}}
    location_name_to_id = {f"{land_name} {suff}" : land_id + hyperrogue_base_id + suff_id
                                    for land_name, land_id in landtable.items()
                                    for suff, suff_id in location_suffixes.items()}
    
    active_location_suffixes = {}

    web = HyperrogueWebWorld()

    def __init__(self, multiworld, player):
        # Assigns to each land the number of already created items for that land:
        # This is relevant, as on hard logic (except for R'Lyeh + Temple of Cthulhu) exactly the first check
        # in each land is relevant for progression.
        self.item_creation_progress = {land_name : 0
                                        for land_name in landlist}
        
        super().__init__(multiworld, player)
        
        
    def generate_early(self) -> None:
        self.active_location_suffixes = deepcopy(location_suffixes)
        # Exclude high treasure locations from the game depending on settings
        if self.options.treasure_requirements.value<50:
            del self.active_location_suffixes["50 Treasures"]
        if self.options.treasure_requirements.value<25:
            del self.active_location_suffixes["25 Treasures"]
        if not self.options.extra_location_10.value:
            del self.active_location_suffixes["10 Treasures Extra"]
        if not self.options.extra_location_25.value:
            del self.active_location_suffixes["25 Treasures Extra"]
        if not self.options.extra_location_50.value:
            del self.active_location_suffixes["50 Treasures Extra"]
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
                for suff in self.active_location_suffixes.keys()
                if not suff == "Unlock" # "Unlock" locations belong to the menu region instead
            })
        
        # Add unlock locations to the menu region
        menu: Region = self.multiworld.get_region("Menu", self.player)
        menu.add_locations({
            f"{land_name} Unlock" : self.location_name_to_id[f"{land_name} Unlock"]
            for land_name in landlist
        })

        # Add connections according to the region_connections dictionary
        for region_name, connecting_regions in region_connections.items():
            region = self.multiworld.get_region(region_name,self.player)
            for target_region_name in connecting_regions:
                target_region = self.multiworld.get_region(target_region_name,self.player)
                region.connect(target_region, None, get_basic_access_rule(target_region_name))
                # Add reverse direction for connections to "Non-Sea Great Wall",
                # as these are not listed in region_connections
                if target_region_name == "Non-Sea Great Wall":
                    target_region.connect(region, None, get_basic_access_rule(region_name))
        
        # R'Lyeh completion allows R'Lyeh to spawn on land
        rLyeh = self.multiworld.get_region("R'Lyeh",self.player)
        nSGW = self.multiworld.get_region("Non-Sea Great Wall",self.player)
        rLyeh.connect(nSGW, None, Has("R'Lyeh", 2) | Has("Temple of Cthulhu", 2))
        nSGW.connect(rLyeh, None, Has("R'Lyeh", 2) | ( Has("Temple of Cthulhu", 2) & get_basic_access_rule("R'Lyeh")))
        

    
    def create_item(self, name: str) -> HyperrogueItem:
        id = self.item_name_to_id[name]
        if (name=="Crossroads"):
            return HyperrogueItem("Crossroads", ItemClassification.progression_skip_balancing, id, player=self.player)
        if (name=="Nothing"):
            return HyperrogueItem("Nothing", ItemClassification.filler, id, player=self.player)
        if name in landlist:
            # R'Lyeh 10 Treasures and Temple of Cthulhu 10 Treasures are progression relevant,
            # as they allow R'Lyeh to spawn on land
            relevant_progress = 2 if name in ["R'Lyeh", "Temple of Cthulhu"] or self.options.logic_difficulty == 0 else 1
            self.item_creation_progress[name] += 1
            if self.item_creation_progress[name] <= relevant_progress:
                return HyperrogueItem(name, ItemClassification.progression, id, player=self.player)
            else:
                return HyperrogueItem(name, ItemClassification.useful, id, player=self.player)
        if name in orblist:
            return HyperrogueItem(name, ItemClassification.useful, id, player=self.player)


    def create_items(self) -> None:
        self.multiworld.itempool += [self.create_item(land_name)
                                     for land_name in landlist
                                     for suff in self.active_location_suffixes.keys()]
        
        num_fill = len(landlist)*(int(self.options.extra_location_10.value) + int(self.options.extra_location_25.value) + int(self.options.extra_location_50.value))
        num_start_orbs = ceil(num_fill * self.options.start_orb_fill_percentage * 1/100)
        self.multiworld.itempool += [self.create_item(self.random_orb())
                                     for i in range(num_start_orbs)]

        num_fill -= num_start_orbs
        self.multiworld.itempool += [self.create_item("Nothing")
                                     for i in range(num_fill)]

        # Add Crossroads item and lock it into Crossroads location for initialization purposes
        cr : HyperrogueItem = self.create_item("Crossroads")
        self.multiworld.push_precollected(cr)
    
    def random_orb(self):
        return choice(list(orblist))

    def set_rules(self) -> None:
        # Add Location Rules
        locations: Dict[str, Dict[str, Location]] = {land_name : {suffix : self.get_location(f"{land_name} {suffix}") 
                                                                  for suffix in self.active_location_suffixes}
                                                 for land_name in landlist}
        for land_name, locs in locations.items():
            for suffix, loc in locs.items():
                self.set_rule(loc, get_location_rule(land_name, suffix))
        
        # Add Goal Rule
        self.set_completion_rule(get_completion_rule())

    def fill_slot_data(self):
        return {
            "death_link": self.options.death_link.value,
            "goal": self.options.goal.value,
            "starting_land": self.options.starting_land.value,
            "treasure_requirements": self.options.treasure_requirements.value,
            "hint_orb": self.options.hint_orb.value,
            "extra_location_10" : self.options.extra_location_10.value,
            "extra_location_25" : self.options.extra_location_25.value,
            "extra_location_50" : self.options.extra_location_50.value
        }


        
        

    

    


