'''
CREATING STRINGS
'''
fred = "Why do gorillas have big nostrils? Big fingers!!"
print(fred)

fred = 'What is pink and fluffy? Pink fluff!!'
print(fred)

fred = "How do dinosaurs pay their bills?'
fred = "How do dinosaurs pay their bills?

# multi-line string
fred = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
print(fred)

'''
Handling Problems with Strings
'''
silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
silly_string = "He said, "Aren't can't shouldn't wouldn't.""
silly_string = '''He said, "Aren't can't shouldn't wouldn't."'''

# escaping
single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""
print(single_quote_str)
print(double_quote_str)

'''
Embedding Values in Strings
'''
myscore = 1000
message = 'I scored %s points'
print(message % myscore)

joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2

# multiple place holders
nums = 'What did the number %s say to the number %s? Nice belt!!'
print(nums % (0, 8))

# more examples in extension

'''
Multiplying Strings
'''
print(10 * 'a')

# see myletter.py

print(1000 * 'snirt')

'''
Lists Are More Powerful than Strings
'''
wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
print(wizard_list)

wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)

# index position
print(wizard_list[2])

# change list element
wizard_list[2] = 'snail tongue'
print(wizard_list)

print(wizard_list[2:5])

some_numbers = [1, 2, 5, 10, 20]
some_strings = ['Which', 'Witch', 'Is', 'Which']
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
print(numbers_and_strings)

# lists might even store other lists:
numbers = [1, 2, 3, 4]
strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
mylist = [numbers, strings]
print(mylist)

'''
Adding Items to a List
'''
wizard_list.append('bear burp')
print(wizard_list)

wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')

'''
Removing Items from a List
'''
del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

'''
List Arithmetic
'''
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)

list1 = [1, 2, 3, 4]
list2 = ['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
list3 = list1 + list2
print(list3)

list1 = [1, 2]
print(list1 * 5)

# division (/) and subtraction (-) give only errors
list1 / 20
list1 - 20

# The same goes for adding anything other than a list to a list.
list1 + 50

# extension: size of a list
print(len(list1))


'''
Tuples
'''
fibs = (0, 1, 1, 2, 3)
print(fibs[3])

fibs[0] = 4
#TypeError: 'tuple' object does not support item assignment

'''
Python Maps Won’t Help You Find Your Way
'''
favorite_sports = ['Ralph Williams, Football',
'Michael Tippett, Basketball',
'Edward Elgar, Baseball',
'Rebecca Clarke, Netball',
'Ethel Smyth, Badminton',
'Frank Bridge, Rugby']

favorite_sports = {'Ralph Williams' : 'Football',
'Michael Tippett' : 'Basketball',
'Edward Elgar' : 'Baseball',
'Rebecca Clarke' : 'Netball',
'Ethel Smyth' : 'Badminton',
'Frank Bridge' : 'Rugby'}
print(favorite_sports['Rebecca Clarke'])

del favorite_sports['Ethel Smyth']
print(favorite_sports)

favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)

# Joining maps doesn’t make sense to Python
favorite_sports = {'Rebecca Clarke': 'Netball',
'Michael Tippett': 'Basketball',
'Ralph Williams': 'Ice Hockey',
'Edward Elgar': 'Baseball',
'Frank Bridge': 'Rugby'}
favorite_colors = {'Malcolm Warner' : 'Pink polka dots',
'James Baxter' : 'Orange stripes',
'Sue Lee' : 'Purple paisley'}
favorite_sports + favorite_colors

