import sys
n = int(sys.stdin.readline())

#A(n+2) = A(n+1) + A(n)

#1. bottom-up 방식

dp = [0]*(n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1) :
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])

#2. top-down 방식

td = [0]*(n+1)

def top_down(z) :
    if z==1 or z==2 :
        return z
    else :
        if td[z]==0 :
            td[z] = top_down(z-1)+top_down(z-2)
        return td[z]
    
top_down(n)
print(td[n])