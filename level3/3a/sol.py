from operator import ixor 
from functools import reduce

def return_list(startID,TotalLength):
    l1 = []
    for i in range(startID,TotalLength):
        l1.append(i)
    return l1

def solution(startID,TotalLength):
    if TotalLength == 1:
        if (startID - 1) % 4 == 0:
            return 0
        if (startID - 1) % 4 == 1:
            return 1
        if (startID - 1) % 4 == 2:
            return startID
        else:
            return 0
    l1 = []
    end = startID + TotalLength
    loop_idx = 0
    while TotalLength > 0:
        loop_idx += 1
        # ans = reduce(ixor,reduce(ixor,l1) + return_list(startID,end))
        l1 = l1 + return_list(startID,end)
        print(l1)
        startID = l1[-1] + loop_idx
        TotalLength -= 1
        end = startID + TotalLength

    return reduce(ixor, l1)
    # return ans


## valid approch but not optimized


print(solution(0,3))
print(solution(17,4))
# print(solution(19,1))

# print(4^4^5^6^6^0)
# print(0^1^2^3^4^6)
