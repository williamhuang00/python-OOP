class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #increment rate to satisfy piles
        '''
        rate = 1 ... max(piles)
         
        #binary search take...
            - if midpoint rate works
            - keep going left
            - else if midpoint rate does not work
                - keep going right
        '''

        l = 1
        r = max(piles)
        min_rate = float('inf')
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            if totalTime <= h:
                r = k - 1
                min_rate = min(min_rate, k)
            else:
                l = k + 1
        
        return min_rate