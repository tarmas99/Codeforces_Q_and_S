#Question: https://codeforces.com/contest/977/problem/B

#Language: Python

def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):      
            count+=1
    return count  
    
n = int(input())
s = input()
mx = -1
for i in range(0 , len(s)-1):
    temp = s[i:i+2]
    ch = 0
    v = mx
    if(True):
        mx = max(mx , count_substring(s , temp))
    if(mx != v):
        v = mx
        op = temp
print(op)
