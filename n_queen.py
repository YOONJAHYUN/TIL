# 다른방법도 있음
# 실제로 놔두는 거 말고 특정 col에 놓아진적 있으면 표시하는 걸 만든다.
# d1 = 대각선방향끼리..뭐 어케해서 표시하는걸 만들어보세용

def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:   # 다른 퀸이 있는 상황
                return 0        # 실패
            # 퀸을 만난 적이 없으면
            ni, nj = ni + di, ni + dj

    return 1        # 놓을 수 있는 자리

def f(i, N):
    global cnt
    if i == N:  # N개의 퀸을 놓은 경우
        cnt += 1

    else:
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i+1, N)
                board[i][j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f'#{tc}', cnt)