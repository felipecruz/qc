#include <stdio.h>

int read(int) {
    return 0;
}

int other(void) {
    char *a;

    a = read();

    return 1;
}

int main(int argc, char *argv[]) {

    int t;

    t = read(0);

    return 0;
}
