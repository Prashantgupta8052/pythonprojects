import random

emojis={ "r" :"🪨" ,"p":"📰" ,"s":"✂️"}
choices=("r", "p","s")

while True:
    user_choice=input("rock paper or Scissor? (r/p/s)").lower()
    if user_choice not in choices:
        print("invalid choice")
        continue

    machine_choice=random.choice(choices)

    print(f"you chose {emojis[user_choice]}")
    print(f"machine chose{emojis[machine_choice]}")

    if user_choice==machine_choice:
         print("match tie! 😑")
    elif (
        (user_choice=="r" and machine_choice=="s") or
        (user_choice=="p" and machine_choice=="r") or 
        (user_choice=="s" and machine_choice=="p")): 

        print("you won the match😍")
    else:
        print("you lost the match and machine won the match 🙇")

    should_continue=input("continue ? (y/n): ").lower()
    if should_continue=="n":
        break