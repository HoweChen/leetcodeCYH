class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result_dict = dict()
        result_list = list()
        for domain in cpdomains:
            split_res = domain.split()
            number = int(split_res[0])
            domain_name = split_res[1]
            # handle the third_class_domain which is the domain_name here
            if domain_name not in result_dict:
                result_dict[domain_name] = number
            else:
                result_dict[domain_name] += number
            parent_domain = domain_name.split('.')
            if len(parent_domain) > 2:
                second_class_domain = '.'.join(parent_domain[1:])
                super_domain = parent_domain[-1]
                if second_class_domain not in result_dict:
                    result_dict[second_class_domain] = number
                else:
                    result_dict[second_class_domain] += number
            else:
                super_domain = parent_domain[-1]
                
            if super_domain not in result_dict:
                result_dict[super_domain] = number
            else:
                result_dict[super_domain] += number
        # get the result from the result_dict
        for key, value in result_dict.items():
            result_list.append(' '.join((str(value), key)))
        return result_list


example_one = ["9001 discuss.leetcode.com"]
example_two = ["900 google.mail.com",
               "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]


def main():
    sol = Solution()
    # print(sol.subdomainVisits(example_one))
    print(sol.subdomainVisits(example_two))


if __name__ == '__main__':
    main()
