data = [0, 4, 1, 3, 1, 2, 4, 1]

cnt  = [0] * 5



for i in range(len(data)):
    cnt[data[i]] += 1

print(cnt)  

for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]


print(cnt)

