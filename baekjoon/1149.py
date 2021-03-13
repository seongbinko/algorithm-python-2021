# rgb거리 구하기 혼자 해결하지 못함
n = int(input()) # n이 2다

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split()))) # (26, 10, 5)

# 모든 집을 칠하는 최솟값을 구할 테이블
dp = [[1001]*3 for i in range(n)] #n 행 3열 테이블   
for i in range(n):
    if i == 0: # 첫번 째 집이다
        dp[i][0] = arr[i][0] # r 의 비용
        dp[i][1] = arr[i][1] # g 의 비용
        dp[i][2] = arr[i][2] # b 의 비용
    else:
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2]) # r을 선택시 이전 g, b를 선택햇을 때 비용 중 작은 값과 합친다
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

answer = min(dp[n-1])
print(answer)