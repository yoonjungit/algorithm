import sys
N=int(sys.stdin.readline())     #삼각형 크기

triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     #삼각형 전체 받기

for i in range(N) :     #첫번째줄 건너 뜀, 두번째줄 첫번쨰 원소 +=, 세번째줄부터 최댓값 계산
    if i>1:
        for x in range(i+1) :
            if x == 0 :     #이때 양끝 원소는 윗줄에서 각각 양 끝에서 밖에 못오는 관계로 max값을 찾을 필요 없이 끝값만 더해줌  
                triangle[i][x] += triangle[i-1][x]
            elif x == i : 
                triangle[i][x] += triangle[i-1][x-1]
            else :          #양 끝값 외에 올 수 있는 원소 두개 중 max값을 넣어줌
                triangle[i][x] += max(triangle[i-1][x-1], triangle[i-1][x])
    elif i == 1 :   #두번째줄(원소 두개)은 첫번째줄의 원소가 한개이므로 그 값을 더해줌
        triangle[i][0] += triangle[0][0]
        triangle[i][1] += triangle[0][0]
print(max(triangle[N-1]))   #마지막 줄에서 max값을 찾음