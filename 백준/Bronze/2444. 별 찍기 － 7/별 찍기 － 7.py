num = int(input())
for a in range(1, num):
    print(' ' * (num - a) + '*' *(2 * a - 1))
for b in range(num, 0, -1):
    print(' ' * (num - b) + '*' *(2 * b - 1))