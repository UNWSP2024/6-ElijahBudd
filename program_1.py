# Elijah Budd
# 2/25/2025
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive)
# and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.
import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    # Sum 2 numbers
    return roll1 + roll2
    # return sum to calling function

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
if __name__ == '__main__':
    total = 0
    rolls = 100
    for i in range(rolls):
        total += randDice()
    average = total / 100
    print(f"The average of 100 rolls is: {average:.2f}")
