import unittest
from reference.processor import TransactionProcessor
class Test04(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertIn(3, tp.process([{'id':3,'amount':50,'category':'Unknown'}])['flagged_ids'])
if __name__ == '__main__': unittest.main()
