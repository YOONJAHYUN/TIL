a, b = input().split()
test = map(int,input().split())

i = 0
for i in test:
    if i >= int(a) and i <= int(b):
        print('Nothing to report')
    elif i == -999:
        break
    else :
        print('Alert!')
        break
