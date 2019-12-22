#!/usr/bin/python

# Head ends here

def update_position(posr, posc, board, move):
    if(move == "CLEAN"):
        return()
    elif(move == "RIGHT"):
        aux = list(board[posr])
        aux[posc] = "-"
        aux[posc+1] = "b"
        
        board[posr] = "".join(aux)
        posc = posc+1
    elif(move == "LEFT"):
        aux = list(board[posr])
        aux[posc] = "-"
        aux[posc-1] = "b"
        
        board[posr] = "".join(aux)
        posc = posc-1
    elif(move == "UP"):
        aux = list(board[posr])
        aux2 = list(board[posr-1])
        aux[posc] = "-"
        aux2[posc] = "b"
        
        board[posr] = "".join(aux)
        board[posr-1] = "".join(aux2)
        posr = posr - 1
    elif(move == "DOWN"):
        aux = list(board[posr])
        aux2 = list(board[posr+1])
        aux[posc] = "-"
        aux2[posc] = "b"
        
        board[posr] = "".join(aux)
        board[posr+1] = "".join(aux2)
        posr = posr + 1
        
    return(posr, posc, board)

def next_move(posr, posc, board):
    if(board[posr][posc] == "d"):
        return("CLEAN")
    
    # find all dirty cell positions
    dirties_pos = []
    for idx,value in enumerate(board):
        if("d" in value):
            for col in [i for i,j in enumerate(list(value)) if j=="d"]:
                dirties_pos.append([idx,col])
    if(len(dirties_pos)==0):
        return()
    
    # find nearest position
    min_pos = []
    min_dis = 100
    for d in dirties_pos:
        cur_dis = abs(d[0] - posr) + abs(d[1] - posc)
        if(cur_dis < min_dis):
            min_dis = cur_dis
            min_pos = d
    
    direction_h = posc - min_pos[1]
    direction_v = posr - min_pos[0]

    if(direction_h < 0):
        return("RIGHT")
    elif(direction_h > 0):
        return("LEFT")

    if(direction_v < 0):
        return("DOWN")
    elif(direction_v > 0):
        return("UP")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))

# i = 0
# while("d" in "".join(board)):    
#     move = next_move(pos[0], pos[1], board)
#     pos[0], pos[1], board = update_position(pos[0], pos[1], board, move)
#     print()
#     print(str(i) + ": " + move)
#     for row in board:
#         print(row)
        
#     i = i + 1    
