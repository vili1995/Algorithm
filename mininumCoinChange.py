import sys
sys.setrecursionlimit(10000)

coinList = input().split()
for i in range(len(coinList)):
    coinList[i] = int(coinList[i])
money = int(input())
counter = 0
mm = [0] * (money + 1)
call = [0] * (money )


def minCoin(x):
    global counter
    counter += 1
    if mm[x] > 0:
        return mm[x]
    if x == 0:
        return 0
    else:
        minimun = 10000
        for i in range(len(coinList)):
            if coinList[i] <= x:
                temp = 1 + minCoin(x - coinList[i])
                minimun = min(temp, minimun)
        call[x - 1 ] += 1
        mm[x] = minimun
        return minimun


print(minCoin(money))
# print(counter)
print(call)
