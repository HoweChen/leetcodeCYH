class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 找第一个空格的下一位看看数字还是字母来分组
        l = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)
        d = filter(lambda l: l[l.find(" ") + 1].isdigit(), logs)

        # 排序
        return sorted(l, key=lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(d)
