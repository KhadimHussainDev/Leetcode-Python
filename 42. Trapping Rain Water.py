#Sollution 1
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=[0]*len(height)
        rmax=[0]*len(height)

        max_left=height[0]  
        for i in range(1,len(height)):
            lmax[i]=max_left
            max_left=max(max_left,height[i])

        max_right=height[len(height)-1] 
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max_right
            max_right=max(max_right,height[i])

        water_trapped = 0
        for i , h in enumerate(height):
            water = min(lmax[i],rmax[i]) - h
            if water < 0:
                water = 0
            water_trapped += water
        return water_trapped

#Solution 2
class Solution:
    def trap(self, height: List[int]) -> int:

        l , r = 0 ,len(height) - 1
        max_left , max_right = height[0] , height[len(height)-1] 
        water_trapped = 0

        while l <= r :
            if max_left <= max_right:
                max_left = max(max_left , height[l])
                water = max_left - height[l]
                l += 1
            else : 
                max_right = max(max_right , height[r])
                water = max_right - height[r]
                r -= 1
            if water < 0:
                water = 0
            water_trapped += water

        return water_trapped

#Solution 3
class Solution:
    def trap(self, height: List[int]) -> int:

        l , r = 0 ,len(height) - 1
        max_left , max_right = height[l] , height[r] 
        water_trapped = 0

        while l < r :
            if max_left <= max_right:
                l += 1
                max_left = max(max_left , height[l])
                water_trapped += max_left - height[l]
            else : 
                r -= 1
                max_right = max(max_right , height[r])
                water_trapped += max_right - height[r]


        return water_trapped
