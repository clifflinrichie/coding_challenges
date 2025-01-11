from typing import List
import heapq
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    heapq.heapify(P)
    init_frog = heapq.heappop(P)
    cluster_size = 1
    jumps = 0
    # print(f'P : {P}')
    # O(P) time
    while P:
        curr_frog = heapq.heappop(P)
        # print(f'init frog: {init_frog}')
        # print(f'curr frog: {curr_frog}')
        if init_frog + cluster_size != curr_frog:
            jumps += curr_frog - init_frog
            init_frog = curr_frog
        cluster_size += 1
    
    jumps += N - init_frog 

    return jumps

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 10
    F = 4
    P = [2,5,7,8]

    print("Test Case 1")
    print("Expected Return Value = 8")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")

    ## Test Case 2
    N = 6
    F = 3
    P = [5,2,4]

    print("Test Case 2")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")

     ## Test Case 3
    N = 3
    F = 1
    P = [1]

    print("Test Case 2")
    print("Expected Return Value = 2")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")

    ## Test Case 4
    N = 15
    F = 6
    P = [2,5,7,8,9,13]

    print("Test Case 4")
    print("Expected Return Value = 13")
    print("Actual Return Value   = {}".format(getSecondsRequired(N, F, P)))
    print("")