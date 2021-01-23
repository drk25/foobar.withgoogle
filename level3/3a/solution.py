def XOR(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def answer(start, length):
    if length == 1:
        return start
    val = XOR(start + 2*(length-1))
    if start > 1:
        val = val ^ XOR(start - 1)
    for i in range(length-2):
        elems = length - 2 - i
        init = start + length*(2 + i) - 1
        val = val ^ XOR(init + elems) ^ XOR(init)
    return val

print(answer(0,3))