#시간복잡도 : O(nlog(n))
import sys
N = int(sys.stdin.readline())   # N : 회의 개수
meetings = []       # meetings : 회의 리스트
#O(n)
for n in range(N) : #순서대로 [회의 시작 시간, 끝나는 시간]을 리스트에 추가해준다 -> [[], []...[]] 형태
    a, b = map(int, sys.stdin.readline().split())   
    meetings.append([a,b])
#O(nlog(n))
#끝나는 시간이 빠른 순서대로 포함시키는 것이 유리. 근데 검증 시에는 만약 끝나는 시간이 같은 회의가 여러개 있다면 시작 시간이 빠른 순서대로 검증 해봐야하므로, 먼저 시작 시간이 빠른 순서대로 정렬 후, 다시 끝나는 시간이 빠른 순서대로 재정렬 한다.
# sorted(정렬시킬 대상, 매개변수(인자)) 
# sort와 sorted의 차이 : sort는 자기 자신을 정렬한 후 반환 값은 없음. sorted는 정렬 후 (자기자신x) 반환 값이 있음
meetings = sorted(meetings, key = lambda a : a[0])      #회의 시작 시간 기준 정렬
meetings = sorted(meetings, key = lambda a : a[1])      #회의 끝나는 시간 기준 정렬

last = 0        #포함된 회의 중 가장 늦게 끝나는 시간
count = 0       #포함된 회의개수

#O(n)
for start, end in meetings :    #start = meetings[i][0] : 시작 시간, end = meetings[i][1] : 끝나는 시간
    if start >= last :      #만약 현재 스케줄에 포함되어있는 회의 중 가장 늦게 끝나는 회의보다 해당 회의가 늦게 끝난다면, 해당 회의를 포함시키고, 개수 +1, last변수 대체
        count += 1
        last = end

print(count)    #최종 개수 출력
