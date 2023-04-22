def solution(id_list, report, k):
    report_dict = {}    #{신고한유저:[신고한ID목록]}
    reported_dict = {}  #{신고당한유저:신고수}
    sue = set()     #신고수가 기준k이상이어서 게시판 이용이 중지된 유저

    answer = []

    for x in report :       #report 차례대로 iterate
        #1. 신고한 유저의 신고한 ID 목록 업데이트
        a, b = x.split()    #a:신고한유저, b:신고당한유저
        c = 0       #중복값 판별 변수
        if a in report_dict :   #기존 신고 이력이 있는 유저라면(dict안에 key값이 존재하면)
            report_list = report_dict[a]    #해당 key의 value, 신고한ID목록 가져오기
            if b not in report_list :       #중복신고가 아니라면
                report_list.append(b)       #목록에 추가
                c+=1    #중복 신고가 아님을 표시
        else :  #신고 이력이 없는 유저라면(dict안에 key값이 없으면)
            report_dict[a]=[b]  #새로운 key:value 쌍 추가
            c+=1    #중복 신고가 아님을 표시
            
        #2. 신고당한 유저의 신고수 업데이트
        if b in reported_dict and c == 1:   #중복신고가 아니고, 이전에도 신고당한 이력이 있다면(key값이 존재)
            reported_dict[b]+=1     #신고수 +1
            if reported_dict[b]>=k:     #신고수가 기준k이상인지 판별
                sue.add(b)
        elif b not in reported_dict and c == 1:     #중복신고가 아니고, 이전에 신고당한 이력이 없다면
            reported_dict[b]=1     #신고수 +1
            if reported_dict[b]>=k:     #신고수가 기준k이상인지 판별
                sue.add(b)
        
    for x in id_list :
        a = 0   #처리결과 메일 수
        if x in report_dict :       #신고한 이력이 있는 유저라면
            y = report_dict[x]      #y: 신고한 ID 목록
            for z in y :
                if z in sue :       #신고한 ID중 신고수가 기준 이상이어 게시판 이용이 중지된 유저가 있다면
                    a +=1   #처리결과 메일수 +1
        answer.append(a)

    return answer

# 답안예시 : 처음부터 set()으로 중복 원소 제거
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)   #처리결과 메일받는 개수 저장 배열
#     reports = {x : 0 for x in id_list}    #{아이디:신고수}

#   #1. 신고수 세기
#     for r in set(report):     #report에서 중복된 원소 제거 위해 set()-집합 변환
#         reports[r.split()[1]] += 1    #신고수

#   #2. 신고한 유저의 처리 결과 메일 개수 세기
#     for r in set(report):
#         if reports[r.split()[1]] >= k:    #신고수가 기준k 이상이면
#             answer[id_list.index(r.split()[0])] += 1      #신고한 유저의 처리결과 메일 개수 +1

#     return answer

# 1.
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# 2.
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

print(solution(id_list, report, k))