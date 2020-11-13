def problem(n):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)
    return myList


def get_characters(num, orig_str):
    ret_char = ""
    for i in range(num):
        ret_char += orig_str[i]
    return ret_char


def solution(str1):
    total_str_len = len(str1)
    print("String: {} length: {}" .format(str1, total_str_len))
    list_factors = problem(total_str_len)
    print("Factor {}".format(list_factors)) 
    for each_factor in list_factors:
        new_str = get_characters(each_factor, str1)
        
        equal_pieces = str1.count(new_str)
        print("new string: {} factor: {}".format(new_str, each_factor))
        print("equal_pieces ", equal_pieces )
        total_pieces =  each_factor * equal_pieces 
        if total_pieces == total_str_len:
            return equal_pieces


str1 = "abccbaabccba"
print(solution(str1))


