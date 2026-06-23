class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_array = [char for char in s if char.isalnum()]
        i=0
        j=len(clean_array)-1
        while i<=j:
            if clean_array[i].casefold()==clean_array[j].casefold():
                i+=1
                j-=1
            else:
                return False
        return True