from copy import deepcopy
from typing import Dict, List

from BaseClasses import ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import HyperrogueItem, land_item_table, nonstandard_land_item_table, item_data_table, item_table
from .Locations import HyperrogueLocation,\
    unlock_location_data_table, standard_location_data_table, nonstandard_location_data_table, location_table
from .Names import ItemName, LocationName
from .Options import HyperrogueOptions, hyperrogue_option_groups


class HyperrogueWebWorld(WebWorld):
    theme = "ice"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Hyperrogue in Archipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["melwei","Joachim Gauck"]
    )

    tutorials = [setup_en]

    option_groups = hyperrogue_option_groups


class HyperrogueWorld(World):
    """A tactical puzzle/roguelike on a hyperbolic plane."""

    # Class Data
    game = "Hyperrogue"
    web = HyperrogueWebWorld()
    options_dataclass = HyperrogueOptions
    options: HyperrogueOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    # Instance Data
    strawberries_required: int
    active_logic_mapping: Dict[str, List[List[str]]]
    goal_logic_mapping: Dict[str, List[List[str]]]


    def create_item(self, name: str) -> HyperrogueItem:
        # Only make required amount of strawberries be Progression
        classification: ItemClassification = ItemClassification.filler
        self.prog = getattr(self, "prog", {})
        if self.prog.get(name,0) == 0:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.useful
        self.prog[name] = self.prog.get(name,0)+1
        return HyperrogueItem(name, classification, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[HyperrogueItem] = []

        location_count: int = len(unlock_location_data_table)*4

        item_pool += [self.create_item(name)
                      for name in land_item_table.keys()
                      if name not in self.options.start_inventory]
        
        for _ in range(3):
            item_pool += [self.create_item(name)
                      for name in land_item_table.keys()]
        
        #filler_item_count: int = location_count - len(item_pool)
        #item_pool += [self.create_item(ItemName.raspberry) for _ in range(filler_item_count)]

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        from .Regions import region_data_table
        for region_name in region_data_table.keys():
            if not region_name=="Non-Sea Great Wall":
                if "Non-Sea Great Wall" in region_data_table[region_name].connecting_regions:
                    region_data_table["Non-Sea Great Wall"] += [region_name]

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in standard_location_data_table.items()
                if location_data.region == region_name
            }, HyperrogueLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

    def get_filler_item_name(self) -> str:
        return "Nothing"


    def set_rules(self) -> None:
        from .Rules import set_rules
        set_rules(self)


    def fill_slot_data(self):
        return {
            "death_link": self.options.death_link.value,
#            "death_link_amnesty": self.options.death_link_amnesty.value,
#            "strawberries_required": self.strawberries_required,
#            "move_shuffle": self.options.move_shuffle.value,
#            "friendsanity": self.options.friendsanity.value,
#            "signsanity": self.options.signsanity.value,
#            "carsanity": self.options.carsanity.value,
#            "badeline_chaser_source": self.options.badeline_chaser_source.value,
#            "badeline_chaser_frequency": self.options.badeline_chaser_frequency.value,
#            "badeline_chaser_speed": self.options.badeline_chaser_speed.value,
        }
