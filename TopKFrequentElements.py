class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        freq_list = []
        for num in count:
            freq_list.append((count[num], num))  
        freq_list.sort(reverse=True)
        result = []
        for i in range(k):
            result.append(freq_list[i][1])

        return result
