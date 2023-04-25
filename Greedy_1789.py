"""
[푼 횟수]
1/5
1. 23/04/25: list 사용 시 시간초과 오류 발생 total로 해결
2.
3.
4.
5.
"""

"""
[문제]
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
"""

"""
[문제 해결]
3 : 1,2
4 : 1,3
5 : 1,4 또는 2,3
10 : 1,2,3,4
11 : 1,2,3,5 

백트래킹으로 풀여야 되지 않을까?
그리디로 이걸 어떻게 풀지?

1부터 더해가면서 그 합이 S보다 크다면
최근에 더해진 수를 뺀다.
이렇게 풀었을 경우 시간초과 발생
total을 구하고 S보다 초과시 count에서 1을 뺴고 출력한다. 
"""

"""
[sudo code]
S = input()
num_list = []
for i in range(1,4,294,967,296):
    if sum(num_list) == S:
        break
    elif sum(num_list) > S:
        num_list에서 마지막을 뺀다.
    else:
        num_list.append(i)

S = input()
total = 0
count = 0
while total < S:
    count += 1
    total += count

if S < total:
    count에서 하나를 뺴고 출력
"""
import sys

S = int(sys.stdin.readline())
total = 0
count = 0

while total < S:
    count += 1
    total += count

if total > S:
    count -= 1

print(count)
