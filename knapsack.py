import sys
sys.setrecursionlimit(10000)

n = [int(i) for i in input().split(' ')]
slot = n[0]
maxweight = n[1]

w = [int(i) for i in input().split(' ')]
v = [int(i) for i in input().split(' ')]

mm = [[-1]*( maxweight + 1 ) for i in range(slot+1)]


def knapSack(i, c):
    global mm
    if mm[i][c] == -1:
        if i == slot:
            mm [i][c] =  0
        else:
            skip = knapSack(i+1,c)
            take = 0
            if w[i] <= c:
                take = knapSack(i+1, c-w[i])+ v[i]
            mm [i][c] = max(skip,take)
    return mm[i][c]


print(knapSack(0,maxweight))