# 1. Write a script that takes a user input. Use conditional statements to identify the following:

input_num = input("Please input a number: ")

# Type casting to make sure the input is a number.
try:
    number1 = float(input_num)
except:
    number1 = input_num

try:
    number1 = int(input_num)
except:
    pass


if type(number1) == int or type(number1) == float: # Check if input is a number
    print("Your number is valid.")
    if type(number1) == int: # Check if input is an integer
        print("Your number is an integer.")
        if number1 % 2 == 0: # Check if input is even or odd
            print("Your number is even.")
            print("Your number is not prime.")
        else:
            print("Your number is odd.")
            if number1 <= 10: # Check if input is less than 10
                print("Your number is less than 10.")
                if number1 == 3 or 5 or 7: # Check if input is prime
                    print("Your number is prime.")
                else:
                    print("Your number is not prime.")
            else:
                print("Your number is larger than 10.")
    else:
        print("Your number is a decimal number.")
else:
    print("Not a valid number.")


# 2. Ask the user for another input. Add the two inputs together if they can be added. Otherwise, print the reason they can't be.

print("\nGive me two numbers to add.")
input2 = input("First number: ")
input3 = input("Second number: ")

# Type casting
try:
    number2 = float(input2)
except:
    number2 = input2

try:
    number3 = float(input3)
except:
    number3 = input3

# Adding the numbers together, checking for errors.
try:
    output2 = number2 + number3
    print(f"\n{input2} plus {input3} is equal to {output2}")
except:
    print("\nOne or more of your inputs were not numbers.")