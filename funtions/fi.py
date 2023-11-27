class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        results =[]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                results.append(True)
            else:
                results.append(False)
        
        return results

    def hello(self):
        return "hello"