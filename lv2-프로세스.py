# 1.
priorities = [2, 1, 3, 2]
location = 2
# 2.
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0

def solution(priorities, location):
    round = []  #실행 원소를 순서대로 저장할 배열(원소 인덱스 저장)
    now = 0     #현재 인덱스 번호
    index = 0   #max인덱스 번호
    
    # 모든 원소를 돌면서 우선순위가 높은 순서대로 round에 index저장

    while len(round)<len(priorities):   #모든 원소가 다 실행되기 전까지
        max_p = 0       #현재 가장 높은 우선순위 숫자
        for x in range(now, len(priorities)) :  #현재인덱스~
            if priorities[x] > max_p :      #max 인덱스 찾기
                max_p = priorities[x]
                index = x
        for x in range(0, now) :        #~현재인덱스
            if priorities[x] > max_p :      #max 인덱스 찾기
                max_p = priorities[x]
                index = x
        priorities[index] = -1      #index : 가장 우선순위 높은 인덱스 / 가장 높은 우선순위 값 -1로 저장(실행됨 표시)
        round.append(index)     #round에 해당 원소 실행되었으니 append
        now = index     #현재 인데스 index로 바꾸기(이후 그 지점부터 실행하기 위해)
    answer = round.index(location)+1        #location의 실행 순서 answer에 저장
    return answer

# 답안예시
# enumerate, any
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]     #(인덱스, 원소값)으로 리스트 만들기
#     answer = 0
#     while True:
#         cur = queue.pop(0)        #일단 queue에서 맨 앞 원소를 뽑는다(cur)
#         if any(cur[1] < q[1] for q in queue):     #우선순위가 현재 cur보다 높은 것이 있으면
#             queue.append(cur)     #cur 다시 queue 들어가
#         else:
#             answer += 1       #cur보다 우선순위 높은 것이 없으면(cur이 우선순위 제일 높으면)
#             if cur[0] == location:    #그리고 그게 찾던 location이면
#                 return answer     #answer반환, while문 종료
            
print(solution(priorities, location))