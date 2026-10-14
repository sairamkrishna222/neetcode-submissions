class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res=defaultdict(list)
        for x in strs:
          sorted_chars = ''.join(sorted(x))
          res[sorted_chars].append(x)
        return list(res.values())


        
