class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class UnsortedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    ''' Розширення UnsortedList '''

    def append(self, item):
        temp = Node(item)

        if self._head is None:
            self._head = temp
            return

        current = self._head

        while current.get_next() is not None:
            current = current.get_next()

        current.set_next(temp)

    def index(self, item):
        current = self._head
        pos = 0

        while current is not None:
            if current.get_data() == item:
                return pos
            pos += 1
            current = current.get_next()
        raise ValueError('item not found')

    def pop(self):
        current = self._head
        previous = None

        if current is None:
            raise ValueError('pop from empty list')

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        if previous is None:
            self._head = None
        else:
            previous.set_next(None)

        return current.get_data()

    def insert(self, position, item):
        new_node = Node(item)

        if position == 0:
            new_node.set_next(self._head)
            self._head = new_node
            return

        current = self._head
        previous = None
        index = 0

        while index < position and current is not None:
            previous = current
            current = current.get_next()
            index += 1

        if previous is None:
            self._head = new_node
            return

        new_node.set_next(current)
        previous.set_next(new_node)

    def slice(self, start, stop):
        new_list = UnsortedList()
        current = self._head
        index = 0

        while current is not None:
            if start <= index < stop:
                new_list.append(current.get_data())
            current = current.get_next()
            index += 1
        return new_list