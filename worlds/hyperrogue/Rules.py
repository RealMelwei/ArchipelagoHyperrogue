from typing import Callable, Dict
from BaseClasses import CollectionState
from .Regions import *
from .Lands import landlist

Rule = Callable[[CollectionState],bool]

# An object of type Ruleset defines a ruleset for the unlock of a land
class Ruleset:
    # The whole ruleset is satisfied if for one of the lists in conditions,
    # every condition in that list is satisfied.
    conditions: List[List[str]] 

    def __init__(self, cond: List[List[str]]):
        self.conditions = cond

    def satisfied(self, state:CollectionState, player) -> bool:
        for condition_block in self.conditions:
            if all([Ruleset.check_condition(cond, state, player)
                    for cond in condition_block]):
                return True
        return False
    
    @staticmethod
    def check_condition(cond:str, state:CollectionState, player) -> bool:
        if cond == "Always":
            return True
        
        if cond in landlist:
            # Land from condition has to be unlocked and reachable for the player to collect treasure there
            land = cond
            return state.has(land, player) and state.multiworld.get_region(land, player).can_reach(state)
        
        if cond == "Anyland":
            return any([Ruleset.check_condition(land, state, player)
                        for land in landlist
                        if not land == "Camelot"]) # It must not be neccessary to collect 30 or more Treasures in Camelot
        
        if cond == "Alllands":
            return all([Ruleset.check_condition(land, state, player)
                        for land in landlist
                        if not land == "Camelot"]) # Camelot is not required for Hyperstone Quest
        
        if cond[:3] == "Min":
            min_number: int = int(cond[3:]) # e.g. for Min15 this is set to 15
            number: int = [Ruleset.check_condition(land, state, player)
                        for land in landlist
                        if not land == "Camelot"
                        ].count(True)
            if [Ruleset.check_condition(land, state, player)
                        for land in landlist
                        if not land == "Camelot"
                        ].count(True)>=min_number:
                
                return True

        return False
        

def get_basic_access_rule(regionname, player) -> Rule:
    return (lambda state : check_basic_access_rule(regionname,state,player))

def check_basic_access_rule(regionname:str, state:CollectionState, player)->bool:
    if regionname in technical_regions:
        return True
    return state.has(regionname, player)

def get_location_unlock_rule(land_name:str, player) -> Rule:
    return lambda state: unlock_condition_by_land_name[land_name].satisfied(state, player)

def get_completion_rule(player) -> Rule:
    return lambda state: Ruleset([["Alllands"]]).satisfied(state, player)


unlock_condition_by_land_name: Dict[str, Ruleset] = {
    "Icy Land":                 Ruleset([["Always"]]),
    "Living Cave":              Ruleset([["Always"]]),
    "Desert":                   Ruleset([["Always"]]),
    "Jungle":                   Ruleset([["Always"]]),
    "Alchemist Lab":            Ruleset([["Always"]]),
    "Hall of Mirrors":          Ruleset([["Anyland"]]),
    "Graveyard":                Ruleset([["Always"]]),
    "Hell":                     Ruleset([["Min9"]]),
    "R'Lyeh":                   Ruleset([["Anyland"]]),
    "Land of Eternal Motion":   Ruleset([["Always"]]),
    "Cocytus":                  Ruleset([["Icy Land", "Hell"]]),
    "Dry Forest":               Ruleset([["Anyland"]]),
    "Vineyard":                 Ruleset([["Anyland"]]),
    "Dead Cave":                Ruleset([["Living Cave"]]),
    "Hive":                     Ruleset([["Anyland"]]),
    "Emerald Mine":             Ruleset([["Palace"],["Dry Forest","Living Cave"]]),
    "Land of Power":            Ruleset([["Anyland"]]), #90
    "Camelot":                  Ruleset([["Emerald Mine"]]),
    "Temple of Cthulhu":        Ruleset([["R'Lyeh"]]),
    "Carribean":                Ruleset([["Anyland"]]),
    "Red Rock Valley":          Ruleset([["Desert"]]),
    "Minefield":                Ruleset([["Anyland"]]),
    "Ocean":                    Ruleset([["Anyland"]]),
    "Whirlpool":                Ruleset([["Anyland"]]),
    "Palace":                   Ruleset([["Anyland"]]),
    "Living Fjord":             Ruleset([["Anyland"]]),
    "Ivory Tower":              Ruleset([["Anyland"]]),
    "Zebra":                    Ruleset([["Land of Eternal Motion"]]),
    "Elemental Planes":         Ruleset([["Windy Plains", "Living Fjord", "Dead Cave", "Dragon Chasms"]]),
    "Land of Storms":           Ruleset([["Anyland"]]),
    "Overgrown Woods":          Ruleset([["Jungle"]]),
    "Clearing":                 Ruleset([["Overgrown Woods"]]),
    "Haunted Woods":            Ruleset([["Graveyard"]]),
    "Windy Plains":             Ruleset([["Anyland"]]),
    "Rose Garden":              Ruleset([["Anyland"]]), #90
    "Warped Coast":             Ruleset([["Anyland"]]),
    "Galapagos":                Ruleset([["Dragon Chasms"]]),
    "Yendorian Forest":         Ruleset([["Ivory Tower"]]),
    "Dragon Chasms":            Ruleset([["Min20"]]), #TODO
    "Kraken Depths":            Ruleset([["Living Fjord"]]),
    "Burial Grounds":           Ruleset([["Kraken Depths"]]),
    "Trollheim":                Ruleset([["Living Cave", "Dead Cave", "Red Rock Valley", "Land of Storms", "Overgrown Woods", "Living Fjord"]]),
    "Dungeon":                  Ruleset([["Palace", "Ivory Tower"]]),
    "Lost Mountain":            Ruleset([["Jungle", "Ivory Tower"]]),
    "Reptiles":                 Ruleset([["Alchemist Lab"]]),
    "Prairie":                  Ruleset([["Anyland"]]), #90
    "Bull Dash":                Ruleset([["Anyland"]]), #90
    "Volcanic Wasteland":       Ruleset([["Alchemist Lab"]]),
    "Hunting Ground":           Ruleset([["Always"]]),
    "Blizzard":                 Ruleset([["Icy Land", "Windy Plains"]]),
    "Terracotta Army":          Ruleset([["Anyland"]]), #90
    "Ruined City":              Ruleset([["Palace"],["Ruined City"],["Dungeon"],["Irradiated Field"],[]]),
    "Jelly Kingdom":            Ruleset([["Alchemist Lab"]]),
    "Brown Island":             Ruleset([["Anyland"]]),
    "Free Fall":                Ruleset([["Ivory Tower", "Land of Eternal Motion"]]),
    "Irradiated Field":         Ruleset([["Ruined City"],["Emerald Mine"],["Graveyard"]]),
    "Wetland":                  Ruleset([["Anyland"]]),
    "Frog Park":                Ruleset([["Reptiles"],["Zebra"],["Jelly Kingdom"]]),
    "Eclectic City":            Ruleset([["Icy Land"],["Land of Storms"],["Palace"],["Dead Cave"]]),
    "Cursed Canyon":            Ruleset([["Alchemist Lab"],["Carribean"],["Ruined City"],["Brown Island"],["Land of Power"]]),
    "Dice Reserve":             Ruleset([["Anyland"]]), #90
}


