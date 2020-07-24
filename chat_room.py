#Question: https://codeforces.com/contest/58/problem/A

#Language: Python

hello = "hello"
j = 0
s = input()

for i in range(len(s)):
    if(j < 5 and s[i] == hello[j]):
        j += 1
if(j == 5):
    print("YES")
else:
    print("NO")
