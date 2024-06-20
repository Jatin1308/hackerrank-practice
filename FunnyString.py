

def funnyString(s):
    if len(s) <= 1:
        return "Not Funny"

    rev = s[::-1]
    currDiffList = []
    revDiffList = []

    for i in range(1, len(s)):
        currDiffList.append(abs(ord(s[i])-ord(s[i-1])))
        revDiffList.append(abs(ord(rev[i]) - ord(rev[i-1])))

    print(currDiffList,revDiffList)

    if (currDiffList == revDiffList):
        return "Funny"
    
    return "Not Funny"
    

    



test = ["ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq",
"holtm",
"uvzxrumuztyqyvpnji",
"tmruzxzuwoskqysxztuvosuyrswrnmtxvzsrqwytzrxpltrwusxupw",
"wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv",
"yrzxrxskrtlpwpmtpxvowrxrpxq",
"pryumtuntmovpwvowslj",
"nosklrxrtyuxtmnurzsryuxtywqwqpxts",
"fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury",
"jkmsxzwrxzy"]

for i in range(len(test)):
    print(funnyString(test[i]))


# print(funnyString("uvzxrumuztyqyvpnji"))