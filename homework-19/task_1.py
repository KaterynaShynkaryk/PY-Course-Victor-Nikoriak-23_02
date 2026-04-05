def with_index(iterable, start = 0):
    for i in iterable:
        yield start, i
        start += 1


items = ['a', 'b', 'c']

result = list(with_index(items, start=1))

print(result)