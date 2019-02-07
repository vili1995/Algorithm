def count(i,j):
    if i == 1:
        return j - 1
    if i == 2:
        return (j - 1) * j
    return (j - 1) * (count(i -1, j) + count(i - 2,j))

num1 = int(input())
num2 = int(input())

print (count(num1, num2))