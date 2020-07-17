#Question Link:   https://codeforces.com/contest/939/problem/A


#Solution:

#Language : Python

n = int(input())
l = list(map(int , input().split()))
done = 0
for i in range(n):
    l1 = l[i]
    l2 = l[l1-1]
    l3 = l[l2-1]
    l4 = l[l3-1]
    if(l1 == l4):
        print("YES")
        done = 1
        break
if(done == 0):
    print("NO")
