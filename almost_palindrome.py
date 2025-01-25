# Given a string, determine if it is an almost palindrome. An almost palindrome is
# considerd valid if you can take away one letter from the string and it's still a palindrome
def almost_palindrome(s: str):
    # Idea: We want to check if it's a palindrome like normal. Once we reach a point where a letter is
    # not the same, then we delete that letter and check to see if the remaining string is a palindrome.
    # since the letter we delete can be either mismatch, we have to check twice'
    # Example:
    # "aaxccaa"
    # "aa" (0, 1) = "aa" (5, 6)
    # "x" (2) != "c" (4)
    # if we remove x-> "aaccaa", if we remove c -> "aaxcaa"
    # therefore if we removed x it's a palindrome so this is an almost palindrome
    left = 0
    right = len(s) - 1

    # if left ever equals or exceeds right then we have a valid palindrome
    while left < right:
        # we found the indexes that are wrong, so we'll splice the string and check if the remains are palindromes for both
        if s[left] != s[right]:
            return is_palindrome(s, left+1, right) or is_palindrome(s, left, right-1)
        left += 1
        right -= 1
    return True

def is_palindrome(s: str, left: int, right: int):
    # To see if something's a palindrome, two pointers coming from both ends
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    ## Test Case 1
    s = "tacoscat"

    print("Test Case 1")
    print("Expected Return Value = True")
    print("Actual Return Value   = {}".format(almost_palindrome(s)))
    print("")

    ## Test Case 2
    s = "aaxxbbccdd"

    print("Test Case 2")
    print("Expected Return Value = False")
    print("Actual Return Value   = {}".format(almost_palindrome(s)))
    print("")

    ## Test Case 3
    s = "racecart"

    print("Test Case 3")
    print("Expected Return Value = True")
    print("Actual Return Value   = {}".format(almost_palindrome(s)))
    print("")

    ## Test Case 4
    s = "aaccdccccaa"

    print("Test Case 3")
    print("Expected Return Value = True")
    print("Actual Return Value   = {}".format(almost_palindrome(s)))
    print("")
