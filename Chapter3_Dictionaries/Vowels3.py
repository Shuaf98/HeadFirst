vowels = ['a', 'e','i', 'o', 'u']
word = input('Whats the word')

#adding without values
dict = {}
dict['a']= 0
dict['e']= 0
dict['i']= 0
dict['o']= 0
dict['u']= 0


for z in word:
    if z in vowels:
        dict[z]+=1
for x, y in sorted(dict.items()):
    print(x, ' is ', y)

#If we just want to add to dictionary when there are values.
dict = {}
for z in word:
    if z in vowels:
        if z not in dict:
            dict[z] = 0
        dict[z]+=1
for x, y in sorted(dict.items()):
    print(x, ' is ', y)