a, m, d, n = map(int, input().split())
result=0
for i in range(n-1):
    a = (a * m) + d

print(a)
