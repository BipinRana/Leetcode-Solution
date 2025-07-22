import random
class RandomizedSet(object):

    def __init__(self):
        self.values = []
        self.values_to_index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.values_to_index:
            return False
        else:
            self.values.append(val)
            self.values_to_index[val] = len(self.values)-1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.values_to_index:
            temp = self.values_to_index[val]
            final = self.values[-1]
            self.values_to_index[val] = self.values_to_index[final]
            self.values_to_index[final] = temp
            self.values[temp] = self.values[-1]
            self.values.pop()
            del(self.values_to_index[val])
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        random_number = random.choice(self.values)
        return random_number


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
