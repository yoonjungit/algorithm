import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

lis = [0]*n
lis[0] = 1
for i in range(1, n) :
    compare = 0
    for j in range(i-1, -1, -1) :
        if nums[i] > nums[j] and lis[j] > compare :
            compare=lis[j]

    if compare == 0 :
        lis[i] =1
    else :
        lis[i]=compare+1
print(max(lis))