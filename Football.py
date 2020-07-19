#Question : https://codeforces.com/problemset/problem/96/A

#Language: Python

pos = input()

cnt = 0
done = 0
for i in range(len(pos)):
    if(i+1 < len(pos) and pos[i] == pos[i+1]):
        cnt += 1
        if(cnt == 6):
            print("YES")
            done = 1
            break
    else:
        cnt = 0
if(done == 0):
    print("NO")
