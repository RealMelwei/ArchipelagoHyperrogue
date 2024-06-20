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

@dataclass
class HyperrogueOptions(PerGameCommonOptions):
    death_link: DeathLink
    goal: Goal
    treasure_requirements: TreasureRequirements