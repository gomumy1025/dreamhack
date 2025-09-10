//Wargame link: https://dreamhack.io/wargame/challenges/17

#include <iostream>
#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

// Data from IDA
// 49 6C 67 74 63 6F 42 6F 78 69 69 6D 88
// 96 94 9F 8D AD 45 90 45 00 00 00 00 00

int main() {
    vector<uint8_t> s={
        0x49, 0x6C, 0x67, 0x74, 0x63, 0x6F, 0x42, 0x6F, 0x78, 0x69, 0x69, 0x6D,
        0x99, 0x96, 0x94, 0x9F, 0x8D, 0xAD, 0x45, 0x90, 0x45, 0x00
    };

    vector<uint8_t> r;
    // Decrypting
    for(size_t i=0;i<s.size();i++){
        uint8_t t=(s[i]^i)^0x55;
        uint8_t a=~t;
        r.push_back(a);
    }

    // Print result
    for(size_t i=0;i<r.size();i++){
        printf("%c",(int)r[i]);
    }
    return 0;
}
