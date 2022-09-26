#target = k - number


def pair_sum(lst, total):
    if len(lst) < 2:
        return 'Invalid Input List'
    else:
        seen = set()
        result = set()

        for l in lst:
            target = total-l
            if target not in seen:
                seen.add(l)
            else:
                result.add((min(l, target), max(l, target)))
    print('\n'.join(map(str, result)))


ser = [1, 3, 2, 2]
pair_sum(ser, 4)
