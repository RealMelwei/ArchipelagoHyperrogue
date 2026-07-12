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
required_treasures_25 = [OptionFilter(TreasureRequirements, TreasureRequirements.option_25)]
required_treasures_50 = [OptionFilter(TreasureRequirements, TreasureRequirements.option_50)]


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
            return Or(*[CanReachRegion(land)
                        for land in landlist
                        if not land == "Camelot"]) # It must not be neccessary to collect 30 or more Treasures in Camelot
        
        if cond[:5] == "Treas":
            num_treas: int = int(cond[5:])
            match num_treas:
                case 90:
                    return Or(*[(UnlockCondition.get_inner_rule("Min2") & hard_logic_difficulty & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min4") & hard_logic_difficulty & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min9") & hard_logic_difficulty),
                                     (UnlockCondition.get_inner_rule("Min3") & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min6") & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min14"))])
                case 60:
                    return Or(*[(UnlockCondition.get_inner_rule("Min2") & hard_logic_difficulty & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min3") & hard_logic_difficulty & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min6") & hard_logic_difficulty),
                                     (UnlockCondition.get_inner_rule("Min3") & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min5") & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min9"))])
                case 30:
                    return Or(*[(UnlockCondition.get_inner_rule("Min1") & hard_logic_difficulty & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min2") & hard_logic_difficulty & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min3") & hard_logic_difficulty),
                                     (UnlockCondition.get_inner_rule("Min2") & required_treasures_50),
                                     (UnlockCondition.get_inner_rule("Min3") & required_treasures_25),
                                     (UnlockCondition.get_inner_rule("Min5"))])

        if cond == "Alllands":
            return And(*[CanReachRegion(land)
                        for land in landlist
                        if not land == "Camelot"]) # Camelot is not required for Hyperstone Quest
        
        if cond[:3] == "Min":
            min_number: int = int(cond[3:]) # e.g. for Min15 this is set to 15

            ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
            if hasattr(rules, 'AtLeast'):
                return AtLeast(min_number, *[CanReachRegion(land) for land in landlist if not land == "Camelot"])
            else:
                return AtLeastHR(min_number, *[CanReachRegion(land) for land in landlist if not land == "Camelot"])
        
        ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
        if cond == "SpecialIrradiatedField":
            relevant = [CanReachRegion("Ruined City"), CanReachRegion("Emerald Mine"), CanReachRegion("Graveyard")]
            return Or(*[Or(*relevant) & hard_logic_difficulty & required_treasures_50,
                        AtLeastHR(2, *relevant) & hard_logic_difficulty | AtLeastHR(2, *relevant) & required_treasures_25,
                        And(*relevant)
                        ])
        
        ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
        if cond == "SpecialFrogPark":
            relevant = [CanReachRegion("Reptiles"), CanReachRegion("Zebra"), CanReachRegion("Jelly Kingdom")]
            return Or(*[Or(*relevant) & hard_logic_difficulty & required_treasures_25,
                        AtLeastHR(2, *relevant) & hard_logic_difficulty | AtLeastHR(2, *relevant) & required_treasures_25,
                        And(*relevant)
                        ])
        
        ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
        if cond == "SpecialEclecticCity":
            relevant = [CanReachRegion("Icy Land"), CanReachRegion("Land of Storms"), CanReachRegion("Palace"), CanReachRegion("Dead Cave")]
            return Or(*[Or(*relevant) & hard_logic_difficulty & required_treasures_50,
                        AtLeastHR(2,*relevant) & hard_logic_difficulty & required_treasures_25 | AtLeastHR(2,*relevant) & required_treasures_50,
                        AtLeastHR(3,*relevant) & hard_logic_difficulty | AtLeastHR(3,*relevant) & required_treasures_25,
                        And(*relevant)
                        ])
        
        ### CODE TO ADJUST IN ARCHIPELAGO 0.6.8
        if cond == "SpecialCursedCanyon":
            relevant = [CanReachRegion("Alchemist Lab"), CanReachRegion("Carribean"), CanReachRegion("Ruined City"), CanReachRegion("Brown Island"), CanReachRegion("Land of Power")]
            return Or(*[Or(*relevant) & hard_logic_difficulty & required_treasures_50,
                        AtLeastHR(2, *relevant) & hard_logic_difficulty & required_treasures_25 | AtLeastHR(2, *relevant) & required_treasures_50,
                        AtLeastHR(3, *relevant) & hard_logic_difficulty | AtLeastHR(3, *relevant) & required_treasures_25,
                        AtLeastHR(4, *relevant)
                        ])

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
    "Hall of Mirrors":          UnlockCondition([["Treas30"]]),
    "Graveyard":                UnlockCondition([["Always"]]),
    "Hell":                     UnlockCondition([["Min9"]]),
    "R'Lyeh":                   UnlockCondition([["Treas60"]]),
    "Land of Eternal Motion":   UnlockCondition([["Always"]]),
    "Cocytus":                  UnlockCondition([["Icy Land", "Hell"]]),
    "Dry Forest":               UnlockCondition([["Treas60"]]),
    "Vineyard":                 UnlockCondition([["Treas60"]]),
    "Dead Cave":                UnlockCondition([["Living Cave", "Treas60"]]),
    "Hive":                     UnlockCondition([["Treas60"]]),
    "Emerald Mine":             UnlockCondition([["Palace"],["Dry Forest","Living Cave"]]),
    "Land of Power":            UnlockCondition([["Hell", "Treas90"]]),
    "Camelot":                  UnlockCondition([["Emerald Mine"]]),
    "Temple of Cthulhu":        UnlockCondition([["R'Lyeh"]]),
    "Carribean":                UnlockCondition([["Treas30"]]),
    "Red Rock Valley":          UnlockCondition([["Desert","Treas60"]]),
    "Minefield":                UnlockCondition([["Treas30"]]),
    "Ocean":                    UnlockCondition([["Treas30"]]),
    "Whirlpool":                UnlockCondition([["Treas30"]]),
    "Palace":                   UnlockCondition([["Treas30"]]),
    "Living Fjord":             UnlockCondition([["Treas30"]]),
    "Ivory Tower":              UnlockCondition([["Treas30"]]),
    "Zebra":                    UnlockCondition([["Land of Eternal Motion","Treas30"]]),
    "Elemental Planes":         UnlockCondition([["Windy Plains", "Living Fjord", "Dead Cave", "Dragon Chasms"],["Elemental Planes"]]),
    "Land of Storms":           UnlockCondition([["Treas60"]]),
    "Overgrown Woods":          UnlockCondition([["Jungle", "Treas60"]]),
    "Clearing":                 UnlockCondition([["Overgrown Woods"]]),
    "Haunted Woods":            UnlockCondition([["Graveyard"]]),
    "Windy Plains":             UnlockCondition([["Treas60"]]),
    "Rose Garden":              UnlockCondition([["Treas90"]]),
    "Warped Coast":             UnlockCondition([["Treas30"]]),
    "Galapagos":                UnlockCondition([["Dragon Chasms"]]),
    "Yendorian Forest":         UnlockCondition([["Ivory Tower"]]),
    "Dragon Chasms":            UnlockCondition([["Min20"]]), #TODO
    "Kraken Depths":            UnlockCondition([["Living Fjord"]]),
    "Burial Grounds":           UnlockCondition([["Kraken Depths"]]),
    "Trollheim":                UnlockCondition([["Living Cave", "Dead Cave", "Red Rock Valley", "Land of Storms", "Overgrown Woods", "Living Fjord"]]),
    "Dungeon":                  UnlockCondition([["Palace", "Ivory Tower"]]),
    "Lost Mountain":            UnlockCondition([["Jungle", "Ivory Tower"]]),
    "Reptiles":                 UnlockCondition([["Alchemist Lab","Treas30"]]),
    "Prairie":                  UnlockCondition([["Treas90"]]),
    "Bull Dash":                UnlockCondition([["Treas90"]]),
    "Volcanic Wasteland":       UnlockCondition([["Alchemist Lab","Treas60"]]),
    "Hunting Ground":           UnlockCondition([["Always"]]),
    "Blizzard":                 UnlockCondition([["Icy Land", "Windy Plains"]]),
    "Terracotta Army":          UnlockCondition([["Treas90"]]),
    "Ruined City":              UnlockCondition([["Palace"],["Ruined City"],["Dungeon"],["Irradiated Field"]]),
    "Jelly Kingdom":            UnlockCondition([["Alchemist Lab","Treas30"]]),
    "Brown Island":             UnlockCondition([["Treas30"]]),
    "Free Fall":                UnlockCondition([["Ivory Tower", "Land of Eternal Motion"]]),
    "Irradiated Field":         UnlockCondition([["SpecialIrradiatedField"]]),
    "Wetland":                  UnlockCondition([["Treas30"]]),
    "Frog Park":                UnlockCondition([["SpecialFrogPark"]]),
    "Eclectic City":            UnlockCondition([["SpecialEclecticCity"]]),
    "Cursed Canyon":            UnlockCondition([["SpecialCursedCanyon"]]),
    "Dice Reserve":             UnlockCondition([["Treas90"]]),
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
