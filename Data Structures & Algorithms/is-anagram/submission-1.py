class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1={}
        res2={}
        for char in s:
            res1[char]=res1.get(char,0)+1
        for char in t:
            res2[char]=res2.get(char,0)+1
        if len(res1)!= len(res2):
            return False
        for key,val in res1.items():
            if key in res2:
                if res2[key]==val:
                    continue
                else:
                    return False
            else:
                return False
        return True
