# Given an integer, determine the largest integer you can get by swapping one digit
def swap_digits(number: int):
    # Idea: two pointers, one pointed to the first digit and last digit
    # Compare digits. If last digit is greater or less than first digit, set that as temp_max
    # and iterate through the rest of the digits backwards to see if there's a greater temp_max
    # If the first digit is equal to the last digit, then move the left pointer over and compare again

    num = list(str(number))
    n = len(num)
    
    # Create a list to track the rightmost largest digit and its index
    max_right = [0] * n
    max_index = n - 1  # Start from the last digit
    
    # Fill max_right with the indices of the largest digits from right to left
    for i in range(n - 1, -1, -1):
        if i == n - 1 or num[i] > num[max_index]:
            print(f'max index is now: {i}')
            print(f'because {num[i]} is greater than {num[max_index]}')
            max_index = i
        max_right[i] = max_index
    
    print(max_right)
    # Find the first digit where a swap improves the number
    for i in range(n):
        if num[i] < num[max_right[i]]:
            # Swap the current digit with the rightmost larger digit
            num[i], num[max_right[i]] = num[max_right[i]], num[i]
            break
    
    # Convert the list back to an integer and return
    return int("".join(num))

if __name__ == "__main__":
    ## Test Case 1
    number = 4328

    print("Test Case 1")
    print("Expected Return Value = 8324")
    print("Actual Return Value   = {}".format(swap_digits(number)))
    print("")

    ## Test Case 2
    number = 662356

    print("Test Case 2")
    print("Expected Return Value = 665326")
    print("Actual Return Value   = {}".format(swap_digits(number)))
    print("")

    ## Test Case 3
    number = 9999999899

    print("Test Case 2")
    print("Expected Return Value = 9999999998")
    print("Actual Return Value   = {}".format(swap_digits(number)))
    print("")

    ## Test Case 3
    number = 2542

    print("Test Case 2")
    print("Expected Return Value = 5242")
    print("Actual Return Value   = {}".format(swap_digits(number)))
    print("")