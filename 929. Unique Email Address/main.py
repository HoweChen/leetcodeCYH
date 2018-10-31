class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        for email in emails:
            prefix, suffix = email.split("@")
            prefix = prefix[0:prefix.index("+")].replace(".", "")
            result.append(prefix+"@"+suffix)

        return len(list(set(result)))


input = ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

sol = Solution()
print(sol.numUniqueEmails(input))
