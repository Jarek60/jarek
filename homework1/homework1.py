#homework1.py
 # --- Variables and Datatypes ---

# --- Variables and Data Types ---

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

# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 9 isnt equal to 10
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) #True,
print(bool(123)) #True
print(bool(["apple","cherry", "banana"])) #True,
print(bool(True)) #True,
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False)) #False
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False

"""
1. The lines with nothing in them, not even a space were false and most of the lines with soemthing in them there was a true unless the word false was major in that line.
2. The Tre and false line suprised me as it was false.
3. bool(56) should reutrn true since as seen above the lines with single numbers or strings in them return true.
4. bool('') should return false as the lines with nothing in the parantheses reutrns false.
"""

# --- Operators ---

    # --- Arithmetic Operators ---

print(10 + 5) #15, performs addition
print(10 - 5) #5, performs subtraction
print(2 * 4) #8, performs multiplication
print(6 / 3) #2, performs division
print(5 % 2) #1, returns the remainder of division
print(3 ** 2) #9, raises to the power of the second number
print(15 // 2) #7, performs division and rounds to the nearest integer

    # --- Comparison Operators ---

print(5 == 2) #False, compares for euqality
print(10 != 10) #False, compares for non equality
print(2 < 5) #True, compares for less than
print(12 > 5) #True, compares for greater than
print(5 <= 6) #True, compares for less than or equal to
print(1 >= 10) #False, compares for greater than or equal to

    # --- Assignment Operators ---

x = 5
x += 5 #10, performs addition and the sum becomes x
print(x)
x -= 4 #6, performs subtraction to previous x and difference becomes x
print(x)
x *= 3 #18, performs multiplication to previous x and multiple becomes x
print(x)

    # --- Logical Operators ---
'''
The operator and makes two arguments have to be true or occur at the same time. (x == x and x > x) should be false.
The operator or makes one of two arguments have to be true. (x < x or x > x) should be false.
The operator not makes returns the opposite of the result from the function given. (not x == x) would be false.

1. The difference between / and // is that // rounds the quotient to the nearest integer.
2. The difference between % and // is that // rounds the quotient and % gives the remainder of the of the quotient.
3. You would use % to calculate the remainder. 7 % 2 gives 1 as the remainder.
4. Assignment operators rquire a variable and when the operator is resolved they assign x to the new value from the expression.
'''
# --- String ---

my_string = "hello"
print(my_string) #prints: hello
print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) #prints: el
print(my_string[0:5:2]) #prints: hlo
print(len(my_string)) #prints: 5
print(my_string + "goodbye") #prints: hellogoodbye
print(my_string * 7) #prints: hellohellohellohellohellohellohello

'''
1. slicing takes subsections of the things in a list or string. In this case it's the letters in hello.
2. name = "Oski" print("Hello, my name is", name) results in Hello, my name is Oski being printed.
3. name = "Oski" print(f"Hello, my name is {name}") also results in Hello, my name is Oski being printed.
4. The difference bwteen the last two strings is that the f-string is a more concise and efficient way of putting expression in your strings using the {} brackets.
'''

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# List. Use it to list the contents of a directory.
# Example: ls

# ls -a
# List all. Use it to list all files including the hidden files.
# Example: ls -a

# mkdir
# Make directory. Use it to make a folder where you are in the terminal.
# Example: mkdir Book.py

# cat
# Use it to print the contents of your file in the terminal without running the code.
# Example: cat Book.py

# pwd
# Print working directory. Use it to show where in the terminal you are going from the main directory to the file or directory you are in.
# Example: pwd

# cd ..
# change directory ... Use it to go to the parent directory of the file/directory you are in.
# Example: cd ..

# cd .
# Change directory .. Use it to stay in the directory you are in.
# Example: cd .

# cd ~
# Change directory ~. Use it to go straight to the home directory.
# Example: cd ~

# cp
# Copy. Use it to copy files.
# Example: cp Book.py

# mv
# Move files. Use it to move files and directories into other directories.
# Example: mv Book.py Jarek/

# rm
# Remove. Use it to remove and delete files.
# Examples: rm Book.py

# clear
# Clear. Use it to clear the terminal screen.
# clear_screen()

# grep
# Use it to print lines in your code with specific patterns or words.
# Example: grep Coding Book.py

'''
1. Touch is used to make a new file in the directory you're in, touch book.py. Nano is used to modify code lines in the designated file from the terminal, nano book.py. Python3 is used to run your code in the terminal, python3 book.py.
2. The difference between ls and ls -a is that ls -a shows all files including hidden files.
3. Hidden files are not shown by ls command and sometimes begin with a dot.
4. -i is a flag for grep tp be case insenstive when searching, grep -i CODE Book.py. -R for ls used for listing all files in subdirectories, ls -R. -r for rm used for deleting a folder and all its contents, rm -r.
'''
