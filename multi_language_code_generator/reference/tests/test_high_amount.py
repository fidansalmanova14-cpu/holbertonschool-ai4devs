import unittest
from reference.processor import TransactionProcessor
class TestHigh(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 2, "amount": 6000.0, "category": "Tech"}])
        self.assertIn(2, res["flagged_ids"])
if __name__ == "__main__": unittest.main()
