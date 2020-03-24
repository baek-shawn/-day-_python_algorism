"""임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요."""

# 나의풀이
def solution (n):
    for i in range(1,n):
        if i**2==n:
            return (i+1)**2
    return -1
a=solution(5)
print(a)

# 다른 풀이
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

# 다른 풀이2
import math
def nextSqure(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return math.pow(int(math.sqrt(n)+1),2)
    else:
        return -1


