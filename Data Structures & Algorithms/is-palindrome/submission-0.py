class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_String=""
        for ch in s:
            if ch.isalnum():
                new_String+=ch.lower()
        
        return new_String == new_String[::-1]
        