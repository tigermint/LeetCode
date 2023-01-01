class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 정렬 list 따로 저장
        sorted_list = [''.join(sorted(str)) for str in strs]
        group_dict = {}
        
        # 비교하면서 index로 dict에 저장
        for index in range(0, len(strs)):
            if sorted_list[index] not in group_dict.keys():
                group_dict[sorted_list[index]] = []                
            group_dict[sorted_list[index]].append(strs[index])            
        return [value for value in group_dict.values()]
                
        
                
        
        
        
        
        