#Rock,Scissors,Paper (game)

import random
import time

print ("welcome to game R P S !")
name = input ("please enter your name : ")
print ("Hello " + name)
print ("Are you ready ? \nwait a few seconds to start !")
print ("-" * 50)
time.sleep(5)

user_rate, sys_rate = 0, 0

while (True) :

    #user's turn to choose rock, paper or scissors
    user_choice = input ("'r' for rock , 's' for scissors , 'p' for paper !\nwhat is your choice ? ")
    
    #system's turn to choose rock, paper or scissors
    choices = ['r','s','p']
    sys_choice = random.choice (choices)

    #checking the choices and scoring
    if user_choice == 'r' and sys_choice == 'r' :
        print (" user choice : rock \n system choice : rock")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 'r' and sys_choice == 's' :
        user_rate += 1
        print (" user choice : rock \n system choice : scissors")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 'r' and sys_choice == 'p' :
        sys_rate += 1
        print (" user choice : rock \n system choice : paper")
        print ("user score :",user_rate , "system score :",sys_rate)

    elif user_choice == 's' and sys_choice == 'r' :
        sys_rate += 1
        print (" user choice : scissors \n system choice : rock")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 's' and sys_choice == 's' :
        print (" user choice : scissors \n system choice : scissors")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 's' and sys_choice == 'p' :
        user_rate += 1
        print (" user choice : scissors \n system choice : paper")
        print ("user score :",user_rate , "system score :",sys_rate)

    elif user_choice == 'p' and sys_choice == 'r' :
        user_rate += 1
        print (" user choice : paper \n system choice : rock")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 'p' and sys_choice == 's' :
        sys_rate += 1
        print (" user choice : paper \n system choice : scissors")
        print ("user score :",user_rate , "system score :",sys_rate)
    elif user_choice == 'p' and sys_choice == 'p' :
        print (" user choice : paper \n system choice : paper")
        print ("user score :",user_rate , "system score :",sys_rate)

    else:
        print ("Invalid choice !!!")

    #break condition
    if user_rate == 3 or sys_rate == 3 :
        break

#showing the result of the game
if user_rate > sys_rate :
    print ("user won the game !")

elif user_rate < sys_rate :
    print ("user Lose the game !")

else:
    print ("the game was tied !")