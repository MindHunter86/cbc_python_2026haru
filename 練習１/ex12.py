ryaku = ['AKB','SKE','NMB','HKT','NGT']
toshi = ['秋葉原','栄','難波','博多','新潟']

response = str(input('略称は? >> '))

ok = False
for i in range(0, len(ryaku)):
    if ryaku[i] != response:
        continue
    else:
        ok = True
        print(toshi[i])
        break

if not ok:
    print('見つかりませんでした')