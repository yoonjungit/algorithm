import sys
N, M = map(int, sys.stdin.readline().split())

chess = sys.stdin.read().split()

for n in range(N) :
    chess[n] = chess[n].replace("W", "0")
    chess[n] = chess[n].replace("B", "1")

mat = (N-7)*(M-7)
score = [0]*mat
s = 0
v = 0
count= 0

for n in range(N-7) :
    for m in range(M-7) :
        even = chess[n][m]
        if even == '1':
            odd = "0"
        else : odd = "1"

        for i in range(0, 8) :
            for t in range(0, 8) :
                if (i+t)%2 == 0 :
                    if chess[n+i][m+t] == even :pass
                    else : s+=1
                elif (i+t)%2 ==1 :
                    if chess[n+i][m+t] == odd :pass
                    else : s+=1
                if (i+t)%2 == 0 :
                    if chess[n+i][m+t] == odd :pass
                    else : v+=1
                elif (i+t)%2 ==1 :
                    if chess[n+i][m+t] == even :pass
                    else : v+=1
                if i ==t==7 :
                    score[count] = min(s,v)
                    count += 1
                    s = 0
                    v = 0

print(min(score))