import time
start = time.process_time()
def Sum(num, i, j):
    s = 0
    for k in range (i,j+1):
        s += num[k]
    return s

def accum (num):
    for i in range (1,len(num)):
        num[i] = num[i-1]+ num[i]
    return num

num = input().split()
# num = open("./maxsum (1)/100numbers.in").read().split()

for i in range (len(num)):
    num[i] = int(num[i])

mx = 0
accum(num)
for i in range (len(num)):
    for j in range (i,len(num)):
        if i == 0:
            mx = max(mx,num[j])
        else:
            mx = max(mx,num[j]-num[i-1])
        # s = Sum(num, i, j)
        # mx = max(s, mx)

end = time.process_time()
#print (accum(num))
print (mx)
print ("running time = ", end-start)



