#Reporting on unique vowels, using lists
vowels = ['a', 'e', 'i', 'o', 'u']
word= input("Whats the word to check?")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)

#Reporting on unique values, using sets
vowels = set('aeiou')
word = input("Whats the word to check?")
Intersection =  vowels.intersection(word)
for x in Intersection:
    print(x)

