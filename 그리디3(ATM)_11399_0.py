import sys
N, *P = map(int, sys.stdin.read().split())  #N:인원 / P:각각 인출 시 걸리는 시간
P.sort()    #sum의 최솟값을 구하기 위해 오름차순 정렬

sum = 0     #sum 변수 지정
#각각 인출 시 걸리는 시간을 각각의 입장에서 구해 더하는 것으로 
#P[0]은 인원 수 만큼 곱해서 sum에 더해진다
#ex) a + (a+b) + (a+b+c) + ...
#따라서 다음과 같이 a*N + b*(N-1) + c*(N-2)가 될 수 있도록 구한다
for p in P :
    sum+=(p*N)      
    N-=1

print(sum)