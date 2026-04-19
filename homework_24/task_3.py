class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def get_from_stack(self, e):
        temp = []

        while self._items:
            top = self.pop()
            if top == e:
                break
            temp.append(top)

        else:
            raise ValueError('Елемент не знайдено')

        while temp:
            self.push(temp.pop())

        return e