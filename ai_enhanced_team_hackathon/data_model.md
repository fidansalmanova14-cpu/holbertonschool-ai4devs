# Data Model - Smart Expense Categorizer

## Entity 1: Transaction
- **id**: UUID
- **description**: String (Raw text from bank)
- **amount**: Decimal
- **date**: Date
- **category_id**: Foreign Key (References Category)

## Entity 2: Category
- **id**: Integer
- **name**: String (e.g., Food, Rent, Transport)
- **icon**: String (Optional UI icon name)
- **is_custom**: Boolean

## Entity 3: SummaryReport
- **id**: UUID
- **total_amount**: Decimal
- **generated_at**: DateTime
- **category_breakdown**: JSON (Map of category names to sums)
