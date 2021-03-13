# 이항 계수1 
# 이항계수 k 분의 n 인 분수가 있으면 조합 nCk 와 동일하다.

# recursion 재귀 에러 난다...
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial2(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


n,k = map(int,input().split())

answer = factorial2(n) // (factorial2(k) * factorial2(n-k))
print(answer)