class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # method 1： 先找到所有的pattern，然后每个pattern放到字符串里去匹配有多少个
        # 可行但超时
        #         min_range = 1
        #         max_range = len(s)//2
        #         patterns = []
        #         for i in range(min_range,max_range+1):
        #             order = "0"*i+"1"*i
        #             r_order = order[::-1]
        #             patterns.append(order)
        #             patterns.append(r_order)

        #         result = 0
        #         for pattern in patterns:
        #             result += s.count(pattern)
        #         return result

        # method 2
        # 1. 先找到从字符串开始最长的连续数字长度
        # 2. 然后记下这个当前最长的长度
        # 3. 继续往下走，如果遇到不同的数字，说明数字发生了变化，现在开始记录这个新的变化的连续性（即重复1的工作）
        #    但这个时候需要开始对比之前记录的最长连续性，和现在的最长连续性，如果大于或等于则说明还会有匹配存在
        #    例如：00011,这个时候第一个最长匹配长度是3（000），第二个最长匹配是2（11）
        #    但是这个时候3>=2，说明有新的匹配存在，即 0011 存在于 00011 中

        prev_len = 0
        curr_len = 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_len += 1
            else:
                prev_len = curr_len
                curr_len = 1
            if prev_len >= curr_len:
                result += 1
        return result
