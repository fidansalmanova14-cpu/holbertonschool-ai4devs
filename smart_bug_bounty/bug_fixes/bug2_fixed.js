/**
 * Task: Print numbers 0 to 2 with a delay.
 * Fixed Version: Uses 'let' for block-level scoping.
 */

function delayedNumbers() {
    console.log("Starting countdown with fixed scoping...");

    // Fixed: 'let' creates a new binding for each iteration
    for (let i = 0; i < 3; i++) {
        setTimeout(function() {
            console.log("Fixed Output - Number: " + i);
        }, 500);
    }

    console.log("Timers scheduled successfully.");
}

// Execution
delayedNumbers();
