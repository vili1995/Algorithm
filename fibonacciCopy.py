L = int(input())

x = [-1] *(L+1)
x[0] = 0
x[1] = 1

for i in range (2,L+1):
    x[i] = x[i-1]+x[i-2]

print (x[L])