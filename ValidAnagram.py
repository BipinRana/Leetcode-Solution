class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        vocab={}
        sec_vocab={}
        for i in s:
            if i in vocab:
                vocab[i]+=1
            else:
                vocab[i]=1 
        for i in t:
            if i in sec_vocab:
                sec_vocab[i]+=1
            else:
                sec_vocab[i]=1 
        return vocab== sec_vocab