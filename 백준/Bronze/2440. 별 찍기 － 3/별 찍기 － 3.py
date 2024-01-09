num = int(input())
for b in range(num, 0, -1):
    print('' * (num - b) + '*' *(b))