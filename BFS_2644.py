"""
링크 : https://www.acmicpc.net/problem/2644
2/3
1. 23/05/19
2. 23/05/31
3.
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
- 전체사람의 수 n 입력 
- n+1 크기의 rel 리스트 선언
- 촌수를 계산해야 되는 두 사람 번호 p1,p2 입력 
- 관계의 갯수 m 입력
- 관계 입력
    r1,r2입력
    만약 r1 index에 r2가 없다면 r1에 r2추가
    반대도 마찬가지
- queue에 rel[p1]과 count append
- 관계찾기 bfs
    queue가 null이 아닐때까지
        queue를 popleft 한것을 l
        l에 있는 원소들을 하나씩 살펴본다.
            l1이 방문했던것이면 continue
            p2가 l에 이라면 return count 
            p2가 없다면 
                count += 1
                queue.append(l1,count)
    관계가 없다면 return -1

- print(bfs())

"""

from collections import deque

def bfs():
    while queue:
        rel_list,cnt = queue.popleft()
        # breakpoint()
        for i in rel_list:
            if i in visited:
                continue
            elif p2 == i:
                return cnt
            else:
                temp_count = cnt + 1
                visited.append(i)
                queue.append((rel[i],temp_count))
    return -1

N = int(input())
visited = []
rel = [[] for _ in range(N+1)]
# breakpoint()
p1,p2 = map(int, input().split())
m = int(input())
for _ in range(m):
    r1,r2 = map(int, input().split())
    if r2 not in rel[r1]:
        rel[r1].append(r2) 
    if r1 not in rel[r2]:
        rel[r2].append(r1)

queue = deque()
count = 1
queue.append((rel[p1],count))
visited.append(p1)

print(bfs())

