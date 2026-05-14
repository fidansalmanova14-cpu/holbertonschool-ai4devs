function printNumbers() {
    for (var i = 0; i < 3; i++) {
        setTimeout(function() {
            console.log(i); // Səhv: Həmişə 3 çap edir
        }, 100);
    }
}
printNumbers();
