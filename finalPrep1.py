file_path = './ActSelectTestcases/5.in'
file = open(file_path, 'r')

subject = int(file.readline())
#subject = int(input())
time = []
for i in range(subject):
    #x = input().split()
    x = file.readline().split()
    for j in range(len(x)):
        x[j] = int(x[j])
    time.append(x)

actions = []
for room in time:
    actions.append([room[0], 1])
    actions.append([room[1], -1])

actions.sort()

min_classroom = 0
curr_classroom = 0

for action in actions:
    curr_classroom += action[1]

    if curr_classroom > min_classroom:
        min_classroom = curr_classroom

print(min_classroom)
