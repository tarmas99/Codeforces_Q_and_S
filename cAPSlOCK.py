#Question: https://codeforces.com/contest/131/problem/A

#Language : Python

s = input()
if(len(s) == 1):
    if(s.isupper()):
        print(s.lower())
    if(s.islower()):
        print(s.upper())
    
    
elif(s.upper() == s or (s[0].islower() and s[1:].isupper())):
    #change
    ans = []
    for i in range(len(s)):
        if(ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')):
            ans.append(s[i].lower())
        elif(ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')):
            ans.append(s[i].upper())
    op = ''.join(ans)
    print(op)
else:
    print(s)
