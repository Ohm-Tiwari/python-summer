# A program to wish my dad happy birthday!

# imports packages
import time
from random import randint

for i in range(1, 85):
    print('')

# creates random emojis and messages
space = ''
for i in range(1, 1000):
    count = randint(1, 100)
    
    while(count > 0):
        space += ' '
        count -= 1
    
    if(i % 10 == 0):
        print(space + 'ð Happy Birthday Papa!')
    elif(i % 9 == 0):
        print(space + 'ð')
    elif(i % 8 == 0):
        print(space + 'ð')
    elif(i % 7 == 0):
        print(space + 'ð«')
    elif(i % 6 == 0):
        print(space + 'â­Happy Birthday Papa!â­')
    elif(i % 5 == 0):
        print(space + 'ð»')
    else:
        print(space + 'ð¸')
    space = ''
    time.sleep(0.2)
    
