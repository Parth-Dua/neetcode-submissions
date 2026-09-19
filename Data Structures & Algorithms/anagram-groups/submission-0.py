from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_to_string_list = defaultdict(list)

        for s in strs: 
            freq = defaultdict(int)

            for char in s: 
                freq[char]+=1

            freq_to_string_list[tuple(sorted(freq.items()))].append(s)

        return list(freq_to_string_list.values())
         

            
