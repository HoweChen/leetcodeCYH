class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # first method: brute force
        # result = []
        # for i in arr2:
        #     for j in arr1:
        #         if j==i:
        #             result.append(j)
        # not_list = []
        # for num in arr1:
        #     if num not in arr2:
        #         not_list.append(num)
                
        # result += sorted(not_list)
        # return result

         # second method:
        from collections import Counter
        ans, cnt = [],Counter(arr1)
        for num in arr2:
            ans.extend([num]*cnt.pop(num))
        cnt = sorted(cnt.items(),key=lambda k:k[0])  # can use a range here
        for num,times in cnt:
            ans.extend([num]*times)
        return ans