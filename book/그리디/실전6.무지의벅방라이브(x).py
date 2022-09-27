# https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3


# 풀이 : 제한시간 30분내에 테스트 통과하지 못함
def solution(food_times, k):
    answer = 0

    time = 0
    l = len(food_times)
    if sum(food_times) < k:
        answer = -1
    else:

        while time <= k:
            if food_times[answer] == 0:
                answer += 1
                answer = answer % l
            food_times[answer] -= 1
            answer += 1
            answer = answer % l

        return answer

# 접근을 무조건 리스트를 순회하며 -1를 한다고 생각하고 접근했지만 효율성에서 좋지 못했고 또한 1,1,2,1 처럼 순회중 0,0,1,0이 되는 케이스에 대한 처리가 불가능했다
# 해답을 검색하니 우선순위 큐를 사용해 처리한다고 되어있는데 이부분 학습후 다시 체크할 예정
# 생각하는 과정이 좀더 이해가 되는 풀이는 https://onejunu.tistory.com/73 이 블로그였다. 추후 참고해 둘다 혼자 풀어봐야함