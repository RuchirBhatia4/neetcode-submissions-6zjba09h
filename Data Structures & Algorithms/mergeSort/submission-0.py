# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        a = pairs
        arr1 = pairs[:(len(a) // 2)]
        arr2 = pairs[(len(a) // 2):]
        arr1 = self.mergeSort(arr1)
        arr2 = self.mergeSort(arr2)
        return self.merge(arr1, arr2)
    def merge(self, x: List[Pair], y: List[Pair]) -> List[Pair]:
        ans = []
        while x and y:
            if x[0].key > y[0].key:
                ans.append(y[0])
                y.pop(0)
            else:
                ans.append(x[0])
                x.pop(0)
        while x:
            ans.append(x[0])
            x.pop(0)
        while y:
            ans.append(y[0])
            y.pop(0)
        return ans