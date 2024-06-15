from copy import deepcopy
from typing import Callable, Dict, List

from BaseClasses import CollectionState, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.hyperrogue.Webinterface import HyperrogueWebWorld
from worlds.zork_grand_inquisitor.data_funcs import location_names_to_id
from .Options import HyperrogueOptions
from .Lands import landtable
from .Regions import *
from .Rules import *

hyperrogue_base_id = 0xCBA00000

location_suffixes: List[str] = ["Unlock", "10 Treasures", "25 Treasures", "50 Treasures"]

class HyperrogueWorld(World):
    """A tactical puzzle/roguelike on a hyperbolic plane."""

    options_dataclass = HyperrogueOptions
    options: HyperrogueOptions

    game = "Hyperrogue"

    item_name_to_id = {land_name : land_id + hyperrogue_base_id
                       for land_name, land_id in landtable.items()}
    
    location_name_to_id = {}
    location_name_to_id.update({f"{land_name} {suff}" : land_id + hyperrogue_base_id
                                    for land_name, land_id in landtable.items()
                                    for suff in location_suffixes})
    
    web = HyperrogueWebWorld()

    def generate_early(self) -> None:
        init_basic_access_rules(self.player)

    def create_regions(self) -> None:
        self.multiworld.regions.extend(Region(region_name, self.player, self.multiworld) 
                                       for region_name in regionlist)
        for region_name, connecting_regions in region_connections.items():
            region = self.multiworld.get_region(region_name,self.player)

            for target_region_name in connecting_regions:
                target_region = self.multiworld.get_region(target_region_name,self.player)
                region.connect(target_region,basic_access_rules[target_region_name])
                if target_region_name == "Non-Sea Great Wall":
                    target_region.connect(region,basic_access_rules[region_name])
        rLyeh = self.multiworld.get_region("R'Lyeh",self.player)
        nSGW = self.multiworld.get_region("Non-Sea Great Wall",self.player)
        rLyehComplete: Rule = lambda state: state.has("R'Lyeh", self.player, 2) or state.has("Temple of Cthulhu", self.player, 2)
        rLyeh.connect(nSGW, rLyehComplete)
        nSGW.connect(rLyeh, rLyehComplete or basic_access_rules["R'Lyeh"])

    def fill_slot_data(self):
        return {
            "death_link": self.options.death_link.value,
        }


        
        

    

    


