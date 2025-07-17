//Wargame site URL: https://dreamhack.io/wargame/challenges/21

#include <stdio.h>

int ROR1(int val, int r){
    r %= 8;
    return (val >> r) | (val << (8 - r));
}

int main() {
    int byte_140003000[] ={
        82, 223, 179,  96, 241, 139,  28, 181,  87, 209, 159,  56,  75,  41, 217,  38, 
        127, 201, 163, 233, 83,  24,  79, 184, 106, 203, 135,  88,  91,  57, 30,   0
    };
    int flag[33]={0,};

    for (int i = 0; i < 31; i++){
        int tmp = byte_140003000[i] ^ i;
        flag[i] = ROR1(tmp, i & 7);
    }

    printf("FLAG: DH{");
    for(int i=0;i<32;i++)printf("%c",flag[i]);
    printf("}");
    
    return 0;
}
