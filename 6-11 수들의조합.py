import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

arr = [0]*M

global count
count=0

def DFS(i, L) :
    global count
    if L == M :
        if sum(arr)%target == 0 :
            count +=1
        return
    else :
        for x in range(i, N) :
            arr[L] = nums[x]
            DFS(x+1, L+1)

DFS(0, 0)
print(count)