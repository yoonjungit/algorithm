#의외로 정렬 알고리즘은 오래 걸린다. 퀵정렬보다 그냥 함수 쓰는게 빨랐음.
import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[K-1])