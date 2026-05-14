import unittest
from reference.processor import TransactionProcessor
class Test02(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertEqual(tp.process([{'id':1,'amount':100,'category':'A'}])['total_balance'], 100.0)
if __name__ == '__main__': unittest.main()
