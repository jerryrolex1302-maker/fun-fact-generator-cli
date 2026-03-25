import random

fun_facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A day on Venus is longer than a year on Venus."
]

input("Press Enter to receive a fun fact: ")
print("\n💡 Fun Fact: " + random.choice(fun_facts))
