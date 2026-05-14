# Architecture Plan - Smart Expense Categorizer

## Technical Stack
- **Frontend**: React.js with Tailwind CSS (for rapid UI development).
- **AI Integration**: OpenAI API (GPT-4o mini) for NLP-based transaction categorization.
- **State Management**: React Hooks (useState, useMemo) for handling transaction lists locally.
- **Deployment**: Vercel for the frontend and demo.

## High-Level Flow
1. **Frontend** captures raw text input from the user.
2. **AI Service** receives descriptions and returns a JSON list of categorized items.
3. **Application Logic** aggregates totals and calculates the breakdown.
4. **UI** renders a Pie Chart and a detailed table of results.
