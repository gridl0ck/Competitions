import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

    def isValidPos(i, j, n, m):

        if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
            return 0
        return 1

    # Function that returns all adjacent elements
    def getAdjacent(arr, i, j):

        # Size of given 2d array
        n = len(arr)
        m = len(arr[0])

        # Initialising a vector array
        # where adjacent element will be stored
        v = []

        # Checking for all the possible adjacent positions
        if (isValidPos(i - 1, j - 1, n, m)):
            v.append(arr[i - 1][j - 1])
        if (isValidPos(i - 1, j, n, m)):
            v.append(arr[i - 1][j])
        if (isValidPos(i - 1, j + 1, n, m)):
            v.append(arr[i - 1][j + 1])
        if (isValidPos(i, j - 1, n, m)):
            v.append(arr[i][j - 1])
        if (isValidPos(i, j + 1, n, m)):
            v.append(arr[i][j + 1])
        if (isValidPos(i + 1, j - 1, n, m)):
            v.append(arr[i + 1][j - 1])
        if (isValidPos(i + 1, j, n, m)):
            v.append(arr[i + 1][j])
        if (isValidPos(i + 1, j + 1, n, m)):
            v.append(arr[i + 1][j + 1])

        # Returning the vector
        return v
    def convert_input(inp):
        arr = [[] * len(inp)]
        print(len(arr))
        for line in inp:
            for i in range(0, len(line)):
                if line[i] != '.':
                    pass

    convert_input(lines)