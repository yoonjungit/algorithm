import sys
I = sys.stdin.readline().rstrip()

num, w, x=0, 0, 0
#num : 문자형->정수형 변환을 위한 변수 / w : 마이너스 판단 여부(스위치)
#x : 정답 변수 (누적 연산)

for i in I :    #문자를 하나하나 차례대로 고찰
    if i in '0123456789' :      #1. 만약 문자가 숫자라면 num에 넣는데 이때, 기존 num값*10+현재 문자 로 계산해서 넣는다
        num=num*10+int(i)
    else :      #2. 문자가 숫자가 아닌 연산자라면
        #2-1) 스택에 있는 숫자를 연산해주는데, 이전에 마이너스가 한번이라도 나왔다면 -를, 아직 안나왔다면 +
        if w == 1:
            x-=num
        elif w == 0 :
            x+=num
        num=0   #num 초기화
        #2-2) 만약 연산자가 -라면, 앞으로도 마이너스 연산만 할 수 있도록 해줌
        if i == '-' :
            w=1
#3. 마지막 숫자 연산
if w == 1 :
    x-=num
if w == 0 :
    x+=num

print(x)

#괄호를 적절하게 넣어서 최소치를 만들라 하였지만 결국 따지고보면
#마이너스 한번이라도 나오면 이후에 나오는 값들은 그냥 다 빼라임 (괄호 잘 쓰면 그렇게 할 수 있음)
#고민할 것도 없이 마이너스 나오기 전까지 다 더하고, 마이너스 나온 이후 값들은 다 뺌

#가장 힘들었던 부분은 숫자가 str으로 주어지고, 연산자와 섞여 바로 int로 변환을 못하는 것.
#그래서 숫자를 연산자와 분리해 어떻게 변환할 것인가가 가장 어려웠음
#문제에서 얘기하는대로 순서대로 푼다면, 나처럼 각각의 문자열을 구분해 이것을 일일이 저런 방식으로 숫자로 변환해야하지만
#그것이 아니면 split함수로 문자형인 숫자를 발라내 int로 변환하는 것이 좋은듯.
#참고
'''
l = input().split('-')
f = lambda: sum(map(int, l.pop(0).split('+')))
s = f()
while l:
    s -= f()

print(s)
'''