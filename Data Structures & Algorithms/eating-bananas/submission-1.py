class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        biggest_pile = piles[-1]
        min_speed = 1
        max_speed = biggest_pile
        speed = 0 
        while min_speed <= max_speed:
            x = min_speed + (max_speed - min_speed) // 2
            count = 0 
            for y in piles:
                count += math.ceil(y / x)
            if count <= h:
                speed = x
                max_speed = x - 1
            else:
                min_speed = x + 1
        return speed