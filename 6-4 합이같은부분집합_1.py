# 1.
# answer = "NO"
# def find(x, list, k) :
#     global answer
#     if x >= len(list) :
#         if sum(stack) == k :
#             answer = "YES"
#     else :
#         stack.append(list[x])
#         find(x+1, list, k)
#         stack.pop()
#         find(x+1, list, k)

# 2.
# 스택을 사용하지 않고 sum으로만도 구현 가능
def find(x, sum) :
    if sum >k :
        return 
    if x >= len(a) :
        if sum == k :
            print("YES")
            sys.exit(0)     #프로그램 종료
    else :
        sum+=a[x]
        find(x+1, sum)
        sum-=a[x]
        find(x+1, sum)


import sys
N = int(sys.stdin.readline())
a = list(map(int, (sys.stdin.readline().split())))
answer = "NO"
stack = []
if sum(a)%2==0 :
    k = sum(a)//2
    #find(0, a, k)  #1번 풀이
    find(0, 0)

#print(answer)  #1번 풀이
print("NO")