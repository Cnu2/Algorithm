"""
3/3
1. 23/05/04
2. 23/05/11
3. 23/06/05
"""

"""
[sudo code]
- m,n을 입력한다.
- index = n - 1 
- 1부터 m까지의 리스트 생성 
- 빈 리스트 생성
- m번 도는 루프를 생성
    - 빈 리스트에 n번째 원소를 뽑아 append
    - index 업데이트
"""
m,n = map(int, input().split())
nums = [i for i in range(1,m+1)]
# breakpoint()
result = []
index = (n-1) % m
for i in range(m):
    result.append(nums[index])
    del nums[index]
    if len(nums) == 0:
        break
    else:
        index = (index+n-1)%len(nums)
r = ", ".join(map(str,result))
print('<'+r+'>')