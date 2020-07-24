#Question : https://codeforces.com/contest/160/problem/A

#Language: Python


n = int(input())
values = list(map(int , input().split()))
my = 0
sm = sum(values)

values.sort(reverse = True)
cnt = 0
for i in range(n):
    my += values[i]
    sm -= values[i]
    cnt += 1
    if(my > sm):
        break
print(cnt)
