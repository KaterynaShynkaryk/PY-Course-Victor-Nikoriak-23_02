class OpenFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

def count_lines(file_obj):
    data = file_obj.read()
    return len(data.splitlines())

import pytest

@pytest.fixture
def file_obj():
    with OpenFile('homework_21/test.txt') as f:
        yield f

def test_line_count(file_obj):
    result = count_lines(file_obj)
    assert result > 0