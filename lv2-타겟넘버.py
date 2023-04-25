def solution(numbers, target):
    global answer
    answer = 0
    make(numbers, target, 0, numbers[0], 0)
    make(numbers, target, 0, -numbers[0], 0)
    return answer

def make(numbers, target, i, number, sum):
    global answer
    sum+=number
    if i == len(numbers)-1 :
        if sum == target :
            answer+=1
    else :
        make(numbers, target, i+1, numbers[i+1], sum)
        make(numbers, target, i+1, -numbers[i+1], sum)
        
numbers = [1, 1, 1, 1, 1]	
target = 3
print("답 : ",solution(numbers, target))