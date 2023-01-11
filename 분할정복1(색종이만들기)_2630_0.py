import sys
N = int(sys.stdin.readline())

rectangle = []      #rectangle : 사각형 만들 리스트(행마다 리스트를 분리 ->이중리스트)
for n in range(N) :
    r = list(map(int, sys.stdin.readline().split()))
    rectangle.append(r)
# [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
# list(map(int, sys.stdin.readline.split for _ in range(N)))
# 로도 바꿔쓸 수 있음

white = 0       # 0 으로만 이루어진 white 정사각형 개수
blue = 0        # 1 로만 이루어진 blue 정사각형 개수

def divide(s,s_,e,e_,n) :   #변수 : 좌표 시작(s, s_)~끝(e, e_) 
    global white, blue      #재귀함수로 값이 변경되는 카운트 변수이기 때문에 global 변수로 지정
    a=[]        # a,b,c,d : 쪼개진 작은 정사각형 4개(1사분면, 2사분면, 3사분면, 4사분면)
    b=[]
    c=[]
    d=[]
    x = n//2    # 작은 정사각형 한변의 길이
    for i in range(n) :
        if i < x :
            a=a+rectangle[s+i][s_:s_+x:]    #1사분면(왼쪽 위 : (s, s_)~(s+x,s_+x))
            b=b+rectangle[s+i][s_+x:e_:]    #2사분면(오른쪽 위 : (s+x, s_)~(s+x, s_+x))
        else :
            c=c+rectangle[s+i][s_:s_+x:]    #3사분면(왼쪽 아래 : (s+x, s_)~(e, s_+x))
            d=d+rectangle[s+i][s_+x:e_:]    #4사분면(오른쪽 아래 : (s+x, s_+x)~(e, e_))
    #리스트->집합 변환해서 집합의 원소와 그 개수로 개수 판단
    
    #(1) 만약 a,b,c,d 정사각형의 집합의 원소가 한개로 그 값이 다 같다면 -> 쪼갤 필요 없음, 사각형 개수는 1개
    if set(a) == set(b) == set(c) == set(d) != {0,1} :
        if set(a) == {0} :
            white +=1
        else :
            blue +=1
    #(2) 만약 a,b,c,d 정사각형의 집합의 원소가 한 사각형이라도 다르면, 각각 네개 사각형으로 쪼개서 판단
    else :
        if set(a) == {0,1} :    #집합의 원소가 {0,1}이라면 재귀, {0} 혹은 {1}이라면 사각형 개수+1
            divide(s,s_,e-x,e_-x,x)
        elif set(a)=={1} :
            blue +=1
        elif set(a)=={0} :
            white +=1
        
        if set(b) == {0,1} :
            divide(s,s_+x,e-x,e_,x)
        elif set(b) == {1} :
            blue +=1
        elif set(b)=={0} :
            white +=1

        if set(c) == {0,1} :
            divide(s+x,s_,e,e_-x,x)
        elif set(c) == {1} :
            blue +=1
        elif set(c)=={0} :
            white +=1

        if set(d) == {0,1} :
            divide(s+x,s_+x,e,e_,x)
        elif set(d) == {1} :
            blue +=1
        elif set(d)=={0} :
            white +=1

divide(0,0,N,N,N)
#출력
print(white)
print(blue)

'''처음에 예제와 반례 모두 다 통과했는데도 계속 6%대에서 틀렸습니다가 나와 고민했는데 알고보니
    set(d)에서 재귀 돌릴 때, 끝점 좌표 변수가 e_(최대치)에서 +x 를 해서 범위를 넘어버려서 였다
    그렇게 해도 내가 넣은 반례에서는 문제가 없었지만 테스트케이스에서는 걸렸나 봄
    앞으로 이런 경우에는 변수를 다 출력해서 확인해 봐야겠다.'''