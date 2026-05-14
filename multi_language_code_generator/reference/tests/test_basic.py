import unittest
from reference.processor import TransactionProcessor
class TestBasic(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 1, "amount": 100.0, "category": "Food"}])
        self.assertEqual(res["total_balance"], 100.0)
if __name__ == "__main__": unittest.main()
