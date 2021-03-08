#The following are different list functions to manipulate a list
list = [1,2,3,4]
print(list)

print("now lets remove")
list.remove(3)
print(list)

print("This is what pop does")
print(list.pop(1))
#pop removes from a list an object based off the index number,
#and returns the value removed. If you don't assign pop to a variable, it will
#be forgotten.

print("This is what extend does")
list.extend([2,3])
print(list)

print("Lets insert 2 after the 1")
list.insert(1, 2)
print(list)


