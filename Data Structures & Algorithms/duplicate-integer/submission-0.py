class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res={}
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            else:
                res[nums[i]]=res.get(nums[i],0)+1
        return False