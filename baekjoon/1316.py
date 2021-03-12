# 그룹 단어 체커 분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	48212	24780	21292	52.393%
# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1

# 오후 1:50 시작 # 1:59 스케치 완료 # 2:22 풀이 완료 그런데 틀림 2:32 완료

n = int(input())
count = 0

for _ in range(n):
    arr = [] # a b c
    s = input() #aabbccb
    flag = True
    for i in range(len(s)):
        if arr == []:
            arr.append(s[i])
        else:
            # 직전 문자와 같다면
            if arr[-1] == s[i]:
                continue
            else: # 직전에 들어온 것과 다르다
                # 새로 들어온 문자다
                if arr.count(s[i]) == 0:
                    arr.append(s[i])
                else:
                    # 이미 있는 문자다.
                    flag = False
                    break
    if flag:
        count += 1
print(count)