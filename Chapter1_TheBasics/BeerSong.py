#BeerSong

for num_of_bottles in range(99, 0, -1):
    print(num_of_bottles, " bottles of beer on the wall,")
    print(num_of_bottles, " bottles of beer!")
    print("Take one down, pass it around,")
    new_num= num_of_bottles - 1
    if new_num == 1:
        print(new_num, " bottle of beer on the wall!")
    else:
        print(new_num, " bottles of beer on the wall!")
    print()
          

