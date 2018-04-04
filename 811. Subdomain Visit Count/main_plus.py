class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        self.result_dict = dict()
        self.result_list = list()
        for domain in cpdomains:
            number, domain_name = domain.split()
            number = int(number)
            self.in_dict(domain_name, number)
            while True:
                try:
                    flag = domain_name.index('.')
                    domain_name = domain_name[flag+1:]
                    self.in_dict(domain_name, number)
                except ValueError:
                    break

        # get the result from the result_dict
        for key, value in self.result_dict.items():
            self.result_list.append(' '.join((str(value), key)))
        return self.result_list

    def in_dict(self, str_var, int_var):
        if str_var not in self.result_dict:
            self.result_dict[str_var] = int_var
        else:
            self.result_dict[str_var] += int_var


example_one = ["9001 discuss.leetcode.com"]
example_two = ["900 google.mail.com",
               "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]


def main():
    sol = Solution()
    # print(sol.subdomainVisits(example_one))
    print(sol.subdomainVisits(example_two))


if __name__ == '__main__':
    main()
