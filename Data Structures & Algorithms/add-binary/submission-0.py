class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0

        for index, digit in enumerate(reversed(a)):
            if digit == '1':
                num1 += 2 ** index

        for index, digit in enumerate(reversed(b)):
            if digit == '1':
                num2 += 2 ** index

        num3 = num1 + num2
        return format(num3, 'b')