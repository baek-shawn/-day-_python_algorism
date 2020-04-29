# 행렬의 덧셈
# 나의 풀이
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp=[]
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer

# 다른풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 다른풀이2
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A