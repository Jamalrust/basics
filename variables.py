print("Hello World!")
# this is comment line
# variable - storage while code runs, varname = value
# note: name should be
# 1. should not start with numbers
# 2. start with lower case letter
a = 45  # number, integer (data type)
b = 6.87  # number , float, double (data type)
name = 'jamal'  # text , i.e. string (data type)
msg = "Hello, this is my first coding practice!!!!!!!!"  # string

print(a)
print(b)
print(name)
print(msg)

a = 90
print(a)
print(a)
print(a)
print(a)
print(a)

a = 1000
print(a)
print(a, b, name, msg)
print('i am printing the variables', a, b, name, msg)
# PEP8 - phyton best practices (in coding) guidlines
print(a + b)
print('summing the a nd b', a + b)
print(name + ' ' + msg)
a = a + 1
print(a)
# length_of_persons_name - snake case
# print(c) 'unknown variable which is not assign wit value' you will get NameError since this is not defined yet
# useful functions for strings
# 'title case' - calls each name with upper case
print("# title(), upper(), lower(), islower(), isupper()")
print('before title', name)
print('name with title:', name.title())
print('name after title', name)
print(name.islower)
print(name)
print(name)
print(name.title())
print('using is lower:', name.islower())
# it will say variables is true or false
print("# concatenation")
print("my message: " + name + ', ' + msg)
print("my message: " + name.title() + ', ' + msg.upper())
name = "john doe"
print(name.islower())
print(name.lower())
print(name.upper())
print("#concatination")
print("my message: " + name + ", " + msg)
print("my message: " + name.upper() + ", " + msg)
print("Special characters : \\t  \\n")
print("my message: \t\t\t" + name.title()+',\n\t'+msg.upper())
## \n \t this is also calles invisible character
## \t   -> it means tab/ space
## \n   -> it mean next/ new line
print("Message to everyone: \n\t\t PLEASE HAVE FUN!!!")


location = '   \thawai\n\t'
print(location)
print('my weding venue: ' +location.strip().title()+' islands')
## strip - is just deletes side spaces and extra lines (whites space)
## You can do double string if needed "+location.strip().title()"


print("########## WORKING WITH NUMBERS ###########")
num1 = 3
num2 = 8
print("addition: ", num1 + num2)
print("subtraction: ", num1 - num2)
print("multiplication: ", num1 * num2)
print("division: ", num1 / num2)
print("exponent: ", num1 ** 2)
print("exponent: ", 3 ** 2)
print("floor division: ", 30 // num1)  ## Floor Division shows how many num1(3) in 10
print("modulo: ", 20 % num1) # it will show what is the remainder after division

#  find odd numbers 20-50 -> 21 (21=2*10 + 1), 23 (23=2*11 + 1)
# if n%2 return 1 the n is odd number (pseudocode)
# if n%2 return 1 the n is odd number (pseudocode)
print("#### str(expression), converts expression to a string")
print("addition: :" + str(num1+num2))
print("#### int(expression), converts expression to a integer, if possible")
num3 = "456" # Even if its number still string because its in a Quotation ## This is a string data type
num4 = 45.7566
print('addition with num3: ',num1+int(num3))
print('converted to int:', int(num4)) # it won't round it, just takes main part of it.

print('### there is Round function you can use it round if needed')
print('converted to int:', int(round(num4)))
status = True # this is a boolean value (True/False)
newstat = False

# Summary:
# variable (naming), values string, int, float, double, boolean(Trues Or False), Primitive data type
# string : remember how to (concatinate), upper(), lower(), str(), '\n', '\t'
#umbers: int, float/double, int(), +, *, /, **, //, %