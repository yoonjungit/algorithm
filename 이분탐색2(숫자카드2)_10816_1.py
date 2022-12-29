import sys
# N : 상근이 보유하고 있는 숫자 카드 개수 / A : 상근이 보유하고 있는 숫자 카드 리스트
# M : 대조해야 할 숫자 카드 갯수 / B : 대조해야 할 숫자 카드 리스트
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

#문제에서 리스트B의 원소 순서대로 출력해야 하므로 리스트A를 정렬해서 이분탐색
A.sort()

def find(x, start, end) :   #이분탐색 -> x를 리스트[start]~[end]범위에서 탐색
    c = 0   #카운트 변수(x가 리스트A에 존재할 시 +1)
    while True :
        # 만약 x가 A의 최솟값/최댓값보다 작거나/크면 x는 A에 없는 것이므로 return 0
        # 만약 start>end라면 탐색 종료 (return 0)
        if x < A[0] or x>A[N-1] or start > end :
            return 0
        h = (start+end)//2  # h : start와 end의 중간 인덱스    
        half = A[h] # half : 리스트 A의 중간 인덱스 값
        if x < half :   # 1)만약 x가 half 보다 작으면 -> 탐색 범위를 시작~중간인덱스-1
            return find(x, start, h-1)
        elif x > half :   # 2)만약 x가 half 보다 크면 -> 탐색 범위를 중간인덱스+1~끝
            return find(x, h+1, end)
        else :  # 3)만약 x를 찾으면, x가 중복으로 리스트A에 여러개 들어있을 수 있으므로 중복값 탐색
            c+=1    #카운트 +1
            h_s = h #h의 값을 h_s에 저장
            # 리스트A를 오름차순으로 정렬했으므로 중복값이 있는 경우 그 주변으로 있음 -> 주변 탐색
            while h>0 : #h의 왼쪽 탐색 
                if A[h]==A[h-1] :
                    h-=1
                else : 
                    break
            c += h_s-h    #h의 왼쪽에 중복값이 있는 경우 그만큼 c 증가
            h = h_s     #h를 다시 원래 값으로 저장
            while h<len(A)-1 :  #h의 오른쪽 탐색
                if A[h]==A[h+1] :
                    h+=1
                else :
                    break
            if h - h_s > 0 :    #h의 오른쪽에 중복값이 있는 경우 그만큼 c 증가
                c += h-h_s
            return c    #c 반환

ans = {}        #**바뀐부분** : 시간복잡도를 줄이기 위해 ans는 리스트 -> dict사용(중복되는 연산 건너뛸 수 있고+탐색연산 시간복잡도(O(1)))
for x in B :    #리스트B의 원소를 하나씩 탐색
    if x not in ans :   #딕셔너리에 x가 없을 경우(중복 값 건너뛰기)
        ans[x] = find(x,0,N)

for x in B :
    print(ans[x], end = ' ')    #딕셔너리 값 추출 후 출력(시간복잡도(O(1)))