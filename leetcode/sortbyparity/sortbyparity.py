class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Time: O(n) - but only loops the array 1 time
        # Space: O(n) (additinal)
        evens = []
        odds = []
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds
