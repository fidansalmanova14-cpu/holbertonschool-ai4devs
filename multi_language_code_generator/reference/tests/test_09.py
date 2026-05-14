import unittest
from reference.processor import TransactionProcessor
class Test09(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertEqual(len(tp.process([{'id':8,'amount':10,'category':'Valid'},{'id':9,'amount':9000,'category':'Valid'}])['flagged_ids']), 1)
if __name__ == '__main__': unittest.main()
