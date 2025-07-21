class StockSpanner(object):

    def __init__(self):
        self.stock = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count =1
        while self.stock and price >= self.stock[-1][0]:
            count += self.stock.pop()[1]
        self.stock.append((price,count))
        return count

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
