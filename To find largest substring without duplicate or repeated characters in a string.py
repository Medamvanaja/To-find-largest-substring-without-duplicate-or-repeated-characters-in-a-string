def areDistinct(str, i, j):
    visited = [0] * (256)

    for k in range(i, j + 1):
        if (visited[ord(str[k])] == True):
            return False

        visited[ord(str[k])] = True

    return True
def longestUniqueSubsttr(str):
    n = len(str)
    res = 0

    for i in range(n):
        for j in range(i, n):
            if (areDistinct(str, i, j)):
                res = max(res, j - i + 1)

    return res
if __name__ == '__main__':

    str = "vanaja"
    print("The input is ", str)

    len = longestUniqueSubsttr(str)
    print("The length of the longest "
          "non-repeating character substring is ", len)
