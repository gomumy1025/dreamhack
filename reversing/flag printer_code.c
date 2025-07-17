// Wargame problem site: https://dreamhack.io/wargame/challenges/1867

#include <stdio.h>

int main() {
    char c[6]="&-17";
    for(int i=0;i<4;i++){
        for(int j=33;j<127;j++){
            int k=c[i];
            if((j^66)==k)printf("%c",j);
        }
    }
    return 0;
}
