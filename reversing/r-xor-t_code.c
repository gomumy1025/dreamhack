//Wargame site URL: https://dreamhack.io/wargame/challenges/901

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int main(void) {
    char result2[70] = "C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q";  //Actual length: 64
    char result[70], rot[70], input[70] = {'?',};
    for (int i = 0; i < 64; i++) {
        result[i] = result2[i] ^ 3;
    }


    rot[0] = result[63];    //byte_413F = rot[0] partial inverse operation

    for (int i = 1; i < 63; i++) {
        rot[63 - i] = result[i];
    }

    rot[63] = result[0];    //result[0] = byte_40DF partial inverse operation

    for (int i = 0; i < 64; i++) {
        input[i] = (rot[i] - 13 + 256) % 256;
    }

    for (int i = 0; i < 64; i++) {
        printf("%c", input[i]);
    }
    printf("\n\n");

    printf("Done.. FLAG IS DH{%s}", input);
    printf("\n\n");
    return 0;
}
