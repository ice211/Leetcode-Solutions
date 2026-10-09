class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
            count = 0
            ans = 0
            for i in range(len(s)-1):
                if ord(s[i])+1 == ord(s[i+1]):
                    count+=1
                else:
                    count = 0
                ans = max(ans, count)
            return ans+1

# TC: O(n) — you scan the string once.
# SC: O(1) — you only use a few variables, regardless of input size.