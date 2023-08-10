%{
#include "comment.tab.h"
%}

%option noyywrap

%%
"/*"        { yylval.comment = strdup(yytext); return COMMENT_START; }
"*/"        { yylval.comment = strdup(yytext); return COMMENT_END; }
"//".*      { yylval.comment = strdup(yytext); return COMMENT_LINE; }
.           { yylval.comment = strdup(yytext); return OTHER; }
%%