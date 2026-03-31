class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n) :
            req = target - nums[i]
            if req in hashmap :
                return [hashmap[req], i]
            hashmap[nums[i]] = i

# Time Complexity - O(n)
# Space Complexity - O(n)
