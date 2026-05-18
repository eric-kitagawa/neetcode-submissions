class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ['1','2','3','4','5','6','7','8','9',"0","a","b","c","d","e","f","g","h","i","j","k","l","m",'n','o','p','q','r','s','t','u','v','w',"x","y","z"]
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l].lower() not in alphanumeric:
                l += 1
            while r > l and s[r].lower() not in alphanumeric:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True