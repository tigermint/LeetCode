class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        # 팰린트룸 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True