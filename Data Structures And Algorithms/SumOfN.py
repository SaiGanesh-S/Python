# sum of N using Loop
# worst case
def sumn(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


sumn(10)  # o(n)

# sum of N using Formula
# Best Case


def sumn1(n):
    return (n*(n+1))//2


sumn1(10)  # o(1) constant
