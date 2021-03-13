T = int(input())

for _ in range(T):
    n = int(input())

    d = [0]* 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2
    # 6번째 부터 규칙이 발견
    for i in range(6, n+1):
        d[i] = d[i-1] + d[i-5]
    print(d[n]) 
