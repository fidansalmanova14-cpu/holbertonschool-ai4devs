# Cross-Language Specification - Transaction Processor

## 1. Algorithm Description
The algorithm processes a list of financial transactions to calculate the total balance and identify flagged transactions. A transaction is flagged if its amount exceeds $5000 or if the transaction category is "Unknown".

## 2. Input Format
- **Format**: JSON list of objects.
- **Fields**: 
  - `id` (integer)
  - `amount` (float)
  - `category` (string)
  - `date` (string, ISO 8601)

## 3. Output Format
- **Format**: JSON object.
- **Fields**:
  - `total_balance`: Sum of all transaction amounts.
  - `flagged_ids`: List of transaction IDs that met the flagging criteria.
  - `processed_count`: Total number of transactions processed.

## 4. Edge Cases
- **Empty list**: Should return 0 balance and empty flagged list.
- **Malformed amounts**: Non-numeric strings should be ignored or treated as 0.
- **Missing fields**: If `category` is missing, treat as "Unknown" and flag the transaction.

## 5. Test Cases
1. **Empty Input**: `[]` -> `{"total_balance": 0.0, "flagged_ids": [], "processed_count": 0}`
2. **Standard Processing**: `[{"id": 1, "amount": 100.5, "category": "Food"}]` -> `{"total_balance": 100.5, "flagged_ids": [], "processed_count": 1}`
3. **High Amount Flag**: `[{"id": 2, "amount": 6000, "category": "Tech"}]` -> `{"flagged_ids": [2]}`
4. **Unknown Category Flag**: `[{"id": 3, "amount": 50, "category": "Unknown"}]` -> `{"flagged_ids": [3]}`
5. **Mixed Input**: Multiple transactions containing both valid and flagged cases.
