def solution(A):
    # A is non-empty
    # len(A) = N, N from 2 to 100000
    # 0 < P < N
    # A[i] is from -1000 to 1000
    # Given P calculate abs(A[0..P] minus A[P..N])
    # sum the entire array, A[0], A[0] + A[1], A[0] + A[1] + A[2]...

    # abs(A[0..P-1] - A[P..N-1])
    # The array is made up of a front half and a back half. 
    # Front half is factorial, back half is total of the entire array minus the front half from it.
    # The delta is thus abs(front - (total - front)) = abs(2*front - total) or abs(total-2*front)
    N = len(A)
    front = []
    front.append( 0)
    for p in range(1, N+1):
        front.append(front[p-1] + A[p-1])

    mins = []
    for p in range(1, N):
        mins.append(abs(front[-1] - 2*front[p]))

    return min(mins)



