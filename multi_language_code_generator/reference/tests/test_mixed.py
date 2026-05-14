import unittest
from reference.processor import TransactionProcessor
class TestMixed(unittest.TestCase):
    def test_run(self):
        data = [{"id": 8, "amount": 10.0, "category": "X"}, {"id": 9, "amount": 7000, "category": "Y"}]
        self.assertEqual(len(TransactionProcessor().process(data)["flagged_ids"]), 1)
if __name__ == "__main__": unittest.main()
