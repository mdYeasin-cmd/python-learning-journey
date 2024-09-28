# f strings
# user_name = "Nazmul Islam"
# user_age = 30
# user_information = f"{user_name} is {user_age} years old"
# bad_approach = user_name + " is " + str(user_age) + " years old" # bad approach
# print(user_information)

# single line if statements
# user_name = "Shifat"
# user_age = 15
# user_status = "Adult" if user_age >= 18 else "Child"
# if user_age < 18:
#     user_status = "Child"
# else:
#     user_status = "Adult"
# print(f"{user_name} is {user_age} years old. The person is a {'adult' if user_age >= 18 else 'child'}.")

# list comprehension
# simple_list = [f"{j}{i}" for i in range(0,11,1) for j in ("a", "b", "c") if j == "a"]
# for i in range(0, 11, 1):
#     simple_list.append(i)
# print(simple_list)

# lamda functions
# def double_value(num):
#     return num * 2

# double_value = lambda num: num * 2
# print(double_value(23))

# some functions want a function as an argument
# random_list = [0, 3, 1, 4, 5, 8, 9, 10, 49]
# sorted_list = sorted(random_list)
# print(sorted_list)

# random_list = [('Anna', 23), ('Paul', 30), ('Shifa', 22)]
# sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
# print(sorted_list)

# exercise
# battleship_board = [f"{j}{i}" for i in range(1, 6, 1) for j in ("A", "B", "C", "D", "E") if not (j == "C" and i == 3)]
# print(battleship_board)

battleship_board = [f"{letter}{num}" for letter in ("A", "B", "C", "D", "E") for num in range(0,6) if f"{letter}{num}" != "C3"]
print(battleship_board)