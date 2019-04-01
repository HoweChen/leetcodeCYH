class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # method 1
        #         sum_A = sum(A)
        #         if sum_A %3 != 0: return False
        #         else:
        #             sub_sum = sum_A/3
        #             part = 3
        #             bool_table = [False] * part
        #             prefix_sum = 0
        #             times = iter(range(1,part+1))
        #             time = next(times)
        #             for num in A:
        #                 prefix_sum +=num
        #                 if bool_table[time-1] is False and prefix_sum == sub_sum * time:
        #                     bool_table[time-1] = True
        #                     try:
        #                         time = next(times)
        #                     except StopIteration:
        #                         break

        #             return all(bool_table)
        # method 2
        # 保证找到 sum // 3 的一倍，和它的两倍
        sum_num = sum(A)
        if sum_num % 3 != 0:
            return False

        key_num = sum_num // 3
        list_num = 0
        flag = 0

        for num in A:
            list_num += num
            if list_num == key_num:
                if flag == 1:
                    # 找到两倍，此时flag为1说明已经找到了一倍
                    return True
                flag = 1  # 找到一倍的时候，设flag为1
                list_num = 0
        return False
