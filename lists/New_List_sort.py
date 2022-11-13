# Chapter 3 : List sort

cars = ['tesla', 'bmw', 'moskvich', 'lexus']
print("Performing sorting - sort().")
print("list before sorting", cars)
cars.sort()  # Sorting in Ascending order # It's sorting in alphabetic order
print("list after sorting:",cars ) # Once you .sort in further executions it will pop up in run tab as sorted result.

names = ['john','jane','mark']
print('List before sorting:',names)
names.sort(reverse=True)  # sorting in descending order
print('List after sorting:',names)

print('Sorting temporarily - sorted()')
cars_models = ['model x', '550 xi','corolla', 'camry']
sorted_car_models_asc = sorted(cars_models)
sorted_car_models_desc = sorted(cars_models, reverse=True)
print("car models after sorting: ", cars_models)

print("sortedcar models after sorting in Ascending order: ", sorted_car_models_asc)
print("sortedcar models after sorting in Descending order: ", sorted_car_models_desc)

print('Reversing the list without sorting: ')
nums = [6,3,9,7,10]
print("List before reversing: ", nums)
nums.reverse()
print('List after reversing: ', nums)

# example
# unsorted List of number 10Mln nums =
# print largest and smallest number
# nums.sort()
# print('smallest number: ', nums[0])
# print ('largest number: ', nums[-1])

print("Numbers of elements in the list with len()")
print("number of elements in the nums list: ",len(nums))
print("number of elements in the cars list: ",len(cars))
print("number of elements in the cars_models list: ",len(cars_models))
# H/W 3-8/ 3-9/ 3-10.
print('==============HW================')

## H/W 3-8
locations = ['baku','paris','moscow','amsterdam','ibiza']
print(locations)

sorted_cities_asc = sorted(locations)
print(locations)

sorted_cities_desc = sorted(locations, reverse=True)
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

print("## H/W 3-9")

print(f'number of cities which is planned to visit', len(locations))