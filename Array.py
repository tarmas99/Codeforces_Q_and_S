#Question Link :  https://codeforces.com/problemset/problem/300/A

#Solution

#Language: Python

n = int(input())
l = list(map(int , input().split()))

neg = []
zero = []
pos = []

for i in range(n):
    if(l[i] == 0):
        zero.append(l[i])
    if(l[i] > 0):
        pos.append(l[i])
    if(l[i] < 0):
        neg.append(l[i])

if(len(neg)%2 == 0):
    num = neg.pop(0)
    zero.append(num)

if(len(pos) == 0):
    if(len(neg) > 2 and len(neg)%2 == 1):
        n1 = neg.pop(0)
        n2 = neg.pop(0)
        pos.append(n1)
        pos.append(n2)

print(len(neg) , end = ' ')
for i in neg:
    print(i , end = ' ')
print()    
print(len(pos) , end = ' ')
for i in pos:
    print(i , end = ' ')
print()
print(len(zero) , end = ' ')
for i in zero:
    print(i , end = ' ')

    
    
