my_name = 'Michelle Jiang'
my_age = 8# not a lie
my_height = 1.25 # metre
my_weight = 23.1 # kg
my_eyes = 'brown'
my_teeth = 'white'
my_hair_color = 'black'
my_hair_style = 'long'
print ('My name is',my_name,'and my age is:', my_age)
print("Let's talk about %s." % my_name)
print("She's %4.2f metres tall." % my_height)
print("She's %d kilogram heavy." % my_weight)
print("Actually that's not too heavy.")
print("she has %s eyes." % my_eyes)
print("she got %s and %s hair." % (my_hair_style, my_hair_color))
print("her teeth are usually %s depending on the coffee." % my_teeth)



# this line is tricky, try to get it exactly right
print ("If I squred %.2f and divide %.2f, I get BMI %.2f." % (
    my_height, my_weight, my_weight/(my_height ** 2)))

'''
HOMEWORK:
    Rewrite the above codes using .format() function
'''

