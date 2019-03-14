import sys
sys.setrecursionlimit(10000)

n =  input().split(' ')
for i in range(len(n)):
   n[i] = int(n[i])

slot = n[0]
maxweight = n[1]

w =  input().split(' ')
for i in range(len(w)):
    w[i] = int(w[i])

v = input().split(' ')
for i in range(len(v)):
    v[i] = int(v[i])

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