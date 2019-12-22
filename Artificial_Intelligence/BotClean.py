#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    move = ""
    
    if(board[posr][posc] == "d"):
        return("CLEAN")
    
    # horizontal (dirty)
    if(posc == 0):
        move = "RIGHT"
        if(board[posr][posc+1] == "d"):
            return("RIGHT")
    elif(posc == len(board[0])-1):
        move = "LEFT"
        if(board[posr][posc-1] == "d"):
            return("LEFT")
    else:
        move = "RIGHT"
        if(board[posr][posc+1] == "d"):
            return("RIGHT")
        elif(board[posr][posc-1] == "d"):
            return("LEFT")
    
    # vertical (dirty)
    if(posr == 0):
        if(board[posr+1][posc] == "d"):
            return("DOWN")
    elif(posr == len(board)-1):
        if(board[posr-1][posc] == "d"):
            return("UP")
    else:
        if(board[posr+1][posc] == "d"):
            return("DOWN")
        elif(board[posr-1][posc] == "d"):
            return("UP")
            move = "UP"
    
    return(move)

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
