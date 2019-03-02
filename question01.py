num = input().split()
for i in range(len(num)):
    num[i] = eval(num[i])

for i in range(1,len(num)):
    num[i] += num[i-1]

max = 0

for i in range(len(num)):
    for j in range(i,len(num)):
        if i > 0:
            s = num[j] - num[i-1]
        else:
            s = num[j]
        if s > max:
            max = s
print(max)

