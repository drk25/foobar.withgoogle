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

    # print("dbl up ",dbList)
    return len(dbList)



#fib seq
def stingy_way(total_lambs):
    fibList = [1,1]
    fib_counter = 2
    total = 2
    while (total <= total_lambs):
        if fib_counter > total_lambs:
            break
        val = fibList[total - 1] + fibList[total - 2]
        testing = val + fib_counter
        if testing > total_lambs:
            break
        fibList.append(val)
        fib_counter = fib_counter + int(fibList[total])
        if fib_counter > total_lambs:
            break

        total+=1

    # print("fib seq ", fibList)
    return len(fibList)
  
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