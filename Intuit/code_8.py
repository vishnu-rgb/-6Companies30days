class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        counter_of_boomerangs = 0
        for x in points:
            x1, y1 = x
            distance_count_dict = {}
            for y in points:
                x2, y2 = y
                diff_x = x2-x1
                diff_y = y2-y1
                dist = diff_x ** 2 + diff_y ** 2
                if dist not in distance_count_dict:
                    distance_count_dict[dist] = 1
                else:
                    distance_count_dict[dist] += 1
            for d in distance_count_dict:
                n = distance_count_dict[d]
                counter_of_boomerangs += n * (n-1)
        return counter_of_boomerangs
