class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2).sort()
        list_length = len(nums1)
        index = list_length//2
        if list_length % 2 == 0:
            result = float((nums1[index]+nums1[index-1]))/2
        else:
            result = nums1[index]
        return result
