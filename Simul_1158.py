"""
1/3
1. 23/05/04
2. 23/05/11
3. 
"""

"""
[문제]
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""

"""
[sudo code]
1. N,K를 입력받는다.
2. num_list와 result 리스트를 만든다.
3. for문을 N번 돌린다.
    3-1. num_list에서 K번째를 result에 append한다.
    3-2. num_list를 업데이트 한다.
4. result를 출력한다.
"""
import sys
N,K = map(int, sys.stdin.readline().split())
#breakpoint()
num_list = [i for i in range(1,N+1)]
yo_list = []
i = (K-1)%N
for _ in range(N):
    yo_list.append(num_list[i])
    num_list = num_list[:i] + num_list[i+1:]
    N -= 1
    if N == 0:
        break
    else:
        i = (i + K-1) % N
output_str = "<" + ", ".join([str(num) for num in yo_list]) + ">"
print(output_str)

