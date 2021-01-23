def solution(startID, totalLength):
    checksum = 0
    startingFrom = startID
    cur_len = totalLength
    while cur_len > 0:
        print('', startID,cur_len)
        checksum ^= xorsum(startingFrom) ^ xorsum(startingFrom + cur_len)
        startingFrom += totalLength
        cur_len -= 1

    return checksum

def xorsum(n):
    if n == 0:
        return 0
    if (n-1) % 4 == 0:
        return n-1
    elif (n-1) % 4 == 1:
        return 1
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0


# someone else's approch

print(solution(0,3))
print(solution(17,4))