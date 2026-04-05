def in_range(start, end, step = 1):
    if step == 0:
        raise ValueError('step не може бути 0')

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


result = list(in_range(0, 5, 1))
print(result)