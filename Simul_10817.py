"""
1/5
1. 23/05/03
2. 23/05/10
3.
"""

"""
[문제]
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

"""

"""
[문제 해결]
숫자를 입력받고
sort을 진행하고
1번째 index를 반환한다.
"""

"""
[sudo code]
list = list(input())
list.sort
print(list[1])

"""
import sys
input  = sys.stdin.readline

num_list = list(map(int, input().split()))
num_list.sort()
# breakpoint()
print(num_list[1])