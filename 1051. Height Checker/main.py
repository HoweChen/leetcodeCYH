class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(0,len(heights)):
            if heights[i]!=sorted_heights[i]:
                count+=1
        return count