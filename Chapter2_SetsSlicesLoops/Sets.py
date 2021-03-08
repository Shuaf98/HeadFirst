#This will search the word for vowels and check them
vowels = ['a', 'e', 'i', 'o', 'u']
word = "milliways"
for letter in word:
    if letter in vowels:
        print(letter)
#'letter' could be any variable, like x. When 'for...in...' is checking strings,
#python knows to search/go through each letter one by one. So through each iteration,
#letter (our x) gets assinged to a different letter in the word, and then that
#letter is checked to see if its in the vowel set.
