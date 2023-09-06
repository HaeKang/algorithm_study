# https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distances = []

        for i in range(len(points)):
            distance =  math.sqrt( ( points[i][0] ) **2 + ( points[i][1] ) **2  )
            distances.append([distance,points[i]])    

        distances.sort()
        for idx in range(k):
            ans.append(distances[idx][1])
        
        return ans
