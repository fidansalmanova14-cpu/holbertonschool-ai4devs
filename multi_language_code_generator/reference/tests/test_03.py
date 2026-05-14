import unittest
from reference.processor import TransactionProcessor
class Test03(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertIn(2, tp.process([{'id':2,'amount':6000,'category':'A'}])['flagged_ids'])
if __name__ == '__main__': unittest.main()
