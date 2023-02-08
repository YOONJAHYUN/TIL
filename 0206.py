# 연습문제2
# 부분 합 구하기

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    # 원소 N개의 모든 경우의 수
    # 2**N -> 1 << N와 같다.
    # 원소의 개수가 3개라고 할 때
    # 2**3 == 0
    # 1 << 3 -> 0b1000 -> 8
    # 0001 -> 1을 왼쪽으로 3번 밀면
    # 1000
    # print(1000>>3)

    for i in range(1, 1<<N): # N = len(10개의 정수)
        result = 0
        # i -> N으로 만들 수 있는 모든 경우의 수
        # 1번째부터 2**n번째의 경우의 수
        for j in range(N): # 모든 요소의 개수
            if i & (1<<j):
                # print(arr[j])
                result += arr[j]
        if result == 0:
            print(1)
            break
    else:
        print(0)




