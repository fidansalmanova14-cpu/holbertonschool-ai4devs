import unittest
from reference.processor import TransactionProcessor
class Test11(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 11, "amount": None, "category": "Food"}])
        self.assertEqual(res["total_balance"], 0.0)
if __name__ == "__main__": unittest.main()
