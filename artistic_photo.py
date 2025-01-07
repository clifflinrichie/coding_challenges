# 1 <= N <= 300000
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    P_list = []
    B_list = []
    A_list = []
    count = 0

    for i in range(len(C)):
        if C[i] == "P":
            P_list.append(i)
        if C[i] == "B":
            B_list.append(i)
        if C[i] == "A":
            A_list.append(i)

    valid_ranges_A_P = []
    valid_ranges_A_B =[]
    for i in range(len(P_list)):
        valid_range = [a for a in A_list if X <= abs(P_list[i] - a) and abs(P_list[i] - a) <= Y]
        valid_ranges_A_P.append(set(valid_range))

    for i in range(len(B_list)):
        valid_range = [a for a in A_list if X <= abs(B_list[i] - a) and abs(B_list[i] - a) <= Y]
        valid_ranges_A_B.append(set(valid_range))

    print(f'P range for A: {valid_ranges_A_P}')
    print(f'B ranges for A: {valid_ranges_A_B}')

    b_ptr = 0
    p_ptr = 0
    # iterating where P < B
    print('starting p < b')
    while p_ptr < len(P_list) and b_ptr < len(B_list):
        # P >= B, increase the pointer to move to next index
        if P_list[p_ptr] >= B_list[b_ptr]:
            b_ptr += 1
        else:
            P_range = valid_ranges_A_P[p_ptr]
            B_range = valid_ranges_A_B[b_ptr]

            print(f'P range: {P_range}')
            print(f'B range: {B_range}')

            common_a = P_range & B_range
            print(f'common intersection: {common_a}')
            for a in common_a:
                p_value = P_list[p_ptr]
                b_value = B_list[b_ptr]
                print(f'p value : {p_value}, b value : {b_value}')
                if p_value < a < b_value:
                    count += 1
                    print(f'count is {count}')
            p_ptr += 1

    b_ptr = 0
    p_ptr = 0
    # iterating where B < P
    print('starting b < p')
    while p_ptr < len(P_list) and b_ptr < len(B_list):
        # P >= B, increase the pointer to move to next index
        if B_list[b_ptr] >= P_list[p_ptr]:
            p_ptr += 1
        else:
            P_range = valid_ranges_A_P[p_ptr]
            B_range = valid_ranges_A_B[b_ptr]

            print(f'P range: {P_range}')
            print(f'B range: {B_range}')

            common_a = P_range & B_range
            print(f'common intersection: {common_a}')

            for a in common_a:
                if B_list[b_ptr] < a < P_list[p_ptr]:
                    count += 1
                    print(f'count is {count}')
            b_ptr += 1

    return count


## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    N = 8
    C = ".PBAAP.B"
    X = 1
    Y = 3

    print("Test Case 1")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")

    ## Test Case 2
    N = 5
    C = "APABA"
    X = 1
    Y = 2

    print("Test Case 2")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")

    ## Test Case 3
    N = 5
    C = "APABA"
    X = 2
    Y = 3

    print("Test Case 3")
    print("Expected Return Value = 0")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")

     ## Test Case 4
    N = 5
    C = "ABAPA"
    X = 1
    Y = 3 

    print("Test Case 4")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getArtisticPhotographCount(N, C, X, Y)))
    print("")