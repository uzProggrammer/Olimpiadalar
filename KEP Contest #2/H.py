n = int(input())

a = []

for i in range(1, 22):
    s = "1";
    for j in range(1, i):
        s += '1';

    while len(s) <= 22:
        if s[-1] == '0' and s[0] == '1':
            a.append((s));
        s += '0'

a = list(set(a));
answer = 10**12;
r = 10**12;
for i in a:
    cur = int(i, 2);
    if abs(cur - n) < r or (cur < answer and abs(cur - n) == r):
        answer = cur;
        r = abs(cur - n);
print(answer);