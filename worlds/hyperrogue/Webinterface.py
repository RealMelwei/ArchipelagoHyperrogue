from typing import List
from BaseClasses import Tutorial
from Options import OptionGroup
from worlds.AutoWorld import WebWorld
from.Options import *

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

    option_groups:List[OptionGroup] = []