# 결론적으로 해당 코드는 시간 초과
import sys

# 재귀함수 사용
def w(a,b,c) :
		# a, b, c 중 하나라도 0보다 작으면 1 반환
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
		# a, b, c 중 하나라도 20 초과이면 w(20, 20, 20)인데 이때 시간초과 없애겠다고 테스트케이스에서
		# w(50, 50, 50)일 때 출력값 (1048576)을 복사해서 넣음. 20초과하는 이상 값은 다 w(20, 20, 20)으로 같으니까..
    elif a > 20 or b > 20 or c > 20 :
        return 1048576
		# 문제 조건에 나온 재귀함수
    if a < b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    

while True :
    a,b,c = map(int, sys.stdin.readline().split())
		# 가장 마지막 줄은 a=b=c=-1이어서 해당 값 나오면 while문 탈출
    if a == b == c == -1 :
        break
		# 재귀함수 돌리기
    v = w(a,b,c)
		# 출력
    print(f'w({a}, {b}, {c}) = {v}')