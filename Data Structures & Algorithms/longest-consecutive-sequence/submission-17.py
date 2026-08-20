class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        record = 0
        for n in seen:
            if n-1 not in seen:
                count = 1
                while n + count in seen:
                    count += 1
                record = max(count, record)
        return record