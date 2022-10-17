# My GitHub:  		GitHub.com/AliRezaJoodi

from display import *

debug=False

######################################################
def checking_winner_v20(player1, player2):
    display("\n", "",debug)
    display("Function:", "rock_paper_scissors_game_v20", debug)
    display("Player1:", player1, debug)
    display("Player2:", player2, debug)
    
    tools_dict ={
        "Rock_Rock":           "Nobody",
        "Rock_Paper":          "Player2",
        "Rock_Scissors":       "Player1",
        "Paper_Rock":          "Player1",
        "Paper_Paper":         "Nobody",
        "Paper_Scissors":      "Player2",
        "Scissors_Rock":       "Player2",
        "Scissors_Paper":      "Player1",
        "Scissors_Scissors":   "Nobody"
    }
    
    player_merge = player1 + "_" + player2
    display("player_merge:", player_merge, debug)
    
    winner = tools_dict[player_merge]
    display("Winner:", winner, debug)
    
    return winner

###################################################### 
# Source Link:  https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/   
def checking_winner_v10(player1, player2):
    display("\n", "",debug)
    display("Function:", "rock_paper_scissors_game_v10", debug)
    display("Player1:", player1, debug)
    display("Player2:", player2, debug)
    
    winner = "Nobody"
    if player1 == "Rock" and player2 == "Scissors":
        winner = "Player1"
    elif player1 == "Paper" and player2 == "Rock":
        winner = "Player1"
    elif player1 == "Scissors" and player2 == "Paper":
        winner = "Player1"
    elif player1 == player2:
        winner = "Nobody"
    else:
        winner = "Player2"
    display("Winner:", winner, debug)
    
    return winner

######################################################
if __name__ == "__main__":
    debug = True
    checking_winner_v10("Rock", "Scissors")
    checking_winner_v20("Rock", "Scissors")
    