//Wargame link: http://dreamhack.io/wargame/challenges/18

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

//Data from IDA
//24 27 13 C6 C6 13 16 E6 47 F5 26 96 47 F5 46 27 13 26 26 C6 56 F5 C3 C3 F5 E3 E3 00 00 00 00 00

int main() {
    vector<uint8_t>s={
    0x24, 0x27, 0x13, 0xC6, 0xC6, 0x13, 0x16, 0xE6, 0x47, 0xF5, 0x26, 0x96, 0x47, 0xF5, 0x46, 0x27, 
    0x13, 0x26, 0x26, 0xC6, 0x56, 0xF5, 0xC3, 0xC3, 0xF5, 0xE3, 0xE3, 0x00, 0x00, 0x00, 0x00, 0x00
    };

    vector<uint8_t>r;
    for(size_t i=0;i<s.size();i++){
        //uint_8 t = ((s[i] & 0x0F) << 4) | ((s[i] & 0xF0) >> 4);
        r.push_back(((s[i] & 0x0F) << 4) | ((s[i] & 0xF0) >> 4));
    }

    for(size_t i=0;i<r.size();i++){
        printf("%c",r[i]);
    }
    return 0;
}
