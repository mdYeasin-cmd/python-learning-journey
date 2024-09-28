# functions
# print("a value")
# print(input("ask for a value"))

# methods -> functions of datatypes
# print("value".lower())
# print("VALUE".upper())
# print("value".replace("v", "V"))

# new functions
# print(abs(-9))
# print(max(10, 6, 34))
# print(min(10, 6, 34))
# print(len("Test"))

# import math

# a, b = input("Enter height and width values: ").split()

# num_a = int(a)
# num_b = int(b)

# c = math.sqrt(num_a * num_a + num_b * num_b)
# print(c)

# pythagoras theorem
side_a = int(input("The width of the triangle: "))
side_b = int(input("The height of the triangle: "))
hypotenuse = (side_a ** 2 + pow(side_b, 2)) ** (1/2)
print("The hypotenuse is:", round(hypotenuse, 2))