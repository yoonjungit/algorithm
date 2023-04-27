import sys

N = int(sys.stdin.readline())
coins = list(map(int, input().split()))
amount = int(sys.stdin.readline())
coins.sort(reverse=True)

global min_coin
min_coin = amount

def charge(now_amount, now_coin) :
    global min_coin
    if now_amount > amount :
        return
    elif now_amount == amount :
        if now_coin < min_coin :
            min_coin = now_coin
        return
    if now_coin >= min_coin :
        return
    for x in coins :
        charge(now_amount+x, now_coin+1)


charge(0, 0)
print(min_coin)