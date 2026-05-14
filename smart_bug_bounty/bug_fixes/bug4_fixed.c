#include <stdio.h>
#include <string.h>

int main() {
    char destination[50]; // Fixed: Increased buffer size to accommodate the message
    char *source = "This is a very long string that is now safe";

    // Fixed: Using safer copy and checking size
    if (strlen(source) < sizeof(destination)) {
        strcpy(destination, source);
        printf("Result: %s\n", destination);
    } else {
        printf("Error: Buffer too small\n");
    }
    
    return 0;
}
