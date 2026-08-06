import random

HEADS = 1
TAILS = 2
TOSSES = 2

def tosses_con():
    for toss in range(TOSSES):
        # print(random.randint(HEADS, TAILS))
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")
            
tosses_con()