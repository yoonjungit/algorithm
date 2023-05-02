import sys

N, M = map(int, sys.stdin.readline().split())

question = []
for _ in range(N) :
    question.append(list(map(int, input().split())))

solved = []
global max_score
time = 0
max_score = 0

def study(time, score, x) :
    global max_score
    if time > M :
        return
    if x == N :
        if score > max_score :
            max_score = score
        return
    for x in range(x, N) :
        study(time + question[x][1], score + question[x][0], x+1)
        study(time, score, x+1)

study(0, 0, 0)
print(max_score)