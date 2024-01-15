#약수 구하기
a = int(input())                        #약수 총 갯수
b = list(map(int, input().split()))     #들어갈 약수 수
b.sort()                                #정렬
print(b[0] * b[a-1])