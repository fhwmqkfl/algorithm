from collections import deque

#BFS매서드 정의
def bfs(graph, start, visited):
	#큐 구현을 위해 deque라이브러리 적용
	queue = deque([start])
	#현재 노드를 방문처리
	visited[start] = True
		#큐가 빌때까지 반복
	while queue:
		#큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end=' ')
		#해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원리스트)
graph =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원리스트)
visited = [False] * 9

#정의된 DFS함수 호출
dfs(graph, 1, visited)

# >>> 1 2 3 8 7 4 5 6
