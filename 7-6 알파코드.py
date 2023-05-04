import sys 
password = list(sys.stdin.readline())

alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

global count
count = 0

def DFS(x, word, tmp) :
    global count
    if x == len(password) :
        print(word.strip())
        count+=1
        return

    DFS(x+1, word + alphabet[int(password[x])], tmp)

    if x<len(password)-1 and int(password[x])*10 + int(password[x+1]) < len(alphabet) :
        DFS(x+2, word + alphabet[int(password[x])*10 + int(password[x+1])], tmp)

DFS(0, "", 0)
print(count)