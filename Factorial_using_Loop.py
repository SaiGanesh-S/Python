#user input as integer
n = int(input('Enter Factoial Number:  '))

#initilise factorial value
factorial = 1

#loop to get factorial value for n
for i in range(1,n+1):
	factorial*=i

#print factorial value of n
print('Factorial For ',n, ' is ',factorial)
