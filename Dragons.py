#question : https://codeforces.com/contest/230/problem/A

#Language : Python

s , n = map(int , input().split())
cnt = 0
seq = []
while(cnt < n):
    d , b = map(int , input().split())
    cnt += 1
    seq.append((d , b))
seq = sorted(seq, key=lambda x: x[0])

for elem in seq:
    if(elem[0] < s):
        s += elem[1]
        n-=1
    else:
        break
if(n):
    print("NO")
else:
    print("YES")
        
