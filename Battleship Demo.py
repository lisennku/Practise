"""
1. Define the size of the play board
2. Random the length and direction of the battleship. Judge the size if it mis-match the play board. and then prompt user to re-input
3. Display the playboard, and the grid that user entered. but the battleship is concealed.
"""

from random import randint

PlayBoard = []
ship_pos = []

N = int(raw_input("Please input an integer to draw the play board: "))

# define a function to display the board
def display(board,N):
    for i in range(N):
        print " ".join(PlayBoard[i])

# draw the board
for i in range(N):
    PlayBoard.append(["O"] * N)
    print " ".join(PlayBoard[i])


# generate start position and direction
ship_row = randint(0, N - 1)
ship_col = randint(0, N - 1)
direction = randint(0, 1)

#print ship_col
#print ship_row
#print direction


# generate ship length
def ship_length(row, col, direct):
    ship_len = randint(0, int(N / 2))
    print ship_len
    if direct == 0:  # horizon
        ship_pos.append(ship_row)
        while col + ship_len > N - 1:
            print "Oops, system is re-generating the ship"  # modify the ship length
            ship_len = randint(0, int(N / 2))
            #print ship_len
        else:
            for i in range(ship_len):
                ship_pos.append(ship_col + i)
            print "Ship is in position!!"
    else:
        ship_pos.append(ship_col)
        while row + ship_len > N - 1:
            print "Oops, system is re-generating the ship"  # modify the ship length
            ship_len = randint(0, int(N / 2))
            #print ship_len
        else:
            for i in range(ship_len):
                ship_pos.append(ship_row + i)
            print "Ship is in position!!"
    return ship_len

length = ship_length(ship_row,ship_col,direction)
#print ship_pos


# judge if the input match part of the ship
def judge(x,y):
    if x == ship_pos[0] or y == ship_pos[0]:
        i = 1
        for i in range(len(ship_pos)):
            if y in ship_pos[i:] or x in ship_pos[i:]:
                return True
    else :
        return False


def check(a,b):
    if a >= N or b >= N:
        return False
    else:
        return True



print "Commander, you have only 5 chances to hit the sub-marine."
print "Remember, ONLY hit all its position that can we win"

Times = 5
count = 0
while Times > 0:
    row = int(raw_input("Please input the row: "))
    col = int(raw_input("Please input the col: "))
    while check(row,col) ==False:
        print "You are out of RANGE!"
        print "Please re-input, and this will not minus your chances"
        row = int(raw_input("Please input the row: "))
        col = int(raw_input("Please input the col: "))
    while PlayBoard[row][col] == "X" or PlayBoard[row][col] == "*":
        print "You already input that one"
        print "Please re-input, and this will not minus your chances"
        row = int(raw_input("Please input the row: "))
        col = int(raw_input("Please input the col: "))
    Times -= 1
    if judge(row,col) == False:
        print "You missed it, that one will be marked as X"
        PlayBoard[row][col] = "X"
        display(PlayBoard,N)
    else :
        print "You HIT it, it will be marked as *"
        PlayBoard[row][col] = "*"
        display(PlayBoard,N)
        count += 1

if length == count - 1:
    print "You WIN!"
else:
    print "You lose this game"
