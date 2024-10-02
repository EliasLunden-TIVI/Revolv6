# REVOLV6 - .PY CMD CODE - V1B - [2/10/24]
# E:L - N3xu_Ss



# INFO LISTED ON WIKIPAGE

import random

8
# Prewarmed Values


Round = 0
Money = 0
Multiplier = 0.5 * Round
GameOn = True

Chambers = [0, 0, 0, 0, 0, 1]



#
print("***CLACK*** the revolvers cylinder swings open. 5 empty chambers. One live...")
#
#





print("""

Your options...
      
Fire - Pull the trigger. If the current chamber is empty you get to live another round. If not so... 

Stop - Pussies way out. Stops the game letting you live with all of the money you have earned with this gamble of life.
      
Roll - Roll the cylinder, reset the state of the revolver... Just hope you dont land on a hot chamber. Rerolling costs 50 money per roll.
      
""")

while GameOn == True:
    #
    print("Round " + str(Round) + " ...") 
    #Displays current round number. Starts at given value. [DEF = 0]
    choice = input("Choose your fate: ").capitalize()
    #If player decides to Shoot
    if choice == "Fire":
        
        Chamber = random.choice(Chambers)
        #Code if the requirements for a empty chamber is met. Continiues the game. [DEF = 0]
        if Chamber == 0:
            print("***CLICK*** Empty... Just like your head if that were a live round... Live to see another round.")
            Round = Round + 1
            Money = Money + 25
            Chambers.remove(0)
        #Code if the requirement for a live round is met. Ends the game. [DEF = 1]
        if Chamber == 1:
            print("***BANG*** The world fades away as you slump over the table... You played russian roulette and pulled the short straw.")
            Dead = True
            break
    #Code if the player re-rolls the cylinder
    if choice == "Roll":
        #Checks if player has enough money to re-roll. [DEF Needed = 50]
        if Money >= 50: 
            print("The revolver is grabbed by a person behind you... He opens it with a clack and spins the cylinder... Reseting the chances...")
            #Resets the chambers and the chances.
            Chambers = [0, 0, 0, 0, 0, 1] 
        #Message if the player lacks the sufficient money to reroll... Resets the current round to the start.
        else: print("- Hey dipshit... you dont have enough money to reroll. A man laughs behind you. Seemingly the big boss of this place...")
    
    #Code for stopping the game with your life still intact. Saves money.    
    if choice == "Stop":
        print("Some call it cowardly and some call it understandable. Standing up from the table with your money without having to use it on medical expenses or a funeral.")
        break

else:
    print("You muttered something under your breath... This seemed to tick the host off... - Little bunny dont want to play anymore? FINE. ***BANG*** Everything fades to black as you were knocked unconsious by the host...")
#Ending message for Stopping before lobotomy via 44 magnum.
if Dead == False:
    print("Game statistics: Money earned - " + str(Money) + " Rounds survived " + str(Round))
#Ending message after lobotomy via 44 magnum.
if Dead == True:
    print("Game statistics: Money - " + str(Money) + " Rounds survived before death " + str(Round))




