import sys

N = int(sys.stdin.readline())
N_list = [x for x in range(1, N+1)]

stack = []
def part(i) :
    if i <= N :
        stack.append(str(i))
        part(i+1)
        stack.pop()
        part(i+1)
    else :
        if stack :
            print(' '.join(stack))
part(1)