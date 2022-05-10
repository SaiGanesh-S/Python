# Problem Description -:  Given two non-negative integers n1 and n2, where n1<n2.
# The task is to find the total number of integers in the range [n1, n2](both inclusive)
#  which have no repeated digits.

# function to find the non repeating digit number in the givenrange

def find(n1, n2):
    count = 0
    for i in range(n1, n2+1):
        num = i
        rep = []
        for j in range(len(str(num))):
            digit = num % 10
            if digit in rep:
                break
            rep.append(digit)
            num //= 10
        if num == 0:
            count += 1
    return count


if __name__ == "__main__":
    n1, n2 = int(input()), int(input())
    print(find(n1, n2))
