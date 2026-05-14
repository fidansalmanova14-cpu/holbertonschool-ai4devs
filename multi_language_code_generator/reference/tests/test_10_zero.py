import unittest
from reference.processor import TransactionProcessor
class Test10(unittest.TestCase):
    def test_run(self):
        self.assertEqual(TransactionProcessor().process([{"id": 10, "amount": 0}])["processed_count"], 1)
if __name__ == "__main__": unittest.main()
