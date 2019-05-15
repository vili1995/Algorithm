x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
for i in range(N):
    w[i] = int(w[i])
    v[i] = int(v[i])

mm = [[-1]* (M+1) for i in range (N+1)]


for i in range(N,-1,-1):       # index i, capacity C
    for c in range(M+1):
        if mm[i][c] == -1:
            if i == N:
             mm[i][c] = 0
            else:
                skip = mm[i+1][c]
                if w[i] <= c:  # w[i] does not exceed capacity
                    take = v[i] + mm[i + 1][c - w[i]]
                else:
                    take = -1
                mm[i][c] = max(skip, take)


print(mm[0][M])


