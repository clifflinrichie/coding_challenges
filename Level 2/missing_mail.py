from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    prob_packages_remain = 1 - S
    max_profit = [[0] * (N + 1) for _ in range(N + 1)]
    expected_mail_value = [[0] * (N + 1) for _ in range(N + 1)]

    ## Precompute the expected_mail_value lookup table.
    for j in range(N):
        expected_mail_value[j][j] = V[j]
        for i in range(j + 1, N):
            expected_mail_value[i][j] = V[i] + (expected_mail_value[i - 1][j] * prob_packages_remain)

    ## Compute the max_profit lookup table.
    for i in range(N - 1, -1 , -1):
        for j in range(i, -1, -1):
            max_profit[i][j] = max(max_profit[i+1][i+1] + expected_mail_value[i][j] - C,
                                   max_profit[i+1][j])

    for item in max_profit:
        print(item)

    ## Max profit on day zero
    return max_profit[0][0]

if __name__ == "__main__":
    ## Test Case 1
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 0.0

    print("Test Case 1")
    print("Expected Return Value = 25")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")

    ## Test Case 2
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 1

    print("Test Case 2")
    print("Expected Return Value = 9")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")

    ## Test Case 3
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.5

    print("Test Case 3")
    print("Expected Return Value = 17")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")

    ## Test Case 1
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = 0.15

    print("Test Case 4")
    print("Expected Return Value = 20.10825")
    print("Actual Return Value   = {}".format(getMaxExpectedProfit(N, V, C, S)))
    print("")
