import random
computer = random.choice([1,-1,0])
print("----------------------Enter Your Choice Based for Snake = 1, Water = -1, and Gun = 0 -----------------------   ")
you = input("Enter your choice:")
yourdic = {"Snake":1,"Water":-1,"Gun":0}
reversedic = {1:"Snake",-1:"Water",0:"Gun"}
you = you.strip()
yourchice = yourdic[you]

print(f"You Choice {reversedic[yourchice]} and Computer Choice {reversedic[computer]}!!..")

if (yourchice == computer):
    print("The match is tied!!")
elif(yourchice== 1 and computer==-1):
    print("The snake drink the water and,  you WIN!!!...")
elif(yourchice == -1 and computer==1 ):
    print("The snake drink the water and,  you LOSS!!!...")
elif(yourchice == 0 and computer ==-1 ):
    print("Gun drowns in the water and, you LOSS!!!...")
elif(yourchice == -1 and computer ==0 ):
    print("Gun drowns in the water and, you WIN!!!...")
elif(yourchice==1 and computer==0):
    print("Gun shoots the snake, you LOSS!!!...")
elif(yourchice==0 and computer==1):
    print("Gun shoots the snake, you wiN!!!...")
else:
    print("you choice some wrong choice!!!")