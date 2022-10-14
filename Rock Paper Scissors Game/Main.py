# My GitHub:  		GitHub.com/AliRezaJoodi

from Rock_Paper_Scissors_Game import rock_paper_scissors_game
from Dispaly import dispaly
import random

tools=["Rock", "Paper", "Scissors"]
dispaly ("Choose Between:", "Rock, Paper, Scissors")
dispaly ("Player1:", "You")
dispaly ("Player2:", "CPU")
dispaly ("Exit Key:", "E or e")

winner = ""
  
def main ():
    player1_score = 0
    player2_score = 0 
    while(True):
        player1 = input("\nEnter Your Choice:     ")
        player1 = player1.capitalize()
        if player1 == "E" or player1 == "e": 
            break
        
        player2 = random.choice(tools)
        dispaly ("Player2 Chose:", player2)
        
        if player1=="Rock" or player1=="Paper" or player1=="Scissors":
            winner = rock_paper_scissors_game(player1, player2)
            dispaly ("Winner:", winner)
            if winner == "Player1":
                player1_score = player1_score + 1
            elif winner == "Player2":
                player2_score = player2_score + 1
        else:
            print ("Not valid")
            
    dispaly ("Player1 Score:", player1_score)
    dispaly ("Player2 Score:", player2_score)
     
if __name__ == "__main__":
    main ()