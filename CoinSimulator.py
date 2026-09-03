#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/11/2025, 9:28AM
import random
def main():
    flip = random.random() #generates a random number betw/ 0 and 1
    if flip < 0.5: #gives heads and tails equal chances of being selected
        print("Result: Heads")
    else:
        print("Result: Tails")
main()
