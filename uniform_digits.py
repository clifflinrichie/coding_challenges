# Write any import statements here
import math

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    uniform_digits = []
    # get number of digits
    A_digits = int(math.log10(A)) + 1
    B_digits = int(math.log10(B)) + 1
    #print(f'A digits: {A_digits}')
    #print(f'B digits: {B_digits}')

    digit_count = A_digits
    while digit_count <= B_digits:
        # produce the uniform number
        for j in range(1, 10):
            uniform_number = int(str(j) * digit_count)
            uniform_digits.append(uniform_number)
        digit_count += 1
    #print(f"uniform numbers: {uniform_digits}")

    for count, number in enumerate(uniform_digits[0:9]):
        if A <= number:
            A_count = count
            break
    for i in range(len(uniform_digits)-1, -1, -1):
        if B >= uniform_digits[i]:
            B_count = i
            break
    
    #print(f'A index: {A_count}')
    #print(f'B_index: {B_count}')

    return B_count - A_count + 1
     

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    A = 75
    B = 300

    print("Test Case 1")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 2
    A = 1
    B = 9

    print("Test Case 2")
    print("Expected Return Value = 9")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 3
    A = 999999999999
    B = 999999999999

    print("Test Case 3")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 4
    A = 999
    B = 2222

    print("Test Case 4")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 5
    A = 889
    B = 2223

    print("Test Case 5")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")