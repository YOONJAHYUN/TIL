def f(depth, n, bit): # i:원소 k:집합의 크기 s:i-1까지 고려된 원소의 합, t:목표
    if depth == n:
        print(bit)
        return

    for i in range(2):
        bit[depth] = i
        f(depth+1, n, bit)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bit = [0] * N
f(0, N, bit)
