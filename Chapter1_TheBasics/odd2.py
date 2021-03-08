#GETTING STARTED


#p. 27 LOOPS


from datetime import datetime
import time
import random

odds= [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31,
       33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59,]


#Want it to run five times, random # of seconds in between each iteration.
for i in range(5):
    this_minute = datetime.today().minute
    rand = random.randint(1,5)
    time.sleep(rand)
    if this_minute in odds:
        print("This minute is odd.")
        if rand in [1]:
            print("It took " + str(rand) + " second to print this")
        else:
            print("It took " + str(rand) + " seconds to print this")
    else:
        print("This minute is even.")
        if rand in [1]:
            print("It took " + str(rand) + " second to print this")
        else:
            print("It took " + str(rand) + " seconds to print this")
       
        
