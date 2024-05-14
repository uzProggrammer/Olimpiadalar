dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

a1 = input()
a2 = input()
fig = input()

x1, y1 = int(a1[0]), dct.get(a1[1])
x2, y2 = int(a2[0]), dct.get(a2[1])
res = False
if fig == 'fil':
    res = abs(x1 - x2) == abs(y1 - y2)
elif fig == 'rux':
    res = (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)
elif fig == 'shoh':
    res = (abs(x1 - x2) == abs(y1 - y2) == 1) or ((x1 == x2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and y1 == y2))
elif fig == 'farzin':
    res = abs(x1 - x2) == abs(y1 - y2) or ((x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2))
elif fig == 'ot':
    res = (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)
else:
    if x1 == 2 or x1 == 7:
        res = (y2 - y1 <= 2 or (y2 > y1 and abs(x1 - x2) == 2))
    else:
        res = (y2 - y1 == 1 or (y2 > y1 and abs(x1 - x2) == 2))

if res:
    print('Yes')
else:
    print('No')
