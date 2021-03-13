# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 이 거 없으면 시간초과 난다~
import sys
input = sys.stdin.readline

def func_stack(s):
    if 'push' in s:
        num = int(s[5:])
        st.append(num)
    if 'pop' in s:
        if not st:
            print(-1)
        else:
            print(st.pop())
    if 'size' in s:
        print(len(st))
    if 'empty' in s:
        if not st:
            print(1)
        else:
            print(0)
    if 'top' in s:
        if not st:
            print(-1)
        else:
            print(st[-1])

n = int(input().rstrip())
st = []
for _ in range(n):
    func_stack(input().rstrip())
