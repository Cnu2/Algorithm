"""
1/5
1. 23/4/11
2.
3.
4.
5.
"""

"""
[문제]
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""

"""
[문제 해결]
1 -> 1(1번)
2 -> 1+1,2(2번)
3 -> 2+1, 1+2, 1+1+1, 3(4번)
4 -> 3+1, 1+3, 2+2, 1+1+2, 2+1+1, 1+2+1, 1+1+1+1(7번)
5 -> 3+2, 2+3, 2+2+1, 2+1+2, 1+2+2, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+1+1+1+1, 3+1+1, 1+3+1, 1+1+3(13번)

이로부터 알 수 있는 것은 f(n) = f(n-1)+f(n-2)+f(n-3)
"""

"""
[sudo code]
T = input()
f(3) = 4
f(2) = 2
f(1) = 1
def count(T):
    if T = 3
        return 4
    if T = 2
        return 2
    if T = 1
        return 1
    else:
        count = count(T-1)+count(T-2)+count(T-3)
    return count
"""
# trial
T = int(input()) 

def count(num):
    if num == 3:
        return 4
    if num == 2:
        return 2
    if num == 1:
        return 1
    else: 
        total = count(num-1) + count(num-2) + count(num-3)
    return total

for _ in range(T):
    n = int(input())
    print(count(n))



