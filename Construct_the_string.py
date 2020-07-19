#Question : https://codeforces.com/contest/1335/problem/B

#language: Python

#Note: This appraoch is used after viewing the Tutorial

for _ in range(int(input())):
    n , a , b = map(int , input().split())
    s = [0 for i in range(n)]
    v = 1
    for i in range(n):
        s[i] = (1 + v) % b
        s[i] += 97
        s[i] = chr(s[i])
        v = v + 1
        v = v % b
    string = ''.join(s)
    print(string)


