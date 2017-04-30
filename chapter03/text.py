'''list are more powerful than strings
'''
wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
print(wizard_list)

wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)

#access list element
print(wizard_list[0])
print(wizard_list[2:5])

#change list element
wizard_list[0] = 'snail tongue'
print(wizard_list)

#list can contain mixed things
numbers = [1, 2, 3, 4, 5. 6]
strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
my_list = [numbers, strings]
print(my_list)

number_and_string = ['why', 'was', 6, 'afraid', 'of', 7, True]
print(number_and_string)

#adding items to list
wizard_list.append('ber burp')
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

#removeing items from list
del wizard_list[5]
print(wizard_list)

#list arithmetic
print(numbers + strings)

list1 = [1, 2]
print(list1 * 5)

print(list1 / 2)

print(list1 - 1)













