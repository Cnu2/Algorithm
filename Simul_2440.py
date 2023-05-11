"""
1/3
1. 23/05/04
2. 
3.
"""

"""
[문제]
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
"""

"""
[sudo code]
1. N 입력
2. N에 -1을 더해가며 *을 출력
"""
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N,0,-1):
    print('*'* i)
