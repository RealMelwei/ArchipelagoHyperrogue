from typing import Dict, List

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from . import HyperrogueWorld
from .Names import ItemName, LocationName


def set_rules(world: HyperrogueWorld):
    world.active_logic_mapping = {}

    # Completion condition.
    world.multiworld.completion_condition[world.player] = lambda state: goal_rule(state, world)

def location_rule(state: CollectionState, world: HyperrogueWorld, loc: str) -> bool:
    return True
#    if loc not in world.active_logic_mapping:
#        return True

#    for possible_access in world.active_logic_mapping[loc]:
#        if state.has_all(possible_access, world.player):
#            return True

#    return False

def goal_rule(state: CollectionState, world: HyperrogueWorld) -> bool:
    if state.has(ItemName.demon_daisy, world.player, 2): return True
    return False
