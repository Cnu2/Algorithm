"""
2/3
1. 23/05/12
2. 23/05/19
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
n 컴퓨터의 수 
edge 연결 선 수
관계를 입력할 array 선언
visited = set() 

연결된 관계 입력

queue 에 1번 컴퓨터 저장

1번 리스트를 돌면서 안에 있는 숫자 queue에 append
visit한 적이 없으면 append


"""
from collections import deque
n = int(input())
edge = int(input())
array = [[] for i in range(n+1)]
visited = set()

for _ in range(edge):
    p1, p2 = map(int, input().split())
    if p2 not in array[p1]:
        array[p1].append(p2)
    if p1 not in array[p2]:
        array[p2].append(p1)

queue = deque()
queue.append(array[1])
visited.add(1)

while queue:
    index_list = queue.popleft()
    for i in index_list:
        if i not in visited:
            visited.add(i)
            queue.append(array[i])

print(len(visited)-1)



