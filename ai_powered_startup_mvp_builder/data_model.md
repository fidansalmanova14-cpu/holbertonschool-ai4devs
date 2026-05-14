# Data Model - EcoTrack

## Entity 1: Activity
- **id**: UUID (Unique Identifier)
- **type**: String (e.g., 'transport', 'food', 'energy')
- **value**: Float (e.g., distance in km or weight in kg)
- **timestamp**: DateTime
- **co2_impact**: Float (calculated value in grams)

## Entity 2: EcoTip
- **id**: Integer
- **category**: String
- **content**: Text
- **is_daily_featured**: Boolean

## Entity 3: UserProfile (Local)
- **id**: UUID
- **preferences**: JSON (e.g., metric vs imperial units)
- **total_saved_co2**: Float
