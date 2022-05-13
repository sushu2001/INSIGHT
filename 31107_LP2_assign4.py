"""Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
Backtracking for n-queens problem or a graph coloring problem"""

''' N-queen Branch and Bound and Backtracking'''
N=int (input("Enter the number: "))

def printSol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()
 

def isOk(row, col, sC, bsC, rowLookup, sCLookup, bsCLookup):
    if (sCLookup[sC[row][col]] or bsCLookup[bsC[row][col]] or rowLookup[row]):
        return False
    return True

def solveNQUtil(board, col, sC, bsC, rowLookup, sCLookup, bsCLookup):
                         
    if(col >= N):
        return True
    for i in range(N):
        if(isOk(i, col, sC, bsC,rowLookup, sCLookup,bsCLookup)):
                     
            
            board[i][col] = 1
            rowLookup[i] = True
            sCLookup[sC[i][col]] = True
            bsCLookup[bsC[i][col]] = True
             
            
            if(solveNQUtil(board, col + 1, sC, bsC, rowLookup, sCLookup, bsCLookup)):
                return True
             
            
            board[i][col] = 0
            rowLookup[i] = False
            sCLookup[sC[i][col]] = False
            bsCLookup[bsC[i][col]] = False
             
    
    return False
 

def solveNQ():
    board = [[0 for i in range(N)]
                for j in range(N)]
     
    
    sC = [[0 for i in range(N)]
                    for j in range(N)]
    bsC = [[0 for i in range(N)]
                        for j in range(N)]
     
    
    rowLookup = [False] * N
     
   
    x = 2 * N - 1
    sCLookup = [False] * x
    bsCLookup = [False] * x
     
   
    for rr in range(N):
        for cc in range(N):
            sC[rr][cc] = rr + cc
            bsC[rr][cc] = rr - cc + (N-1)
     
    if(solveNQUtil(board, 0, sC, bsC, rowLookup, sCLookup, bsCLookup) == False):
        print("Solution does not exist")
        return False
         
    # solution found
    printSol(board)
    return True

solveNQ()

# if __name__ == '__main__':
#     N=int (input("Enter"))
#     board = [['-' for x in range(N)] for y in range(N)]
#     solveNQ(board, 0)


"""arr=[]
for i in range(N):
    brr=[]
    for j in range(N):
        x=int(input())
        brr.append(x)
    arr.append(brr)"""

