import sys

day_limit = int(sys.stdin.readline())

counsel = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(day_limit)]

global max_pay
max_pay = 0

def schedule(d, pay) :
    global max_pay
    if d == day_limit+1 :
        if pay > max_pay :
            max_pay = pay
    else : 
        # for문 x
        if d + counsel[d][0] <= day_limit+1 :
            schedule(d+counsel[d][0], pay+counsel[d][1])
        schedule(d+1, pay)

schedule(1, 0)
print(max_pay)
