# if statements
# if 5 < 4:
#     print("Correct result!")
# elif 3 == 3 and 5 > 1:
#     print("Some other result")
#     if len([1, 2, 3]) > 2:
#         print("List is long enough")
# else:
#     print("Incorrect result!")

# while loop
# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         print("Counter is 5")
# print("while loop has finished")

# for loop
# test_list = { 1:2, 3:4, 2:2 }
# for k, v in test_list.items():
#     print(k)
#     print(v)

# truthy and falsy
# if 0:
#     print("truthy")
# else:
#     print("falsy")

# exercise
# a_list = [1, 2, 3, 4, 5]
# for value in a_list:
#     if value == 2:
#         print('the value is 2')
#     elif value == 5:
#         counter = 0
#         while counter <= 5:
#             print('last items')
#             counter += 1
#     else:
#         print("the value is not 2")

exercise_list = [1, 2, 3, 4, 5]
exercise_counter = 0
for x in exercise_list:
    if x == 2:
        print('the value is 2')
    else: 
        print('the value is not 2')
while exercise_counter < 6:
    print('last item')
    exercise_counter += 1