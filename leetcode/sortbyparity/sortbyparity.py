class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Time: O(n) - but loops the array 2 times
        # Space: O(1) (additional)
        evens = [n for n in nums if n % 2 == 0]
        odds = [n for n in nums if n % 2 != 0]
        return evens + odds
