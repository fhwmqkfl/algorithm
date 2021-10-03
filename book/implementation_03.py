#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
#열의 경우 아스키 코드문법 이용해서 숫자로 변형시킨뒤 계산하기!
column = int(ord(input_data[0]) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
	next_row = row + step[0]
	next_column = row + step[1]
	#해당 위치로 이동이 가능하면 카운트 증가
	if next_row >= 1 or next_column >= 1 or next_row <= 8 or next_column <= 8:
		result += 1

print(result)
