"""
[문제 풀이]
1. 23/05/12
2. 23/05/19
3. 23/06/20
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
n = int(input()) # 컴퓨터 대수 입력
edge = int(input()) # 연결선 입력
visited = []
count = 1
_map = [] * n+1
for i in range(n):
    관계 입력
queue.append(_map[1])
visited.append(1)
def bfs():
    while queue:
        comp_list = queue.popleft()
        for comp in comp_list:
            comp 가 visited에 없으면:
                visited.append(comp)
                queue.append(_map[comp])
        count += 1


"""
from collections import deque

def bfs():
    count = 0
    while queue:
        comp_list = queue.popleft()
        for comp in comp_list:
            if comp not in visited:
                visited.append(comp)
                queue.append(_map[comp])
                count += 1    

    return count   

queue = deque()
n = int(input())
edge = int(input())
visited = []
_map = [[] for _ in range(n+1)]
for i in range(edge):
    c1,c2 = map(int, input().split())
    if c2 not in _map[c1]:
        _map[c1].append(c2)
    if c1 not in _map[c2]:
        _map[c2].append(c1)

queue.append(_map[1])
visited.append(1)



print(bfs())