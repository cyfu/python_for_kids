my_name = 'samantha yang'
my_age = 9 
my_height = 1.35 # metre
my_weight = 27 # kg
my_eyes = 'black'
my_hair_color = 'brown'
my_hair_style = 'long'

print ('My name is',my_name,'and my age is',my_age)
print("she's %4.2f metres tall." % my_height)
print("she's %d kilograms." % my_weight)
print("Actually that's pretty light.")
print("she has %s eyes." % my_eyes)
print("she's got %s and %s hair." % (my_hair_style, my_hair_color))



# this line is tricky, try to get it exactly right
print ("If I squred %.2f and divide %.2f, I get BMI %.2f." % (
    my_height, my_weight, my_weight/(my_height ** 2)))

'''
HOMEWORK:
    Rewrite the above codes using .format() function
'''
