import unittest
from reference.processor import TransactionProcessor
class Test04(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 3, "amount": 50.0, "category": "Unknown"}])
        self.assertIn(3, res["flagged_ids"])
if __name__ == "__main__": unittest.main()
