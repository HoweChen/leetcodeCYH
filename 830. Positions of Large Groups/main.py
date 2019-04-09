class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        result = []
        counter = 0
        tmp_char = None
        for i in range(len(S)):
            # meet the first character of the S
            if tmp_char is None:
                tmp_char = S[i]
                counter = 1
            else:
                # when new char meet the tmp_char and they are same
                if S[i] == tmp_char:
                    counter += 1
                else:
                    # if not the same character
                    if counter >= 3:
                        # append the index into the result
                        index = i-1
                        result.append([index-counter+1, index])
                    # reset the tmp_char and counter
                    tmp_char = S[i]
                    counter = 1

        # add the new sub_list into result when the condition match in the bottom of the list
        if counter >= 3:
            result.append([len(S)-counter, len(S)-1])
        return result
