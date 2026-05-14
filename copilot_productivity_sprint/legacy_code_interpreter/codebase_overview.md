# Codebase Overview - Legacy jQuery (v1.x)

## Age
The project started in 2006. The v1.x branch was maintained until around 2016, specifically focusing on legacy browser support (like IE6/7/8).

## Size
Approximately 9,000 - 10,000 LOC (Lines of Code) in a single core file (uncompressed).

## Main Dependencies
- No external runtime dependencies (it is a standalone library).
- Grunt (for build processes).
- QUnit (for testing).

## Known Issues or Pain Points
- **Cross-browser hacks:** The code is filled with specific "if/else" logic to handle bugs in old Internet Explorer versions.
- **Global Scope:** Extensive use of the global namespace which can lead to conflicts.
- **Synchronous AJAX:** Heavy reliance on older AJAX patterns that are now considered sub-optimal compared to Fetch API.
- **Complexity:** Highly nested functions and complex regex patterns for DOM selection that are hard to read.
