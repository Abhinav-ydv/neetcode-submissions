class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        while True :
        
            if len(s)!=len(t):
                return False

            for i in range(len(s)):
                if s.count(s[i])!=t.count(s[i]):
                    return False 
                    break
            return True
            break
        