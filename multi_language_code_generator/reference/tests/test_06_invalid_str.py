import unittest
from reference.processor import TransactionProcessor
class Test06(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 5, "amount": "abc", "category": "Food"}])
        self.assertEqual(res["total_balance"], 0.0)
if __name__ == "__main__": unittest.main()
