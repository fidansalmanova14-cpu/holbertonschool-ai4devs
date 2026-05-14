#include <stdio.h>
#include <string.h>

/*
 * Task: Safe string copying.
 * Fixed Version: Prevents buffer overflow.
 */

int main() {
    char destination[50]; // Increased buffer size
    const char *source = "This string is now safely stored";

    printf("Source: %s\n", source);

    // Fixed: Checking bounds before copying
    if (strlen(source) < sizeof(destination)) {
        strcpy(destination, source);
        printf("Success! Result: %s\n", destination);
    } else {
        fprintf(stderr, "Error: Buffer overflow prevented!\n");
        return 1;
    }

    return 0;
}
