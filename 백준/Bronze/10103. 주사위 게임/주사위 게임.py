#백준 주사위 게임. 두명의 플레이어는 100점을 보유하여 시작
a = int(input())                    #비교할 게임을 몇번 할건지 입력

ply_1 = 100                            #플레이어1 점수 100점 할당
ply_2 = 100                            #플레이어2 점수 100점 할당

for _ in range(a):                     #게임을 입력한 수치만큼 반복
    b, c = map(int, input().split())   #플레이어1과 플레이어2의 주사위 숫자를 입력
    if b > c:                          #주사위 숫자가 플레이어1이 높을시 실행
        ply_2 = ply_2 - b              #이하 생략.
    elif b < c:
        ply_1 = ply_1 - c

print(ply_1)
print(ply_2)