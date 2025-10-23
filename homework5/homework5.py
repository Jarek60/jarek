''' Vocabulary Review'''

# Git vs. GitHub: Git is in your terminal and is a version control system that allows you to track changes in your code. GitHub is a web-based platform that hosts Git repositories and provides collaboration features.
# Terminal vs. Command Line: Terminal is a program that provides a text-based interface to interact with the operating system. Command Line refers to the actual text interface where you type commands.
# Local vs. Remote Repository: Local repository is the version of your code stored on your computer. Remote repository is the version of your code stored on a server, such as GitHub.
# Version Control: Version control is a system that tracks changes to files over time, allowing you to revert to previous versions and collaborate with others.
# Staging Area: The staging area is a place where you prepare changes before committing them to the local repository.
# git add: git add is a command used to add changes in the working directory to the staging area.
# git commit: git commit is a command used to save changes from the staging area to the local repository with a descriptive message.
# git push: git push is a command used to upload local repository changes to a remote repository on GitHub.
# git status: git status is a command that shows the current state of the working directory and staging area, including which files are modified, staged, or untracked.
# git pull: git pull is a command used to fetch and merge changes from a remote repository into the local repository.
# pwd: pwd is a command that prints the current working directory.
# ls: ls is a command that lists the files and directories in the current working directory.
# cd: cd is a command used to change the current working directory.
# nano: nano is a command-line text editor used to create and edit files directly in the terminal.
# touch: touch is a command used to create an empty file or update the timestamp of an existing file.
# mv: mv is a command used to move or rename files and directories.
# rm: rm is a command used to remove files or directories.
# cat: cat is a command used to display the contents of a file in the terminal.

''' A directory tree '''
# You have been plopped into Judy’s directory system. What command will tell you what your current working directory is? pwd
# The terminal responds by saying you are in∼/python decal/judy decal. What command will list all the files in your current working directory? ls
# Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes? cd ../brianna_decal.git git pull
# How would you move this new homework.py to the homework/ folder in your personal repository? mv homework.py ../judy_decal/homework/
# How would you move yourself to the same repository as homework.py? cd ../judy_decal/homework/
# You want to see the contents of homework.py in your terminal, how would you do this? cat homework.py
# Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository? current working directory is? git add . git commit -m "Completed homework" git push
# Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?) git pull git push
''' ! [rejected] main -> main (fetch first)
error: failed to push some refs to ’https://github.com
/judy/judy_decal.git’
hint: Updates were rejected because the remote contains
work that you do
hint: not have locally. This is usually caused by another
repository pushing
hint: to the same ref. You may want to first integrate
the remote changes
hint: (e.g., ’git pull ...’) before pushing again.
hint: See the ’Note about fast-forwards’ in ’git push
--help’ for details.'''
# What absolute path will allow you to move to Recents/? /Users/Brianna/Recents/

''' Data Types '''
# Write a function that takes any input and returns a string indicating its data type.
def checkDataType(inputData):
    return type(inputData).__name__
# Example usage:
checkDataType(3.14) # float
checkDataType(True) # bool

''' Conditionals '''
# Write a function that takes an integer as input and returns ’Even’ if the integer is even, and ’Odd’ otherwise.
def evenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage:
evenOrOdd(7) # odd
evenOrOdd(10) # Even

''' Loops '''
# Write a function that takes a list of integers and returns their sum using a loop (do NOT use the built-in sum() function).
def sumWithLoop(intList):
    total = 0
    for num in intList:
        total += num
    return total
# Example usage:
numbers = [1, 2, 3, 4, 5]
sumWithLoop(numbers) # 15

''' Lists '''
# Write a function that takes a list and returns a new list with each element duplicated.
def duplicateList(inputList):
    duplicated = []
    for item in inputList:
        duplicated.append(item)
        duplicated.append(item)
    return duplicated
# Example usage:
duplicateList(["a", "b", "c"]) # ["a", "a", "b", "b", "c", "c"]

''' Debugging '''
# There’s an error in the following function that’s supposed to return the square of a number. Find and correct it:
# def square(num)
#    return num * num
def square(num):
    return num * num
# Example usage:
square(4) # 16
# The error was a missing colon at the end of the function definition line.

# Favorite Code
def sumWithLoop(intList):
    total = 0
    for num in intList:
        total += num
    return total
# Example usage:
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers)) # 15