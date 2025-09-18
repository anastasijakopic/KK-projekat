parser grammar Dart2Parser;

options { tokenVocab = Dart2Lexer; }

// Početno pravilo
program: statement* EOF;

// Naredbe
statement:
    variableDeclaration SEMI
    | expressionStatement SEMI
    | ifStatement
    | forStatement
    | whileStatement
    | doWhileStatement
    | returnStatement SEMI
    | block;

// Deklaracija promenljive
variableDeclaration: (VAR | FINAL | type) ID (ASSIGN expression)?;

// Izraz naredba
expressionStatement: expression;

// If naredba
ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;

// For petlja
forStatement: FOR LPAREN forInitializer? SEMI expression? SEMI forIterator? RPAREN statement;

forInitializer: variableDeclaration | expressionStatement;
forIterator: expressionStatement;

// While petlja
whileStatement: WHILE LPAREN expression RPAREN statement;

// Do-while petlja
doWhileStatement: DO statement WHILE LPAREN expression RPAREN SEMI;

// Return naredba
returnStatement: RETURN expression?;

// Blok
block: LBRACE statement* RBRACE;

// Tipovi
type: INT | DOUBLE | BOOL | STRING | VOID;

// Izrazi
expression:
    primary
    | expression (PLUS | MINUS | MULT | DIV) expression
    | expression (EQ | NEQ | LT | LTE | GT | GTE) expression
    | expression (AND | OR) expression
    | assignment;

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