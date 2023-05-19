"""
1/3
1. 23/05/19
2.
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
- 전체 사람의 수 p 입력
- 사람 수 만큼 빈 배열 생성 arr = [] * p+1 (번호대로 index를 사용하기 위해 p+1을 함)
- 촌수를 계산해야 되는 두 사람 번호 입력 p1, p2
- count = 1 # 촌수
- najibreak = False # 이 중 loop를 빠져나올 때 사용할 것
- edge의 갯수 입력 
- 관계 입력
    - index1, index2 입력
    - arr[index1]에 index2가 없다면 
        - arr[index1].append(index2)
    - arr[index2]에 index1이 없다면
        - arr[index2].append(index1)

- queue에 p1과 count를 넣자
- while queue
    - list,cnt = queue.popleft()
    - list에 p2가 있다면
        - print(cnt)
        - break
    - 없다면
    - for i in list:
        - i가 방문한곳이 아니라면
            - visited.append(i)
            - temp_count = cnt + 1
            - queue.append(arr[num], temp_count)
"""
from collections import deque
# 사람의 수 입력
n = int(input())
# 사람의 수 만큼 배열 생성
arr = [[] for i in range(n+1)]
# 촌수를 계산해야 되는 두 사람 번호 입력 p1, p2
p1,p2 = map(int, input().split())
# 촌수
count = 1 
# loop를 빠져나올 때 사용할 것
najibreak = False 
# edge의 갯수 입력
edge = int(input())

# 관계입력
for _ in range(edge):
    index1, index2 = map(int, input().split())
    if index2 not in arr[index1]:
        arr[index1].append(index2)
    if index1 not in arr[index2]:
        arr[index2].append(index1)
    # breakpoint()

visited = set()
queue = deque()

queue.append((arr[p1],count))

while queue:
    list, cnt = queue.popleft()
    # breakpoint()
    # p2가 list에 있다면
    if p2 in list:
        najibreak = True
        print(cnt)
        break
    # 없다면 queue에 append
    for i in list:
        if i not in visited:
            visited.add(i)
            temp_count = cnt + 1
            queue.append((arr[i], temp_count))
    # breakpoint()
if najibreak == False:
    print(-1)