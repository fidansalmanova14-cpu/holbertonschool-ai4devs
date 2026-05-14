#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    // Səhv: 10-dan çox xarakter daxil edildikdə yaddaş xətası verir
    strcpy(buffer, "This string is too long for the buffer");
    printf("%s\n", buffer);
    return 0;
}
