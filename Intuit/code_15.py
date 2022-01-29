class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cannot_eat(piles, h, k):
            hours = 0
            for x in piles:
                if x % k == 0:
                    hours += x // k
                else:
                    hours += x // k + 1
            return hours > h
        
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if cannot_eat(piles, h, mid):
                low = mid + 1
            else:
                high = mid
        return low
