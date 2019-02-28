class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # method 1: bi-directional search
        # A = sorted(A)
        # len_a = len(A)
        # pivot = len_a//2
        # result = None
        # for index in range(pivot,len_a):
        #     if A[index] == A[index-1]:
        #         result = A[index]
        #     if A[len_a-1-index]== A[len_a-index]:
        #         result = A[len_a-1-index]
        # return result

        # method 2: hashmap
        # count = collections.Counter(A)
        # for k in count:
        #     if count[k] > 1:
        #         return k

        # method 3: set comparison
        # A=sorted(A)
        # set_a = sorted(list(set(A)))
        # for index in range(0,len(set_a)):
        #     if A[index] != set_a[index]:
        #         print(index)
        #         return A[index]
        # return A[-1]

        # method 4: stack
        stack = []
        for _ in range(0, len(A)):
            num = A.pop()
            if num in stack:
                return num
            else:
                stack.append(num)
