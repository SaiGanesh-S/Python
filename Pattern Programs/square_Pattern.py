# user input int value
n = int(input('Enter the value: '))

# outer loop for the columns and inner loop for the rows
for _ in range(n):
    for _ in range(n):
        print('# ', end=" ")

    # After completion of a row to go to new line
    print()
