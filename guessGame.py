#rock paper and scissors
import random
for t in range(3):
    p1 = input("player one enter your option : ")

    r = random.randint(0,2)
    if r == 0:
        computer = "rock"
    elif r == 1:
        computer = "scissors"
    else:
        computer = "paper"
        print(f"computer choose {computer}" )

    if p1 == computer:
        print("Match drawn")
    elif(p1 == "rock" and computer == "scissors"):
        print("p1 wins")
    elif(p1 == "scissors" and computer == "paper"):
        print("p1 wins")
    elif(p1 == "paper" and computer == "rock"):
        print("p1 wins")
    else:
        print("computer wins")