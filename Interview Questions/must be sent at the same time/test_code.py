import unittest

from code import TimeForDay

class TestTimeForDay(unittest.TestCase):
    def test_object_create(self):
        return TimeForDay()

    def test_api_call(self):
        self.assertEqual(self.test_object_create().api_call(), True)

    def test_input_from_user(self):
        self.assertEqual(self.test_object_create().input_from_user(), None)

    def test_start_method(self):
        self.assertEqual(self.test_object_create().start_method(), None)


if __name__ == "__main__":
    unittest.main()

"""
Output:
/Users/chetan/Personal/Project/pythonBasic/venv/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py --path /Users/chetan/Personal/Project/pythonBasic/must be sent at the same time/test_code.py 
Testing started at 15:13 ...
Launching unittests with arguments python -m unittest /Users/chetan/Personal/Project/pythonBasic/must be sent at the same time/test_code.py in /Users/chetan/Personal/Project/pythonBasic/must be sent at the same time

enter timestamps you want to add (HH:MM:SS). or press 'N'.enter timestamps you want to add (HH:MM:SS). or press 'N'.Cron job running...
API Call 1 in process for 13:45:09.
API Call 2 in process for 13:45:09.
API Call 3 in process for 13:45:09.


Ran 4 tests in 5.389s

OK

Process finished with exit code 0
"""