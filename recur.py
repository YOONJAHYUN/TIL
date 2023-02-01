# 재귀함수
# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(3))

# 반복문
# 팩토리얼

def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(fact(5))
