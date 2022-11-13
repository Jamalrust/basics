# Chapter 6: Dictionary - data structure (key-value pair)

# creating the empty dictionary
person1 = {}
person2 = dict()
language_list = ['eng', 'ru', 'esp', 'marsian']
person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny',
           'cars': ['audi', 'bmw', 'subaru', 'toyota'],   # independent value
           'languages': language_list}  # two-way reference

# accessing the value (R)
# person1['name']

print(f"getting name of person1 {person1['name']} .... ")
print(f"getting age of person1 '{person1['age']}' .... ")

print("#### 3. adding/updating key value pair to the dictionary (U)")
person1['phone'] = '(123) 456-7891'
# phone does not exist in keys in person1 dictionary, so it adds new key-value pair (element)
print('Updated with new key dictionary: ',person1)
print("updating the value of 'age' in the person1 dictionary.")
person1['age'] = 30 # pay attention that you are mentionig the existing key
print('Update age person1 dictionary: ', person1)
print('updating the list value inside the dictionary')
# cars[0] = 'merc'
person1['cars'][0] = 'merc'
print('Updated list (audi to merc) in person1 dictionary: ', person1)

# language_list = ['eng', 'ru', 'esp', 'marsian']
print("updating the list lamguage_list (marsian to ger)...")
language_list[3] = 'ger'
print('update list:', language_list)
print('Dictionary:', person1)

print("updating the value of  the list in the dictionary...")
person1['languages'][2] = 'french'
print('updated list: ', language_list)
print('dictionary:', person1)

# copying the list to a  value of the dictionary (independent values)
# language_list = ['eng', 'ru', 'esp', 'marsian']
# person1['languages'] = Languages_list[:]
# print(person1)

print('##### 4. Delete key-value pair from the Dicitionary (D) ')
print('Deleting the location key-value pair from person1.....' )
del person1['location']
print("update person1 Dictionary: person1")
person1['age'] = None # no value, Like Null in sql
print("updated age in person1 dictionary: ", person1)

# exercise : 6-2 Favorite Numbers
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
# print each person's name and their favorite number.
print(f"Nicoles's favourite number is : {fav_nums['nicole']}")
print(f"Alex's favourite number is : {fav_nums['alex']}")
