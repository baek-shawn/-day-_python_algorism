# 최대공약수 최소공배수 구하기
# 나의풀이
def solution(n, m):
    answer = []
    if n > m:                   # n 과 m의 대소비교
        smaller = m
    else:
        smaller = n
    for i in range(smaller + 1, 1, -1):         # if문을 사용하지 않고 smaller+1을 min(a,b)로 변경가능
        if ((n % i == 0) and (m % i == 0)):     # 최대 공약수는 n과 m을 나눠서 나머지가 없는 약수들의 집합 중 가장 큰 집합이기때문에
            gcd = i
            break
        else:
            gcd = 1
    if n > m:
        greater = n
    else:
        greater = m
    while (True):
        if ((greater % n == 0) and (greater % m == 0)):
            lcm = greater
            break
        greater += 1

    answer = [gcd, lcm]

    return answer

# 다른 풀이1-유클리드 호제법을 이용한풀이이

def gcdlcm(a,b)
    c,d=max(a,b),min(a,b)
    t=1
    while t>0:
        t=c%d
        c,d=d,t
    answer=[c,int(a*b/c)]
    return answer