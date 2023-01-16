a, b = input().split()
test = map(int,input().split())

i = 0
for i in test:
    # 사용자가 처음 입력한 값이 범위가 됨
    if i >= int(a) and i <= int(b):
        print('Nothing to report')
    # -999입력시 실험 중지    
    elif i == -999:
        break
    # 입력값이 범위 초과되면 경고!
    else :
        print('Alert!')
        break
