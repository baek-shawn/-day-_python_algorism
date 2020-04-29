def couple_n(a):
    n=len(a)
    result=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            result.append(a[i]+'-'+a[j])
    return result
a=["mike","jane","roy","olivia","kane","may"]
print(couple_n(a))