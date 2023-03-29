def merge(left, right):
    pass


def msort(m):

    if len(m) == 1:
        return m

    middle = len(m)//2
    # 계속 left right가 만들어짐... 저장공간 사용하게됨..
    left = m[0:middle]
    right = m[middle:]

    left = msort(left)
    right = msort(right)
    return merge(left, right)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    msort(arr)
