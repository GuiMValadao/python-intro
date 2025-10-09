def solution(k = int):
    k = int(k)
    nums=[1]
    summer, appender = 0, 0
    nums[len(nums)-1] += (k+1)//(k//10)
    summer += (k+1)//(k//10)
    while sum(nums) <= k:
        nums.append(nums[len(nums)-1])
    appender = len(nums)-1
    return summer + appender
            



n = input()
print(solution(n))