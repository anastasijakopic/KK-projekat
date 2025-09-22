lexer grammar Dart2Lexer;

// KLJUČNE RIJEČI
ABSTRACT    : 'abstract';
AS          : 'as';
ASSERT      : 'assert';
BREAK       : 'break';
CASE        : 'case';
CATCH       : 'catch';
CLASS       : 'class';
CONST       : 'const';
CONTINUE    : 'continue';
DEFAULT     : 'default';
DO          : 'do';
ELSE        : 'else';
ENUM        : 'enum';
EXTENDS     : 'extends';
FALSE       : 'false';
FINAL       : 'final';
FINALLY     : 'finally';
FOR         : 'for';
IF          : 'if';
IN          : 'in';
IS          : 'is';
NEW         : 'new';
NULL        : 'null';
RETHROW     : 'rethrow';
RETURN      : 'return';
SUPER       : 'super';
SWITCH      : 'switch';
THIS        : 'this';
THROW       : 'throw';
TRUE        : 'true';
TRY         : 'try';
VAR         : 'var';
VOID        : 'void';
WHILE       : 'while';
WITH        : 'with';
YIELD       : 'yield';
PRINT       : 'print';
ON          : 'on';

// PRIMITIVNI TIPOVI
INT_TYPE    : 'int';
DOUBLE_TYPE : 'double';
STRING_TYPE : 'String';
BOOL_TYPE   : 'bool';
LIST_TYPE   : 'List';
MAP_TYPE    : 'Map';
SET_TYPE    : 'Set';
DYNAMIC     : 'dynamic';

// SIMBOLI
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
SEMI        : ';';
COLON       : ':';
COMMA       : ',';
DOT         : '.';
QMARK       : '?';
ARROW       : '=>';
AT          : '@';

// OPERACIJE
PLUSEQ      : '+=';
MINUSEQ     : '-=';
MULEQ       : '*=';
DIVEQ       : '/=';
MODEQ       : '%=';

PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
INC         : '++';
DEC         : '--';

EQ          : '==';
NEQ         : '!=';
LT          : '<';
GT          : '>';
LEQ         : '<=';
GEQ         : '>=';

ASSIGN      : '=';

AND         : '&&';
OR          : '||';
NOT         : '!';

// IDENTIFIKATORI I LITERALNE VRIJEDNOSTI
ID              : [a-zA-Z_$][a-zA-Z0-9_$]*;
INT_LITERAL     : [0-9]+;
DOUBLE_LITERAL  : [0-9]+ '.' [0-9]* ([eE][+-]?[0-9]+)?
                | '.' [0-9]+ ([eE][+-]?[0-9]+)?;
STRING          : '"' ( ~["\\\r\n] | '\\' . )* '"'
                | '\'' ( ~['\\\r\n] | '\\' . )* '\'';

// KOMENTARI I PRAZNINE
LINE_COMMENT    : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip;
WS              : [ \t\r\n]+ -> skip;
