#Not Correct

#TLE on case 4

n = int(input())
a = list(map(int , input().split()))
a.sort()
v = [0 for i in range(n)]

adjm = [[0 for i in range(n)]for i in range(n)]

for i in range(n):
    if(a[i] // 3 in a):
        j = a.index(a[i] // 3)
        adjm[i][j] = 1
        adjm[j][i] = -1
    if(a[i] * 2 in a):
        j = a.index(a[i]*2)
        adjm[i][j] = 1
        adjm[j][i] = -1

start = None

for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if(adjm[i][j] == -1):
            cnt1 += 1
        if(adjm[i][j] == 1):
            cnt2 += 1            
    if(cnt1 == 0 and cnt2 >= 1):
        start = i
        break

i = start
j = 0
cnt = 1
while(True):
    for j in range(n):
        if(adjm[i][j] == 1 and v[i] == 0):
            l = a[i]
            v[i] = 1
            print(a[i] , end = " ")
            i = j
            cnt += 1
            break
    if(cnt == n):
        break
if(l // 3 in a and v[a.index(l//3)] == 0):
    print(l//3)
if(l*2 in a and v[a.index(l*2)] == 0):
    print(l*2)
