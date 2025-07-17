//Wargame site URL: https://dreamhack.io/wargame/challenges/19

#include <stdio.h>

//Data from IDA(Hex)
//AD D8 CB CB 9D 97 CB C4 92 A1 D2 D7 D2 D6 A8 A5 DC C7 AD A3 A1 98 4C 00 00 00 00 00 00 00 00 00

//Data from IDA(Decimal)
//173, 216, 203, 203, 157, 151, 203, 196, 
//146, 161, 210, 215, 210, 214, 168, 165, 
//220, 199, 173, 163, 161, 152,  76,   0,   
//0,   0,   0,   0,   0,   0,    0,   0

int main() {
    int data[33]={
    173, 216, 203, 203, 157, 151, 203, 196,
    146, 161, 210, 215, 210, 214, 168, 165,
    220, 199, 173, 163, 161, 152,  76,   0,
    0,   0,   0,   0,   0,   0,    0,   0};
    int flag[33]={0,};

    for(int i=23;i>=0;i--){
        flag[i]=data[i]-flag[i+1];
        //printf("%d=%d-%d\n",flag[i],data[i],flag[i+1]);
    }

    printf("\n");

    for(int i=0;i<24;i++){
        printf("%c",flag[i]);
    }
    printf("\n\n");

    printf("FLAG: DH{");
    for(int i=0;i<24;i++){
        printf("%c",flag[i]);
    }
    printf("}");
    return 0;
}
