"""
링크 : https://www.acmicpc.net/problem/2644
1. 23/05/19
2. 23/05/31
3. 23/06/19
"""

"""
[문제]
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 

이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 

예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
"""

"""
[sudo code]
- 사람 수 n 입력
- rels: n + 1 크기의 빈 리스트 생성 
- 알고싶은 p1,p2입력
- 관계 수 m 입력
- m번 동안
    - r1,r2 관계 입력
    - rels에서 r1 index에 r2가 없다면 
        - rels[r1].append(r2)
    - rels에서 r2 index에 r1이 없다면
        - rels[r2].append(r1)

- bfs()
    - queue에 (rels[p1], count)을 입력
    - while queue
        - rel, temp_count = queue.popleft()
        - 만약 rel에 p2가 있다면
            - temp_count += 1
            - return temp_count
        - 없다면
            - visited에 없다면
            - visited.append(해당 인덱스)
            - rel의 길이에 따라
                - temp_count += 1
                - queue.append(rels[index], temp_count)
    
    마지막 까지 없다면 return -1

"""
from collections import deque

def bfs():
    count = 0
    queue.append((rels[p1], count))
    visited.append(p1)
    while queue:
        rel, count = queue.popleft()
        if p2 in rel:
            count += 1
            return count
        
        else:
            for i in rel:
                if i in visited:
                    continue
                else:
                    temp_count = count + 1
                    queue.append((rels[i],temp_count))
                    visited.append(i)
    return -1

queue = deque()
visited = []
n = int(input())
rels = [[] for _ in range(n+1)]
p1, p2 = map(int, input().split())
m = int(input())
for _ in range(m):
    r1,r2 = map(int, input().split())
    if r2 not in rels[r1]:
        rels[r1].append(r2)
    if r1 not in rels[r2]:
        rels[r2].append(r1)

print(bfs())

