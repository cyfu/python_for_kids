life_stages = ["TAMAGOTCHI",
    "BABITCHI",
    "MARUTCHI",
    "TAMATCHI",
    "KUCHITAMATCHI",
    "MAMETCHI",
    "GINJIROTCHI",
    "MASKTCHI",
    "KUCHIPATCHI",
    "NYOROTCHI",
    "TARAKOTCHI",
    "OYAJICHI"
]

def feed(pet):
    pet["hungry"] = False
    pet["life_stage"] = pet["life_stage"] + 1
    pet["weight"] = pet["weight"] + 2