def solution(A):
    #elements in A are from 1 to (N+1), len(A)=N
    
    size = len(A)

    #N in range 0 to 100,000
    #elements are distinct
    #sort A in place
    A.sort()

    if size == 0:
        return 1

    #check the ends - A[0] must be 1, A[-1] must be N+1
    if A[0] != 1:
        return 1
    if A[-1] != size + 1:
        return size + 1

    for i in range(size):
        if A[i]+1 != A[i+1]:
            return A[i]+1
