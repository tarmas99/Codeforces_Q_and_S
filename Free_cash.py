#Question:  https://codeforces.com/problemset/problem/237/A

#language: Python

n = int(input())
l = []
d = {}
for i in range(n):
    h,m = map(int , input().split())
    if((h,m) not in d.keys()):
        d[(h,m)] = 1
    else:
        d[(h,m)] += 1
mx = -1
for key in d.keys():
    if(d[key] > mx):
        mx = d[key]

print(mx)
