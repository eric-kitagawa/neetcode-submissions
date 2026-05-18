from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_char_list_1 = defaultdict(int)
        my_char_list_2 = defaultdict(int)
        for char in s:
            my_char_list_1[char] += 1
        
        for char in t:
            my_char_list_2[char] += 1

        return my_char_list_1 == my_char_list_2
        