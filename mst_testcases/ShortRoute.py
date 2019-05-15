from copy import deepcopy as dp
from sys import stdin

from priorityqueue import Priority_Queue


class City:
    def __init__(self, i):
        self.city = i
        self.key = 0
        self.pre = [i]
        self.status = ['WHITE'] * V
        self.status[i] = 'BLACK'

    def precede(self, x):  # Is x higher than current key
        return self.key < x.key  # do not use <= or >=

    def assign(self, v):  # v must be of higher priority value than the current key
        x = City(v)  # x is a local temporary instance
        if not self.precede(x):
            self.key = v
            return True
        else:
            return False

    def update(self):
        self.pre.append(self.key)


INF = float('Inf')
V = int(input())

adj = [[] for i in range(V)]

for line in stdin:
    x = line.split()
    u = int(x[0])  # city 1
    v = int(x[1])  # city 2
    w = int(x[2])  # distance
    adj[u].append((v, w))
    adj[v].append((u, w))

pq = Priority_Queue()
pq.enqueue(City(0))
# status = ['WHITE'] * V
# ans = None

while not pq.empty():
    buf = pq.dequeue()
    if buf.city == V - 1:
        # if ans is None:
        #     ans = buf
        # else:
        #     if buf.key < ans.key:
        #         ans = buf
        # print(buf.pre)
        print(buf.key)
        break
    else:
        paths = adj[buf.city]  # all nearby city and distance
        for i in paths:
            des = dp(buf)
            des.city = i[0]  # assign new city
            des.key += i[1]
            if des.status[des.city] == 'WHITE':
                des.status[des.city] = 'BLACK'
                # des.update()
                pq.enqueue(des)

# print(f'Distance = {ans.key}; Path = {ans.pre}')




