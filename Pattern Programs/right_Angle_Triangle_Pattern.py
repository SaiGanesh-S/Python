# user input int value
n = int(input('Enter the value: '))

# outer loop for the columns and inner loop for the rows
for i in range(n):
    for j in range(i+1):
        print('# ', end=" ")

    # After completion of a row to go to new line
    print()
