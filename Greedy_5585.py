"""
[푼 횟수]
1/5
1. 23/04/21
2.
3.
4.
5.
"""

"""
[문제]
타로는 자주 JOI잡화점에서 물건을 산다. 
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
"""

"""
[문제 해결]
500엔, 100엔, 50엔, 10엔, 5엔, 1엔
총 거스름돈에서
큰 것부터 나눠 떨어지걸 제외시킨다. 
"""

"""
[sudo code]
Money = input()
count = 0
coin_list = [500, 100, 50, 10, 5, 1]
for c in coin_list:
    if Money < coin_list:
        스킵
    else:
        count += Money를 c로 나눈 몫
        Money = Money를 c로 나눈 나머지


"""
import sys

# 1000엔을 내고 물품을 구입하고 받아야 될 거스름 돈
money = 1000 - int(sys.stdin.readline()) 
count = 0
coin_list = [500, 100, 50, 10, 5, 1]

for c in coin_list:
    if money < c:
        continue
    else:
        # breakpoint()
        count += money // c
        money = money % c

print(count)