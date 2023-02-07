class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            # 이미 처리된 문자 여부 확인 -> 있다면 skip
            if char in seen: 
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
        