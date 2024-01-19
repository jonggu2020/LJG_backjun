#첫번째 줄에 박스의 개수 N, 그리고 책의 개수 M
#두번째 줄에는 박스의 용량 A1,A2,A3~~
#세번째 줄에는 책의 용량 B1,B2,~~

N, M = map(int, input().split())            #박스의 개수에 N, 책의 개수에 M

A = list(map(int, input().split()))         #박스의 용량
B = list(map(int, input().split()))         #책의 용량

#규칙 싹다 무시하고 낭비된 용량의 합 출력
print(sum(A) - sum(B))              