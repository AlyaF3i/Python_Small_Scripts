class Solution:
    def solve(self, prices):
        if len(prices)<2:
            return 0

        min=prices[0]
        total=0
        for a in range(1,len(prices)):
            if prices[a]>prices[a-1]:
                continue
            else:
                temp=prices[a-1]-min
                if temp>total:
                    total=temp
                min=prices[a]
        else:
            if prices[a]>prices[a-1]:
                tem=prices[a]
            else:
                tem=prices[a-1]
            if tem-min>total:
                return tem-min
        return total
a=Solution()

print(a.solve([9,11,8,5,7,10]))