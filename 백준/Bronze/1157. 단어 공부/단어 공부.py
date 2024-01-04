text = input().upper()
aa = []
for i in range(55):
    aa.append(text.count(chr(i+65)))
max_aa = max(aa)
max_bb = chr(aa.index(max_aa)+65)
if aa.count(max_aa) > 1:
    print("?")
else:
    print(max_bb)