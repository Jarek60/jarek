""" 3 Print Functions """
# prints goodbye message
def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Jarek")

# print area of circle given a radius
def area_of_circle(radius):
    print(3.14*radius**2)
area_of_circle(5)

""" 4 Return Functions """
# subtracts two numbers and returns the result
def subtract(x, y):
    return x - y
print(subtract(10, 4))  # Example usage

# multiplies two numbers and returns the result
def multiply(x, y):
    return x * y
print(multiply(3, 7))  # Example usage

# divides two numbers and returns the result
def divide(x, y):
    return x / y
print(divide(20, 4))  # Example usage

""" 5 Consitionals """
# Takes list of temperatures and returns the minumum and maximum temperatures
def min_max_temps(list_of_temps):
    min_temp = min(list_of_temps)
    max_temp = max(list_of_temps)
    return (min_temp, max_temp)
print(min_max_temps([72, 85, 90, 78, 88, 95, 80]))  # Example usage

# Takes integer representing day of the weel and returns true for weekend
# true for weekend (6 or 7) and false for weekday (1-5)
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False
print(is_weekend(6))  # Example usage
    
# Takes miles and fuel used and returns miles per gallon
def fuel_efficiency(miles, gallons):
    mpg = miles / gallons
    return mpg
print(fuel_efficiency(375, 15))  # Example usage

# Takes integer and moves last digit to the front
def encrypted_date(num):
    num_str = str(num)
    encrypted_str = num_str[-1] + num_str[:-1]
    return int(encrypted_str)
print(encrypted_date(1234))  # Example usage

""" 6 Loops """
# Compute powers of a number using a loop
def x_to_the_y(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
print(x_to_the_y(2, 3))  # Example usage

# take a list of integers and use a for loop to give max and min
def min_max_loop(list_of_ints):
    max_value = list_of_ints[0]
    for number in list_of_ints[1:]:
        if number > max_value:
            max_value = number
    min_value = list_of_ints[0]
    for number in list_of_ints[1:]:
        if number < min_value:
            min_value = number
    return (min_value, max_value)
print(min_max_loop([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Example usage

# take a list of integers and use a while loop to give max and min
def min_max_while(list_of_ints):
    max_value = list_of_ints[0]
    min_value = list_of_ints[0]
    index = 1
    while index < len(list_of_ints):
        number = list_of_ints[index]
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
        index += 1
    return (min_value, max_value)
print(min_max_while([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Example usage

# Take an integer and return the sum of its digits
def sum_of_digits(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit)
    return total
print(sum_of_digits(2468))  # Example usage


# take a list of integers and use a for loop to give max and min
def min_max(list_of_ints):
    max_value = list_of_ints[0]
    for number in list_of_ints[1:]:
        if number > max_value:
            max_value = number
    min_value = list_of_ints[0]
    for number in list_of_ints[1:]:
        if number < min_value:
            min_value = number
    return (min_value, max_value)
result = min_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print(f"The maximum and minimum of the list [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] is {result}")  # Example usage