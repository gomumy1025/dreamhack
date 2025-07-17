//Wargame site URL: https://dreamhack.io/wargame/challenges/22

#include <stdio.h>

int main() {
    int byte_140003000[] ={
    172, 243,  12,  37, 163,  16, 183,  37,  22, 198, 183, 188,   7,  37,   2, 213, 
    198,  17,   7, 197, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 0,   0
    };
    int flag[33]={0,};

    
    printf("FLAG: DH{");
    for(int i=0;i<22;i++){
        for(int k=0;k<128;k++){
            int j=k;
            j*=-5;
            while(j<0 || j>256)j+=256;
            if(j==byte_140003000[i])printf("%c",k);
        }
    }
    printf("}");
    
    return 0;
}
