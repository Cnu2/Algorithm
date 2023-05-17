"""
1/3
1. 23/05/17
2.
3.
"""

"""
[문제]
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 

이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 

한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
"""

"""
[sudo code]
- n,m 을 입력한다.
- map을 만든다.
- 방향벡터 d를 설정한다.
- count = 1
- queue에 (0,0,count)을 append한다.
- map(0,0)은 값을 0으로 만들어준다.

- bfs():
    - while queue:
        - r,c,count = queue.popleft()
        - 네 방향으로 이동해본다.
            - arr에서 벗어나면
                - continue
            - 이동한 좌표가 n,m이면
                - count += 1
                - result에 count append
            - 1이 있으면 
                - 해당 좌표는 0으로 만들어준다.
                - next_count = count + 1
                - queue.append(r,c,next_count)
        - return min(result)

"""
from collections import deque
import sys
# input = sys.stdin.readline

def bfs():
    while queue:
        r,c,count = queue.popleft()
        # 네 방향으로 이동해본다.
        for i in d:
            dr = r + i[0]
            dc = c + i[1]
            # breakpoint()
            if dr < 0 or dr >= n or dc < 0 or dc >= m:
                continue
            elif dr == n-1 and dc == m-1:
                count += 1 
                result.append(count)
            elif int(arr[dr][dc]) == 1:
                arr[dr][dc] = 0
                next_count = count + 1
                queue.append((dr,dc,next_count))
        
    return(min(result))



# n,m을 입력한다.
n,m = map(int, input().split())
# map을 만든다.
arr = [[int(ch) for ch in input()] for _ in range(n)]
# 방향벡터 d를 설정
d = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우
result = []
count = 1
queue = deque()
queue.append((0,0,count))
# breakpoint()
arr[0][0] = 0

print(bfs())


