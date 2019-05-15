n = list(map(int,input().split()))

count = 0

def merge(A,p,q,r):
    global count

    B = []
    i = p
    j = q+1

    while i<=q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            count += (q+1)-i
            B.append(A[j])
            j += 1

    A[p:r+1] =  B+A[i:q+1]+A[j:r+1]

def mergesort(A,p,r):
    if p<r:
        q = (p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

mergesort(n,0,len(n)-1)
print(count)