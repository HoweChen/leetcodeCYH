class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        #A_len = len(A)
        A = sorted(A)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
#         result = self.find_triangle(A_sort)
#         return result

#     # method 1: recursive
#     def find_triangle(self, sub_list:List[int]) -> int:
#         #print(sub_list)
#         sub_list_len = len(sub_list)
#         if sub_list_len <=2:
#             return 0
#         else:
#             a = sub_list[0]
#             b = sub_list[1]
#             c = sub_list[2]

#             if a>= b + c:
#                 return self.find_triangle(sub_list[1::])
#             else:
#                 return a+b+c
