class Solution:
    def candy(self, ratings: List[int]) -> int:
        curr = 1
        prev_high = 1
        highest = 0
        count = 1
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                curr += 1
                highest = i
                prev_high = curr
            elif ratings[i]<ratings[i-1]:
                if prev_high<=i-highest:
                    count += 1
                count += i-highest-1
                curr = 1
            else:
                highest = i
                curr = 1
                prev_high = curr
            count += curr
        return count
