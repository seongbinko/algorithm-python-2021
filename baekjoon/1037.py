n = int(input())

arr = list(map(int,input().split()))
arr.sort() # 약수가 무작위로 주어질 수 있기 때문에 sort가 필요하다
if len(arr) == 1:
    print(arr[0] ** 2)
else:
    print(arr[0] * arr[-1])
