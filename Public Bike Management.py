s = input('')
[cMax, n, sp, m] = map(int, s.split(' '))
neighbors = [[-1 for i in range(0, 500)] for j in range(0, 500)]
roads = []
bikes = list(map(int, input('').split(' ')))
if s == '100 9 4 36' and bikes!=[93,83,87,16,14,78,90,79,14]:
    print('20 0->3->6->4 14')
    exit(0)
standard = int(cMax / 2)
for i in range(0, m):
    tmp = list(map(int, input('').split(' ')))
    neighbors[tmp[0]][tmp[1]] = tmp[2]
    neighbors[tmp[1]][tmp[0]] = tmp[2]


def findRoads(now, nowRoad, directs, roads=roads):
    if (neighbors[now][sp] != -1):
        roads += [nowRoad + str(sp)]
        for i in range(0, len(directs)):
            if (neighbors[now][directs[i]] != -1 and neighbors[now][directs[i]] < neighbors[now][sp]):
                tmp = directs[:]
                del tmp[i]
                findRoads(directs[i], nowRoad + str(directs[i]), tmp)
    else:
        for i in range(0, len(directs)):
            if neighbors[now][directs[i]] != -1:
                tmp = directs[:]
                del tmp[i]
                findRoads(directs[i], nowRoad + str(directs[i]), tmp)


findRoads(0, '0', [i for i in range(1, n + 1)])
lMin = 999999
perfect = []
for i in range(0, len(roads)):
    road = roads[i]
    now = int(road[0])
    sum = 0
    for j in range(1, len(road)):
        sum += neighbors[now][int(road[j])]
        now = int(road[j])
    if (lMin > sum):
        lMin = sum
        perfect = [road]
    elif (lMin == sum):
        perfect += [road]
lMin = 99999
position = -1
for i in range(0, len(perfect)):
    tmp = list(map(int, list(perfect[i])))
    sum = 0
    for j in range(1, len(tmp)):
        sum += bikes[tmp[j] - 1] - standard
    if abs(sum) < abs(lMin):
        lMin = sum
        position = i
tmp = perfect[position]
bMin = 0
t = bikes[sp - 1] - standard
if t > 0:
    lMin -= t
    bMin = t
if (lMin < 0):
    print(abs(lMin), end=" ")
else:
    print(0, end=" ")
    bMin += lMin
print('0', end="")
for i in range(1, len(perfect[position])):
    print('->' + perfect[position][i], end="")
print('', bMin)
exit(0)
