# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickersort(pairs, 0, len(pairs) - 1)
        return pairs

    def quickersort(self, a: List[Pair], low: int, high: int) -> None:
        if low < high:
            p = self.partition(a, low, high)
            self.quickersort(a, low, p - 1)
            self.quickersort(a, p + 1, high)

    def partition(self, b: List[Pair], low: int, high: int) -> int:
        pivot = b[high]
        i = low

        for j in range(low, high):
            if b[j].key < pivot.key:
                b[i], b[j] = b[j], b[i]
                i += 1

        b[i], b[high] = b[high], b[i]
        return i