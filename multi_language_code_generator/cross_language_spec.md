# Cross-Language Specification - Transaction Processor

## Algorithm Description
The algorithm processes a list of financial transactions to calculate the total balance and identify flagged transactions. A transaction is flagged if its amount exceeds $5000 or if the transaction category is "Unknown".

## Input Format
- **Format**: JSON list of objects.
- **Fields**: 
  - `id`: Unique integer identifier.
  - `amount`: Float representing the transaction value.
  - `category`: String representing the type of expense.
  - `date`: String in ISO 8601 format.

## Output Format
- **Format**: JSON object.
- **Fields**:
  - `total_balance`: Sum of all valid transaction amounts.
  - `flagged_ids`: Array of IDs that met the flagging criteria (amount > 5000 OR category == "Unknown").
  - `processed_count`: Total number of objects in the input list.

## Edge Cases
- **Empty List**: Should return a balance of 0.0 and empty flagged list.
- **Missing Fields**: If category is missing, it must default to "Unknown" and be flagged.
- **Non-Numeric Data**: If amount is not a valid number, the record should be ignored or treated as 0.0.

## Test Cases
1. **Empty Input**:
   - Input: `[]`
   - Output: `{"total_balance": 0.0, "flagged_ids": [], "processed_count": 0}`
2. **Normal Transaction**:
   - Input: `[{"id": 1, "amount": 100.0, "category": "Food", "date": "2024-01-01"}]`
   - Output: `{"total_balance": 100.0, "flagged_ids": [], "processed_count": 1}`
3. **High Amount Flagging**:
   - Input: `[{"id": 2, "amount": 7500.0, "category": "Tech", "date": "2024-01-02"}]`
   - Output: `{"total_balance": 7500.0, "flagged_ids": [2], "processed_count": 1}`
4. **Unknown Category Flagging**:
   - Input: `[{"id": 3, "amount": 50.0, "category": "Unknown", "date": "2024-01-03"}]`
   - Output: `{"total_balance": 50.0, "flagged_ids": [3], "processed_count": 1}`
5. **Combined Complex Scenario**:
   - Input: `[{"id": 4, "amount": 10.0, "category": "Office"}, {"id": 5, "amount": 6000.0, "category": "Travel"}]`
   - Output: `{"total_balance": 6010.0, "flagged_ids": [5], "processed_count": 2}`
