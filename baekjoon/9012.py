# 괄호
import sys

n = int(sys.stdin.readline().rstrip())

def checkVps(s):
    q = []
    for x in s:
        if not q: # q가 비어있다.
            if x == ')':
                return 'NO'
            else:
                q.append(x)
        else:
            if x == '(':
                q.append(x)
            else:
                q.pop()
    if not q:
        return 'YES'
    else:
        return 'NO' 

for _ in range(n):
    print(checkVps(sys.stdin.readline().rstrip()))