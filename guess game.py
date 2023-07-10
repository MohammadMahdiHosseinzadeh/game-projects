import random

def guess (g):
    if g==x :
        print ("You guessed the right number :)")
        return True
    else :
        print ("You guessed the wrong number !!!")
        return False

def score ():
    try:
        with open ("best score.txt","r") as f:
            content=f.read()
        return content
    except FileNotFoundError :
        with open ("best score.txt","w") as f:
            f.write (str(bestScore))
        with open ("best score.txt","r") as f:
            content=f.read()
        return content

def endGame ():
    print ("Your score : ",ebox)
    result=score ()
    if ebox > (int(result)) :
        print ("Congratulations, you have earned the best score until now")
        with open ("best score.txt","w") as f:
            f.write (str(ebox))
        print ("Best score : ",ebox)
    else:
        print ("It's ok, you can get the best score next time :)")

#------------------------------------------------------------
while (True) :

    start=input ("Do you want to start the game? (yes/no/exit) : ")

    try:
        if start=="yes" :
            print ("Welcome to the game :)")

            ebox=0
            bestScore=0
            chance=2

            result=score ()
            print ("Best score : ",result)

            x=random.randint(1,10)

            while (True) :
                try:
                    g=int (input ("Guess a number between 1 and 10 : "))
                    if 0 < g <= 10 :
                        result=guess (g)
                        if result :
                            ebox+=2
                            chance=2
                            c=input ("Well done, do you want to continue playing? (yes/no) : ")
                            try:
                                if c=="yes" :
                                    print ("Your score until now : ",ebox)
                                    x=random.randint(1,10)

                                elif c=="no" :
                                    endGame()
                                    break
                                
                                else:
                                    raise ValueError

                            except ValueError:
                                print ("Wrong input !!!")
                                break

                        else:
                            if ebox!=0 :
                                ebox-=1
                            chance-=1
                            if chance==0 :
                                print ("Your chances are over ):")
                                endGame()
                                break
                            print ("You have one chance left !!!")
                            if g > x :
                                print ("Hint : guess a number smaller than",g,)
                            else:
                                print ("Hint : guess a number bigger than",g,)

                    else:
                        print ("The entered number must be between 1 and 10 !!!")

                except ValueError:
                    print ("You must enter a number !!!")
                    continue

        elif start=="no" :
            print ("The game didn't start")

        elif start=="exit" :
            print("You exited from the game")
            break

        else:
            raise ValueError

    except ValueError:
        print ("Wrong input !!!")