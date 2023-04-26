import sys
C, N = map(int, sys.stdin.readline().split())
# badugi=list(map(int, sys.stdin.read().split())) #시간 초과 나옴
badugi=[0]*N
for i in range(N) :
    badugi[i]=int(input())
global answer
answer = 0
total_sum = sum(badugi)

# 시간초괴
# def find_max(max_weight, i) :
#     global answer
#     if max_weight > C :
#         return 
#     elif i >= N :
#         if max_weight <= C and max_weight > answer:
#             answer = max_weight
#     else : 
#         find_max(max_weight+badugi[i], i+1)
#         find_max(max_weight, i+1)

def find_max(max_weight, i, tsum) :     #max_weight : 적재한 바둑이 무게, i : 현재 인덱스, tsum : 현재 원소까지 바둑이를 모두 포함했을 때 무게
    global answer
    if max_weight > C :     #최대 적재 가능 무게 초과한 경우
        return 
    elif max_weight+ (total_sum-tsum) < answer :       # 앞으로 나머지 바둑이 다 태워도 이전 최대 적재한 몸무게 보다 적은 경우
        return 
    elif i >= N :      #인덱스가 끝 원소보다 클 때, 이전 max 보다 큰 경우 answer 바꿈
        if max_weight > answer:
            answer = max_weight
    else : 
        find_max(max_weight+badugi[i], i+1, tsum+badugi[i])
        find_max(max_weight, i+1, tsum+badugi[i])

find_max(0, 0, 0)
print(answer)