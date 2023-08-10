%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex(void);
int yyerror(const char* msg);  // Add this declaration
%}

%union {
    char* comment;
}

%token <comment> COMMENT_START
%token <comment> COMMENT_END
%token <comment> COMMENT_LINE
%token <comment> OTHER

%start input

%%

input: /* empty */ | input line | program ;

line: COMMENT_START { printf("Multiline Comment: %s\n", $1); free($1); }
    | COMMENT_END { printf("End of Multiline Comment: %s\n", $1); free($1); }
    | COMMENT_LINE { printf("Single Line Comment: %s\n", $1); free($1); }
    ;

program : comment { printf("Accepted\n"); exit(EXIT_SUCCESS); }
        | COMMENT_LINE { printf("Single Line Comment: %s\n", $1); free($1); exit(EXIT_SUCCESS); }
        | COMMENT_START { printf("Multiline Comment: %s\n", $1); free($1); exit(EXIT_SUCCESS); }
        | COMMENT_END { printf("End of Multiline Comment: %s\n", $1); free($1); exit(EXIT_SUCCESS); }
        | OTHER { yyerror("Syntax error"); exit(EXIT_FAILURE); }
        ;

comment : COMMENT_START { printf("Multiline Comment: %s\n", $1); free($1); }
        | COMMENT_LINE { printf("Single Line Comment: %s\n", $1); free($1); }
        ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char* msg) {
    fprintf(stderr, "Error: %s\n", msg);
    return 0;
}