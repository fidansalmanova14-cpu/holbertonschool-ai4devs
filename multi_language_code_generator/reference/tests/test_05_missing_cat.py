import unittest
from reference.processor import TransactionProcessor
class Test05(unittest.TestCase):
    def test_run(self):
        res = TransactionProcessor().process([{"id": 4, "amount": 50.0}])
        self.assertIn(4, res["flagged_ids"])
if __name__ == "__main__": unittest.main()
