from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(['+', '-', '*', '/'])
        n_s = []
        for t in tokens:
            if t == '+':
                n_s.append(n_s.pop()+n_s.pop())
            elif t == '-':
                n_s.append(-n_s.pop()+n_s.pop())
            elif t == '*':
                n_s.append(n_s.pop()*n_s.pop())
            elif t == '/':
                a = n_s.pop()
                b = n_s.pop()
                n_s.append(int(b/a))
            else:
                n_s.append(int(t))
        return n_s[-1]

