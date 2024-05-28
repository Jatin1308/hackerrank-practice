# using itertools module


def alternate(s):
    import re
    from itertools import combinations

    myset = set(s)
    if len(myset)<2:
        return 0
    
    if len(s) < 2 and len(myset) == len(s):
        return 2

    res = 0
    pattern = r'^(.)(?!\1)(.)(\1\2)*\1?$'

    combs = list(combinations(myset,2))

    tmp = s

    for comb in combs:
        tmp = s
        for char in comb:
            tmp = tmp.replace(char,'')

        if bool(re.match(pattern,tmp)):
            res = max(res,len(tmp))
    return res

print(alternate('beabeefeab'))