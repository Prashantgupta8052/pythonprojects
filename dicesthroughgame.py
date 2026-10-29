import random

while(True):
    choice=(input("do you want to play game?(y/n)"))
    if(choice=="y" or choice=="Y"):
        dice1=random.randint(1,6)
        dice2 =random.randint(1,6)
        print(f"you rolles {dice1} and {dice2}")
    else if(choice=="n"):
        print("thank you so much for playing")
    else:
        print("invalid input")