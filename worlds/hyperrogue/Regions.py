from typing import Dict, List

technical_regions: List[str] = ["Menu","Non-Sea Great Wall","Sea Great Wall"]

region_connections: Dict[str, List[str]] = {
    "Menu":                     ["Icy Land"],
    "Non-Sea Great Wall":       [],
    "Sea Great Wall":           ["Carribean","Ocean","Living Fjord","Warped Coast","Kraken Depths"],
    "Icy Land":                 ["Non-Sea Great Wall"],
    "Living Cave":              ["Non-Sea Great Wall"],
    "Desert":                   ["Non-Sea Great Wall"],
    "Jungle":                   ["Non-Sea Great Wall","Lost Mountain"],
    "Alchemist Lab":            ["Non-Sea Great Wall"],
    "Hall of Mirrors":          ["Non-Sea Great Wall"],
    "Graveyard":                ["Non-Sea Great Wall","Haunted Woods"],
    "Hell":                     ["Non-Sea Great Wall"],
    "R'Lyeh":                   ["Ocean","Temple of Cthulhu"],
    "Land of Eternal Motion":   ["Non-Sea Great Wall"],
    "Cocytus":                  ["Non-Sea Great Wall"],
    "Dry Forest":               ["Non-Sea Great Wall"],
    "Vineyard":                 ["Non-Sea Great Wall"],
    "Dead Cave":                ["Non-Sea Great Wall"],
    "Hive":                     ["Non-Sea Great Wall"],
    "Emerald Mine":            ["Non-Sea Great Wall"],
    "Land of Power":            ["Non-Sea Great Wall"],
    "Camelot":                  ["Non-Sea Great Wall"],
    "Temple of Cthulhu":        ["R'Lyeh"],
    "Carribean":                ["Sea Great Wall"],
    "Red Rock Valley":          ["Non-Sea Great Wall"],
    "Minefield":                ["Non-Sea Great Wall"],
    "Ocean":                    ["Non-Sea Great Wall","Sea Great Wall", "R'Lyeh", "Whirlpool", "Brown Island"],
    "Whirlpool":                ["Ocean"],
    "Palace":                   ["Non-Sea Great Wall"],
    "Living Fjord":             ["Non-Sea Great Wall", "Sea Great Wall"],
    "Ivory Tower":              ["Non-Sea Great Wall"],
    "Zebra":                    ["Non-Sea Great Wall"],
    "Elemental Planes":         ["Non-Sea Great Wall"],
    "Land of Storms":           ["Non-Sea Great Wall"],
    "Overgrown Woods":          ["Non-Sea Great Wall", "Clearing"],
    "Clearing":                 ["Overgrown Woods"],
    "Haunted Woods":            ["Graveyard"],
    "Windy Plains":             ["Non-Sea Great Wall"],
    "Rose Garden":              ["Non-Sea Great Wall"],
    "Warped Coast":             ["Non-Sea Great Wall", "Sea Great Wall"],
    "Galapagos":                ["Dragon Chasms"],
    "Yendorian Forest":         ["Non-Sea Great Wall"],
    "Dragon Chasms":            ["Non-Sea Great Wall", "Galapagos"],
    "Kraken Depths":            ["Sea Great Wall"],
    "Burial Grounds":           ["Non-Sea Great Wall"],
    "Trollheim":                ["Non-Sea Great Wall"],
    "Dungeon":                  ["Non-Sea Great Wall"],
    "Lost Mountain":            ["Jungle"],
    "Reptiles":                 ["Non-Sea Great Wall"],
    "Prairie":                  ["Non-Sea Great Wall"],
    "Bull Dash":                ["Non-Sea Great Wall"],
    "Volcanic Wasteland":       ["Non-Sea Great Wall"],
    "Hunting Ground":           ["Non-Sea Great Wall"],
    "Blizzard":                 ["Non-Sea Great Wall"],
    "Terracotta Army":          ["Non-Sea Great Wall"],
    "Ruined City":              ["Non-Sea Great Wall"],
    "Jelly Kingdom":            ["Non-Sea Great Wall"],
    "Brown Island":             ["Ocean"],
    "Free Fall":                ["Non-Sea Great Wall"],
    "Irradiated Field":         ["Non-Sea Great Wall"],
    "Wetland":                  ["Non-Sea Great Wall"],
    "Frog Park":                ["Non-Sea Great Wall"],
    "Eclectic City":            ["Non-Sea Great Wall"],
    "Cursed Canyon":            ["Non-Sea Great Wall"],
    "Dice Reserve":             ["Non-Sea Great Wall"],
}

regionlist: List[str] = region_connections.keys()