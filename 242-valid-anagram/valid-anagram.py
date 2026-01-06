class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        freq1 = {}
        freq2 = {}
        for alpha in s:
            if alpha in freq1:
                freq1[alpha]+=1
            else:
                freq1[alpha] = 1

        for alpha in t:
            if alpha in freq2:
                freq2[alpha]+=1
            else:
                freq2[alpha] = 1
            
        if freq1 == freq2:
            return True
        
        else:
            return False