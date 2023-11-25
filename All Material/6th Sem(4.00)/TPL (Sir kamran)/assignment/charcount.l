%{
#include<stdio.h>
int lines=0,words=0,c_letters=0,num=0,spl_chr=0,total=0,space=0;
%}

%%
\n { lines++; }
[\t ' ']+ { space++; }
[0-9] { num++; c_letters++; }
[0-9]+ { num += yyleng; }
[a-zA-Z]+ { words++; c_letters += yyleng; }
. { spl_chr++; }

%%

int main()
{
	yyin=fopen("input.txt","r");
	yylex();
	total=c_letters+num+spl_chr;
	printf("\nFile contents...\n");
	printf("\n\t%d line",lines+1);
	printf("\n\t%d words",words);
	printf("\n\t%d characters (alphabets)",c_letters);
	printf("\n\t%d Digits",num);
	printf("\n\t%d Special Characters",spl_chr);
	printf("\n\t%d Spaces",space);
	printf("\n\t Total %d characters",total);
}
int yywrap()
{
	return 1;
}