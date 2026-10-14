class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict={}
        tDict={}
        for x in range(0,len(s)):
            if s[x] in sDict:
                count=sDict[s[x]]
                sDict[s[x]]=count+1
            else:
                sDict[s[x]]=1
            
            if t[x] in tDict:
                count=tDict[t[x]]
                tDict[t[x]]=count+1
            else:
                tDict[t[x]]=1
        
        if sDict == tDict:
            return True
        else:
            return False
