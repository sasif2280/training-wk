import random

captains_call=input("head or tails  ")

ran=random.randint(0,1)
if ran==0:
    print("heads \n you won the toss \n what you want to do?")
    print("1.batting \n 2.bowling")
    choice=int(input())
    if choice==1:
        print("you are batting")
    elif choice==2:
        print("you are bowling")

else:
    print("tails \n you lose the toss ")