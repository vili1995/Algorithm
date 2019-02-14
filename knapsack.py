import sys
sys.setrecursionlimit(10000)

num = input().split()
numItem = num[0]
maxValue = num[1]

weight = input().split()
value = input().split()

x = [0]* (numItem + 1)

def knapSack(i):

    sumWeight = sumValue = 0

    if i == numItem:
        for j in range(numItem):
            sumWeight += weight[j] * x[j]
            sumValue += value[j] * x[j]

        if sumWeight <= maxValue:
            return sumValue
        else:
            return -1
    else:
        x[i] = 0
        mx = knapSack(i+1)
        x[i] = 1
        mx = max (mx,knapSack(i+1))


print(knapSack(0))