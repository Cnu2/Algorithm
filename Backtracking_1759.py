"""
1/5
1. 23/4/13
2.
3.
4.
5.
"""

"""
[문제]
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
"""
"""
[문제해결]
백트래킹
암호를 만든다 -> 모음과 자음의 개수를 체크
모음이 한개이상, 자음이 두개 이상이면 암호를 잘 만든 것으로 출력
암호는 반복문과 백 트래킹을 활용하여 만든다
"""

"""
[SUDO CODE]
L,C = input()
words = sorted(input().split())
vowels = [a, e, i, o , u]
def backtracking(count, index):
    if count == L:
        모음과 자음 체크 후
        answer 출력
    else:
        for i in range(index, C)
            answer.append(words[index])
            backtracking(count+1, index+1)
            answer에서 문자 하나 pop
"""

import sys


def back_tracking(cnt, idx):

    # 암호를 만들었을 때
    if cnt == l:
        # 모음, 자음 체크
        vo, co = 0, 0
        
        for i in range(l):
            if answer[i] in vowels:
                vo += 1
            else:
                co += 1

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer))

        return
        
    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1) # 백트래킹
        answer.pop()


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
vowels = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)

"""
[Keywords]
수학
브루트포스 알고리즘
조합론
백트래킹
"""