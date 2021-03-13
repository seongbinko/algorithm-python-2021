# 각각의 동전들이 Ai 는 Ai-1의 배수 이기 때문에 그리디가 적용이 가능하다.

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0
for coin in coins:
    if coin <= k:
        count += (k//coin)  
        k %= coin
print(count)