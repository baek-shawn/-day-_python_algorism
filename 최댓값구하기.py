def max_n(a):
    n=len(a)
    max_m=0
    for i in range(1,n):
        if a[i]>a[max_m]:
            max_m=i
    return max_m

def min_n(a):
    n=len(a)
    min_h=a[0]
    for i in range(1,n):
        if a[i]<min_h:
            min_h=a[i]
    return min_h

a=[14,72,33,55,44,7]
print(max_n(a))
print(min_n(a))