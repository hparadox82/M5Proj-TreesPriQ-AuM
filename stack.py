class arrayStack:
    ##LIFO stack implementation using list:

    def __init__(self):
        self._data = []
        ##empty stack creation, nonpublic

    def __len__(self):
        return len(self._data)
        ##returns num of elements in stack

    def is_empty(self):
        return len(self._data) == 0
        ##true if stack is empty

    def push(self, e):
        self._data.append(e)
        ##add element e to top of stack

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._data[-1]
        ##return without removing top element/raise index error if empty

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._data.pop()
        ##remove/return top element/raise IE if empty





