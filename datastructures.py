class Solution(object):
    def findClosestNumber(self, nums):
        self.nums=nums
        self.closest=nums[0]
        for x in nums:
            if abs(x)<abs(closest):
                closest=abs(x)
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return abs(closest)            
