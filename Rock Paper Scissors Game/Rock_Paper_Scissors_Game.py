# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly import dispaly

######################################################
def rock_paper_scissors_game_v20(player1, player2):
    debug=False
    dispaly ("\n", "",debug)
    dispaly ("Function:", "rock_paper_scissors_game_v20", debug)
    dispaly ("Player1:", player1, debug)
    dispaly ("Player2:", player2, debug)
    
    tools_dict ={
        "RockVsRock":           "Nobody",
        "RockVsPaper":          "Player2",
        "RockVsScissors":       "Player1",
        "PaperVsRock":          "Player1",
        "PaperVsPaper":         "Nobody",
        "PaperVsScissors":      "Player2",
        "ScissorsVsRock":       "Player2",
        "ScissorsVsPaper":      "Player1",
        "ScissorsVsScissors":   "Nobody"
    }
    
    player_merge = player1 + "Vs" + player2
    dispaly ("player_merge:", player_merge, debug)
    
    return tools_dict[player_merge]

###################################################### 
# Source Link:  https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/   
def rock_paper_scissors_game_v10(player1, player2):
    debug=False
    dispaly ("\n", "",debug)
    dispaly ("Function:", "rock_paper_scissors_game", debug)
    dispaly ("Player1:", player1, debug)
    dispaly ("Player2:", player2, debug)
    
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
    dispaly ("winner:", winner, debug)
    
    return winner
    