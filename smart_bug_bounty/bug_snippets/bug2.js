/**
 * Task: Print numbers 0 to 2 with a delay.
 * Intended Behavior:
 * The console should show 0, then 1, then 2.
 */

function delayedNumbers() {
    console.log("Starting countdown...");

    // Bug: 'var' has function scope, not block scope
    // By the time setTimeout runs, 'i' is already 3
    for (var i = 0; i < 3; i++) {
        setTimeout(function() {
            console.log("Number: " + i);
        }, 500);
    }

    console.log("Loop finished (but timeouts are pending).");
}

delayedNumbers();
