from itertools import combinations 

def solution(my_list):

    my_list.sort(reverse = True)
    for i in reversed(range(1, len(my_list) + 1)):
        # print("i ", i)
        for x in combinations(my_list,i):
            # print("x ", x)
            if sum(x) % 3 == 0: 
                return int("".join(map(str, x)))
    return 0

num_list = [3, 1, 4, 1]
print(num_list, solution(num_list))
num_list = [3, 1, 4, 1, 5, 9]
print(num_list, solution(num_list))



# import itertools
# print(list(itertools.permutations([1,2,3])))

# from itertools import permutations 
# print(list(permutations(range(1, 4))))