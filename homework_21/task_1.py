import logging

logging.basicConfig(filename = 'errors.log', level = logging.INFO)

class OpenFiles:
    def __init__(self, filename, mode = 'r', start = 0):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.value = start

    def __enter__(self):
        logging.info(f'File open {self.filename}')
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logging.error(f'Error in file {self.filename}', exc_info = True)

        if self.file:
            logging.info(f'File closed {self.filename}')
            self.file.close()

        return exc_type is None

    def increment(self):
        self.value += 1
        return self.value

    def read(self):
        data = self.file.read()
        self.increment()
        return data