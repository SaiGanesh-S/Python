# user input as int
user_input = int(input('Enter the number: '))

# initilize first and second value
first, second = 0, 1

# printing first two values because its default
print(first, second, end=" ")

# loop to print fibonacci series till n(user input)
for i in range(user_input-2):
    third = first+second
    print(third, end=" ")
    first, second = second, third
