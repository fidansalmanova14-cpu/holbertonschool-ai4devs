# System Architecture - EcoTrack

## High-Level Overview
The MVP follows a modern Single Page Application (SPA) architecture with a decoupled backend.

- **Frontend**: React.js with Tailwind CSS for a responsive UI.
- **State Management**: React Context API to manage local activity logs.
- **Backend (Mock/API)**: Node.js Express server to handle carbon calculations and Eco-tip generation (simulated with AI logic).
- **Storage**: LocalStorage for the MVP to ensure data persistence without complex Auth.

## Component Diagram
1. **ActivityForm**: Captures user input.
2. **ImpactEngine**: Logic layer that converts activities to CO2 grams.
3. **Dashboard**: Visualization layer using Chart.js or simple CSS bars.
4. **TipEngine**: Service that provides daily suggestions.
