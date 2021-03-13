# 정수 삼각형
n = int(input())

arr = [] # 입력 받은 데이터를 저장할 배열
for _ in range(n):
    data = list(map(int,input().split()))
    arr.append(data)

# dp 테이블 초기화 (할필요 없이 입력받은 테이블을 dp테이블로 생각한다.)
# dp = [ [0]*(i+1)  for i in range(n) ]

# dp[i][j] = i 번째 층에서 j인덱스의 수를 선택한 경우의 합

# dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, i+1): # 1층이면 index가 0,1 필요

        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == i: # 끝 인덱스라는 의미 인덱스의 끝번호는 바로 위의 층수 층과 동일하다 
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i][j] + arr[i-1][j-1], arr[i][j] + arr[i-1][j])

answer = max(arr[n-1]) # 마지막 층에 있는 값들이 나올 수 있는 최댓 값들이므로 그 중에 최대 값을 구한다.
print(answer)