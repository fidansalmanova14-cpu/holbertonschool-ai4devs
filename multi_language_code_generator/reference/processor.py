import json

class TransactionProcessor:
    def __init__(self):
        self.flag_limit = 5000.0

    def process(self, transactions):
        if not isinstance(transactions, list):
            return {"total_balance": 0.0, "flagged_ids": [], "processed_count": 0}
        total_balance = 0.0
        flagged_ids = []
        processed_count = 0
        for tx in transactions:
            processed_count += 1
            try:
                raw_val = tx.get('amount')
                amount = float(raw_val) if raw_val is not None else 0.0
            except (ValueError, TypeError):
                amount = 0.0
            total_balance += amount
            category = tx.get('category', 'Unknown')
            tx_id = tx.get('id')
            if amount > self.flag_limit or category == "Unknown" or category is None:
                if tx_id is not None:
                    flagged_ids.append(tx_id)
        return {"total_balance": round(total_balance, 2), "flagged_ids": flagged_ids, "processed_count": processed_count}
