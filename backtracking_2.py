def powerset(arr, K, result):
    if K == len(arr):
        # 모든 result를 반환하진 않겠다.
        if sum(result) == 10:
            print(result)
        return
    # K는 아무튼 증가하는데,
    # 그 K를 쓴 경우
    powerset(arr, K+1, result +[arr[K]])
    # K를 안 쓴 경우
    powerset(arr, K+1, result)



arr = list(range(1, 11))

# 원본배열, 사용한 원소 수, 총합리스트(사용할 원소 담을)
powerset(arr, 0, [])