cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw' and 3 == 5:
        print(f'car values was bmw so we are doing Upper() print: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() print: {car.title()}')

# car = 'tesla'   # assigning the 'tesla' as value of car variables
# car == 'bmw'  # comparing the value of car value with 'bmw' stiring, this expression results in True

# Expression: return True/False
name = 'john'
num = 45.55
is_good = True
friends = []

# name == 'jane'  # False, checking if the value of the name var is equal to
# name > 'abc'  # A-Z  (a,b, .... j...), true
# num == 45 # false
# num < 45 # False
# num <= 45 # False
# num >= 45 # True
# num > 45 # True
# is_good == False # false
# # name.lower() != 'jane' # true, Jane, jAne, JANE, janNe

# Multiple condition with AND/OR
# name == 'john' and num >45 # True and True >> True
# name == 'john' and num < 45 # True and False >> False
#
# name == 'john' or num > 45  # True or True >> True
# name == 'john' or num < 45  # True or False >> True
# name == 'jane' or num < 45  # False or False >> False

if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this means is empty list')
# friends is not empty list
# cars = ['audi', 'bmw', 'subaru', 'toyota']
print("-----------------------")
print(cars)
if 'tesla' in cars:
    print(f'cars list includes tesla')
else:
    print(f'tesla is not in the car list.')

# H/W Exercise: 5-1, 5-2
