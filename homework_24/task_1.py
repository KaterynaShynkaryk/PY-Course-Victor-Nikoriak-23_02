class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

text = input('Введи текст: ')

stack = Stack()

for item in text:
    stack.push(item)

result = []

while not stack.is_empty():
    result.append(stack.pop())

print(''.join(result))