class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.square_of_digits(n)
        return True

    def square_of_digits(self, num: int) -> int:
        total = 0
        while num > 0:
            total += (num % 10) * (num % 10)
            num = num // 10
        return total
