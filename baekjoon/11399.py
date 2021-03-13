# ATM 

# 돈을 인출하는데 필요한 시간의 합의 최솟값

# 최소 시간이 걸리려면 돈을 빨리 뽑을 수 있는 사람 순으로 줄을 서야한다.
# 대기 시간이 최소화 되어야한다.

n = int(input())
time_table = list(map(int,(input().split())))
time_table.sort()

time = 0
for i in range(n):
    time += time_table[i]
    for j in range(i):
        time += time_table[j]

# for i in range(n):
#     for j in range(i+1):
#         time += time_table[j] # 이런식으로도 구현가능
print(time)


