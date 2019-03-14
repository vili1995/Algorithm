import sys
sys.setrecursionlimit(10000)

coin = input().split(' ')
for i in range(len(coin)):
    coin[i] = int(coin[i])
V = int(input())

mm = [-1]* (V+1)

for v in range(V+1):
    if v == 0:
        mm[v] = 0
    else:
        minc = 1000000000000
        for c in coin:
            if c <= v:
                minc = min(minc, mm[v-c]+1)
        mm[v] = minc

print(mm[V])


