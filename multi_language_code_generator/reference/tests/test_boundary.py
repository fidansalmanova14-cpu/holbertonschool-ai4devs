import unittest
from reference.processor import TransactionProcessor
class TestBoundary(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 6, "amount": 5000.0, "category": "Rent"}])
        self.assertEqual(res["flagged_ids"], [])
if __name__ == "__main__": unittest.main()
