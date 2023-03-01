class MinStack:

    def __init__(self):
        self.stack = []
        self.min_idx = []
        self.curr_min = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_idx.append([0, 1])
            return

        self.stack.append(val)
        if val < self.stack[self.curr_min]:
            self.curr_min = len(self.stack)-1
            self.min_idx.append([self.curr_min, 1])
        else:
            self.min_idx[-1][1] += 1

    def pop(self) -> None:
        self.stack.pop()
        if self.min_idx:
            if self.min_idx[-1][1] > 1:
                self.min_idx[-1][1] -= 1
            else:
                self.min_idx.pop()
            if self.min_idx:
                self.curr_min = self.min_idx[-1][0]
            else:
                self.curr_min = 0
        else:
            self.curr_min = 0

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(f'{self.curr_min} : {len(self.stack)}')
        return self.stack[self.curr_min]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
