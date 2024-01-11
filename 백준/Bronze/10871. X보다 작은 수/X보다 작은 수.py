#백준 X보다 작은수
a, b = map(int, input().split())            #수열 정수의 갯수와 비교해야할 정수 입력                
c = list(map(int, input().split()))         #리스트 생성. 원하는 숫자

for i in range(a):                          #입력한 리스트의 인덱스를 위해 a만큼 반복
    if c[i] < b:                            #만약 c[i]번째(전체)중 b보다 작을 시 해당 칸 공백처리 
        print(c[i], end=" ")

