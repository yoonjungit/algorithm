import sys
A,B,C = map(int, sys.stdin.readline().split()) #인풋 차례대로 받기

def recursive(a,b,c) :
    if b == 1 :
        return a%c      #만약 b=1이라면, 추가적인 곱셈을 안해도 되므로, a%c 반환
    temp = recursive(a,b//2,c)      #만약 b>=1이라면, 재귀함수(b를 반 나눠서 계산하기 위해)
    if b%2==0:
        return temp*temp%c          #b가 짝수라면, 그대로 반만 제곱한 것을 곱하고 그것의 나머지를 구함
    else :
        return temp*temp*a%c        #b가 홀수라면, 반만 제곱한 것에 a를 한번 더 곱해서 맞춰준 후 나머지를 구함

print(recursive(A,B,C))