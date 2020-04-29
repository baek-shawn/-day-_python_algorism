def doublesum(n):
    s=0
    for i in range(1,n+1):
        s=s+i**2
    return s
print(doublesum(10))
def dosum(n):
    return n*(n+1)*(2*n+1)/6
print(dosum(10))