class Solution:
    def maxArea(self, height: List[int]) -> int:
        # method 1:
        # slide window, time limit exceeded
        # list_len = len(height)
        # result = 0
        # for w_range in range(1,list_len):
        #     for i in range(0,list_len):
        #         y = min(height[i],height[w_range])
        #         x = w_range-i
        #         area = x*y
        #         if area > result:
        #             result = area
        # return result

        # method 2:
        # two_pointer, bi-direction ptr
        h_ptr = 0
        t_ptr = len(height)-1
        result = 0
        while h_ptr < t_ptr:
            area = min(height[h_ptr], height[t_ptr]) * (t_ptr-h_ptr)
            if area > result:
                result = area
            if height[h_ptr] <= height[t_ptr]:
                h_ptr += 1
            else:
                t_ptr -= 1
        return result
