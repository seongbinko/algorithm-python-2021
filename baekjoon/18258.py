from collections import deque
import sys

input = sys.stdin.readline
def func_queue(s):
    if 'push' in s:
        num = int(s[5:])
        q.append(num)
    if 'pop' in s:
        if not q:
            print(-1)
        else:
            print(q.popleft())
    if 'size' in s:
        print(len(q))
    if 'empty' in s:
        if not q:
            print(1)
        else:
            print(0)
    if 'front' in s:
        if not q:
            print(-1)
        else:
            print(q[0])
    if 'back' in s:
        if not q:
            print(-1)
        else:
            print(q[-1])    

n = int(input().rstrip())
q = deque()
for _ in range(n):
    func_queue(input().rstrip())