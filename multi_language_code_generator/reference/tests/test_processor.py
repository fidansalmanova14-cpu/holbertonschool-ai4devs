import unittest
from reference.processor import TransactionProcessor

class TestTransactionProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TransactionProcessor()

    def test_empty_input(self):
        self.assertEqual(self.processor.process([]), {"total_balance": 0.0, "flagged_ids": [], "processed_count": 0})

    def test_single_normal(self):
        data = [{"id": 1, "amount": 100.0, "category": "Food"}]
        self.assertEqual(self.processor.process(data)["total_balance"], 100.0)

    def test_high_amount_flag(self):
        data = [{"id": 2, "amount": 6000.0, "category": "Tech"}]
        self.assertIn(2, self.processor.process(data)["flagged_ids"])

    def test_unknown_category_flag(self):
        data = [{"id": 3, "amount": 50.0, "category": "Unknown"}]
        self.assertIn(3, self.processor.process(data)["flagged_ids"])

    def test_missing_category_flag(self):
        data = [{"id": 4, "amount": 50.0}] # Category yoxdur -> Unknown sayılır
        self.assertIn(4, self.processor.process(data)["flagged_ids"])

    def test_invalid_amount(self):
        data = [{"id": 5, "amount": "invalid", "category": "Food"}]
        self.assertEqual(self.processor.process(data)["total_balance"], 0.0)

    def test_multiple_mixed(self):
        data = [
            {"id": 6, "amount": 10.0, "category": "Office"},
            {"id": 7, "amount": 10000.0, "category": "Luxury"}
        ]
        result = self.processor.process(data)
        self.assertEqual(result["total_balance"], 10010.0)
        self.assertIn(7, result["flagged_ids"])

    def test_zero_amount(self):
        data = [{"id": 8, "amount": 0.0, "category": "Service"}]
        self.assertEqual(self.processor.process(data)["processed_count"], 1)

    def test_boundary_amount(self):
        data = [{"id": 9, "amount": 5000.0, "category": "Tech"}]
        self.assertNotIn(9, self.processor.process(data)["flagged_ids"])

    def test_large_dataset_count(self):
        data = [{"id": i, "amount": 1.0, "category": "Test"} for i in range(100)]
        self.assertEqual(self.processor.process(data)["processed_count"], 100)

if __name__ == '__main__':
    unittest.main()
