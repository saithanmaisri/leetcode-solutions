class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = nums1 + nums2
        n.sort()
        mid = len(n) // 2
        if len(n) % 2 == 1:
            return n[mid]
        else:
            return (n[mid - 1] + n[mid]) / 2.0
