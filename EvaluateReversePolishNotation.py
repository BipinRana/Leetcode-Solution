class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        for token in tokens:
            if token not in "*-/+":
                res.append(int(token))
            else:
                prev = res.pop()
                if token=="+":
                    res[-1] = res[-1]+prev
                elif token=="-":
                    res[-1] = res[-1]-prev
                elif token=="*":
                    res[-1] = res[-1]*prev
                elif token=="/":
                    res[-1] = int(float(res[-1])/float(prev))
        return res[0]


            
            

                

                
        
