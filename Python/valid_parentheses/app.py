class Solution:
    def isValid(self, s: str) -> bool:
        o = set(['(', '[', '{'])
        cash = []
        for l in s:
            if l in o:
                cash.append(l)
            else:
                if len(cash)==0: return False
                if l == ')' and cash[-1] != '(': return False
                elif l == ']' and cash[-1] != '[': return False
                elif l == '}' and cash[-1] != '{': return False
                cash.pop()
        return len(cash) == 0 

