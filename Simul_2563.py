"""
3/3
1. 23/05/10
2. 23/05/17
3. 23/06/15
"""

"""
[문제]
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.
"""

"""
[sudo code]
1. 색 종이의 갯수를 입력받는다.
2. 100 * 100의 array를 만든다.
3. 종이 수 만큼 위치를 입력받는다.
    3-1. 입력받은 위치에서 부터 x,y좌표 각각 10의 방향으로 만큼 array에서 1로 변환한다.
4. 1로 바꿔준 값을 더하여 결과값을 출력한다.
    
"""
import sys
input = sys.stdin.readline
m = int(input())
coords = []
_sum = 0
# 흰색 도화지 생성
_map = [[0]*100 for i in range(100)]
# breakpoint()
for _ in range(m):
    coords.append(list(map(int, input().split())))
# breakpoint()
for c in coords:
    x,y = c
    # breakpoint()
    for i in range(10):
        for j in range(10):
            if _map[y+i-1][x+j-1] == 0:
                _map[y+i-1][x+j-1] = 1
# breakpoint()
for row in _map:
    _sum += sum(row)

print(_sum)