from typing import Callable, Dict
from BaseClasses import CollectionState
from .Regions import *
from .Names import landlist
from rule_builder.rules import *
from .Options import *

# CODE TO REMOVE IN ARCHIPELAGO 0.6.8
from rule_builder import rules

hard_logic_difficulty = [OptionFilter(LogicDifficulty, LogicDifficulty.option_hard)]
yendor_goal = [OptionFilter(Goal, Goal.option_orb_of_yendor)]

# An object of type Ruleset defines a ruleset for the unlock of a land
class UnlockCondition:
    # The whole ruleset is satisfied if for one of the lists in conditions,
    # every condition in that list is satisfied.
    conditions: List[List[str]] 

    def __init__(self, cond_block_list: List[List[str]]):
        self.conditions = cond_block_list

    def get_rule(self) -> bool:
        return Or(*[And(*[self.get_inner_rule(cond) for cond in condition_block]) for condition_block in self.conditions])

    @staticmethod    
    def get_inner_rule(cond:str) -> Rule:
        if cond == "Always":
            return True_()
        
        if cond in landlist:
            # Land from condition has to be unlocked and reachable for the player to collect treasure there
            return Has(cond)
        
        if cond == "Anyland":
            return HasAny(*[land
                        for land in landlist
                        if not land == "Camelot"]) # It must not be neccessary to collect 30 or more Treasures in Camelot
        
        if cond == "Alllands":
            return HasAll(*[land
                        for land in landlist
                        if not land == "Camelot"]) # Camelot is not required for Hyperstone Quest
        
        if cond[:3] == "Min":
            min_number: int = int(cond[3:]) # e.g. for Min15 this is set to 15

            ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
            if hasattr(rules, 'AtLeast'):
                return AtLeast(min_number, *[Has(land) for land in landlist if not land == "Camelot"])
            else:
                return AtLeastHR(min_number, *[Has(land) for land in landlist if not land == "Camelot"])

        return False_()

def get_basic_access_rule(regionname) -> Rule:
    if regionname in technical_regions:
        return True_()
    else:
        return Has(regionname)

def get_location_rule(land_name:str, suffix:str) -> Rule:
    if suffix == "Unlock":
        return unlock_condition_by_land_name[land_name].get_rule()
    elif suffix == "10 Treasures" or suffix == "10 Treasures Extra":
        return Has(land_name)
    else:
        return Has(land_name, 2) | (Has(land_name) & hard_logic_difficulty)
    

def get_completion_rule() -> Rule:
    return (Has("Hell", 2) & yendor_goal) | UnlockCondition([["Alllands"]]).get_rule()


unlock_condition_by_land_name: Dict[str, UnlockCondition] = {
    "Icy Land":                 UnlockCondition([["Always"]]),
    "Living Cave":              UnlockCondition([["Always"]]),
    "Desert":                   UnlockCondition([["Always"]]),
    "Jungle":                   UnlockCondition([["Always"]]),
    "Alchemist Lab":            UnlockCondition([["Always"]]),
    "Hall of Mirrors":          UnlockCondition([["Anyland"]]),
    "Graveyard":                UnlockCondition([["Always"]]),
    "Hell":                     UnlockCondition([["Min9"]]),
    "R'Lyeh":                   UnlockCondition([["Anyland"]]),
    "Land of Eternal Motion":   UnlockCondition([["Always"]]),
    "Cocytus":                  UnlockCondition([["Icy Land", "Hell"]]),
    "Dry Forest":               UnlockCondition([["Anyland"]]),
    "Vineyard":                 UnlockCondition([["Anyland"]]),
    "Dead Cave":                UnlockCondition([["Living Cave"]]),
    "Hive":                     UnlockCondition([["Anyland"]]),
    "Emerald Mine":             UnlockCondition([["Palace"],["Dry Forest","Living Cave"]]),
    "Land of Power":            UnlockCondition([["Hell"]]), #90
    "Camelot":                  UnlockCondition([["Emerald Mine"]]),
    "Temple of Cthulhu":        UnlockCondition([["R'Lyeh"]]),
    "Carribean":                UnlockCondition([["Anyland"]]),
    "Red Rock Valley":          UnlockCondition([["Desert"]]),
    "Minefield":                UnlockCondition([["Anyland"]]),
    "Ocean":                    UnlockCondition([["Anyland"]]),
    "Whirlpool":                UnlockCondition([["Anyland"]]),
    "Palace":                   UnlockCondition([["Anyland"]]),
    "Living Fjord":             UnlockCondition([["Anyland"]]),
    "Ivory Tower":              UnlockCondition([["Anyland"]]),
    "Zebra":                    UnlockCondition([["Land of Eternal Motion"]]),
    "Elemental Planes":         UnlockCondition([["Windy Plains", "Living Fjord", "Dead Cave", "Dragon Chasms"],["Elemental Planes"]]),
    "Land of Storms":           UnlockCondition([["Anyland"]]),
    "Overgrown Woods":          UnlockCondition([["Jungle"]]),
    "Clearing":                 UnlockCondition([["Overgrown Woods"]]),
    "Haunted Woods":            UnlockCondition([["Graveyard"]]),
    "Windy Plains":             UnlockCondition([["Anyland"]]),
    "Rose Garden":              UnlockCondition([["Anyland"]]), #90
    "Warped Coast":             UnlockCondition([["Anyland"]]),
    "Galapagos":                UnlockCondition([["Dragon Chasms"]]),
    "Yendorian Forest":         UnlockCondition([["Ivory Tower"]]),
    "Dragon Chasms":            UnlockCondition([["Min20"]]), #TODO
    "Kraken Depths":            UnlockCondition([["Living Fjord"]]),
    "Burial Grounds":           UnlockCondition([["Kraken Depths"]]),
    "Trollheim":                UnlockCondition([["Living Cave", "Dead Cave", "Red Rock Valley", "Land of Storms", "Overgrown Woods", "Living Fjord"]]),
    "Dungeon":                  UnlockCondition([["Palace", "Ivory Tower"]]),
    "Lost Mountain":            UnlockCondition([["Jungle", "Ivory Tower"]]),
    "Reptiles":                 UnlockCondition([["Alchemist Lab"]]),
    "Prairie":                  UnlockCondition([["Anyland"]]), #90
    "Bull Dash":                UnlockCondition([["Anyland"]]), #90
    "Volcanic Wasteland":       UnlockCondition([["Alchemist Lab"]]),
    "Hunting Ground":           UnlockCondition([["Always"]]),
    "Blizzard":                 UnlockCondition([["Icy Land", "Windy Plains"]]),
    "Terracotta Army":          UnlockCondition([["Anyland"]]), #90
    "Ruined City":              UnlockCondition([["Palace"],["Ruined City"],["Dungeon"],["Irradiated Field"]]),
    "Jelly Kingdom":            UnlockCondition([["Alchemist Lab"]]),
    "Brown Island":             UnlockCondition([["Anyland"]]),
    "Free Fall":                UnlockCondition([["Ivory Tower", "Land of Eternal Motion"]]),
    "Irradiated Field":         UnlockCondition([["Ruined City"],["Emerald Mine"],["Graveyard"]]),
    "Wetland":                  UnlockCondition([["Anyland"]]),
    "Frog Park":                UnlockCondition([["Reptiles"],["Zebra"],["Jelly Kingdom"]]),
    "Eclectic City":            UnlockCondition([["Icy Land"],["Land of Storms"],["Palace"],["Dead Cave"]]),
    "Cursed Canyon":            UnlockCondition([["Alchemist Lab"],["Carribean"],["Ruined City"],["Brown Island"],["Land of Power"]]),
    "Dice Reserve":             UnlockCondition([["Anyland"]]), #90
}

### CODE TO REMOVE IN ARCHIPELAGO 0.6.8

class AtLeastHR(NestedRule[TWorld], game = "Hyperrogue"):
    """A rule that returns true when at least N child rules evaluate as true"""

    count: int | FieldResolver

    def __init__(
        self,
        count: int | FieldResolver,
        *children: Rule[TWorld],
        options: Iterable[OptionFilter] = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(*children, options=options, filtered_resolution=filtered_resolution)
        self.count = count

    @override
    def _instantiate(self, world: TWorld) -> Rule.Resolved:
        count = resolve_field(self.count, world, int)
        if count == 0:
            return True_().resolve(world)

        children_to_process = [c.resolve(world) for c in self.children]
        return AtLeastHR.from_resolved(count, world, children_to_process)

    @classmethod
    def from_resolved(cls, count: int, world: TWorld, children_to_process: list[Rule.Resolved]) -> Rule.Resolved:
        clauses: list[Rule.Resolved] = []

        while children_to_process:
            child = children_to_process.pop(0)
            if child.always_true:
                if count == 1:
                    return child
                count -= 1
                continue
            if child.always_false:
                # falses can be ignored
                continue

            clauses.append(child)

        if len(clauses) < count:
            return False_().resolve(world)
        if count == 1:
            # Switch to Or which has more optimized handling
            return Or.from_resolved(world, clauses)
        if count == len(clauses):
            # Switch to And which has more optimized handling
            return And.from_resolved(world, clauses)
        return AtLeastHR.Resolved(
            tuple(clauses),
            count=count,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    @override
    def to_dict(self) -> dict[str, Any]:
        output = super().to_dict()
        count = self.count
        output["count"] = count.to_dict() if isinstance(count, FieldResolver) else count
        return output

    @override
    @classmethod
    def from_dict(cls, data: Mapping[str, Any], world_cls: "type[World]") -> Self:
        args = cls._parse_field_resolvers(data, world_cls.game)
        options = OptionFilter.multiple_from_dict(data.get("options", ()))
        children = [world_cls.rule_from_dict(c) for c in data.get("children", ())]
        return cls(
            args.pop("count"),
            *children,
            options=options,
            filtered_resolution=data.get("filtered_resolution", False),
        )

    class Resolved(NestedRule.Resolved):
        count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            count = self.count
            for rule in self.children:
                if rule(state):
                    if count == 1:
                        return True
                    count -= 1
            return False

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            messages: list[JSONMessagePart] = []
            if state is None:
                messages = [
                    {"type": "text", "text": "At least "},
                    {"type": "color", "color": "cyan", "text": str(self.count)},
                    {"type": "text", "text": " of ("},
                ]
            else:
                satisfied_count = sum(1 if child(state) else 0 for child in self.children)
                messages = [
                    {"type": "text", "text": "At least "},
                    {"type": "color", "color": "cyan", "text": f"{satisfied_count}/{self.count}"},
                    {"type": "text", "text": " of ("},
                ]
            for i, child in enumerate(self.children):
                if i > 0:
                    messages.append({"type": "text", "text": ", "})
                messages.extend(child.explain_json(state))
            messages.append({"type": "text", "text": ")"})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            clauses = ", ".join([c.explain_str(state) for c in self.children])
            if state is None:
                return f"At least {self.count} of ({clauses})"
            satisfied_count = sum(1 if child(state) else 0 for child in self.children)
            return f"At least {satisfied_count}/{self.count} of ({clauses})"

        @override
        def __str__(self) -> str:
            clauses = ", ".join([str(c) for c in self.children])
            return f"At least {self.count} of ({clauses})"
