class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cmap1 = {}
        cmap2 = {}

        for c1, c2 in zip(s, t):
            if c1 in cmap1:
                cmap1[c1] += 1
            else:
                cmap1[c1] = 1
            
            if c2 in cmap2:
                cmap2[c2] += 1
            else:
                cmap2[c2] = 1
        
        return cmap1 == cmap2