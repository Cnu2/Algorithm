"""
1/5
1. 23/05/09
2. 
3.
4.
5.
"""

"""
[문제]
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

"""

"""
[문제 해결]

1) 먼저 벽을 꼭 3개를 세워야하므로 벽을 3개 세웠을 때 바이러스를 퍼트려야한다.
2) 바이러스는 상하좌우의 인접한 빈칸으로 이동하므로 bfs를 여기서 사용한다.
2-1) 바이러스의 위치를 큐에 전부 넣고 while queue를 돌린다. 
2-2 ) 바이러스를 퍼트린 후에 0(빈칸) 이 몇개있는지 체크하고, 최대값을 찾는다.
3) 모든 과정이 끝나고 최대값을 출력한다.

"""

"""
[sudo code]
def make_wall(count):
    벽이 3개 세워지면 bfs()
    아니면 0인 부분에 1 입력
    make_wall(count+1)
    만들었던 wall 그대로

def bfs():
    queue = deque()
    test_map
    2의 위치 파악
    
    while queue:
        네 방향으로 이동해서 이동한 곳이 0이면 2로 감염
        2의 위치 파악
    
    0의 갯수 파악

"""

from collections import deque
import copy
import sys
input = sys.stdin.readline

d = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우 

def bfs():
    queue = deque()
    #queue에 2의 위치 전부 append
    test_map = copy.deepcopy(lab_map) # 깊은 복사
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue:
        r,c = queue.popleft()

        for i in range(4): # 네 방향으로 이동
            dr = r+d[i][0]
            dc = c+d[i][1]

            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0: # 이동한 곳이 0이면
                    test_map[dr][dc] =2 # 감염
                    queue.append((dr,dc)) # 큐에 추가

    global result
    count = 0
    for i in range(n): # 0의 갯수 확인
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)


def make_wall(count): # 벽 3개를 세우는 과정
    if count == 3: # 벽을 3개 세웠으면,
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1 # 벽을 세운다
                make_wall(count+1) 
                lab_map[i][k] = 0


n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)