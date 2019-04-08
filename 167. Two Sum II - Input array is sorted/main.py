class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # method 1
        # use python syntax to solve, very slow
        # for index, value in enumerate(numbers):
        #     another_value = target-value
        #     if another_value in numbers[index+1::]:
        #         result_index = index +1
        #         return [result_index,numbers[result_index::].index(another_value)+1+result_index]

        # method 2:
        # two ptrs start as index 0 and 1, time limit exceeded
        # for i in range(0,len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j] > target:
        #             break
        #         elif numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        # method 3:
        # use dictionary to record the number so that "is in" operation would take less time
        # better than method 4 when there are plenty of redundent numbers in the list
        numbers_set = set(numbers)
        is_seen_dict = dict(zip(numbers_set, [False]*len(numbers_set)))
        for num in numbers:
            # the reason why we use numbers in this for-loop is that the dictionary is inorder
            a_num = target-num
            if is_seen_dict[num] is False:
                if a_num in is_seen_dict.keys() and is_seen_dict[a_num] is False:
                    # only when a_num in keys and dict[a_num] is False
                    first_index = numbers.index(num)+1
                    second_index = numbers[first_index::].index(
                        a_num)+first_index+1
                    return [first_index, second_index]
                else:
                    # Neither the a_num is not in the dictionary nor the a_num is True in that dictionary
                    # both are not ok for the num, so we set the num in dictionary as True
                    is_seen_dict[num] = True
            else:
                # which means this number has been searched
                continue

        # method 4:
        # left and right pointers
        # l, r = 0, len(numbers)-1
        # while l < r:
        #     s = numbers[l] + numbers[r]
        #     if s == target:
        #         return [l+1, r+1]
        #     elif s < target:
        #         l += 1
        #     else:
        #         r -= 1
