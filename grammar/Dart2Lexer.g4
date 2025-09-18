lexer grammar Dart2Lexer;

// Ključne reči
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
DO: 'do';
RETURN: 'return';
VAR: 'var';
FINAL: 'final';
BOOL: 'bool';
INT: 'int';
DOUBLE: 'double';
STRING: 'String';
VOID: 'void';

// Operatori
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
ASSIGN: '=';
EQ: '==';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';

// Separatori
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';
DOT: '.';

// Literali
BOOL_LITERAL: 'true' | 'false';
INT_LITERAL: [0-9]+;
DOUBLE_LITERAL: [0-9]+ '.' [0-9]*;
STRING_LITERAL: '"' (~["\\] | '\\' .)* '"';

// Identifikatori
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// Komentari i beline
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;