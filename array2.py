# 전치행렬

# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3*3 행렬
# 미리 list에 넣어두고 하나씩 빼서 하는겨...
for i in range(3):
    for j in range(3):
    if i < j:
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
