def main():
    score=randomscore()
    printgrade(score)
def printgrade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 0 <= score < 50:
        print("Bad")
    elif 50 <= score < 90:
        print("Passable")
    elif 90 <= score <= 100:
        print("Excellent")
import random
def randomscore():
    randomscore=random.randint(0,100)
    print(randomscore)
    return randomscore
main()
