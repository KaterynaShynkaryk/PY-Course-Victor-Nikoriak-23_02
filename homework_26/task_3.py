''' Реалізувати in (__contains__) та len (__len__) методи для HashTable '''

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash(self, key):
        return len(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        return self.table[index][1]

    def __contains__(self, key):
        index = self._hash(key)
        return self.table[index] is not None and self.table[index][0] == key

    def __len__(self):
        count = 0
        for item in self.table:
           if item is not None:
               count += 1
        return count