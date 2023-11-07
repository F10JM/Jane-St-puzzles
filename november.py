import numpy as np
from collections import Counter
l = np.array([[ 9,  8, 10, 12, 11,  8, 10, 17],
              [ 7,  9, 11,  9, 10, 12, 14, 12],
              [ 4,  7,  5,  8,  8,  6, 13, 10],
              [ 4, 10,  7,  9,  6,  8,  7,  9],
              [ 2,  6,  4,  2,  5,  9,  8, 11],
              [ 0,  3,  1,  4,  2, 7, 10,  7],
              [ 1,  2,  0,  1,  2, 5,  7,  6],
              [ 0,  2,  4,  3,  5, 6,  2,  4]], dtype=float)

def matrix_to_chess(i, j):
    columns = 'abcdefgh'
    row = 8 - i
    column = columns[j]
    return f"{column}{row}"

def chess_to_matrix(chess_notation):
    columns = 'abcdefgh'
    column_letter = chess_notation[0]
    row_number = int(chess_notation[1])
    i = 8 - row_number
    j = columns.index(column_letter)
    return (i, j)


def opposite(x,y):
    return((7-x,7-y))

def same_altitude(x,y):
    v=l[x,y]
    n=0
    for i in range (8):
        for j in range(8):
            if (l[i,j]==v):
                n+=1
    return(n)


def one_minute_passed(x,y,n):
    v=l[x,y]
    for i in range (8):
        for j in range(8):
            if (l[i,j]==v):
                l[i,j]= l[i,j] - round (1 / n , 2)

def possible_jumps(x,y,seen):
    jumps=[]
    min_i = max(x - 2, 0)
    max_i = min(x + 2, 7)
    min_j = max(y - 2, 0)
    max_j = min(y + 2, 7)
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if ((i, j) != (x, y)):
                if (Counter([abs(x-i),abs(y-j),abs(l[x,y]-l[i,j])])==Counter([0,1,2])) and (seen[i,j]<4):
                    jumps.append((i,j))
    return(jumps)

def main():
    (x,y)=chess_to_matrix("a1")
    seen=np.zeros((8,8))
    seen[x,y]=1
    list_res=[]

    def rec(x,y,seen,res):
        print( matrix_to_chess(x,y)  , end="")
        if matrix_to_chess(x,y)=="h8":
            list_res.append(res)
            print(res)
        else:
            n=same_altitude(x,y)
            jumps0=[]
            jumps1=possible_jumps(x,y,seen)
            t=0
            while (len(jumps1)>0):
                #for (i,j) in jumps:
                #    new_seen=seen.copy()
                #    new_seen[i,j]+=1
                #    rec(i,j,new_seen,res+[(t,matrix_to_chess(i,j))])
                one_minute_passed(x,y,n)
                jumps0=jumps1
                jumps1=possible_jumps(x,y,seen)
                t+=1
            for (i,j) in jumps0:
                    new_seen=seen.copy()
                    new_seen[i,j]+=1
                    rec(i,j,new_seen,res+[(t-1,matrix_to_chess(i,j))])
    rec(x,y,seen,[])
    
                
main()


     
                


        