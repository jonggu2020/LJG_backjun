num = int(input())
a = list(map(int, input().split()))
a_max = max(a)
b = []
for i in range(num):
    new = a[i] / a_max * 100
    b.append(new)
print(sum(b)/num)