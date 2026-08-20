class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}

        if len(nums) == 0:
            return 0

        for i,n in enumerate(nums):
            seen[n] = i
        record = 0
        for i,n in enumerate(nums):
            if n-1 not in seen:
                count = 0
                start = n
                while start in seen:
                    count += 1
                    start += 1
                if count > record:
                    record = count
        return record