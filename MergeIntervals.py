class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for item in intervals:
            if not res or item[0]>res[-1][1]:
                res.append(item)
            else:
                res[-1][1] = max(res[-1][1],item[1]) 
        return res

