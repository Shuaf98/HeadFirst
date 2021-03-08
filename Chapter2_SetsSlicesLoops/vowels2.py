vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Which word do you want to search for?")
found = []
#Here, we want the code to not print duplicates. We do this by making another list
#which only holds each vowel once. WE do this through a 'not in'.
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)



