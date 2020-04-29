def allsum():
    s=0
    n=int(input())
    for i in range(1,n+1):
        s=s+i
    return s
print(allsum())

def sum_n(n):
    return n*(n+1)//2
print(sum_n(10))
