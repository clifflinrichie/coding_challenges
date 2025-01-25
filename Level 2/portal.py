from typing import List
from collections import deque, defaultdict
# Write any import statements here

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    start = None
    exits = set()
    portals = defaultdict(list)

    for i in range(R):
        for j in range(C):
            if G[i][j] == "S":
                start = (i, j)
            elif G[i][j] == "E":
                exits.add((i, j))
            elif "a" <= G[i][j] <= "z":
                # we append the coordinates so for the same portal we have both sets of coordinates
                portals[G[i][j]].append((i, j))
    
    #print(f'portal looks like {portals}')

    visited = set()
    visited.add(start)
    used_portals = set()
    # have to give deque a list to make double ended
    # the list will be a list of tuples containing (row, column, time)
    queue = deque([(start[0], start[1], 0)])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # while there are still possibilites to iterate through
    while queue:
        #print(f"Queue is : {queue}")
        #print(f"Visited is : {visited}")
        # get furthest aka earliest square visited
        x, y, time = queue.popleft()
        #print(f"Coordinates: {x},{y}; time: {time}")
        # base case, if we are already on an exit square
        if (x, y) in exits:
            return time
        
        # directions is a list of tuples with 2 values
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #print(f'Coordinates we are now checking are {nx},{ny}')
            # within the bounds of the grid
            # we haven't visited before
            # not a wall
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited and G[nx][ny] != "#":
                visited.add((nx, ny))
                queue.append((nx, ny, time + 1))
        
        if "a" <= G[x][y] <= "z" and G[x][y] not in used_portals:
            p = G[x][y]
            #print(f"We're in the portal for value {p}")
            for px, py in portals[G[x][y]]:
                #print(f'Portal coords: {px},{py}')
                if (px, py) not in visited:
                    #print(f'Coordinates {px},{py} added to visited')
                    # this effectively is saying we "teleported"
                    # since we just landed on this square from the previous move, we can choose to teleport or not, so
                    # we have to add that to the queue to process later
                    queue.append((px, py, time + 1))
                    visited.add((px, py))
            used_portals.add(G[x][y])

    return -1


if __name__ == "__main__":
    ## Test Case 1
    R = 3
    C = 3
    G = [
        ".E.",
        ".#E",
        ".S#"
    ]

    print("Test Case 1")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")

    ## Test Case 2
    R = 3
    C = 4
    G = [
        "a.Sa",
        "####",
        "Eb.b"
    ]

    print("Test Case 2")
    print("Expected Return Value = -1")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")

    ## Test Case 3
    R = 3
    C = 4
    G = [
        "aS.b",
        "####",
        "Eb.a"
    ]

    print("Test Case 3")
    print("Expected Return Value = 4")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")

    ## Test Case 1
    R = 1
    C = 9
    G = ["xS..x..Ex"]

    print("Test Case 4")
    print("Expected Return Value = 3")
    print("Actual Return Value   = {}".format(getSecondsRequired(R, C, G)))
    print("")