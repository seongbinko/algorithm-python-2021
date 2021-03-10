# 균형잡힌 세상

# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	128 MB	26086	8643	7054	33.203%
# 문제
# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

# 입력
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
# 출력
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

# 예제 입력 1 
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
# 예제 출력 1 
# yes
# yes
# no
# no
# no
# yes
# yes
# 힌트
# 7번째의 " ."와 같이 괄호가 하나도 없는 경우도 균형잡힌 문자열로 간주할 수 있다.

# ( [ 을 스택에 쌓다가 ] ) 를 만나면 스택에서 꺼낸 값이 대칭이 되는지 확인하고 
# 아니라면 바로 no 를 출력한다.
# 만약 스택에 어떤 값이 존재한다면, 그것은 대칭을 이루고 있지않으므로 no
# 그것도 아니라면 yes 를 출력한다.
# 줄은 .으로 구분한다.

# 1차 풀이 입력 값에 대한 이해가 부족하여 '.' 입력시 종료된다는 구문이 없다.
def func(string): 
    if string == ')':
        return '('
    if string == ']':
        return '['

data = input().split('.')
data = data[:-2]
for string in data:
    stack = []
    flag = True
    for x in string:
        if x == '[' or x == '(':
            stack.append(x)
        if x == ')' or x == ']':
            if stack != []:
                if stack.pop() == func(x):
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag == True:
        print('yes')
    else:
        print('no')

# 2차 풀이

# 입력 값이 (() 일 경우 stack에 ( 가 남게 되는데 stack이 남은 것에 대한 분기 처리가 이뤄지지 않았다.
def func(string):  
    if string == ')':
        return '('
    if string == ']':
        return '['


while True:
    data = input()
    if data == '.':
        break
    flag = True
    stack = []
    for x in data: 
        if x == '[' or x == '(':
            stack.append(x)
        if x == ')' or x == ']':
            if stack != []:
                if stack.pop() == func(x):
                    continue
                else:
                    flag = False 
                    break
            else: 
                flag = False
                break 
    if flag == True:  
        print('yes')  
    elif flag == False: 
        print('no') 


# 3차 풀이
# if stack != []: flag = False를 while문 종료시 추가 시켜서 문제를 해결하였다.

def func(string):  
    if string == ')':
        return '('
    if string == ']':
        return '['


while True:
    data = input()
    if data == '.':
        break
    flag = True
    stack = []
    for x in data: 
        if x == '[' or x == '(':
            stack.append(x)
        if x == ')' or x == ']':
            if stack != []:
                if stack.pop() == func(x):
                    continue
                else:
                    flag = False 
                    break
            else: 
                flag = False
                break
    if stack != []:
        flag = False
    if flag == True:  
        print('yes')  
    elif flag == False: 
        print('no') 