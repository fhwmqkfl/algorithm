# # 순서, 요청 시각, 페이지수
# def solution(data):
#     start_time = data[0][1]
#     end_time = start_time + data[0][2]
#     answer = [data[0][0]]
#     data.remove(data[0])

#     while data:
#         # 앞전의 프린트가 종료된 시점에 요청된 문서가 있을경우 걔가 먼저
#         for i in data:
#             if end_time == i[1]:
#                 start_time = end_time
#                 end_time = start_time + i[2]
#                 answer.append(i[0])
#                 data.remove(i)
#                 continue
#         # 마지막 시간 기점으로 대기중인 문서번호 별도로 리스트화
#         time_table = list()
#         for i in data:
#             if end_time > i[1]:
#                 time_table.append(i)
#         if time_table:
#             time_table.sort(key=lambda a:(a[2],a[1]))
#             # 제일 뒤의 값이 최선이므로 해당 값으로 프린트
#             start_time = end_time
#             end_time = start_time + time_table[0][2]
#             answer.append(time_table[0][0])
#             data.remove(time_table[0])
#         else:
#             end_time += 1
#     return answer

# day = 1월 1일의 요일, k 관리비 내는 날짜
# def solution(day,k):
#   month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   dd= 1
#   #1월부터 12월까지 돌기(리스트 인덱스값 기준으로 돔)
#   cnt = 0
#   answer = []
#   # 요일별 날짜별 값 더하기
#   while cnt < 12:
#     # 도는 중 관리비 낼 날짜다
#     if dd == k:
#         # 토,일요일? 그럼 1
#         if day == 5 or day == 6:
#             answer.append(1)
#         else:
#             answer.append(0)
#     # 동일한 날짜로 왔다? 그럼 다음달로 이동
#     if dd == month[cnt]:
#         dd = 0
#         cnt += 1
#     day = (day + 1) % 7
#     dd += 1
#     print("day,dd",day,dd)
#     print("answer", answer)

#   print(answer)
#   return answer

# solution(6,1)
# card = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"]
# word = ["GPQM", "GPMZ", "EFU", "MMNA"]
# answer = ["GPQM","MMNA"]


# a = [1,2]

# b = [3,0]

# if b[0] in a:
#   print("YY")