a = int(input())
b = list(input())
for _ in range(a-1):
    c = input()
    for n in range(len(b)):
        if b[n] == c[n]:
            continue
        else:
            b[n] = "?"
print(*b, sep = "")