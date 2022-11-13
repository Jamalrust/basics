# CHAPTER 5:Looping Through a Dictionary
# Dictionaries keys, only values, key and value

person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}
print('# default case, looping trough keys only -------')

for key in person1:
    print('key in this iteration is: ', key)


# Exercises 6-5 . Rivers: Make a dictionary containig three major rivers and the country
# each river runs through. one key-value pair might be 'nile': 'egypt'.
# . Use a loop to print a  sentence about each river, such as The Nile runs through Egypt.
# . use a loop to print the name of each river included in the dictionary.
# . Use a loop to print the name of each country included in the dictionary.

rivers_countries = {'nile': 'egypt',
                    'amazon': 'brazil',
                    'volga': 'russia',
                    'mississippi': 'usa',
                    'thames': 'uk'}