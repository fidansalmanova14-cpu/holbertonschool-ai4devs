import unittest
from reference.processor import TransactionProcessor
class TestLarge(unittest.TestCase):
    def test_run(self):
        data = [{"id": 7, "amount": 10000.55, "category": "Asset"}]
        self.assertEqual(TransactionProcessor().process(data)["total_balance"], 10000.55)
if __name__ == "__main__": unittest.main()
