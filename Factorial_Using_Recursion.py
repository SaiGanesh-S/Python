# user input as int
n = int(input('Enter the Factorail Number  :'))

# define a function for recuresion


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# call the function
output = factorial(n)

# print the output
print('Factorial For ', n, ' is ', output)
