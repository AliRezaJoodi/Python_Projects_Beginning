# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:  	https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/

from Dispaly import dispaly

def rock_paper_scissors_game(player1, player2):
    debug=True
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
        winner = "Tie"
    else:
        winner = "Player2"
    dispaly ("winner:", winner, debug)
    
    return winner
    