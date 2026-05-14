# Cross-Language Specification - Transaction Processor

## 1. Algorithm Description
The algorithm processes a list of financial transactions to calculate the total balance and identify flagged transactions. A transaction is flagged if its amount exceeds $5000 or if the transaction category is "Unknown".

## 2. Input Format
- **Format**: JSON list of objects.
- **Fields**: `id` (int), `amount` (float), `category` (string), `date` (ISO 8601).

## 3. Output Format
- **Format**: JSON object.
- **Fields**: `total_balance`, `flagged_ids`, `processed_count`.

## 4. Edge Cases
- Empty input list.
- Missing category (default to "Unknown").
- Non-numeric amount values.

## 5. Test Cases
1. **Empty**: `[]` -> balance: 0.0, flagged: []
2. **Normal**: `[{"id": 1, "amount": 100.0, "category": "Food"}]` -> balance: 100.0, flagged: []
3. **High Amount**: `[{"id": 2, "amount": 6000.0, "category": "Tech"}]` -> flagged: [2]
4. **Unknown Cat**: `[{"id": 3, "amount": 50.0, "category": "Unknown"}]` -> flagged: [3]
5. **Mixed**: Multiple items with mixed criteria.
