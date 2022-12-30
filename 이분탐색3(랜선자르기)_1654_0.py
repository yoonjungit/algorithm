import sys
sys.setrecursionlimit(10**6)    #재귀 최대 깊이 설정

K, N = map(int, sys.stdin.readline().split())   # K : 주어진 랜선 개수, N : 필요한 랜선 개수
n = list(map(int, sys.stdin.read().split()))    # n : 리스트 - 주어진 랜선 각각의 길이
k = max(n)  # k : 가장 긴 랜선의 길이

def divide(start, end) : # 이분탐색 -> 이때 start 이상 end 미만
    if end-start<=1 :  # 탐색 시작점과 끝점 차이가 1 이하 = 범위에 숫자가 start 하나밖에 없음
        return start
    m = (start+end)//2  # 이분탐색을 위한 중간값 m 계산
    c = 0   # c : 랜선 수 카운팅 변수
    for x in n :
        c+=x//m     # 랜선 개수
    if c>= N :      # 만약 랜선 개수가 필요한 랜선 보다 같게 혹은 많이 나온 경우 -> 길이를 늘린다 = 최소 길이를 늘림 (같게 나와도 최대 길이 값을 찾아야 하기 때문)
        return divide(m, end)
    else :          # 만약 랜선 개수가 필요한 랜선 보다 적게 나온 경우 -> 길이를 줄인다 = 최대 길이를 줄임
        return divide(start, m)

print(divide(1, k+1))   #end는 포함 안함(1이상 k+1미만)