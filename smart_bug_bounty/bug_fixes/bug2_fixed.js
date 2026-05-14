function delayedNumbers() {
    console.log("Starting countdown...");

    // Fixed: Changed 'var' to 'let' to ensure block scoping for each iteration
    for (let i = 0; i < 3; i++) {
        setTimeout(function() {
            console.log("Number: " + i);
        }, 500);
    }
}
delayedNumbers();
