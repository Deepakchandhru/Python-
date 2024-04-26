import random
def number():
    print("\n\n\t\t Welcome to number guessing game . Guess the 3-digit number \n\n")
    a=random.randint(100,999)
    guess=True
    while guess:
        b=int(input("Enter number: "))
        if a==b:
            print("\t\t You are absolutely right.")
            guess=False
        elif a>b and a-b>10:
            print("\t\t Give a bigger number.")
        elif b>a and b-a>10:
            print("\t\t Give a smaller number.")
        else:
            print("\t\t You are closer to it.")
    print("The number is ",a)
    print("\n\n\t\t Thankyou for playing. \n")

number()
game=True
while game:
    c= int(input("Do you want to play again?(1.Yes 2.No) : "))
    if c==1:
        number()
    else:
        game=False
