import unittest
from reference.processor import TransactionProcessor
class Test07(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertEqual(tp.process([{'id':6,'amount':5000,'category':'Valid'}])['flagged_ids'], [])
if __name__ == '__main__': unittest.main()
