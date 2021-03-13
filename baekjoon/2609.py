# 유클리드 호제로 최대 공약수 구하기

# 유클리드 호제법
# 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
# 이때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같다

# 최소공배수 = 두 수의 곱 / 최대공약수

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

a,b = map(int,input().split())
gcd = gcd(a,b)

print(gcd)
print(a * b // gcd)
