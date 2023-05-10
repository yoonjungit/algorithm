"""
1. 도시 내 집, 피자집 좌표 저장
2. 피자집 중 m개 선택(조합)
    - 각 조합마다 최소 피자배달거리 구하기
        - 각 집마다 조합에서 선택한 피자집 중 가장 가까운 피자배달거리 구한 후 더하기
3. 그중 최소 피자배달거리 출력
"""

import sys
n, m = map(int, sys.stdin.readline().split())   # n:도시크기, m:선택한 피자집 개수

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    #도시 지도

house = []  #집좌표
pizza = []  #피자집 좌표

#1. 집, 피자집 좌표 구하기
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            house.append((i, j))
        elif graph[i][j] == 2 :
            pizza.append((i, j))

p = len(pizza)  #피자집 총 개수
arr = [0]*m     #m개 저장할 피자집 배열(조합)
picked=[]   #피자집 조합 저장할 배열

global distance     #조합마다 min(피자배달거리)저장 배열
distance = []

def min_distance(arr) :     #3. 현 조합(arr)에서 min(피자배달거리 구하기)
    global distance
    dis = 0     #현 조합(arr)의 피자배달거리 저장 변수
    for h in house :
        h_distance = []     #집마다 각 피자집과의 거리 저장 배열
        for v in arr :
            x=abs(h[0]-v[0])    #피자집-집 거리 구하기
            y=abs(h[1]-v[1])
            h_distance.append(x+y)
        dis+=min(h_distance)    #집과 가장 가까운 피자집 거리 구한 후(min) 조합 전체 배달 거리(dis)에 더하기
    distance.append(dis)    #조합 최소 배달거리 배열에 저장

def DFS(z, level) :     #2. 조합 구하기, z:범위 시작점, level:현재조합순번(레벨)
    if level == m :     #만약 m개 피자집 다 선택했으면
        min_distance(arr)   #전체 조합 배열에 append
        return
    for i in range(z, p-m+level+1) :    #범위 : z이상 p-m+level이하
        arr[level] = pizza[i]
        DFS(i+1, level+1)

DFS(0, 0)

print(min(distance))