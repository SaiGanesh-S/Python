def anagram(s1, s2):
    j1 = s1.replace(' ', '').lower()
    j2 = s2.replace(' ', '').lower()

    # Edge check
    if len(j1) != len(j2):
        return False
    count = {}
    for L in j1:
        if L in count:
            count[L] += 1
        else:
            count[L] = 1

    for L in j2:
        if L in j2:
            count[L] -= 1
        else:
            count[L] = 1

    for i in count:
        if count[i] != 0:
            return False
    return True


def anagram1(s1, s2):
    j1 = s1.replace(' ', '').lower()
    j2 = s2.replace(' ', '').lower()

    return sorted(j1) == sorted(j2)


def anagram2(s1, s2):
    j1 = s1.replace(' ', '').lower()
    j2 = s2.replace(' ', '').lower()
    if len(j2) == len(j1):
        for i in range(len(j1)):
            if j1[i] not in j2:
                return False
            if j1[i] in j2 and j1[i] == j1[-1]:
                return True
        return True
    else:
        return False


print(anagram('123', '1 2  3'))
