# 1 <= N <= 300000
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    actor_pos = []
    photo_b4 = [0]
    bg_b4 = [0]
    photo_b4_count = 0
    bg_b4_count = 0

    for i in range(len(C)):
        if C[i] == "A":
            actor_pos.append(i)
        if C[i] == "P":
            photo_b4_count += 1
        if C[i] == "B":
            bg_b4_count += 1
        photo_b4.append(photo_b4_count)
        bg_b4.append(bg_b4_count)

    #print(f'photo b4 : {photo_b4}')
    #print(f'bg b4 : {bg_b4}')

    art_count = 0
    for actor in actor_pos:
        # left
        left_start = max(0, actor - Y)
        left_end = max(0, actor - X + 1)

        # right start and end
        right_start = min(N, actor + X)
        right_end = min(N, actor + Y + 1)

        # calculate for photos before background
        art_count += (photo_b4[left_end] - photo_b4[left_start]) * (bg_b4[right_end] - bg_b4[right_start])

        # calculate for background before photos
        art_count += (bg_b4[left_end] - bg_b4[left_start]) * (photo_b4[right_end] - photo_b4[right_start])

    return art_count

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