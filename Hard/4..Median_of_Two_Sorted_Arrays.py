class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=len(nums1)
        b=len(nums2)
        liste = []
        i=0
        j=0
        while i < a and j < b:
            if nums1[i] < nums2[j]:
                liste.append(nums1[i])
                i += 1
            else:
                liste.append(nums2[j])
                j += 1
        while i < a:
            liste.append(nums1[i])
            i += 1
        while j < b:
            liste.append(nums2[j])
            j += 1
        n = a + b
        if n % 2 == 1:
            return( float(liste[n // 2]))
        else:
            return ((liste[n // 2] + liste[(n//2)-1]) / 2.0)