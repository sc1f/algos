class Stack(object):
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

    def __len__(self):
        return len(self.items)

class MaxStack():
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        self.stack.pop(item)
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

    def get_max(self):
        return self.max_stack.peek()

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if len(self.s2) == 0:
            # basically reverse the first stack, otherwise we know s2 is s1[::-1] so just return head of s2
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def __str__(self):
        return str(self.s1) + " " + str(self.s2)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)

