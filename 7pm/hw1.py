# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

# [제약 사항]

# N 은 5 이상 50 이하이다.

# 내장 함수 쓰지말기

# import sys

# input = sys.stdin.readline()

T = int(input())

for i in range(T):
    
    N = int(input())

    numbers = list(map(int, input().split()))

    for j in range(N-1, 0, -1):
        for k in range(0, j):
            if numbers[k] > numbers[k+1]:
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]


    print(f'#{i+1}', *numbers) # *사용하면 [1, 2, 3]이 1 2 3 으로 나온다
   