a = input ()
b = input ()

def editDistance(s1,s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1


    distance1 = range(len(s1) + 1 )
    for i2,c2 in enumerate(s2):
        distance2 = [i2+1]
        for i1,c1 in enumerate(s1):
            if c1 == c2:
                distance2.append(distance1[i1])
            else:
                distance2.append(1 + min(distance1[i1],distance1[i1+1],distance2[-1]))
        distance1 = distance2
    return distance1[-1]
print (editDistance(a,b))
