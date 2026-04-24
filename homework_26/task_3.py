''' Реалізувати in (__contains__) та len (__len__) методи для HashTable '''

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def put(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)

        if self.table[index] is None:
            return None

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

    def __contains__(self, key):
        index = self._hash(key)

        if self.table[index] is None:
            return False

        for k, _ in self.table[index]:
            if k == key:
                return True

        return False

    def __len__(self):
        count = 0

        for bucket in self.table:
           if bucket is not None:
               count += len(bucket)

        return count