import unittest
from reference.processor import TransactionProcessor
class Test01(unittest.TestCase):
    def test_run(self):
        self.assertEqual(TransactionProcessor().process([]), {"total_balance": 0.0, "flagged_ids": [], "processed_count": 0})
if __name__ == "__main__": unittest.main()
