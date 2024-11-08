
def convertToSign(n):
    if n == 0:
        return " "
    elif n == 1: return "X"
    return "O"

def PrintGameState(game): # prints the current game state
    
    for i in range(3):
        print(" ", convertToSign(game[3 * i]), " | ", convertToSign(game[3 * i + 1]), " | ", convertToSign(game[3 * i + 2]))
        if i != 2 : print("-----------------")

def checkIfAvailable(game, move): # checks if the place is available
    return False if game[move - 1] != 0 else True

def getMove(game): # gets the next move from the player
    while True:
            try: 
                m = int(input("Your move: "))
                if m in range(1,10) and checkIfAvailable(game, m):
                    return m
                else:
                    print("Move is not available!")
            except:
                print("Invalid input!")

def checkWinner(game):

    winning_patterns = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # First diagonal
        (2, 4, 6),  # Second diagonal
    ]
    
    
    for i in range(1, 3):  # 1 for "X" and 2 for "O"
        for pattern in winning_patterns:
            if all(game[pos] == i for pos in pattern):
                return i
    return None


def startGame():
    board = [0] * 9

    for i in range(9):
        print("O player turn" if i % 2 else "X player turn")
        PrintGameState(board)

        move = getMove(board) # we already checked if the move is possible

        board[move - 1] = 2 if i % 2 else 1 # update game state

        winner = checkWinner(board)

        if winner != None:
            print("Player X wins!" if winner == 1 else "Player O wins!")
            return
    print("It's a draw!")

startGame()
