def twoSum(nums: list[int], target: int):
    ans = []
    for i_index, i in enumerate(nums):
        for j_index, j in enumerate(nums):
            if i == j: 
                continue
            if i + j == target:
                ans = [i_index, j_index]
    return ans
