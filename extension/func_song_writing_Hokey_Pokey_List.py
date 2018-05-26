'''
We will use function to write a song called Hokey Pokey
'''
body_parts = [
  "right foot",
  "left foot",
  "right arm",
  "left arm",
  "head",
  "knees",
  "shoulders",
  "elbows",
  "bottom",
  "quiet voice",
  "loud voice",
  "tummy",
  "nose",
  "whole self!"
  ]

def chorus(body_part):
    print("You put your {} in".format(body_part))
    print("You take your {} out".format(body_part))
    print("You put your {} in".format(body_part))
    print("And you shake it all about")
    print("")
    print("You do the hokey pokey")
    print("And you turn yourself around")
    print("That's what it's all about")
    print("")
  

for i in range(len(body_parts)):
  chorus(body_parts[i])
