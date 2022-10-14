# My GitHub:  		GitHub.com/AliRezaJoodi

from Rock_Paper_Scissors_Game import rock_paper_scissors_game
from Dispaly import dispaly
import random

tools=["Rock", "Paper", "Scissors"]
dispaly ("Choose Between:", "Rock, Paper, Scissors")
dispaly ("Player1:", "CPU")
dispaly ("Player2:", "You")
dispaly ("\n")
  
def main ():
    player1 = random.choice(tools)
    dispaly ("Player1 Chose:", "-----")
    
    player2 = input("Enter Your Choice: ")
    player2 = player2.capitalize()
   
    Winner = rock_paper_scissors_game(player1, player2)
    
    dispaly ("\n")
    dispaly ("Player1 Choice:", player1)
    dispaly ("Player2 Choice:", player2)
    dispaly ("Winner:", Winner)
    
    
if __name__ == "__main__":
    main ()