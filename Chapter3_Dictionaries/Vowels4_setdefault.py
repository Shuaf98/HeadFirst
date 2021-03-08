#Displaying dictionaries to show only keys with values.
vowels = ('a', 'e', 'i', 'o', 'u')
word= input("Whats the word to check?")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1
for k, in sorted(found):
    print(k, ' was found ', found[k] , ' times')

