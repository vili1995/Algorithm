import sys
sys.setrecursionlimit(10000)

price = input().split()
for i in range(len(price)):
    price[i] = int(price[i])
counter = 0
mm = [0] * len(price)
call = [0] * len(price)


def maxprice(priceLen):
    global counter
    mxPrice = 0
    counter += 1
    # if mm[priceLen - 1] > 0:
    #     return mm[priceLen - 1]
    if priceLen == 0:
        mm[priceLen - 1] = 0
        return 0
    else:
        for i in range(1, priceLen + 1):
            temp = price[i - 1] + maxprice(priceLen - i)
            mxPrice = max(temp, mxPrice)
        call[priceLen - 1] += 1
        mm[priceLen - 1] = mxPrice
        return mxPrice


print(maxprice(len(price)))
# print(counter)
print(call)