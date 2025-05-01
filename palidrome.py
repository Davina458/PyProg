def isPalidrome(word):
    word = ("".join(word.split())).lower()
    return True if word == word[::-1] else  False
        


print(isPalidrome("RaceAr"))


