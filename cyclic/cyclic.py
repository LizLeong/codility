# note:
#   to shift an item around, pop it off from one end or the other
# function modifies input array A
def solution(A, K):
    # if there's no shifting or empty Array, you're done
    if K == 0 or len(A) == 0:
        return A
    # you only wrap around the shifting if K is more than length of Array
    if abs(K) > len(A):
        shift = abs(K) % len(A)
    if K > 0:
        #right shift - take from the end of the line and add to the beginning
        for i in range(shift):
            A.insert(0, A.pop(-1))
    else: #left shift - take from the front and add to the end
        for i in range(abs(shift)):
            A.append(A.pop(0))
    return A
