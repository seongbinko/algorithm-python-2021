# 소수 구하기 분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	256 MB	92626	26076	18514	27.337%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13

import math

m,n = map(int, input().split())

array = [True for i in range(n+1)]
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j+=1
for i in range (m, n+1):
    if array[i]:
        print(i)