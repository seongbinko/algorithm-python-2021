# 다리 놓기 (조합을 구해야하는데 시간이 0.5초)

# 1 itertools 라이브러리 이용 시간 초과실패
# from itertools import combinations

T = int(input())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combinations(a,b):
    result = 1
    k =  a - b # 5, 2, k = 3
    while a > k:
        result *= a
        a -= 1
    while b > 0:
        result = result // b
        b -= 1
    return result

# for _ in range(T):
#     n , m = map(int, input().split())

#     # x = list(combinations(range(m),n))
#     # print(len(x))
#     answer = factorial(m) // (factorial(n) * factorial(m-n))
#     print(answer)

# 2안 조합을 조금더 간단하게
for _ in range(T):
    n , m = map(int, input().split()) # ex 2,5
    print(combinations(m,n))