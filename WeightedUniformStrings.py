def weightedStrings(s):
    d ={}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char]+=1
    
    for val in d.values:
        


weightedStrings('abbcccdddd')