#################################################################
# Print every number from 1 to 100 in a new line.
# Print "fizz" instead of numbers for each floor of 3.
# Print "buzz" instead of the number for each floor of 5.
# Print "fizzbuzz" instead of numbers for numbers that are multiple of 3 and 5.
#################################################################

for i in range(0, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5:
        print("buzz")
    else:
        print(i)
