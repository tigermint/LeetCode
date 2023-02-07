class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, d, stack = [0] * len(temperatures), {}, []
        
        # 딕셔너리 삽입
        for i in range(len(temperatures)):
            d[i] = temperatures[i]
        
        # stack 연산
        for i in range(len(temperatures)):
            # 비교 -> stack 제거, stack에는 index 삽입
            while stack:
                if d[stack[-1]] < d[i]:
                    # 차이 연산
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                else: break            
            stack.append(i)
        return result            
            