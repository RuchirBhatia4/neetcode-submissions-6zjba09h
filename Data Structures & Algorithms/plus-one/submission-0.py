class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        size = len(digits) - 1
        for i, num in enumerate(digits):
            number = number * 10 + num
        number += 1
        l = []
        while number:
            l.append(number % 10)
            number //= 10
        l.reverse()
        return l
            



            

