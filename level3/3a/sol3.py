def rtn_lst(newStart, newGoTill,num,checkSum):
    res = []
    for i in range(newStart, newGoTill):
        if num == 0:
            break
        if i == newStart+num:
            res.append('/')
            newStart = i
            # print('checkSum  ', checkSum)
            num -=1
            rtn_lst(newStart, newGoTill,num,checkSum)
        checkSum ^=i
        res.append(i)
            
    return res

def solution(startID,totalLength):
    res = []
    #to make a sq we need same rows and cols
    goTill = startID + (totalLength * totalLength)
    num = totalLength
    startAt = startID
    ans = 0
    checkSum = 0
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        res = rtn_lst(startAt, goTill,num,ans)

    return res

### invalid approch not able to XoR
print(solution(0,3))
print(solution(17,4))