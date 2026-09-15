class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char>target:
                return char
        return letters[0]
    

obj=Solution()
print(obj.nextGreatestLetter(["c","f","j"],"a"))