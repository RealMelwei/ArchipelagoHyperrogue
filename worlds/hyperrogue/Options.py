from dataclasses import dataclass
from Options import DeathLink, PerGameCommonOptions

@dataclass
class HyperrogueOptions(PerGameCommonOptions):
    death_link: DeathLink