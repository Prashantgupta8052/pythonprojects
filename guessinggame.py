from itertools import count
import random
jackpot= random.randint(1,100)
guess=int(input("chal number guess kar"))
count=1
while guess!=jackpot:
    if guess<jackpot:
        print("guess uper")
    else:
        print("guess lower")
    guess=int(input("chal number guess kar"))
    count=count+1
print("shi jawab")
print("how many guess", count)