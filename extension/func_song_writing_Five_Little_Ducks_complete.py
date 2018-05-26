#Simple version
def chorus(duck_num):
  print("{} little ducks".format(duck_num))
  print("Went out one day")
  print("Over the hill and far away")
  print("Mother duck said")
  print("\"Quack, quack, quack, quack.\"")
  print("But only {} little ducks came back.".format(duck_num-1))
  print("")

for ducks in range(5, 1, -1):
  chorus(ducks)
print("Sad mother duck")
print("Went out one day")
print("Over the hill and far away")
print("The sad mother duck said")
print("\"Quack, quack, quack.\"")
print("And all of the five little ducks came back.")
