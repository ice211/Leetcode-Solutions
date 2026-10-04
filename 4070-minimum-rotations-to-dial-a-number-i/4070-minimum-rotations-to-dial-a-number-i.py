class Solution:
    def minRotations(self, s: str) -> int:
        output, current = 0,0
        for i in range(len(s)):
            number = int(s[i])
            distance = abs(number - current)
            altDistance = 10 - distance
            minDistance = min(distance,altDistance)
            
            output += minDistance
            current = number
        return output