List = list

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        1. cut the list using list comprehension
        2. if left >= then pop left else right
        3. if left list empty then append right
        4. if right list empty then append left
        """
        for num in nums2[:n:]:
            nums1.insert(0, num)
        while len(nums1) > m+n:
            nums1.pop(m+n)
        nums1.sort()
        return nums1



x = Solution()

print(x.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(x.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(x.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))

