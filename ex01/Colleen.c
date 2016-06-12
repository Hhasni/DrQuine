#include <stdio.h>
void prout(){}
/*
	toto
*/
int main()
{
	char*a="#include <stdio.h>%cvoid prout(){}%c/*%c%ctoto%c*/%cint main()%c{%c%cchar*a=%c%s%c;%c%cprintf(a,10,10,10,9,10,10,10,10,9,34,a,34,10,9,10,9,10,9,10,9,9,10,9,10,10);%c%cprout();%c%c/*%c%c%cpouet%c%c*/%c}%c";
	printf(a,10,10,10,9,10,10,10,10,9,34,a,34,10,9,10,9,10,9,10,9,9,10,9,10,10);
	prout();
	/*
		pouet
	*/
}
