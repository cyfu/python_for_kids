my_name = 'Joseph Yang'
my_age = 9 # not a lie
my_height = 1.38 # metre
my_weight = 27.1 # kg
my_eyes = 'black'
my_teeth = 'white'
my_hair_color = 'black'
my_hair_style = 'short'

print ('My name is',my_name,'and my age is:', my_age)

print("Let's talk about %s." % my_name)
print("He's %4.2f metres tall." % my_height)
print("He's %d kilogram heavy." % my_weight)
print("Actually that's not too heavy.")
print("He has %s eyes." % my_eyes)
print("He's got %s and %s hair." % (my_hair_style, my_hair_color))
print("His teeth are usually white")
# this line is tricky, try to get it exactly right
print ("If I squred %.2f and divide %.2f, I get BMI %.2f." % (
    my_height, my_weight, my_weight/(my_height ** 2)))

'''
HOMEWORK:
    Rewrite the above codes using .format() function
'''
print("my name is{0}and my age is{1}".format(my_name,my_age))
print("he's{0}meters tall.".format(my_height))                                    
