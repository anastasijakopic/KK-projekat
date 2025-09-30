parser grammar Dart2Parser;

options { tokenVocab=Dart2Lexer; }

// Početni simbol
program: statement* EOF;

// Sve vrste naredbi
statement
    : printStatement
    | varDecl
    | constDecl
    | finalDecl
    | functionDecl
    | ifStatement
    | whileStatement
    | doWhileStatement
    | forStatement
    | tryStatement
    | returnStatement
    | exprStatement
    | block
    | breakStatement
    | continueStatement
    | throwStatement
    | switchStatement
    | typedVarDecl 
    ;

printStatement
    : PRINT LPAREN expression? RPAREN SEMI?
    ;

// Definicija funkcije sa parametrima i opcionalnim tipom
functionDecl
    : (type | VOID)? ID LPAREN parameterList? RPAREN (block | ARROW expression SEMI?)
    ;

parameterList: parameter (COMMA parameter)*;
parameter: type ID 
         | ID COLON type   // tip je obavezan
         | ID             // tip nije obavezan
         ;

// Tipovi podataka (Dart)
type
    : INT_TYPE
    | DOUBLE_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    | LIST_TYPE LT type (COMMA type)* GT
    | MAP_TYPE LT type COMMA type GT
    | SET_TYPE LT type GT
    | DYNAMIC
    | ID   // korisnički definisani tipovi
    ;

// If-else izraz
ifStatement: IF LPAREN expression RPAREN block (ELSE block)?;

// While petlja
whileStatement: WHILE LPAREN expression RPAREN block;

// Do-while petlja
doWhileStatement: DO block WHILE LPAREN expression RPAREN SEMI?;

// For petlja (klasična i foreach stil) - AŽURIRANO
forStatement
    : FOR LPAREN forLoopParts RPAREN block
    ;

forLoopParts
    : (forInitializerStatement | /* prazno */) 
      expression? SEMI 
      expressionList?
    | declaredIdentifier IN expression
    | ID IN expression
    ;

forInitializerStatement
    : localVariableDeclaration
    | expression (COMMA expression)* SEMI?
    ;

// Switch-case struktura (Dart-stil)
switchStatement
    : SWITCH LPAREN expression RPAREN LBRACE switchCase* defaultCase? RBRACE
    ;

switchCase
    : CASE expression COLON statement*
    ;

defaultCase
    : DEFAULT COLON statement*
    ;

// Try-catch-finally blok
tryStatement: TRY block (catchClause | onClause)* finallyClause?;
// onClause: ON type block;
onClause
    : ON type (LPAREN ID RPAREN)? block
    ;

catchClause: CATCH LPAREN ID (COLON type)? RPAREN block;
finallyClause: FINALLY block;

// Return naredba
returnStatement: RETURN expression? SEMI?;

// Deklaracije promenljivih
varDecl: VAR ID (ASSIGN expression)? SEMI?;
// intDecl: INT? ID (ASSIGN expression)? SEMI?;
finalDecl: FINAL ID (ASSIGN expression)? SEMI?;
constDecl: CONST ID (ASSIGN expression)? SEMI?;

typedVarDecl: type ID (ASSIGN expression)? SEMI?;

// Lokalna deklaracija varijable (dodato za for petlje)
localVariableDeclaration: (VAR | FINAL | CONST) ID (ASSIGN expression)? SEMI?;

// Deklarisani identifikator (dodato za for petlje)
declaredIdentifier: (VAR | FINAL | CONST) ID;

// Obična naredba izraza
exprStatement: expression SEMI?;

// Blok koda
block: LBRACE statement* RBRACE;
breakStatement: BREAK SEMI?;
continueStatement: CONTINUE SEMI?;
throwStatement: THROW expression SEMI?;

// Izrazi
expression
    : literal
    | ID
    | listLiteral
    | ID ASSIGN expression                      // dodela vrijednosti
    | expression (PLUSEQ | MINUSEQ | MULEQ | DIVEQ | MODEQ) expression  // OPERATORI DODJELE
    | expression DOT ID                         // npr. obj.method
    | expression DOT ID LPAREN argumentList? RPAREN     // metoda 
    | expression LPAREN argumentList? RPAREN    // poziv funkcije 
    | expression binaryOp expression            // binarni izrazi
    | unaryOp expression                        // prefiks unarni
    | expression unaryPostfixOp                 // postfiks unarni
    | LPAREN expression RPAREN
    | expression LBRACK expression RBRACK       // pristup listi/mapi
    ;
// Dodajte list literal produkciju
listLiteral: LBRACK expressionList? RBRACK;

// argumentList: expression (COMMA expression)*;

// Lista izraza (dodato za for petlje)
expressionList: expression (COMMA expression)*;

// Metadata (dodato za for petlje)
metadata: (AT metadatum)*;
metadatum: ID | constructorDesignation arguments;
constructorDesignation: typeName typeArguments? DOT ID?;
typeName: ID (DOT ID)?;
typeArguments: LT typeList GT;
typeList: type (COMMA type)*;
arguments: LPAREN (argumentList COMMA?)? RPAREN;
argumentList: expression (COMMA expression)*;

// Literali
literal
    : INT_LITERAL
    | DOUBLE_LITERAL
    | STRING
    | TRUE
    | FALSE
    | NULL
    ;

// Binarni operatori
binaryOp
    : PLUS | MINUS | MUL | DIV | MOD
    | EQ | NEQ | LT | GT | LEQ | GEQ
    | AND | OR
    ;

// Prefiks unarni operatori
unaryOp
    : PLUS | MINUS | NOT | INC | DEC
    ;

// Postfiks unarni operatori
unaryPostfixOp
    : INC | DEC
    ;