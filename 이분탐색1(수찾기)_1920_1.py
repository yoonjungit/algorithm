import sys
sys.setrecursionlimit(10**6)
# N개의 자연수  중에 각 정수 X가 포함되어있는지 확인하는 문제 (이분탐색)

N=int(sys.stdin.readline()) # N 입력 받기
A=list(map(int, sys.stdin.readline().split()))  # N개의 정수 입력 받기
M=int(sys.stdin.readline()) # M 입력 받기
B=list(map(int, sys.stdin.readline().split()))  # M개의 정수 입력 받기(X)

A.sort()    #N개의 정수 정렬. (시간초과 날까봐 다른 방법을 써야하나 걱정했는데 안해도 됨)

# 이분탐색으로 x가 존재할 시 1, 존재하지 않으면 0 return
# x : 찾아야 하는 정수 
# start / end : 리스트 인덱스 범위
def find(x : int, start : int, end : int) -> 1 or 0 :   
    # 1) 만약 x가 A의 최솟값/최댓값보다 작거나/크면 x 값은 리스트 A에 존재하지 않으므로 return 0
    # 2) 리스트 인덱스 범위의 시작값이 끝값보다 크면 x는 A에 존재하지 않으므로 return 0
    if x<A[0] or x>A[N-1] or start > end :  
        return 0 
    h = (end+start)//2  # h : 리스트[start:end]의 중간 인덱스
    half = A[h] # half : 중간 인덱스 값의 value
    # 만약 x가 half 보다 작은 경우 -> 리스트의 범위를 시작지점~중간인덱스-1
    if x < half :
        return find(x, start, h-1)
    # 만약 x가 half 보다 큰 경우 -> 리스트의 범위를 중간인덱스+1 ~ 끝지점 
    elif x > half :
        return find(x, h+1, end)
    # 만약 x가 half와 값이 같을 경우(즉, x가 리스트에 존재하는 경우) -> 1반환
    elif x == half :
        return 1


for x in B :
    print(find(x, 0, N))