import sys
N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))     #각 도시간 거리
gas = list(map(int, sys.stdin.readline().split()))      #각 도시별 주유소 기름 가격(/liter)
gas.pop()       #맨 마지막 도시의 기름 가격은 필요 없으므로 삭제(기름 넣을 일이 없음)
cheapest = min(gas)     #마지막 도시를 제외한 나머지 도시에서의 기름 가격

money = 0       #비용 누적합
price = 0       #이 도시까지 나온 최소 기름 값
for i in range(N-1) :       #기름값 리스트를 돌며 비용 계산
    if i == 0 :             #만약 첫번째 도시라면, 무조건 이 도시에서 기름을 넣어야 하므로 price에 대입 
        price = gas[i]
    if price > gas[i] :     #만약 이 도시 이전까지 최소 기름값(price)이 현재 도시보다 비싸면 현재 도시의 기름값으로 price 대체
        price = gas[i]
    money += price * dist[i]    #현재 도시까지 최소 기름값(price)로 다음 도시까지의 거리를 곱해서 비용에 더해줌

print(money)

''' 현실에서, 최소비용으로 맨 첫 도시부터 맨 끝도시까지 가려면 미리 각 도시별 기름값을 꿰차고 있어서
    다음 기름값이 더 싼 도시가 나오기 이전까지 기름을 최소로 채우고 가는게 맞지만, 이 부분까지 알고리즘으로 표현하기에는
    힘드니까(복잡하니까) 도시를 하나씩 갈 때마다 기름값을 비교하고 더 싼곳에서 기름을 넣는다고 생각하자.
'''