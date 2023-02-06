class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop(): # 대응하는게 x or 닫히는게 없음
                return False
        return len(stack) == 0
                            
            