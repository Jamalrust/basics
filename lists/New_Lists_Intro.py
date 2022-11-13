#  chapter 3: Data structure - storage to hold multiple values, manage (creat, add, update, remove
#  Python Data structures: Lists, Dictionary, (Set, Tuple)
#  [4, 10, 6] ['john', 'mark', 'jane'] [True, False, True]
#  Pycharm shortcut: ctrl + alt + l Autoformat the file
#  List is considered mutable object (we can make a change in the list)
#  Tuple - Immutable data Structure (DS) can not add or remove values after defining
friends = []  # empty list
players = list()  # it also creates a list

nums = [4, 10, 6]
names = ['john', 'mark', 'jane']
bool_values = [True, False, True]

print(nums)
print(names)
#  add elements, remove, update, read through values ( access each value)

print("### How to find specific value in variable")
print('Hi, ', names[0].title())  # .title we have for letter capitalization
print("Hi  ", names[-1].upper())  # .upper we have for full letter upper case
print("Hi  ", names[-1])  # this is the just execution as is

#  print('Hi, ', nanme[3].title()) # IndexError: List index out of range
#  we do not have [3] value in names. variable.
print("### adding th elements to the list")

#  Listname.appened(newvalue) - adds newvalue to the end of the list
names.append("alex")
print(names)
#Listname.Insert(index, value) - puts the 'value' to the 'index',
# other values shifter to the left
names.insert(0,"araz")
print(names)

names[-1] = 'benny' # updating the last elemnt of the list 'alex' -> 'benny'
print(names)

print("Removing the values from the list----------")
print("# removing elements by value : del Listname(index), removing 'jane' ")
del names[3]
print(names)
print("# removing elements by index : Listname.pop(), removing last in the list")
deleted_name = names.pop()
names.pop() # automatically deletes last value
print(names)
names.pop(0)
print(names)
print('we deleted following name:', deleted_name)

## --------------------------------------------------------------------------------------------
########### 10/16/22 #############
#EXERCISES:

guests = ['akmal', 'said', 'lenur']
print('Hello '+ guests[0].title() + ', I am inviting you to the party')  ## variation 1.
print(f'Hello {guests[0].title()}, I am inviting you to the party')      ## variation 2.
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')

# print(guests[1], 'I am inviting you to the party')
# print(guests[2], 'I am inviting you to the party')
## Hello Akmal, i'm inviting you to the party

print('## Removing Guest')
removed_guest = guests.pop(1)
## We removed 'said' with .pop function for assign to 'removed_guest' variable.

## now we have to make message for printing about said absence
## said can't make it to the party

print(f'{removed_guest.title()}, cant make it to the party')
###  f-stream help us to make it sentence whole string with variable whenever we use f-stream
## have to use variable in curly brackets {}
print(guests)
guests.append('max')
print(guests)

print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')

## hw Exercise 3-6, 3-7

guests.insert(0, 'jesica')
guests.insert(2, 'john')
guests.insert(5, 'jason')

print(f'Hello {guests[0].title()}, I found bigger table and inviting you to the party')
print(f'Hello {guests[2].title()}, I found bigger table and inviting you to the party')
print(f'Hello {guests[5].title()}, I found bigger table and inviting you to the party')

print(guests)

## I can only invite 2 people for diner

print(f'Sorry {guests.pop(0)}, i cant invite you to the party')
print(f'Sorry {guests.pop(1)}, i cant invite you to the party')
print(f'Sorry {guests.pop(2)}, i cant invite you to the party')
print(guests)

print(f'Sorry {guests.pop(0)}, i cant invite you to the party')


print(f'Hello {guests[0].title()}, you are still on my list and still invited')
print(f'Hello {guests[1].title()}, you are still on my list and still invited')
print(guests)
del(guests)[0]
del(guests)[0]
print(guests)


guests.append('jason')
guests.append('jacob')
print(guests)

del(guests)[0]

del(guests)[0]
print(guests)

print(f'number of guests', len(guests))
