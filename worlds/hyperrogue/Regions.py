from typing import Dict, List, NamedTuple


class HyperrogueRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, HyperrogueRegionData] = {
    "Menu":                     HyperrogueRegionData(["Icy Land"]),
    "Non-Sea Great Wall":       HyperrogueRegionData(),
    "Sea Great Wall":           HyperrogueRegionData(["Carribean","Ocean","Living Fjord","Warped Coast","Kraken Depths"]),
    "Icy Land":                 HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Living Caves":             HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Desert":                   HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Jungle":                   HyperrogueRegionData(["Non-Sea Great Wall","Lost Mountain"]),
    "Alchemist Lab":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Hall of Mirrors":          HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Graveyard":                HyperrogueRegionData(["Non-Sea Great Wall","Haunted Woods"]),
    "Hell":                     HyperrogueRegionData(["Non-Sea Great Wall"]),
    "R'Lyeh":                   HyperrogueRegionData(["Non-Sea Great Wall","Ocean","Temple of Cthulhu"]),
    "Land of Eternal Motion":   HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Cocytus":                  HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Dry Forest":               HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Vineyard":                 HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Dead Caves":               HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Hive":                     HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Emerald Mines":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Land of Power":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Camelot":                  HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Temple of Cthulhu":        HyperrogueRegionData(["R'Lyeh"]),
    "Carribean":                HyperrogueRegionData(["Sea Great Wall"]),
    "Red Rock Valley":          HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Minefield":                HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Ocean":                    HyperrogueRegionData(["Non-Sea Great Wall","Sea Great Wall", "R'Lyeh", "Whirlpool", "Brown Island"]),
    "Whirlpool":                HyperrogueRegionData(["Ocean"]),
    "Palace":                   HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Living Fjord":             HyperrogueRegionData(["Non-Sea Great Wall", "Sea Great Wall"]),
    "Ivory Tower":              HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Zebra":                    HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Elemental Planes":         HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Land of Storms":           HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Overgrown Woods":          HyperrogueRegionData(["Non-Sea Great Wall", "Clearing"]),
    "Clearing":                 HyperrogueRegionData(["Overgrown Woods"]),
    "Haunted Woods":            HyperrogueRegionData(["Graveyard"]),
    "Windy Plains":             HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Rose Garden":              HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Warped Coast":             HyperrogueRegionData(["Non-Sea Great Wall", "Sea Great Wall"]),
    "Galapagos":                HyperrogueRegionData(["Dragon Chasms"]),
    "Yendorian Forest":         HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Dragon Chasms":            HyperrogueRegionData(["Non-Sea Great Wall", "Galapagos"]),
    "Kraken Depths":            HyperrogueRegionData(["Sea Great Wall"]),
    "Burial Grounds":           HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Trollheim":                HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Dungeon":                  HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Lost Mountain":            HyperrogueRegionData(["Jungle"]),
    "Reptiles":                 HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Prairie":                  HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Bull Dash":                HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Volcanic Wasteland":       HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Hunting Ground":           HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Blizzard":                 HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Terracotta Army":          HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Ruined City":              HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Jelly Kingdom":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Brown Island":             HyperrogueRegionData(["Ocean"]),
    "Free Fall":                HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Irradiated Field":         HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Wetland":                  HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Frog Park":                HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Eclectic City":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Cursed Canyon":            HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Dice Reserve":             HyperrogueRegionData(["Non-Sea Great Wall"]),
    "Wild West":                HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
    "Halloween":                HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
    "Crystal Caverns":          HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
    "Snake Nest":               HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
    "Docks":                    HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
    "Space Rocks":              HyperrogueRegionData(["Non-Sea Great Wall"]), # Nonstandard Land
}
