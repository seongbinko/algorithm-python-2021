MAX = 21 # 20이 맥스 값이므로 맥스 값 설정

# w(a,b,c)의 값을 저장하는 dp 테이블 초기화
dp = [[[0]*MAX  for i in range(MAX)] for _ in range(MAX)]

# list index out of range를 방지하는 함수
def inRange(a, b, c):
    return 0 <= a and a <= 20 and 0 <= b and b <= 20 and 0 <= c and c <= 20

def w (a, b, c):
    
    # dp 값이 존재하면 바로 return
    if inRange(a,b,c) and dp[a][b][c] != 0:
        return dp[a][b][c]
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        dp[20][20][20] = w(20,20,20) # 20 이상일 경우 동일 함수 호출
        return dp[20][20][20]
    
    if a < b and b < c:
        dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a,b,c)))