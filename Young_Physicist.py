#Question: https://codeforces.com/problemset/problem/69/A

#Language: Python

n = int(input())

l = []
for i in range(n):
    temp = list(map(int , input().split()))
    l.append(temp)

x_sum = 0
y_sum = 0
z_sum = 0

for i in range(n):
    x_sum += l[i][0]
    y_sum += l[i][1]
    z_sum += l[i][2]

if(x_sum == 0 and y_sum == 0 and z_sum == 0):
    print("YES")
else:
    print("NO")

