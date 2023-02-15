# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Steven Magdaleno>
# Creation Date: <20230212>
# Below is a simple program with several errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''') #un-tabbed these lines so the formatting looked better when printed.
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave #moved this line in line with the chooseCave() function. It was off by itself down below. Also removed
                #the s and the end of 'caves' to make the variable 'cave'

def checkCave(cave): #changed this variable from 'chosenCave' which was undefined to 'cave'
    print('You approach the cave...')
    # sleep for 2 seconds
    time.sleep(2)

    print('It is dark and spooky...')
    # sleep for 2 seconds
    time.sleep(2) #changed the int here from '3' to '2'

    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    # sleep for 2 seconds
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if cave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!') #moved this up and formatted as a print line

displayIntro()
caveNumber = chooseCave() #capitalized the c in "choosecave()"
checkCave(caveNumber)

print("Thanks for playing") #changed the spelling, assume you meant 'Thanks for playing'