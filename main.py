import random as rand

def get_input():
    playerMove = None
    while playerMove is None:
        candidate = input("Please input a new move: ").lower()
        if candidate in validMoves:
            playerMove = candidate
        else:
            print("invalid move!")
    return playerMove

def get_result(playerPicked, enemyPicked):
    matrix = [
        ["draw", 'loss', 'win'],
        ["win", "draw", "loss"],
        ["loss", "win", "draw"],
    ]

    return matrix[playerPicked][enemyPicked]

validMoves = ["rock", "paper", "scissors"]

enemyMoveIndex = rand.randint(0, 2)
enemyMove = validMoves[rand.randint(0, 2)]



playerMove = get_input()

playerMoveIndex = validMoves.index(playerMove)

print("enemy picked: ", enemyMove)

result = get_result(playerMoveIndex, enemyMoveIndex)

print('You', result)

