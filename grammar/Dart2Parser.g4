parser grammar Dart2Parser;

options { tokenVocab = Dart2Lexer; }

// Početno pravilo
program: functionDeclaration* statement* EOF;

// Deklaracija funkcije - KORISTI POSTOJEĆE TOKENE
functionDeclaration: functionType ID LPAREN parameterList? RPAREN block;
functionType: VOID | INT | DOUBLE | BOOL | STRING; // Koristi postojeće tokene

parameterList: parameter (COMMA parameter)*;
parameter: type ID;

// Naredbe
statement:
    variableDeclaration SEMI
    | expressionStatement SEMI
    | ifStatement
    | forStatement
    | whileStatement
    | doWhileStatement
    | returnStatement SEMI
    | block
    | expression SEMI;

// Izrazi
expression:
    primary
    | expression (PLUS | MINUS | MULT | DIV) expression
    | expression (EQ | NEQ | LT | LTE | GT | GTE) expression
    | expression (AND | OR) expression
    | assignment
    | postfixExpression;

// Postfix izrazi (i++, i--)
postfixExpression: primary (PLUS_PLUS | MINUS_MINUS);

assignment: ID ASSIGN expression;

primary:
    LPAREN expression RPAREN
    | ID
    | literal
    | functionCall;

functionCall: ID LPAREN argumentList? RPAREN;
argumentList: expression (COMMA expression)*;

literal:
    INT_LITERAL
    | DOUBLE_LITERAL
    | BOOL_LITERAL
    | STRING_LITERAL;

variableDeclaration: (VAR | FINAL | type) ID (ASSIGN expression)?;
ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;
forStatement: FOR LPAREN forInitializer? SEMI expression? SEMI forIterator? RPAREN statement;
forInitializer: variableDeclaration | expressionStatement;
forIterator: expressionStatement;
whileStatement: WHILE LPAREN expression RPAREN statement;
doWhileStatement: DO statement WHILE LPAREN expression RPAREN SEMI;
returnStatement: RETURN expression?;
block: LBRACE statement* RBRACE;
type: INT | DOUBLE | BOOL | STRING | VOID;
expressionStatement: expression;