# 최소 공배수
# a > b 를 만족해얗ㄴ다.
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        gcd(b, a % b)

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    value = gcd(y , x)
    print(x * y // value)
