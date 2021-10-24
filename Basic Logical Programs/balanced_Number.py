# requirement
'''Balanced number is the number that * 
The sum of all digits to the left of the middle digit(s) and
the sum of all digits to the right of the middle digit(s) are equal*.'''

# sample testcase
'''(balanced-num 7) ==> return "Balanced"
(balanced-num 295591) ==> return "Not Balanced"
'''

# user_input as int
user_input = 424

# logic to seperate left and right and add them and check
if len(str(user_input)) > 2:
    if len(str(user_input)) % 2 != 0:
        mid = (len(str(user_input)))//2
    else:
        mid = ((len(str(user_input)))//2)-1

    left = 0
    right = 0

    for i in range(mid):
        left += int(str(user_input)[i])

    for i in range(mid):
        right += int(str(user_input)[::-1][i])

    if left == right:
        print('Balanced')
    else:
        print('Not Balanced')

else:
    print('Balanced')


# with function
string = str(user_input)
length = (len(string)-1)//2
same = len(string) < 3 or sum(
    map(int, string[:length])) == sum(map(int, string[-length:]))
if same:
    print('Balanced')
else:
    print('Not Balanced')
