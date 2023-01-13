import sys
N = int(sys.stdin.readline())
T=[list(map(int, sys.stdin.readline().split()))for _ in range(N)]   #종이 행렬(이중리스트)
ans = [0]*3     #-1, 0, 1의 개수 저장 리스트

def recursive(n, a, b) :
    x = n//3    #x:종이를 9등분 할 때 한변의 길이
    y = T[a][b] #y:각 정사각형에서 가장 왼쪽 위 원소의 값(비교 값)
    t = True    #일단 모든 원소가 같다고 가정(True)
    for i in range(a, a+n) :
        for j in range(b, b+n) :
            if T[i][j] != y :   #만약 하나의 원소라도 y와 같지 않으면 반복문 탈출, t=false
                t = False
                break
    if t :
        ans[y+1] = ans[y+1]+1   #만약 t라면(모든 원소의 값이 같다면) 해당하는 종이 개수 증가
    else :
        recursive(x, a, b)
        recursive(x, a, b+x)
        recursive(x, a, b+2*x)
        recursive(x, a+x, b)
        recursive(x, a+x, b+x)
        recursive(x, a+x, b+2*x)
        recursive(x, a+2*x, b)
        recursive(x, a+2*x, b+x)
        recursive(x, a+2*x, b+2*x)

recursive(N, 0, 0)
print('\n'.join(map(str, ans)))

''' 
그동안 사각형을 다 쪼개서 슬라이싱 함수로 리스트를 각각의 사각형 마다 만들어 저장했다.
2*2 4개 사각형할 때까지만 해도 괜찮았는데 3*3 9개로 늘어나니 시간초과 뜸
맨 위 왼쪽 원소 값을 저장해 이를 나머지 원소와 비교해서 검증하는 방식으로 바꾸니 해결
그동안 그리고 좌표처럼 시작점, 끝점 행/열(x,y)값을 일일이 다 함수 변수로 넣었는데 
한변의 길이만 알면 시작점의 행, 열 값만 알아도 되므로 끝점 좌표는 필요하지 않음
'''