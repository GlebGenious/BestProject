
word = input("Enter a word: ")
Dictionary = {}
for letter in word:
    if letter in Dictionary:
        Dictionary[letter] += 1
    else:
        Dictionary[letter] = 1
for letter in Dictionary:
    print(letter, Dictionary[letter])




