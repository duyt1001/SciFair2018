
from random import*

print('''TWENTY ONE
22222222222222222222222222222222222222222
Try to score 21 points!! (DUDE, ur supposed to be elatedly happy!)
''')
    
playing = True
score = 0
while playing == True:
    num = randint(1,10)
    score = score + num
    print("Here. Take it. It's ur new number!",num)
    print("Your score is...:",score)

    if score > 21:
        print("Umm. sorry. u lost ...")

    elif score == 21:
        print("Uhhh...I suppose u won. yay?")

    if score >= 21:
        print("Another game? I'm gonna die. TOO MUCH CODE!! CAPLOOM! (That's my brain exploding.)Good job. Making people's brain spontaniously combust. Mark that on your bucket list")
        reply = input().lower()
        if reply == "no":
            playing == False
            print("BUH BYE")
        else:
            score = 0 
    else :
        print("Do you want...another...number? I CAN'T SAY ANY MORE, JUST FRICKIN' REPLY!!!")
    
        reply = input().lower
        if reply == "no":
            playing == False
