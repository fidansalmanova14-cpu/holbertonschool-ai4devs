import unittest
from reference.processor import TransactionProcessor
class Test08(unittest.TestCase):
    def test_run(self):
        tp = TransactionProcessor()
        self.assertEqual(tp.process([{'id':7,'amount':1000.55,'category':'Valid'}])['total_balance'], 1000.55)
if __name__ == '__main__': unittest.main()
