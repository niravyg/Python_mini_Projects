import random

# Guess The Number
print("------------------ Guess The Number Game----------------------")
print("------------------ Guess The Number from 1 t0 10----------------------")

# Take input from the user
num = int(input("Guess the Number Between 1 to 10:"))

# list use to store the number that user guess and print the total attmept to guess the  correct number
guess_list = []


#  genrate the random Number Between 1 t0 10
Computer_nunber = random.randint(1,11)

# for Loop to give Chance to user to guess the number 
for i in range(1,11):

    #Enter The number between 1 t0 10
    if (num >= 11):
        print("Pleas Enter Valid Number between 1 to 10")
    else:
        # if Guess number is Greater then Computer Number
        if (num > Computer_nunber ):
            print("Lower Number Please")

        # if Guess number is Lower then Computer Number
        elif (num < Computer_nunber):
            print("Higher Number Please")

        # if Guess number is equal to Computer Number
        elif(num == Computer_nunber):
            print(f"The attmpt to arrive at Correct answer is: {len(guess_list)} ")
            break
    # Take Continue Input From The user until the user Guess the correct answer
    num = int(input("Guess the Number Between 1 to 10:"))
    # add all the number That user Guess 
    guess_list.append(num)
