def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4)) # 24


# 재귀 만들 때 나를 호출했다면 return을 넣어서 꼭 반환


