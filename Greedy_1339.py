"""
3/3
1. 23/04/28
2. 23/05/05
3. 23/06/01

링크 : https://www.acmicpc.net/problem/1339
"""

"""
[문제]
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.
"""

"""
[sudo code]
n 숫자의 갯수를 입력
alpha에 단어를 저장
alpha안에 단어의 알파벳마다 각 자리수를 제곱근으로 표현
단어를 내림차순으로 정렬
9부터 0까지 각 단어마다 곱해준다.
"""
import sys
n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
num_list = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 (1의 자리면 1)
        else: # 자리에 없으면 새로 추가 (10의 자리면 10)
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1) 
breakpoint()
for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    num_list.append(val)

num_list.sort(reverse=True) # 수들을 내림차순 정렬
# breakpoint()

sum = 0
pows = 9
for i in num_list: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다.
    sum += pows * i
    pows -= 1
# 네려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1
print(sum)

