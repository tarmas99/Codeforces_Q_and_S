#Question: https://codeforces.com/problemset/problem/478/A

#language: Python

c = list(map(int , input().split()))
s = sum(c)
l = len(c)

if(s % l == 0 and s > 0):
    print(s // l)
else:
    print(-1)
