import random
def rps():
    print("\n\n\n...Welcome to the ROCK PAPER SCISSOR game...")
    cs=0
    ps=0
    choice=["Rock","Paper","Scissor"]
    while True:
        c=int(input("Enter your Choice:\n(1.Rock \n 2.Paper \n 3.Scissor)\n"))
        pc=choice[c-1]
        com=random.randint(0,2)
        cc=choice[com]
        print("Computer choice:",cc)
        print("Your choice:",pc)

        if c-1==com:
            print("No point")
        elif choice[choice.index(pc)-1] == choice[choice.index(cc)] :
            ps+=1
            print("You won the point")
        elif choice[choice.index(pc)] == choice[choice.index(cc)-1] :
            cs+=1
            print("Computer won the point")

        print("Computer score:",cs)
        print("Your score:", ps)

        if ps==5:
            print("\n\n\t\t\t\t You Won the game. keep it up.")
            return False
        if cs==5:
            print("\n\n\t\t\t\t Computer won the game.Better luck next time.")
            return False

    print("\n\n\n...Thank you for playing. Try again...")

game=True
while game:
    rps()
    p=int(input("Do you want to continue? \n 1. Yes \n 2. No \n"))
    if p!=1:
        game=False
