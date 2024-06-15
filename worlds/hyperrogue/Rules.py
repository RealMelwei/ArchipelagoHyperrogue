from typing import Callable, Dict
from BaseClasses import CollectionState
from .Regions import *

Rule = Callable[[CollectionState],bool]

basic_access_rules: Dict[str,Rule]

def init_basic_access_rules(player):
    basic_access_rules = {regionname : (lambda state : check_basic_access_rule(regionname,state,player))
                                     for regionname in regionlist}

def check_basic_access_rule(regionname:str, state:CollectionState, player)->bool:
    if regionname in technical_regions:
        return True
    return state.has(regionname, player)