from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName


hyperrogue_base_id: int = 0xCBA000


class HyperrogueItem(Item):
    game = "Hyperrogue"


class HyperrogueItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

land_item_table: Dict[str, HyperrogueItemData] = {
    ItemName.ice_diamond:           HyperrogueItemData(hyperrogue_base_id + 0x00, ItemClassification.progression_skip_balancing),
    ItemName.gold:                  HyperrogueItemData(hyperrogue_base_id + 0x01, ItemClassification.progression_skip_balancing),
    ItemName.spice:                 HyperrogueItemData(hyperrogue_base_id + 0x02, ItemClassification.progression_skip_balancing),
    ItemName.ruby:                  HyperrogueItemData(hyperrogue_base_id + 0x03, ItemClassification.progression_skip_balancing),
    ItemName.elixir_of_life:        HyperrogueItemData(hyperrogue_base_id + 0x04, ItemClassification.progression_skip_balancing),
    ItemName.shard:                 HyperrogueItemData(hyperrogue_base_id + 0x05, ItemClassification.progression_skip_balancing),
    ItemName.necromancers_totem:    HyperrogueItemData(hyperrogue_base_id + 0x06, ItemClassification.progression_skip_balancing),
    ItemName.demon_daisy:           HyperrogueItemData(hyperrogue_base_id + 0x07, ItemClassification.progression_skip_balancing),
    ItemName.statue_of_cthulhu:     HyperrogueItemData(hyperrogue_base_id + 0x08, ItemClassification.progression_skip_balancing),
    ItemName.phoenix_feather:       HyperrogueItemData(hyperrogue_base_id + 0x09, ItemClassification.progression_skip_balancing),
    ItemName.ice_sapphire:          HyperrogueItemData(hyperrogue_base_id + 0x0A, ItemClassification.progression_skip_balancing),
    ItemName.fern_flower:           HyperrogueItemData(hyperrogue_base_id + 0x0B, ItemClassification.progression_skip_balancing),
    ItemName.wine:                  HyperrogueItemData(hyperrogue_base_id + 0x0C, ItemClassification.progression_skip_balancing),
    ItemName.silver:                HyperrogueItemData(hyperrogue_base_id + 0x0D, ItemClassification.progression_skip_balancing),
    ItemName.royal_jelly:           HyperrogueItemData(hyperrogue_base_id + 0x0E, ItemClassification.progression_skip_balancing),
    ItemName.emerald:               HyperrogueItemData(hyperrogue_base_id + 0x0F, ItemClassification.progression_skip_balancing),
    ItemName.powerstone:            HyperrogueItemData(hyperrogue_base_id + 0x10, ItemClassification.progression_skip_balancing),
    ItemName.holy_grail:            HyperrogueItemData(hyperrogue_base_id + 0x11, ItemClassification.progression_skip_balancing),
    ItemName.grimoire:              HyperrogueItemData(hyperrogue_base_id + 0x12, ItemClassification.progression_skip_balancing),
    ItemName.pirate_treasure:       HyperrogueItemData(hyperrogue_base_id + 0x13, ItemClassification.progression_skip_balancing),
    ItemName.red_gem:               HyperrogueItemData(hyperrogue_base_id + 0x14, ItemClassification.progression_skip_balancing),
    ItemName.bomberbird_egg:        HyperrogueItemData(hyperrogue_base_id + 0x15, ItemClassification.progression_skip_balancing),
    ItemName.amber:                 HyperrogueItemData(hyperrogue_base_id + 0x16, ItemClassification.progression_skip_balancing),
    ItemName.pearl:                 HyperrogueItemData(hyperrogue_base_id + 0x17, ItemClassification.progression_skip_balancing),
    ItemName.hypersian_rug:         HyperrogueItemData(hyperrogue_base_id + 0x18, ItemClassification.progression_skip_balancing),
    ItemName.garnet:                HyperrogueItemData(hyperrogue_base_id + 0x19, ItemClassification.progression_skip_balancing),
    ItemName.ivory_figurine:        HyperrogueItemData(hyperrogue_base_id + 0x1A, ItemClassification.progression_skip_balancing),
    ItemName.onyx:                  HyperrogueItemData(hyperrogue_base_id + 0x1B, ItemClassification.progression_skip_balancing),
    ItemName.elemental_gem:         HyperrogueItemData(hyperrogue_base_id + 0x1C, ItemClassification.progression_skip_balancing),
    ItemName.fulgurite:             HyperrogueItemData(hyperrogue_base_id + 0x1D, ItemClassification.progression_skip_balancing),
    ItemName.mutant_sapling:        HyperrogueItemData(hyperrogue_base_id + 0x1E, ItemClassification.progression_skip_balancing),
    ItemName.mutant_fruit:          HyperrogueItemData(hyperrogue_base_id + 0x1F, ItemClassification.progression_skip_balancing),
    ItemName.black_lotus:           HyperrogueItemData(hyperrogue_base_id + 0x20, ItemClassification.progression_skip_balancing),
    ItemName.white_dove_feather:    HyperrogueItemData(hyperrogue_base_id + 0x21, ItemClassification.progression_skip_balancing),
    ItemName.thornless_rose:        HyperrogueItemData(hyperrogue_base_id + 0x22, ItemClassification.progression_skip_balancing),
    ItemName.coral:                 HyperrogueItemData(hyperrogue_base_id + 0x23, ItemClassification.progression_skip_balancing),
    ItemName.baby_tortoise:         HyperrogueItemData(hyperrogue_base_id + 0x24, ItemClassification.progression_skip_balancing),
    ItemName.apple:                 HyperrogueItemData(hyperrogue_base_id + 0x25, ItemClassification.progression_skip_balancing),
    ItemName.dragon_scale:          HyperrogueItemData(hyperrogue_base_id + 0x26, ItemClassification.progression_skip_balancing),
    ItemName.sunken_treasure:       HyperrogueItemData(hyperrogue_base_id + 0x27, ItemClassification.progression_skip_balancing),
    ItemName.ancient_jewelry:       HyperrogueItemData(hyperrogue_base_id + 0x28, ItemClassification.progression_skip_balancing),
    ItemName.golden_egg:            HyperrogueItemData(hyperrogue_base_id + 0x29, ItemClassification.progression_skip_balancing),
    ItemName.slime_mold:            HyperrogueItemData(hyperrogue_base_id + 0x2A, ItemClassification.progression_skip_balancing),
    ItemName.amethyst:              HyperrogueItemData(hyperrogue_base_id + 0x2B, ItemClassification.progression_skip_balancing),
    ItemName.dodecahedron:          HyperrogueItemData(hyperrogue_base_id + 0x2C, ItemClassification.progression_skip_balancing),
    ItemName.green_grass:           HyperrogueItemData(hyperrogue_base_id + 0x2D, ItemClassification.progression_skip_balancing),
    ItemName.spinel:                HyperrogueItemData(hyperrogue_base_id + 0x2E, ItemClassification.progression_skip_balancing),
    ItemName.lava_lily:             HyperrogueItemData(hyperrogue_base_id + 0x2F, ItemClassification.progression_skip_balancing),
    ItemName.turquoise:             HyperrogueItemData(hyperrogue_base_id + 0x30, ItemClassification.progression_skip_balancing),
    ItemName.forgotten_relic:       HyperrogueItemData(hyperrogue_base_id + 0x31, ItemClassification.progression_skip_balancing),
    ItemName.ancient_weapon:        HyperrogueItemData(hyperrogue_base_id + 0x32, ItemClassification.progression_skip_balancing),
    ItemName.chrysoberyl:           HyperrogueItemData(hyperrogue_base_id + 0x33, ItemClassification.progression_skip_balancing),
    ItemName.tasty_jelly:           HyperrogueItemData(hyperrogue_base_id + 0x34, ItemClassification.progression_skip_balancing),
    ItemName.tigers_eye:            HyperrogueItemData(hyperrogue_base_id + 0x35, ItemClassification.progression_skip_balancing),
    ItemName.meteorite:             HyperrogueItemData(hyperrogue_base_id + 0x36, ItemClassification.progression_skip_balancing),
    ItemName.torbernite:            HyperrogueItemData(hyperrogue_base_id + 0x37, ItemClassification.progression_skip_balancing),
    ItemName.water_lily:            HyperrogueItemData(hyperrogue_base_id + 0x38, ItemClassification.progression_skip_balancing),
    ItemName.gold_ball:             HyperrogueItemData(hyperrogue_base_id + 0x39, ItemClassification.progression_skip_balancing),
    ItemName.lazurite_figurine:     HyperrogueItemData(hyperrogue_base_id + 0x3A, ItemClassification.progression_skip_balancing),
    ItemName.capon_stone:           HyperrogueItemData(hyperrogue_base_id + 0x3B, ItemClassification.progression_skip_balancing),
    ItemName.crystal_die:           HyperrogueItemData(hyperrogue_base_id + 0x3C, ItemClassification.progression_skip_balancing),
}

# Nonstandard Lands
nonstandard_land_item_table: Dict[str, HyperrogueItemData] = {
    ItemName.bounty:                HyperrogueItemData(hyperrogue_base_id + 0x50, ItemClassification.progression_skip_balancing),
    ItemName.treat:                 HyperrogueItemData(hyperrogue_base_id + 0x51, ItemClassification.progression_skip_balancing),
    ItemName.glowing_crystal:       HyperrogueItemData(hyperrogue_base_id + 0x52, ItemClassification.progression_skip_balancing),
    ItemName.snake_oil:             HyperrogueItemData(hyperrogue_base_id + 0x53, ItemClassification.progression_skip_balancing),
    ItemName.sea_glass:             HyperrogueItemData(hyperrogue_base_id + 0x54, ItemClassification.progression_skip_balancing),
    ItemName.fuel:                  HyperrogueItemData(hyperrogue_base_id + 0x55, ItemClassification.progression_skip_balancing),
}

#collectable_item_data_table: Dict[str, HyperrogueItemData] = {
#    ItemName.strawberry: HyperrogueItemData(hyperrogue_base_id + 0x00, ItemClassification.progression_skip_balancing),
#    ItemName.raspberry:  HyperrogueItemData(hyperrogue_base_id + 0x9, ItemClassification.filler),
#}

#unlockable_item_data_table: Dict[str, HyperrogueItemData] = {
#    ItemName.dash_refill:        HyperrogueItemData(hyperrogue_base_id + 0x1, ItemClassification.progression),
#    ItemName.double_dash_refill: HyperrogueItemData(hyperrogue_base_id + 0x2, ItemClassification.progression),
#    ItemName.feather:            HyperrogueItemData(hyperrogue_base_id + 0x3, ItemClassification.progression),
#    ItemName.coin:               HyperrogueItemData(hyperrogue_base_id + 0x4, ItemClassification.progression),
#    ItemName.cassette:           HyperrogueItemData(hyperrogue_base_id + 0x5, ItemClassification.progression),
#    ItemName.traffic_block:      HyperrogueItemData(hyperrogue_base_id + 0x6, ItemClassification.progression),
#    ItemName.spring:             HyperrogueItemData(hyperrogue_base_id + 0x7, ItemClassification.progression),
#    ItemName.breakables:         HyperrogueItemData(hyperrogue_base_id + 0x8, ItemClassification.progression),
#}

#move_item_data_table: Dict[str, HyperrogueItemData] = {
#    ItemName.ground_dash: HyperrogueItemData(hyperrogue_base_id + 0xA, ItemClassification.progression),
#    ItemName.air_dash:    HyperrogueItemData(hyperrogue_base_id + 0xB, ItemClassification.progression),
#    ItemName.skid_jump:   HyperrogueItemData(hyperrogue_base_id + 0xC, ItemClassification.progression),
#    ItemName.climb:       HyperrogueItemData(hyperrogue_base_id + 0xD, ItemClassification.progression),
#}

item_data_table: Dict[str, HyperrogueItemData] = {**land_item_table, **nonstandard_land_item_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
