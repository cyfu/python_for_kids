import pandas as pd

pokemon_df = pd.read_csv("pokemon_list_cleaned.txt", delimiter="\t")
pokemon_names = pokemon_df["Name"]

card_name = "Dedenne"
card_found = False
card_checked = 0
for name in pokemon_names:
    card_checked += 1

    if name == card_name:
        card_found = True
        print('I found card {0}.'.format(card_name))
        break
print("I have checked {0} cards.".format(card_checked))
if (not card_found):
    print("I didn\'t find card {0}".format(card_name))
