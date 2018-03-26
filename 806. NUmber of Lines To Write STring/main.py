import string


class Solution(object):

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        width_dict = dict(zip(string.ascii_lowercase, widths))
        line_counter = 1
        out_flag = 0
        now_width = 0
        max_length = 100
        for character in S:
            character_length = width_dict.get(character)
            if now_width+character_length > max_length:
                line_counter += 1
                now_width = character_length
            elif now_width+character_length == max_length:
                line_counter += 1
                now_width = 0
            else:
                now_width += character_length
        if now_width == 0:
            line_counter -= 1
        result = [line_counter, now_width]
        return result
