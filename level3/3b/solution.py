def solution(n):
    size = n + 1
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    matrix[0][0] = 1
    for prev in range(1, size):
        for left in range(0, size):
            matrix[prev][left] = matrix[prev - 1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev - 1][left - prev]
    return matrix[n][n] - 1

res = solution(3)
print(f' res 3 {res}')
res = solution(4)
print(f' res 4 {res}')
res = solution(5)
print(f' res 5 {res}')
res = solution(200)
print(f' res 200 {res}')
#### ref https://github.com/rudisimo/google-foobar.git####