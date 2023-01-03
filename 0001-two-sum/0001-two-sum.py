class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]: #파이썬 내부 함수로 구현된 in은 파이썬 레벨에서 매번 값을 비교하는 것에 비해 훨씬 더 빨리 실행된다
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]