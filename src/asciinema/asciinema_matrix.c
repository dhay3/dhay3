#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define T "\x1b["
#define H 1999
#define e printf

int matrix[H + 1];

int main() {
    int M, a, t, r;

    for (a = 0; a <= H; a++)
        matrix[a] = a < 80 ? rand() % 48 : 0;

    while (1) {
        for (M = 0; M <= H; M++) {
            if (M < 80) {
                a = matrix[M] = (matrix[M] + 1) % 48;
                if (a < 24) {
                    matrix[(a + 1) * 80 + M] = (rand() & 63) * 16 | 15;
                }
            } else {
                a = matrix[M] & 15;
                t = a > 7 ? (a - 8) * 32 : 0;
                r = a < 8 ? (a << 5) + 31 : 255;
                e(T "38;2;%d;%d;%dm%c", t, r, t, 32 + matrix[M] / 16);
                if (M % 80 == 79) {
                    e(T "0m\n" T "48;2;0;32;0m");
                }
                a = a ? a - 1 : a;
                matrix[M] = (matrix[M] & 240) | a;
            }
        }
        e(T "24A");
        usleep(32 * H);
    }

    return 0;
}