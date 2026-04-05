class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __getitem__(self, index):
        return self.iterable[index]

    def __iter__(self):
        self.index = len(self.iterable)
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.iterable[self.index]


my_obj = MyIterator([10, 20, 30])

for x in my_obj:
    print(x)