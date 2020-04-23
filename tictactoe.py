def tic_tac_toe_col(board, c, r, up):
    #print("col"+str(c))
    #print("row"+str(r))
    #print("up"+str(up))
    if(r-1<0):
        a = False
        up += 1
        #print("up" + str(up))
        if up == len(board):
            a = True
        return a
    if ((r-1>=0)and (board[r][c] == board[r-1][c])):
        up += 1
        tic_tac_toe_col(board, c, r-1, up)
    return(tic_tac_toe_col(board, c, r-1, up))


def tic_tac_toe_row(board, c, r, across):
    if(c-1<0):
        a = False
        across += 1
        if across == len(board[0]):
            a = True
        return a
    if ((c-1>=0)and (board[r][c] == board[r][c-1])):
        across += 1
        tic_tac_toe_row(board, c-1, r, across)
    return(tic_tac_toe_row(board, c-1, r, across))

def tic_tac_toe_diag1(board, c, r, d,lon):
    if((c-1<0) or (r+1>=lon)):
        a = False
        d += 1
        if d == lon:
            a = True
        return a
    if ((c-1>=0)and(r+1<lon)and(board[r][c] == board[r+1][c-1])):
        d += 1
        tic_tac_toe_diag1(board, c-1, r+1, d,lon)
    return(tic_tac_toe_diag1(board, c-1, r+1, d,lon))
def tic_tac_toe_diag2(board, c, r, di,lon):
    #print("c" +str(c))
    #print("r" + str(r))
    #print("ogdi"+ str(di))
    if (c-1)<0 or (r-1)<0:
        a=False
        di+=1
        if di ==lon:
            a=True
        return a
    if ((c-1>=0)and(r-1>=0)and(board[r][c] == board[r-1][c-1])):
        di += 1
        tic_tac_toe_diag2(board, c-1, r-1, di,lon)
    return(tic_tac_toe_diag2(board, c-1, r-1, di,lon))



def tic_tac_toe_test(col, row, brd):
    for x in range (0, len(brd)):
        up = 0
        a=tic_tac_toe_col(brd, col-1-x, row-1, up)
        if(a):
             return True, brd
    for x in range (0, len(brd[0])):
        across = 0
        b=tic_tac_toe_row(brd, (col-1), (row-1-x), across)
        if(b):
            return True, brd

    if len(brd)>len(brd[0]):
        longest = len(brd)
    else:
        longest = len(brd[0])
    diag = 0
    if tic_tac_toe_diag1(brd, col-1, 0, diag, longest):
        return True, brd
    diag = 0
    if tic_tac_toe_diag2(brd, col - 1, row-1, diag, longest):
        return True, brd


c = input("Number of columns:")
r = input("Number of Rows:")
brd = [['' for x in range(int(c))] for y in range(int(r))]

print("")
print("STARTING BOARD:")
for i in brd:
    print(i)


for x in range (0, int(r)):
    for y in range(0, int(c)):
        a = input("Pick an row coordinate, starting at 1, to be the y value of the coordinate you put your X or O. ")
        b = input("Pick a column coordinate, starting at 1, to be the x value of the coordinate you put your X or O. ")
        brd[int(a)-1][int(b)-1] = input("Place a value, lowercase 'x' or lowercase 'o', in row " + a + ", column " + b + ". ")

        print("UPDATED BOARD:")
        for i in brd:
            print(i)

print(tic_tac_toe_test(int(c), int(r), brd))

k = {3,3,2}

print(len(k));
one.moneyy+= RandomNumber;