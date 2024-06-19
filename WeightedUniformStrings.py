def weightedUniformStrings(s,queries):
    if len(s)==0:
        return ["No"]*len(queries)
    

    i,j=0,1
    alphabet_dict = {}
    for i in range(26):
        alphabet_dict[chr(ord('a') + i)] = i + 1
    print(alphabet_dict)

    arr = []
    i = 0
    j = 1
    freqDict = {}
    if len(s) == 1:
            freqDict[alphabet_dict[s]] = True
    while i<len(s) and j<len(s):
        if i == 0:
            freqDict[alphabet_dict[s[i]]] = True
        
        if s[i]!=s[j]:
            if s[j] not in freqDict:
                freqDict[alphabet_dict[s[j]]] = True
            i = j
            j+=1
        else:
            if s[i:j+1] not in freqDict:
                freqDict[alphabet_dict[s[i:j+1][0]]*len(s[i:j+1])] = True
            j+=1
    
    print(freqDict)

    for i in range(len(queries)):
        if queries[i] in freqDict:
            queries[i] = 'Yes'
        else:
            queries[i] = 'No'

    return queries



# print(weightedUniformStrings("",[1,7,5,4,15]))

# print(weightedUniformStrings("aaaaaa",[1,4,7,3]))

print(weightedUniformStrings('l',[1,12]))

# print(weightedUniformStrings('abbcccdddd',[1,7,5,4,15]))
# print(weightedStrings('abcdeabcd',[1,7,5,4,15]))