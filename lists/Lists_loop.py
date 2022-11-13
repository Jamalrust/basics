## Chapter 4: Looping through the list

places = ['hawai', 'paris', 'bahamas', 'iceland']
# Loops - executing the code repetitively (what to loop through, how many times)
print("looping through entire list")
print(f"i want to visit {places[0]} next summer")
# for var_each_element in List_name:
# print('lines of code to be repeated')
print('we are looping trough places')
for place in places:
    # comment line
    print(place)
    print(f"i want to visit {place.title()} next summer")
    print(f"how far is the {place.title()} from New York")

print('ohhhh, i need to convince my wife now.')
# H/W 4-1, 4-2

print("#working with list of the numbers,range() functions")
# Working list of numbers, range() function
# range(5) -> 0, 1, 2, 3, 4
# range(2, 6) -> 2, 3, 4, 5
# range(4, 15, 3) -> 4, 7, 10, 13     ## (4, 15, 3) (first number[4] start, second[15] end, third[3] steps)
print(range(5))
print(list(range(5)))

for num in range(5):
    print(f'each number: {num}')
print("================================")

for num in range(2, 6):
    print(f'each number: {num}')
print('================================')

print("list all number between 21 and 36 that can be devided by 4")
for num in range(24, 36, 4):
    print(f'each number: {num}')
print('=================================')

print("# problem2: crate a list of squares of the numbers between 25 and 30")
num_squares = []
for num in range(25, 31):  # might be interview question
    print(f'num = {num} and square is: {num ** 2}')
    num_squares.append(num ** 2)
print("final list of squares", num_squares)

nums = [4, 2, 9, 10]
print(f'sum of the nums: {sum(nums)}')
starting = 0
for num in nums:
   sum = starting + num
print(sum)

print('============H/W===========')

## H/W 4-1
pizzas = ["cheese", 'peperoni', 'margarita']
for pizza in pizzas:
    print(f'I like',{pizza},'pizza')
print('I really love pizza.')

## H/W 4-2
animals = ['cat','lion','tiger']
for animal in animals:
    print(f'A '+animal,'would make a great pet.')
print('all these animals related to felidae group')

## H/W 4-3
for num in (range(21)):
    print(num)

## H/W 4-4
## for num in (range(1,1000001)):
##     print(num)

## H/W 4-5


##  H/W 4-8


## H/W 4-9 list comrehension - short form
cubes = [num ** 3 for num in range(1,11)]
print(cubes)
print(f'This is our new list:{cubes}')

cubes = []
for num in range(1,11):
    print(num**3)
    cubes.append(num**3)
