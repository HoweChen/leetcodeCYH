class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # first attempt
        # for index in range(len(A)):
        #     if index % 2 == 0 and A[index] % 2 != 0:
        #         sub_index = index + 1
        #         while A[sub_index] % 2 != 0 and sub_index < len(A):
        #             sub_index += 1
        #         A[index], A[sub_index] = A[sub_index], A[index]
        #         continue
        #     if index % 2 != 0 and A[index] % 2 == 0:
        #         sub_index = index + 1
        #         while A[sub_index] % 2 == 0 and sub_index < len(A):
        #             sub_index += 1
        #         A[index], A[sub_index] = A[sub_index], A[index]
        #         continue
        # return A

        # second attempt better then first
        # A = sorted(A, key=lambda x: x % 2 == 0)
        # mid = len(A) // 2
        # odd_list = A[0:mid]
        # even_list = A[mid:]
        # result = []
        # if len(odd_list) == len(even_list):
        #     for i in range(0, mid):
        #         result.append(even_list[i])
        #         result.append(odd_list[i])
        #     return result
        # else:
        #     return None

        # third attemp 两个指针
        result = [0] * len(A)  # 初始化结果数组
        even_ptr = 0
        odd_ptr = 1
        for num in A:
            if num % 2 == 0:
                result[even_ptr] = num
                even_ptr += 2
            else:
                result[odd_ptr] = num
                odd_ptr += 2
        return result


sol = Solution()

A = [4, 2, 5, 7]
print(sol.sortArrayByParityII(A))
