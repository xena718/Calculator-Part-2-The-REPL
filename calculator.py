"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# input_string = 'pow 3 5'

# def calculator():
while True:
    input_S = input("Please provide your input:")
    # input_string = 'pow 3 5'
    input_L = input_S.split(" ")
    # print(input_split)
    # if len(input_L) >3
    # 1,2,3
    if input_L[0] == "q":
        break 
    num1 = float(input_L[1])
    if len(input_L) == 3:
        num2 = float(input_L[2])
    if input_L[0] == "+":
        output = add(num1, num2) 
    elif input_L[0] == "-":
        output = subtract(num1, num2) 

    elif input_L[0] == "*":
        output = multiply(num1, num2) 
            
    elif input_L[0] == "pow":
        output = power(num1, num2)
        # print(output)
    elif input_L[0] == "/":
        output = divide(num1, num2)
    elif input_L[0] == "mod":
        output = mod(num1, num2)
    ####
    elif input_L[0] == "square":
        output = square(num1)
    elif input_L[0] == "cube":
        output = cube(num1)

    print(output)






# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print(output)

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)

# Replace this with your code