import re


def hackerrankInString(s):
    requiredString = 'hackerrank'
    reqCounter = 0
    collected = ''

    for i in range(len(s)):
        if reqCounter < 10 and s[i] == requiredString[reqCounter]:
            collected+=s[i]
            reqCounter+=1
    return 'YES' if collected == requiredString else 'NO'




print(hackerrankInString('knarrekcah'))
print(hackerrankInString('hackerrank'))
print(hackerrankInString('hackeronek'))
print(hackerrankInString('abcdefghijklmnopqrstuvwxyz'))
print(hackerrankInString('rhackerank'))
print(hackerrankInString('ahankercka'))
print(hackerrankInString('hacakaeararanaka'))
print(hackerrankInString('hhhhaaaaackkkkerrrrrrrrank'))
print(hackerrankInString('crackerhackerknar'))
print(hackerrankInString('hhhackkerbanker'))