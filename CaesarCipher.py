# # # print(chr(65),chr(97),chr(90),chr(122))

def caesarCipher(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=char
 
    return result



print(caesarCipher('middle-Outz',2))