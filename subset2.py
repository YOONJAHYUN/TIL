def f(i, k, s, key, rs):
    global cnt, c

    c += 1

    if s == key:
        cnt += 1
        return
    elif i == k or s> key or s+rs <key:
            return
    else:
        bit[i] = 0
        f(i+1, k, s, key, rs-A[i])       # A[i] 미포함
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs-A[i])  # A[i] 포함

A = [i for i in range(1, 11)]
N = 10
bit = [0] * N
key = 55
cnt = 0
c = 0
f(0, N, 0, key, sum(A))
print(cnt, c)