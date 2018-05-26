#We will write a song Old MacDonald had a farm.
#It is originated from code.org lesson "song writing"
#https://code.org/curriculum/course4/13/Activity13-Songwriting.pdf

def chorus(annimal_name, sound):
    print("Old MacDonald had a farm")
    print("e-i-e-i-o")
    print("And on that farm he had a {}".format(annimal_name))
    print("e-i-e-i-o")
    print("With a {} here and a {} there".format(sound, sound))
    print("Here a {}, there a {}".format(sound, sound))
    print("Everywhere a {}, {}".format(sound, sound))

animal_sounds = {
    "chick": "Chick",
    "pig": "Oink",
    "cow": "Moo",
    "horse": "Neigh",
    "duck":"Quack",
    "sheep":"Baa-Baa"
}

for animal in animal_sounds:
    chorus(animal, animal_sounds[animal])