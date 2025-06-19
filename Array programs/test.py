from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums):
        d=dict(Counter(nums))
        f=list(filter(lambda x: d[x]==1,d.keys()))
        print(f)
obj=Solution()
obj.singleNonDuplicate([11,2,2,3,3])
