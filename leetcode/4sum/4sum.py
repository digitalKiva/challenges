class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time: O(n^4) - this is not good
        # Space: O(n) (additinal) - not 100% sure on this
        res = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range (j+1, len(nums)):
                    for l in range (k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ans = sorted([nums[i],nums[j],nums[k],nums[l]])
                            res[f"{ans}"]=ans

        return [v for v in res.values()]