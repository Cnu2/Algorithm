"""
3/3
1. 23/05/03
2. 23/05/10
3. 23/06/05
"""

"""
[문제]
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

"""

"""
[sudo code]
A,B,C를 리스트 형태로입력
sort
1번째 원소를 print
"""

abc = list(map(int, input().split()))
abc.sort()
# breakpoint()
print(abc[1])