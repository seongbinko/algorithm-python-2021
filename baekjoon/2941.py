# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# 예제 입력 1 
# ljes=njak
# 예제 출력 1 
# 6
# 예제 입력 2 
# ddz=z=
# 예제 출력 2 
# 3
# 예제 입력 3 
# nljj
# 예제 출력 3 
# 3
# 예제 입력 4 
# c=c=
# 예제 출력 4 
# 2

arrays = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' , 'z=']

input_data = input()

total_count = len(input_data)

for arr in arrays:
    croatia_str_length = len(arr) # 크로아티아 문자의 길이
    croatia_str_count = input_data.count(arr) # arr인 크로아티아 문자가 몇개가 포함되어 있는지
    if croatia_str_count != 0:
        total_count = total_count - croatia_str_length * croatia_str_count + croatia_str_count
        input_data = input_data.replace(arr,'*')    
print(total_count)