#include <stdio.h>
#include <string.h>

/*
 * Task: Copy a user-provided message into a fixed-size buffer.
 * Intended Behavior:
 * Securely copy the string "Hello" into a 10-byte buffer.
 */

int main() {
    char destination[10];
    char *source = "This is a very long string that will overflow";

    printf("Source length: %lu\n", strlen(source));
    printf("Destination capacity: 10\n");

    // Bug: strcpy does not check for buffer boundaries
    // This will cause a segmentation fault or memory corruption
    strcpy(destination, source);

    printf("Result: %s\n", destination);
    return 0;
}
