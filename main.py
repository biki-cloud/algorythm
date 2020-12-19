from tree.binary_search_tree import BinarySearchTree


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            mx = self.stack[-1][1]
            self.stack.append((x, max(x, mx)))

    def pop(self) -> int:
        if self.stack:
            e = self.stack.pop()
            return e[0]
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

    def popMax(self) -> int:
        if self.stack:
            max, index = 0,0
            for i,n in enumerate(self.stack):
                if max < n or max == n:
                    max = n
                    index = i
            return self.stack.pop(index)
        return 0


obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(5)
print(obj.stack)
print(obj.top())
print(obj.stack)
print(obj.popMax())
print(obj.stack)
print(obj.top())
print(obj.stack)
print(obj.peekMax())
print(obj.stack)
print(obj.pop())
print(obj.stack)
print(obj.top())
print(obj.stack)
