# Create a function
def print_x_times(parameter = "loop", loop_ammount = 5):
    counter = 0
    # print(global_var)
    while counter < loop_ammount:
        print(counter, parameter)
        counter += 1
    return "Return something"

def hypotenuse_calculator(side_a = 1, side_b = 1):
    hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
    return round(hypotenuse, 2)

# call
# print("print")
# global_var = "global variable"
# test = print_x_times("test", 2)
# print(test)

# print(hypotenuse_calculator(side_a = 5, side_b = 4))

# exercise
def shout(output_string = "hello", repitition_amount = 2):
    print(list(range(repitition_amount)))
    if(repitition_amount <= 10):
        for i in range(repitition_amount):
            print(output_string.upper())
    else: 
        print("you are to loud")
    return "done"

status = shout()
print(status)

# def souter(str, number):
#     counter = 0
#     while counter < number:
        
#         if(counter == 11):
#             print(counter, "you are too lound")
#         else:
#             print(counter, str.capitalize())
#         counter += 1

# souter("func", 15)