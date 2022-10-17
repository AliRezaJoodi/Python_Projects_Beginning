# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *
from display import LENGHT_TITLE as LENGHT
#from rock_paper_scissors_game import *
from rock_paper_scissors_game import checking_winner_v20 as checking_winner
import random

tools= ["Rock", "Paper", "Scissors"]
display("Choose Between:", "Rock, Paper, Scissors")
display("Player1:", "You")
display("Player2:", "CPU")
display("Exit Key:", "E or e")

winner = ""
  
def main ():
    player1_score = 0
    player2_score = 0 
    while(True):
        player1 = input("\nEnter Your Choice:".ljust(LENGHT+2, " "))
        player1 = player1.capitalize()
        if player1 == "E" or player1 == "e": 
            break
        
        player2 = random.choice(tools)
        display("Player2 Chose:", player2)
        
        if player1=="Rock" or player1=="Paper" or player1=="Scissors":
            winner = checking_winner(player1, player2)
            display("Winner:", winner)
            if winner == "Player1":
                player1_score = player1_score + 1
            elif winner == "Player2":
                player2_score = player2_score + 1
        else:
            display("Winner:", "x")
            
    display("Player1 Score:", player1_score)
    display("Player2 Score:", player2_score)
     
if __name__ == "__main__":
    main ()