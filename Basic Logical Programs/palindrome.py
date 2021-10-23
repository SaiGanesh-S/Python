# user input as string
user_input = input('Enter the String : ')

# condition to check Palindrome
if user_input == user_input[::-1]:
    print(user_input, ' is Palindrome')
    print(user_input, ' = ', user_input[::-1])

else:
    print(user_input, ' is Not Palindrome')
    print(user_input, ' != ', user_input[::-1])
