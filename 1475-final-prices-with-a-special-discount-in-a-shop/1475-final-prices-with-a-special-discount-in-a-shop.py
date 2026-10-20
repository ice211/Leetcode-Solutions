class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        result = prices[:]

        for i in range(len(prices)):

            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] = prices[index] - prices[i]

            stack.append(i)

        return result