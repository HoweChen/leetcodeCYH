class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:

        sum_A = sum(A)
        sum_B = sum(B)
        # here we use set because we want to remove the redundent number in each list
        A = set(A)
        B = set(B)
        # sum_A - x + y = sum_B - y + x => y-x = (sum_B - sum_A) / 2
        y_minus_x = (sum_B-sum_A)//2
        for x in A:
            y = x+y_minus_x
            if y in B:
                return [x, y]
