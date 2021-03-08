panic = "Don't panic"
paniclist = list(panic)

print(paniclist)
for i in range(3):
    paniclist.pop()
    print(paniclist)

New_phrase = ''.join(paniclist[1:3:])
New_phrase = New_phrase + ''.join(paniclist[5]) + ''.join(paniclist[4])+ ''.join(paniclist[7]) + ''.join(paniclist[6])

print(New_phrase)


paranoid_android = "marvin"
list = list(paranoid_android)
for i in list:
    print('\t', i)

p_android = "Marvin, the paranoid android"
list = p_android
for i in list[:6]:
    print('\t' , i)
for i in list[12:20]:
    print('\t'*2, i)
for i in list[-7:]:
    print('\t'*3, i)
    
    
    
