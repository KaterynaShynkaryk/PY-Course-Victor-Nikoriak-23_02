import unittest
from homework_21.task_1 import OpenFiles


class TestOpenFile(unittest.TestCase):
    def test_read_file(self):
        with OpenFiles('test.txt', 'r') as f:
            data = f.read()

        self.assertGreater(len(data), 0)
        self.assertIsInstance(data, str)


    def test_counter(self):
        with OpenFiles('test.txt', 'r') as f:
            f.read()
            f.read()

        self.assertEqual(f.value, 2)

    def test_file_closed(self):
        with OpenFiles('test.txt', 'r') as f:
            f.read()

        self.assertTrue(f.file.closed)

    def test_error_handling(self):
        with OpenFiles('test.txt') as f:
            with self.assertRaises(ZeroDivisionError):
                1 / 0
        self.assertTrue(f.file.closed)




if __name__ == "__main__":
    unittest.main()
