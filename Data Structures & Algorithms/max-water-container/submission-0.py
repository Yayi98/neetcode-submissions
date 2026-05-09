class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) -1
        max_area = min(height[i],height[j]) * (j-i)

        while (i<j):
            area = min(height[i],height[j]) * (j-i)
            if area>max_area:
                max_area = area
            if(height[i]<height[j]):
                i +=1
            else:
                j-=1
        return max_area