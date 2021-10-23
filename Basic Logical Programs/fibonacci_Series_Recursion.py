# recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


# user input as int
user_input = int(input('Enter the value: '))

# loop to call the recursive function
for i in range(user_input):
    print(fibonacci(i), end=" ")
