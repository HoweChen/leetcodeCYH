# Cannot handle super large list.
# Time limit exceed


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        else:
            left_list = []
            right_list = []
            result = []
            for num in nums:
                if num < 0:
                    left_list.append(num)
                else:
                    right_list.append(num)

            left_list = sorted(left_list)
            right_list = sorted(right_list)

            # when left list and right list are not none
            if left_list and right_list:
                print("~~~~~~~~~~~~~~~~New Start:~~~~~~~~~~~~~~")
                print("left_list:{0}".format(left_list))
                print("right_list:{0}".format(right_list))
                if right_list.count(0) >= 3:
                    result.append([0, 0, 0])
                for index in range(0, len(left_list)):
                    for i in range(0, len(right_list)):
                        target_num = -(left_list[index]+right_list[i])
                        if target_num in right_list[i+1:]:
                            target_list = sorted([left_list[index],
                                                  right_list[i], target_num])
                            if target_list not in result:
                                print("==========")
                                print("Sub-list: {0}".format(target_list))
                                print("Result:{0}".format(result))
                                result.append(target_list)

                for index in range(0, len(right_list)):
                    for i in range(0, len(left_list)):
                        target_num = -(right_list[index]+left_list[i])
                        if target_num in left_list[i+1:]:
                            target_list = sorted([right_list[index],
                                                  left_list[i], target_num])
                            if target_list not in result:
                                print("==========")
                                print("Sub-list: {0}".format(target_list))
                                print("Result:{0}".format(result))
                                result.append(target_list)
                result = sorted(result)
                # print(result)
                return result
            else:
                # one of left list and right list is None
                if left_list and not right_list:
                    return []
                else:
                    if sum(right_list) == 0:
                        if len(right_list) >= 3:
                            return [right_list[0:3]]
                        else:
                            return []
                    else:
                        return []


test_cases = [[-1, 0, 1, 2, -1, -4], [0, 0, 0],
              [0, 0, 0, 0], [1, -1, 2, -2], [], [0], [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0], [4, 4, 3, -5, 0, 0, 0, -2, 3, -5, -5, 0]]
sol = Solution()
for case in test_cases:
    print(sol.threeSum(case))
