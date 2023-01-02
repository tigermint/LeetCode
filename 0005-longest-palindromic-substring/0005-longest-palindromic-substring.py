class Solution:
    def longestPalindrome(self, s: str) -> str:        
        length, s_length = [len(s), len(s)] 
        while length > 0:
            for i in range(0, s_length - length + 1):
                tmp = s[i:i+length] 
                if len(tmp)%2 == 0 and tmp[0:len(tmp)//2] == tmp[-1:len(tmp)//2-1:-1]:
                    return tmp
                if len(tmp)%2 !=0 and tmp[0:len(tmp)//2] == tmp[-1:len(tmp)//2:-1]:
                    return tmp
            length -= 1
        return ''
        
        
        
    
        