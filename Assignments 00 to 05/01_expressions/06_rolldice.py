# Problem Statement
# # Simulate rolling two dice, and prints results of each roll as well as the total.
# solution
import random
num=6
def rolldice():
    dice1 : int =random.randint(1,num)
    dice2 : int =random.randint(1,num)
    total=dice1 + dice2
    print(f"Dice have{num} sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)


def main():
    rolldice()
main()    