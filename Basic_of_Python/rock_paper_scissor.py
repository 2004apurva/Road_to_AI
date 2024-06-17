import random

choices=("rock","paper","scissors")

computer=random.choice(choices)

player=None

while player not in choices:
    player=input("rock , paper,or scissors :").lower()



if player==computer:
    print("Player:", player)
    print("Computer:", computer)
    print("Tie")

elif player=="rock":
    if computer=="paper":
        print("Player:", player)
        print("Computer:", computer)
        print("Computer Wins")
    if computer=="scissors":
        print("Player:", player)
        print("Computer:", computer)
        print("Player Wins")

elif player=="paper":
    if computer=="scissors":
        print("Player:", player)
        print("Computer:", computer)
        print("Computer Wins")
    if computer=="rock":
        print("Player:", player)
        print("Computer:", computer)
        print("Player Wins")

elif player=="scissors":
    if computer=="rock":
        print("Player:", player)
        print("Computer:", computer)
        print("Computer Wins")
    if computer=="papen":
        print("Player:", player)
        print("Computer:", computer)
        print("Player Wins")

print("Bye")





