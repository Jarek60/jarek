""" Lists """
# 3.1 List Operations
my_fav_foods = ["burger", "sushi", "taco", "ice cream", "fries"]
print(my_fav_foods[1])
print(my_fav_foods[-1])
my_fav_foods.append("pizza")
my_fav_foods.insert(0, "apple")
my_fav_foods.remove("sushi")
print(len(my_fav_foods))
for food in my_fav_foods:
    print(food.upper())
new_list = [my_fav_foods[0], my_fav_foods[-1]]
if "potato" in my_fav_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding
numbers = list(range(0, 21))
def get_first_15(numbers):
    return numbers[0:15]
def get_every_fifth(step1):
    return step1[::5]
def reverse_and_stride(step2):
    reversed_list = step2[::-1]
    return reversed_list[::3]
step1 = get_first_15(numbers)
step2 = get_every_fifth(step1)
step3 = reverse_and_stride(step2)
print(step1)
print(step2)
print(step3)

# 3.3 Nested Lists
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers[2][0], numbers[2][1], numbers[2][2])
print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested(numbers):
    total = 0
    for sublist in numbers:
        for num in sublist:
            total += num
    return total
print(sum_nested(numbers))

# 3.4 Create a 5x5 List
# nested loop to create a 5x5 list of 1 to 25
my_list = []
for i in range(5):
    row = []
    for j in range(1, 6):
        row.append(i * 5 + j)
    my_list.append(row)
One_to_25 = my_list
print(One_to_25)

# all multiples of 3 in list as ?
def replace_multiples_of_3(One_to_25):
    multiples_of_3 = []
    for row in One_to_25:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        multiples_of_3.append(new_row)
    return multiples_of_3
result = replace_multiples_of_3(One_to_25)
print(result)

# Sum of all non ? numbers in the modified list
def sum_of_integers(multiples_of_3):
    Sum = 0
    for row in multiples_of_3:
        for item in row:
            if item != "?":
                Sum += item
    return Sum
print(sum_of_integers(result))

""" 4 Dictionaries """
# 4.1 Dictionary Operations
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
# Change Mira's age to 100
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(f"{name} is {age} years old.")

