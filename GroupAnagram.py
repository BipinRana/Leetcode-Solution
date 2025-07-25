class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for i in strs:
            temp_word = ''.join(sorted(i))
            res[temp_word].append(i)
        return(res.values())


               
                    



        
