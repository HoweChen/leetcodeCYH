class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # method 1
        # using counter, time limit exceeded
        # nums_len = len(nums)
        # if nums_len == 1:
        #     return 1
        # else:
        #     from collections import Counter
        #     _,frequency = Counter(nums).most_common(1)[0]
        #     right = nums_len-1
        #     shortest = nums_len
        #     sub_lists = []
        #     # print(nums_len)
        #     for w_size in range(nums_len-1,frequency-1,-1):
        #         for i in range(0,nums_len-w_size+1):
        #             # print(w_size,i)
        #             sub_list = nums[i:i+w_size]
        #             # print(sub_list)
        #             sub_list_counter = Counter(sub_list)
        #             if frequency in sub_list_counter.values():
        #                 sub_list_len = len(sub_list)
        #                 if sub_list_len < shortest:
        #                     shortest = sub_list_len
        #     # print("-----")
        #     return shortest

        # method 2
        # 通过记录那个频率最高的数字出现的位置来解决问题
        # 最短的 sublist 一定是那个数字出现的起点和终点的长度
        c = dict(collections.Counter(nums))
        nums2 = nums.copy()
        nums2.reverse()
        m = max(c.values())
        if m == 1:
            return 1
        dist = []
        for i, j in c.items():
            if j == m:
                a = nums.index(i)
                b = len(nums)-nums2.index(i)-1
                dist.append((b-a+1))
        return (min(dist))
