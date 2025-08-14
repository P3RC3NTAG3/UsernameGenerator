from random import randint,choice
import sys
adjectives = [
    "Calm", "Clear", "Crisp", "Daily", "Early", "Even", "Fair", "Fresh",
    "Local", "Mild", "Neat", "New", "Nice", "Open", "Plain", "Prime",
    "Pure", "Round", "Soft", "Solid", "Special", "Steady", "Sweet",
    "True", "Warm", "Balanced", "Brisk", "Central", "Classic", "Constant",
    "Cool", "Core", "Current", "Direct", "Equal", "Essential", "Fixed",
    "General", "Gentle", "Golden", "Grand", "Key", "Level", "Main", "Major",
    "Minimal", "Neutral", "Normal", "Notable", "Novel", "Ordinary",
    "Parallel", "Perfect", "Regular", "Select", "Simple", "Single",
    "Smooth", "Standard", "Static", "Subtle", "Supreme", "Uniform",
    "Unique", "Universal", "Upper", "Usual", "Vital", "Whole"
]
nouns = [
    "Acorn", "Anchor", "Apple", "Arch", "Arrow", "Atom", "Band",
    "Base", "Beam", "Berry", "Block", "Bloom", "Bolt", "Branch", "Brick",
    "Brush", "Bud", "Cable", "Candle", "Cap", "Cloud", "Cloth", "Coral",
    "Corner", "Cotton", "Crate", "Creek", "Cube", "Cup", "Curve", "Dawn",
    "Desk", "Dew", "Dock", "Door", "Dot", "Dune", "Dust", "Feather",
    "Field", "Film", "Flame", "Flax", "Floor", "Flower", "Fog", "Forest",
    "Frame", "Frost", "Gate", "Glass", "Glow", "Grain", "Grass", "Grid",
    "Grove", "Hill", "Hive", "Key", "Lake", "Leaf", "Line", "Map", "Meadow",
    "Metal", "Moon", "Moss", "Nest", "Note", "Oak", "Orb", "Page", "Path",
    "Pearl", "Pine", "Pixel", "Plain", "Planet", "Plate", "Pond", "Quill",
    "Rain", "Ray", "Ring", "River", "Rock", "Roof", "Root", "Sand", "Sea",
    "Seed", "Shade", "Shell", "Shore", "Sky", "Snow", "Soil", "Sound",
    "Spark", "Spring", "Star", "Stem", "Stone", "Stream", "Sun", "Table",
    "Thorn", "Thread", "Tree", "Vale", "Valley", "Vine", "Wave", "Wing",
    "Wood"
]
delimiters=["",".","-","_"]
try:
    namequantity=int(input("How many usernames would you like generated? "))
except:
    print("Please enter a valid integer.")
    sys.exit()
for j in range(namequantity):
    numbers=""
    for i in range(randint(0,4)):
        numbers+=str(randint(0,9))
    delimiter=choice(delimiters)
    print(choice(adjectives)+delimiter+choice(nouns)+("" if numbers=="" else delimiter)+numbers)
input("Press enter to quit.")
