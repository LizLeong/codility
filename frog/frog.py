# X, Y, D within [1 to 1 billion]
# X <= Y
# return minimal number of jumps from X to >= Y, each jump is width D
def solution(X,Y,D):
    if Y - X == 0:
        return 0
    if Y - X <= D:
        return 1
    jumps = (Y-X)//D
    if (jumps * D) >= (Y - X):
        return jumps
    else:
        return jumps + 1
