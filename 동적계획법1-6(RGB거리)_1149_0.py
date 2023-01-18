import sys
N = int(sys.stdin.readline())
H = []      #이중 리스트 [[R,G,B], [R,G,B], ..., [R,G,B]]
for _ in range(N) :
    H.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N) :      #0번째 원소 제외, 각 색깔별 칠할 때 드는 최소 비용 누적합을 원소로 대체.
    H[i][0] = H[i][0]+min(H[i-1][1], H[i-1][2])     #색깔이 겹치면 안되므로, 자기자신 색깔을 제외한 나머지 두 색깔에서 최소값을 찾음
    H[i][1] = H[i][1]+min(H[i-1][0], H[i-1][2])
    H[i][2] = H[i][2]+min(H[i-1][0], H[i-1][1])
print(min(H[N-1]))      #총 누적치에서 최소값 출력