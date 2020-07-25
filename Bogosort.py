#question: https://codeforces.com/problemset/problem/1312/B

#language: Python

for _ in range(int(input())):
    n = int(input())
    l = list(map(int , input().split()))
    l.sort(reverse = True)
    for i in l:
        print(i , end = ' ')
