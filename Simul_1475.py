"""
1/3
1. 23/05/11
2. 
3. 
"""

"""
[문제]
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 

(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

"""

"""
[sudo code]
1. n을 입력받는다.
2. 크기가 10인 result 리스트를 만든다.
3. n에 대하여 for문을 돌린다.
    n[i]가 6 또는 9이면
        n[6] <= n[9] 이면
            n[6]에 +1
        그렇지 않으면
            n[9]에 +1
    else
        n[i] += 1
"""
import sys
input = sys.stdin.readline
N = list(str(int(input())))
# breakpoint()
result = [0]*10
for num in N:
    if int(num) == 6 or int(num) == 9:
        if result[6] <= result[9]:
            result[6] += 1
        else:
            result[9] += 1
    else:
        result[int(num)] += 1
    
print(max(result))


