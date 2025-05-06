import random

'''
snake = 1
water = -1
gun =0
'''

computer = random.choice([1,-1,0])

user = input("Enter your choose (S, W, G): ")
if not(user=="s" or user=="w" or user=="g"):
    print("Invalide Input Try Again")
else:
    userdic= { "s":1, "w":-1, "g":0}
    reversedic= {1:"Snake", -1:"Water", 0:"Gun"}
    you = userdic[user]
    print(f"You chose : {reversedic[you]}\nComputer chose : {reversedic[computer]}")

    if(computer == you):
        print("Its A Draw")

    else:

        if(computer==1 and you == -1):
            print("You Lose")


        elif(computer==1 and you == 0):
            print("You Win")


        elif(computer==-1 and you == 1):
            print("You Win")


        elif(computer==-1 and you == 0):
            print("You Lose")


        elif(computer==0 and you == 1):
            print("You Lose")


        elif(computer==0 and you == -1):
            print("You Win")

        else:
            print("Something is wrong")
