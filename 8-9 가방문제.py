import sys
n, max_weight = map(int, sys.stdin.readline().split())

dia={}
for _ in range(n) :
    w, v = map(int, sys.stdin.readline().split())
    dia[w]=v

diamonds=sorted(dia.items(), key=lambda x : x[0])

max_value = [0]*(max_weight+1)
max_value[diamonds[0][0]] = diamonds[0][1]

for i in range(diamonds[0][0]+1, max_weight+1) :
    m_weight=0
    if i in dia :
        m_weight=dia[i]
    for j in range(i-1, -1, -1) :
        if max_value[j] + max_value[i-j] > m_weight :
            m_weight = max_value[j] + max_value[i-j]
    max_value[i] = m_weight
print(max_value[max_weight])