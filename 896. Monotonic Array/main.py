class Solution:

    def increasing(self, A: List[int])->bool:
        return all(x <= y for x, y in zip(A, A[1::]))

    def decreasing(self, A: List[int])->bool:
        return all(x >= y for x, y in zip(A, A[1::]))

    def isMonotonic(self, A: List[int]) -> bool:
        return self.increasing(A) or self.decreasing(A)
