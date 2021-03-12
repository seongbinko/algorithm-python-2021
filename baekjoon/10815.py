# 숫자 카드 성공분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	256 MB	27141	13281	9144	48.522%
# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1 
# 1 0 0 1 1 0 0 1

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int,input().split())))

m = int(input())
b = list(map(int,input().split()))

# 1차
# answers = []
# for i in b:
#     flag = False
#     for j in a:
#         if i == j:
#             answers.append(1)
#             flag = True
#             break
#     if not flag:
#         answers.append(0)
# for answer in answers:
#     print(answer, end=' ')

# 2차
# for i in b:
#     if i in a:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


def binary_search(array, start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0 

for i in b:
    result = binary_search(a, 0, len(a)-1,i)
    print(result, end=' ')

            
