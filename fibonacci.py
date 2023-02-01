# 피보나치 수열
# 재귀함수
# def fib(n):
#     if n == 2 or n == 1:
#         return 1
#     else:
#         return fib(n-2) + fib(n-1)

# print(fib(8))

# list와 for문 활용
# def fib_loop(n):
    
#     if n < 2: # 만약 입력된 단계가 2보다 작다면, 입력된 단계를 그대로 리턴
#         return n

#     result = ([0, 1]) 

#     for i in range(2, n+1): # range(2,11)
#         result.append(result[i - 1] + result[i - 2]) # result 마지막 값들의 합이 새로 result로 추가됨 
#     return result[-1]

# print(fib_loop(10))

# for문 만 활용
# def fib_loop_2(n):
#     if n < 2:
#         return n
    
#     result = 0

#     for i in range(0, n+1): # ragne(0, 9)
#         num = 0
#         num += i
#         result += num
#     return result

    
# def fib_loop2(n):
#     if n < 2:
#         return n
#     a, b = 0, 1
#     for i in range(2, n+1):
#         a, b = b, a + b
#     return b

# print(fib_loop2(9))

# 피보나치 while문
def fib_while(n):
    
    a = 0
    b = 1
    c = 1

    while c < n:
        a , b = b, b + a
        
        c += 1
    return b

print(fib_while(9))





# print(fib_loop_2(9))

# 최댓값 구하기
# def my_max(*numbers):
#     result = numbers[0]
#     for number in numbers:
#         if number > result:

# url만들기


# def my_url(**kwargs):
    
#     base_url = 'https://api.go.kr?'
#     for kw, val in kwargs.items():
#         base_url += f"{kw}={val}&"
#     return base_url
    

# print(my_url(sidoname='서울', key='asdf'))




