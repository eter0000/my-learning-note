class Solution:
    def findErrorNums(self, nums):
        sub = sum(set(nums)) # 去重複後加總
        repeat = sum(nums) - sub #全部加總 - 去重複後加總
        miss = sum(range(len(nums)+1)) - sub # 正確加總 - 去重複後加總
        return [repeat,miss]
