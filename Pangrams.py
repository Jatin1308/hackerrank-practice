def checkPangram(s):
    import string
    s = s.lower()
    
    uniq = set(s)
    l = string.ascii_lowercase
    for char in uniq:
        l = l.replace(char,'')

    if len(l) == 0:
        return "pangram"
    return "not pangram"
        


print(checkPangram('We promptly judged antique ivory buckles for the next prize'))
print(checkPangram('We promptly judged antique ivory buckles for the prize'))