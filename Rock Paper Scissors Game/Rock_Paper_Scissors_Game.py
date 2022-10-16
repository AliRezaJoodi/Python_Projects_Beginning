# My GitHub:  		GitHub.com/AliRezaJoodi

from Display import display

debug=False

######################################################
def rock_paper_scissors_game_v20(player1, player2):
    display ("\n", "",debug)
    display ("Function:", "rock_paper_scissors_game_v20", debug)
    display ("Player1:", player1, debug)
    display ("Player2:", player2, debug)
    
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
    display ("player_merge:", player_merge, debug)
    
    winner = tools_dict[player_merge]
    display ("Winner:", winner, debug)
    
    return winner

###################################################### 
# Source Link:  https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/   
def rock_paper_scissors_game_v10(player1, player2):
    display ("\n", "",debug)
    display ("Function:", "rock_paper_scissors_game_v10", debug)
    display ("Player1:", player1, debug)
    display ("Player2:", player2, debug)
    
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
    display ("Winner:", winner, debug)
    
    return winner

######################################################
if __name__ == "__main__":
    debug = True
    rock_paper_scissors_game_v10("Rock", "Scissors")
    rock_paper_scissors_game_v20("Rock", "Scissors")
    