#We want to turn Don't Panic into On Tap
panic = "Don't panic"
paniclist = list(panic)

#This removes the last 3 letters
print(paniclist)
for i in range(3):
    paniclist.pop()
    print(paniclist)

#This removes the D
paniclist.pop(0)
paniclist.remove("'",)
#This swaps the p and a
paniclist.extend([paniclist.pop(), paniclist.pop()])
print(paniclist)
#this swaps the space after the t and puts it in front of the n
paniclist.insert(2, paniclist.pop(3))
print(paniclist)
New_phrase = ''.join(paniclist)
#The '' is just a seperator, has no meaning.
print(New_phrase)



#Now, we will do the same thing, just with slicing.
#We want to turn Don't Panic into On Tap




