my_name = 'michelle jiang'
my_age = 8 #not a lie
my_height = 1.23 # metre
my_weight = 47 # kg
my_eyes = 'black'
my_teeth = 'white'
my_hair_color = 'black'
my_hair_style = 'long'

#print ('My name is',my_name,'and my age is:', my_age)

print("Let's talk about {0}." .format(my_name))
print("she has {0} eyes."  .format (my_eyes))

print("she got {0} and {1} hair." .format(my_hair_style, my_hair_color))
print("her teeth are usually {0} depending on the coffee." .format(my_teeth))
# this line is tricky, try to get it exactly right
print ("If I squred {:.2f} and divide {:.2f}, I get BMI {:.2f}." .format (
    my_height, my_weight, my_weight/(my_height ** 2)))
print("she {0} kilogram heavy." .format (my_weight))
print("Actually that's not too heavy.")
print("she has {0}eyes." .format
      (my_eyes))
print("she got {0}and {1} hair." .format(my_hair_style, my_hair_color))
print("her teeth are usually {0} depending on the coffee." 
.format( my_teeth))

