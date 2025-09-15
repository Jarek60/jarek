#homework1.py
 # --- Variables and Datatypes ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex, a complex number with imaginary part of 3

d = "hello"
print(d)
print(type(d)) # d is a string, characters enclosed in quotes

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, ordered sequence of elements enclosed in square brackets

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, collection of key-value pairs enclosed in curly braces

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, ordered immutable sequence of elements

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, ordered changeable collection enclose in square brackets

i = True
print(i)
print(type(i)) # i is a boolean, represents truth values so true and false

j = None
print(j)
print(type(j)) # j is a NoneType, absence of value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, different types of data and square brakets

l = str(14)
print(l)
print(type(l)) # l is a string, str converts data into string

m = 1e4
print(m)
print(type(m)) # m is a float, 1*10^4 so scientific notation

"""
1. 9 datatypes
2. integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
3. b and m are floats, d and l are string, e h adn k are list
4. 1 wasn't an integer because it wasn't alone, it was either multiplied with somenthing, in a list with other things, in a function or a decimal point. str() converts the data into a string. 1 was a float.
5. A range, an immutable seuence of numbers.
"""

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 9 isnt equal to 10
print(10 <= 9) # False, 10 is not less than or equal to 9
bool("abc")
bool(123)
bool(["apple","cherry", "banana"])
bool(True)
bool(False)
bool(0)
bool("")
bool(" ")
bool(())
bool([])
bool({})
bool(True and False)
bool(True and True)
bool(False and False)
bool(True or False)
bool(True or True)
bool(False or False)
bool(not(False))
bool(not(True))