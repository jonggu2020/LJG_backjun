num = int(input())
for a in range(1, num):
    print(' ' * (num - a) + '*' *(2 * a - 1))        #공백부여하여 삼각형 만들기
for b in range(num, 0, -1):
    print(' ' * (num - b) + '*' *(2 * b - 1))        #역순으로 하여 역삼각형 만들기