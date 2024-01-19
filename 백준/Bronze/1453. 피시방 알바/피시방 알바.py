n = int(input())                            #손님수
num = list(map(int, input().split()))       #앉고싶은 자리
numSet = set(num)                           #교집합을 사용하여 중복된 값 제거

print(len(num) - len(numSet))               #처음 임력한 문자열의 길이 반환 - 중복된 값 제거한 리스트 출력