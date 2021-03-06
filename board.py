board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(board1):
    for i in range(len(board1)):
        if i % 3 == 0 and i != 0:           # creates division line for every 3rd row
            print("-----------------------")
    
        for j in range(len(board1[0])):
            if j % 3 == 0 and j != 0:       # creates division line for every 3rd column
                print(" | ", end = "")

            if j == 8:
                print(board1[i][j])
            else:
                print(str(board1[i][j]) + " ", end = "")

printBoard(board)