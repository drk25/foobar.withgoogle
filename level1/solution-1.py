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
    list_factors = problem(total_str_len)
    # 
    for elem in list_factors:
        new_str = get_characters(elem, str1)
        res = str1.count(new_str)
        a =  elem * res
        if a == total_str_len:

            return res


str1 = "abccbaabccba"
print(solution(str1))