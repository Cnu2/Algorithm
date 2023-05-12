"""
1/3
1. 23/05/12
2.
3.
"""

"""
[문제]
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 

1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 

하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""

"""
[sudo code]
1. n = 컴퓨터의 수 
2. v = 연결선 개수
3. graph = [] * n+1 
4. visited = [0] * n+1
5. 그래프 생성
6. visited[1] = 1 
7. Q = deque([1])
8. while문
    c = Q.popleft()
    c에 있는 값을 체크
        c에 있는 값이 visited[c] == 0이라면
            Q에 c값을 넣어주고
            visited[c]를 방문처리
9. visited에 값을 합치고 - 1 

"""
from collections import deque
n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화,1번 컴퓨터를 1번 인덱스로 쓰기 위해 공간 하나를 더 씀
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시

for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
# breakpoint()

visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)


