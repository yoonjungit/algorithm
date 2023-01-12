import sys
N = int(sys.stdin.readline())

Q=[]    #정사각형 이중 배열 리스트
for _ in range(N) :
    Q.append(list(sys.stdin.readline().rstrip()))   #숫자가 띄어쓰기 없이 주어지므로 정수형 변환 없이 리스트에 삽입(이때 숫자 각각 원소로 나뉘어짐 ['0', '1'])
# Q = [list(sys.stdin.readline().rstrip())for _ in range(N)] 로 대체 가능

ans = []    #정답 리스트
def recursive(n, f,f_,r,r_) :
    x = n //2   #나뉘어지는 정사각형 한변의 길이
    a=[]        #나뉘어지는 정사각형 4개
    b=[]
    c=[]
    d=[]
    for i in range(x) :
        a=a+Q[f+i][f_:f_+x:]    #왼쪽 위 정사각형(2사분면)
        b=b+Q[f+i][f_+x:r_:]    #오른쪽 위 정사각형(1사분면)
        c=c+Q[f+x+i][f_:f_+x:]  #왼쪽 아래 정사각형(3사분면)
        d=d+Q[f+x+i][f_+x:r_:]  #오른쪽 아래 정사각형(4사분면)

    if set(a)==set(b)==set(c)==set(d)!={'0','1'} :  #만약 네 정사각형 모두 다 같은 한개의 원소로 이루어져 있다면 -> 괄호 없이 해당 숫자만 출력
        if set(a) == {'1'} :
            ans.append('1')
        else :
            ans.append('0')
        pass
    else :            
        ans.append("(")     #네개의 정사각형이 같지 않은 경우(하나라도 다르면), 이때 괄호로 각각의 정사각형 값 묶기
        if set(a) == {'0','1'} :    #원소가 두개라면 재귀함수
            recursive(x,f,f_,r-x,r_-x)
        elif set(a) == {'1'} :
            ans.append('1')
        elif set(a) == {'0'} :
            ans.append('0')

        if set(b) == {'0','1'} :
            recursive(x,f,f_+x,r-x,r_)
        elif set(b) == {'1'} :
            ans.append('1')
        elif set(b) == {'0'} :
            ans.append('0')    

        if set(c) == {'0','1'} :
            recursive(x,f+x,f_,r,r_-x)
        elif set(c) == {'1'} :
            ans.append('1')
        elif set(c) == {'0'} :
            ans.append('0')        
       
        if set(d) == {'0','1'} :
            recursive(x,f+x,f_+x,r,r_)
        elif set(d) == {'1'} :
            ans.append('1')
        elif set(d) == {'0'} :
            ans.append('0')
        
        ans.append(')')     #정답 괄호 닫기

recursive(N, 0, 0, N, N)

print(''.join(ans))