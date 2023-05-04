"""
1/5
1. 23/05/04
2. 
3.
4.
5.
"""

"""
[문제]
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
"""

"""
[문제 해결]
for 문을 돌리면 되지 않을까?
"""

"""
[sudo code]
N = input()
for i in range(N,1,-1)
    print()
"""
import sys
N = int(sys.stdin.readline())
for i in range(N,0,-1):
    print(i * '*')