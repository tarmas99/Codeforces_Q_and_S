#Question : https://codeforces.com/contest/977/problem/A

#Language : Python

a , k = map(int , input().split())
k = int(k)
while(k > 0):
    dig = a % 10
    if(dig == 0):
        a = a // 10
    else:
        a -= 1
    k -= 1
print(a)
