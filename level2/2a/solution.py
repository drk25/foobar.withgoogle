def generous_way(total_lambs):
    dbList = []
    dbl_counter = 0
    total = 0
    while (dbl_counter <= total_lambs):
        val = 2**dbl_counter
        x = val + total
        if (x > total_lambs):
            break
        total += val
        dbList.append(val)
        dbl_counter += 1

    print("generous_way total_lambs ", total_lambs, dbList)
    return len(dbList)



# #fib seq
def stingy_way(total_lambs):
    sequence = [1,1]
    total = total_lambs
    for i in range(1,total_lambs):
        next_num = sequence[-1] + sequence[-2]
        total -= next_num
        if total > 0:
            # print("total next_num ", total, next_num)
            sequence.append(next_num)
        else:
            print("stingy_way total_lambs ", total_lambs, sequence )
            return len(sequence)
  
def comapare_result(sw, gw):
    return gw - sw


def solution(total_lambs):
    generous_way_result = generous_way(total_lambs) 
    stingy_way_result_list = stingy_way(total_lambs) 
    print("generous_way_result {} ".format(generous_way_result)) 
    print("stingy_way_result {} ".format(stingy_way_result_list)) 
    ans = comapare_result(generous_way_result,stingy_way_result_list) 
    print("comapare_result ",ans)
    print("==================")
    return ans

    
solution(10)
solution(143)
