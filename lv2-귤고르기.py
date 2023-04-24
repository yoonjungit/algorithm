def solution(k, tangerine):
    kind = set(tangerine)
    count_t = {x:0 for x in kind}
    
    for x in tangerine :
        count_t[x]+=1
    
    count_t_sort = sorted(count_t.items(), key=lambda x:x[1], reverse=True)
    
    a = 0
    answer = 0
    
    for i in count_t_sort :
        answer+=1
        a+=i[1]
        if a>=k :
            break

    return answer
