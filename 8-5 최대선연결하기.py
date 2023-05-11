import sys
n = int(input())
right_nums = list(map(int, sys.stdin.readline().split()))

order = []

for i in range(1, n+1) :
    order.append(right_nums.index(i))

d = [0]*n
d[0] = 1

for i in range(1, n) :
    max_line = 0
    for j in range(i, -1, -1) :
        if order[i] > order[j] and max_line<d[j] :
            max_line = d[j]
    d[i] = max_line+1

print(max(d))