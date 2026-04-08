import unittest
from homework_20.task_2 import phonebook
import json
import os

class TestPhonebook(unittest.TestCase):
    def test_save_and_load(self):
        data = [{"name": "Max", "phone": "999"}]
        filename = "test.json"

        phonebook.save_phonebook(filename, data)
        result = phonebook.load_phonebook(filename)

        self.assertEqual(result, data)
        os.remove(filename)

    def test_empty_save(self):
        data = []
        filename = "test.json"

        phonebook.save_phonebook(filename, data)
        result = phonebook.load_phonebook(filename)

        self.assertEqual(result, data)
        os.remove(filename)

    def test_many_contacts(self):
        data = [{"name": f'User{i}', "phone": str(100000000000 + i)} for i in range(100)]
        filename = "test.json"

        phonebook.save_phonebook(filename, data)
        result = phonebook.load_phonebook(filename)

        self.assertEqual(result, data)
        os.remove(filename)

    def test_error_load(self):
        with open('bad.json', 'w', encoding='utf-8') as f:
            f.write('{not a valid json}')

        with self.assertRaises(json.JSONDecodeError):
            phonebook.load_phonebook('bad.json')

        os.remove('bad.json')

    def overwrite_file(self):
        filename = "test_overwrite.json"

        phonebook.save_phonebook(filename, [{"name": "A", "phone": "111"}])
        phonebook.save_phonebook(filename, [{"name": "B", "phone": "222"}])

        result = phonebook.load_phonebook(filename)
        self.assertEqual(result, [{"name": "B", "phone": "222"}])

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()