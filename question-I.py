#################################################################
# Print every number from 1 to 100 in a new line.
# Print "fizz" instead of numbers that can be divisible to 3.
# Print "buzz" instead of numbers that can be divisible to 5.
# Print "fizzbuzz" instead of numbers that are multiple of 3 and 5.
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
