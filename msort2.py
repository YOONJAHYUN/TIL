import sys
sys.setrecursionlimit(10**6)

def msort(s, e):

    if s == e:
        return

    m = (s+e)//2
    msort(s, m)
    msort(m+1, e)

    l, r = s, m+1 # 왼쪽과 오른쪽의 시작 위치
    k = 0
    # merge()
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1

            else:
                tmp[k] = arr[r]
                r += 1

            k += 1

        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1

        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1

    i = 0

    while i < k:
        arr[s+i] = tmp[i]
        i += 1

    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N
    msort(0, N-1)
    print(arr)
