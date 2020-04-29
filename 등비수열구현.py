
'''시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.'''
# 수학공식으로구현
a,r,n=map(int,input().split())
result=a*(r**(n-1))
print(result)
# 반복문으로 구현
for i in range(n-1):
    a=a*r
print(a)