from dataclasses import dataclass
from Options import Choice, DeathLink, PerGameCommonOptions

class Goal(Choice):
    """
    The goal required to complete the game for Archipelago.

    10 Hyperstones: Collect 10 Hyperstones.

    50 Hyperstones: Collect 50 Hyperstones.

    Orb of Yendor: Successfully collect an Orb of Yendor.
    """
    display_name = "Goal"
    option_10_hyperstones = 0
    option_50_hyperstones = 1
    option_orb_of_yendor = 2
    default = 2

class TreasureRequirements(Choice):
    """
    The treasure numbers per land included in the randomization.
    """
    display_name = "Treasure Requirements"
    option_10 = 10
    option_25 = 25
    option_50 = 50
    default = 25

class StartingLand(Choice):
    """
    The land each run starts in. It is recommended to choose the starting to land to be unlocked from the beginning.
    """
    display_name = "Starting Land"
    option_crossroads_1             =-1
    option_crossroads_2             =-2
    option_crossroads_3             =-3
    option_crossroads_4             =-4
    option_crossroads_5             =-5
    option_random_unlocked_land     =-10
    option_icy_land                 =0x00
    option_living_cave              =0x01
    option_desert                   =0x02
    option_jungle                   =0x03
    option_alchemist_lab            =0x04
    option_hall_of_mirrors          =0x05
    option_graveyard                =0x06
    option_hell                     =0x07
    option_rLyeh                    =0x08
    option_land_of_eternal_motion   =0x09
    option_cocytus                  =0x0A
    option_dry_forest               =0x0B
    option_vineyard                 =0x0C
    option_dead_cave                =0x0D
    option_hive                     =0x0E
    option_emerald_mine             =0x0F
    option_land_of_power            =0x10
    option_carribean                =0x13
    option_red_rock_valley          =0x14
    option_minefield                =0x15
    option_ocean                    =0x16
    option_palace                   =0x18
    option_living_fjord             =0x19
    option_zebra                    =0x1B
    option_elemental_planes         =0x1C
    option_land_of_storms           =0x1D
    option_overgrown_woods          =0x1E
    option_windy_plains             =0x21
    option_rose_garden              =0x22
    option_warped_coast             =0x23
    option_galapagos                =0x24 
    option_dragon_chasms            =0x26
    option_burial_grounds           =0x28
    option_trollheim                =0x29
    option_reptiles                 =0x2C
    option_prairie                  =0x2D
    option_bull_dash                =0x2E
    option_volcanic_wasteland       =0x2F
    option_hunting_ground           =0x30
    option_blizzard                 =0x31
    option_terracotta_army          =0x32
    option_ruined_city              =0x33
    option_jelly_kingdom            =0x34
    option_brown_island             =0x35
    option_irradiated_field         =0x37
    option_wetland                  =0x38
    option_frog_park                =0x39
    option_eclectic_city            =0x3A
    option_cursed_canyon            =0x3B
    option_dice_reserve             =0x3C

    default                         =-1

@dataclass
class HyperrogueOptions(PerGameCommonOptions):
    death_link: DeathLink
    goal: Goal
    treasure_requirements: TreasureRequirements
    starting_land: StartingLand