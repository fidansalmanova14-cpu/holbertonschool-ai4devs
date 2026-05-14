import unittest
from reference.processor import TransactionProcessor
class Test05(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertIn(4, tp.process([{'id':4,'amount':50}])['flagged_ids'])
if __name__ == '__main__': unittest.main()
