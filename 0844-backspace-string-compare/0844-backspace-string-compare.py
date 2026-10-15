class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []

        for each in s:
            if stackS and each == "#":
                stackS.pop()
            elif each != "#":
                stackS.append(each)
        
        for each in t:
            if stackT and each == "#":
                stackT.pop()
            elif each != "#":
                stackT.append(each)

        return stackS == stackT
