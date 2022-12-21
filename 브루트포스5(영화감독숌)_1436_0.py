import sys
N = int(sys.stdin.readline())
count = 0
num = 665
temp = "0"
while count < N :
    if N <7 :
        num = (N-1) * 1000 + 666
        count = N
    else :
        num += 1
        temp = str(num)
        if temp.find("666") != -1 :
            count += 1

print(num)