#define function chorus, which repeats many time in the song
#We have to define function before it is called
def chorus(duck_num):
  print("{} little ducks".format(duck_num))
  print("Went out one day")
  print("Over the hill and far away")
  print("Mother duck said")
  print("\"Quack, quack, quack, quack.\"")
  print("But only {} little ducks came back.".format(duck_num-1))
  print("")

######### Main Program Start ########
for ducks in range(5, 1, -1):
  chorus(ducks) #Call function to complete song writing