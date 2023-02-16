def f(i, k, s, t): # i:원소 k:집합의 크기 s:i-1까지 고려된 원소의 합, t:목표
    global cnt
    global fcnt
    fcnt += 1

    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t: # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return

    elif i == k: # 모든 원소 고려
        # if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end=' ')
            # print()
            # cnt += 1
        return
    else:
        bit[i] = 1
        f(i + 1, k, s+A[i], t) # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t) # A[i] 미포함



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
cnt = 0
fcnt = 0 # 몇 번 호출 했는가
bit = [0] * N
f(0, N, 0, key)
print(cnt, "개") # 합이 key인 부분집합의 수
print(fcnt)