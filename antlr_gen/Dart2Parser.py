# Generated from grammar/Dart2Parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,41,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,3,2,66,8,2,1,2,1,2,1,2,3,
        2,71,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,82,8,4,1,5,1,5,
        1,5,3,5,87,8,5,1,5,1,5,3,5,91,8,5,1,5,1,5,3,5,95,8,5,1,5,1,5,1,5,
        1,6,1,6,3,6,102,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,122,8,10,1,11,1,11,5,11,126,8,
        11,10,11,12,11,129,9,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,3,13,
        138,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,149,8,
        13,10,13,12,13,152,9,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,165,8,15,1,16,1,16,1,16,3,16,170,8,16,1,16,1,
        16,1,17,1,17,1,17,5,17,177,8,17,10,17,12,17,180,9,17,1,18,1,18,1,
        18,0,1,26,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        0,5,1,0,9,13,1,0,14,17,1,0,19,24,1,0,25,26,1,0,34,37,191,0,41,1,
        0,0,0,2,60,1,0,0,0,4,65,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,10,83,
        1,0,0,0,12,101,1,0,0,0,14,103,1,0,0,0,16,105,1,0,0,0,18,111,1,0,
        0,0,20,119,1,0,0,0,22,123,1,0,0,0,24,132,1,0,0,0,26,137,1,0,0,0,
        28,153,1,0,0,0,30,164,1,0,0,0,32,166,1,0,0,0,34,173,1,0,0,0,36,181,
        1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,
        0,0,46,47,3,4,2,0,47,48,5,31,0,0,48,61,1,0,0,0,49,50,3,6,3,0,50,
        51,5,31,0,0,51,61,1,0,0,0,52,61,3,8,4,0,53,61,3,10,5,0,54,61,3,16,
        8,0,55,61,3,18,9,0,56,57,3,20,10,0,57,58,5,31,0,0,58,61,1,0,0,0,
        59,61,3,22,11,0,60,46,1,0,0,0,60,49,1,0,0,0,60,52,1,0,0,0,60,53,
        1,0,0,0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,60,59,1,0,0,0,
        61,3,1,0,0,0,62,66,5,7,0,0,63,66,5,8,0,0,64,66,3,24,12,0,65,62,1,
        0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,70,5,38,0,0,68,
        69,5,18,0,0,69,71,3,26,13,0,70,68,1,0,0,0,70,71,1,0,0,0,71,5,1,0,
        0,0,72,73,3,26,13,0,73,7,1,0,0,0,74,75,5,1,0,0,75,76,5,27,0,0,76,
        77,3,26,13,0,77,78,5,28,0,0,78,81,3,2,1,0,79,80,5,2,0,0,80,82,3,
        2,1,0,81,79,1,0,0,0,81,82,1,0,0,0,82,9,1,0,0,0,83,84,5,3,0,0,84,
        86,5,27,0,0,85,87,3,12,6,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,
        0,0,88,90,5,31,0,0,89,91,3,26,13,0,90,89,1,0,0,0,90,91,1,0,0,0,91,
        92,1,0,0,0,92,94,5,31,0,0,93,95,3,14,7,0,94,93,1,0,0,0,94,95,1,0,
        0,0,95,96,1,0,0,0,96,97,5,28,0,0,97,98,3,2,1,0,98,11,1,0,0,0,99,
        102,3,4,2,0,100,102,3,6,3,0,101,99,1,0,0,0,101,100,1,0,0,0,102,13,
        1,0,0,0,103,104,3,6,3,0,104,15,1,0,0,0,105,106,5,4,0,0,106,107,5,
        27,0,0,107,108,3,26,13,0,108,109,5,28,0,0,109,110,3,2,1,0,110,17,
        1,0,0,0,111,112,5,5,0,0,112,113,3,2,1,0,113,114,5,4,0,0,114,115,
        5,27,0,0,115,116,3,26,13,0,116,117,5,28,0,0,117,118,5,31,0,0,118,
        19,1,0,0,0,119,121,5,6,0,0,120,122,3,26,13,0,121,120,1,0,0,0,121,
        122,1,0,0,0,122,21,1,0,0,0,123,127,5,29,0,0,124,126,3,2,1,0,125,
        124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,
        130,1,0,0,0,129,127,1,0,0,0,130,131,5,30,0,0,131,23,1,0,0,0,132,
        133,7,0,0,0,133,25,1,0,0,0,134,135,6,13,-1,0,135,138,3,30,15,0,136,
        138,3,28,14,0,137,134,1,0,0,0,137,136,1,0,0,0,138,150,1,0,0,0,139,
        140,10,4,0,0,140,141,7,1,0,0,141,149,3,26,13,5,142,143,10,3,0,0,
        143,144,7,2,0,0,144,149,3,26,13,4,145,146,10,2,0,0,146,147,7,3,0,
        0,147,149,3,26,13,3,148,139,1,0,0,0,148,142,1,0,0,0,148,145,1,0,
        0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,27,1,0,0,
        0,152,150,1,0,0,0,153,154,5,38,0,0,154,155,5,18,0,0,155,156,3,26,
        13,0,156,29,1,0,0,0,157,158,5,27,0,0,158,159,3,26,13,0,159,160,5,
        28,0,0,160,165,1,0,0,0,161,165,5,38,0,0,162,165,3,36,18,0,163,165,
        3,32,16,0,164,157,1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,
        1,0,0,0,165,31,1,0,0,0,166,167,5,38,0,0,167,169,5,27,0,0,168,170,
        3,34,17,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,
        5,28,0,0,172,33,1,0,0,0,173,178,3,26,13,0,174,175,5,32,0,0,175,177,
        3,26,13,0,176,174,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,35,1,0,0,0,180,178,1,0,0,0,181,182,7,4,0,0,182,37,1,
        0,0,0,17,41,60,65,70,81,86,90,94,101,121,127,137,148,150,164,169,
        178
    ]

class Dart2Parser ( Parser ):

    grammarFileName = "Dart2Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'return'", "'var'", "'final'", "'bool'", "'int'", 
                     "'double'", "'String'", "'void'", "'+'", "'-'", "'*'", 
                     "'/'", "'='", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "WHILE", "DO", "RETURN", 
                      "VAR", "FINAL", "BOOL", "INT", "DOUBLE", "STRING", 
                      "VOID", "PLUS", "MINUS", "MULT", "DIV", "ASSIGN", 
                      "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "COMMA", 
                      "DOT", "BOOL_LITERAL", "INT_LITERAL", "DOUBLE_LITERAL", 
                      "STRING_LITERAL", "ID", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_expressionStatement = 3
    RULE_ifStatement = 4
    RULE_forStatement = 5
    RULE_forInitializer = 6
    RULE_forIterator = 7
    RULE_whileStatement = 8
    RULE_doWhileStatement = 9
    RULE_returnStatement = 10
    RULE_block = 11
    RULE_type = 12
    RULE_expression = 13
    RULE_assignment = 14
    RULE_primary = 15
    RULE_functionCall = 16
    RULE_argumentList = 17
    RULE_literal = 18

    ruleNames =  [ "program", "statement", "variableDeclaration", "expressionStatement", 
                   "ifStatement", "forStatement", "forInitializer", "forIterator", 
                   "whileStatement", "doWhileStatement", "returnStatement", 
                   "block", "type", "expression", "assignment", "primary", 
                   "functionCall", "argumentList", "literal" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    WHILE=4
    DO=5
    RETURN=6
    VAR=7
    FINAL=8
    BOOL=9
    INT=10
    DOUBLE=11
    STRING=12
    VOID=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    ASSIGN=18
    EQ=19
    NEQ=20
    LT=21
    LTE=22
    GT=23
    GTE=24
    AND=25
    OR=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    SEMI=31
    COMMA=32
    DOT=33
    BOOL_LITERAL=34
    INT_LITERAL=35
    DOUBLE_LITERAL=36
    STRING_LITERAL=37
    ID=38
    LINE_COMMENT=39
    BLOCK_COMMENT=40
    WS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Dart2Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = Dart2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 533247049722) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(Dart2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(Dart2Parser.VariableDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def expressionStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(Dart2Parser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(Dart2Parser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(Dart2Parser.DoWhileStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ReturnStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Dart2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.variableDeclaration()
                self.state = 47
                self.match(Dart2Parser.SEMI)
                pass
            elif token in [27, 34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.expressionStatement()
                self.state = 50
                self.match(Dart2Parser.SEMI)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.ifStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.forStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.whileStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.doWhileStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.returnStatement()
                self.state = 57
                self.match(Dart2Parser.SEMI)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 8)
                self.state = 59
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def VAR(self):
            return self.getToken(Dart2Parser.VAR, 0)

        def FINAL(self):
            return self.getToken(Dart2Parser.FINAL, 0)

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = Dart2Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 62
                self.match(Dart2Parser.VAR)
                pass
            elif token in [8]:
                self.state = 63
                self.match(Dart2Parser.FINAL)
                pass
            elif token in [9, 10, 11, 12, 13]:
                self.state = 64
                self.type_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 67
            self.match(Dart2Parser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 68
                self.match(Dart2Parser.ASSIGN)
                self.state = 69
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = Dart2Parser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Dart2Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(Dart2Parser.ELSE, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = Dart2Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(Dart2Parser.IF)
            self.state = 75
            self.match(Dart2Parser.LPAREN)
            self.state = 76
            self.expression(0)
            self.state = 77
            self.match(Dart2Parser.RPAREN)
            self.state = 78
            self.statement()
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(Dart2Parser.ELSE)
                self.state = 80
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Dart2Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.SEMI)
            else:
                return self.getToken(Dart2Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Dart2Parser.StatementContext,0)


        def forInitializer(self):
            return self.getTypedRuleContext(Dart2Parser.ForInitializerContext,0)


        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def forIterator(self):
            return self.getTypedRuleContext(Dart2Parser.ForIteratorContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = Dart2Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(Dart2Parser.FOR)
            self.state = 84
            self.match(Dart2Parser.LPAREN)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532710178688) != 0):
                self.state = 85
                self.forInitializer()


            self.state = 88
            self.match(Dart2Parser.SEMI)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532710162432) != 0):
                self.state = 89
                self.expression(0)


            self.state = 92
            self.match(Dart2Parser.SEMI)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532710162432) != 0):
                self.state = 93
                self.forIterator()


            self.state = 96
            self.match(Dart2Parser.RPAREN)
            self.state = 97
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(Dart2Parser.VariableDeclarationContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_forInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitializer" ):
                listener.enterForInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitializer" ):
                listener.exitForInitializer(self)




    def forInitializer(self):

        localctx = Dart2Parser.ForInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forInitializer)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.variableDeclaration()
                pass
            elif token in [27, 34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.expressionStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIteratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_forIterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForIterator" ):
                listener.enterForIterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForIterator" ):
                listener.exitForIterator(self)




    def forIterator(self):

        localctx = Dart2Parser.ForIteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forIterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expressionStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Dart2Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Dart2Parser.StatementContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = Dart2Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(Dart2Parser.WHILE)
            self.state = 106
            self.match(Dart2Parser.LPAREN)
            self.state = 107
            self.expression(0)
            self.state = 108
            self.match(Dart2Parser.RPAREN)
            self.state = 109
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(Dart2Parser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(Dart2Parser.StatementContext,0)


        def WHILE(self):
            return self.getToken(Dart2Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = Dart2Parser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(Dart2Parser.DO)
            self.state = 112
            self.statement()
            self.state = 113
            self.match(Dart2Parser.WHILE)
            self.state = 114
            self.match(Dart2Parser.LPAREN)
            self.state = 115
            self.expression(0)
            self.state = 116
            self.match(Dart2Parser.RPAREN)
            self.state = 117
            self.match(Dart2Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(Dart2Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = Dart2Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(Dart2Parser.RETURN)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532710162432) != 0):
                self.state = 120
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Dart2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Dart2Parser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = Dart2Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(Dart2Parser.LBRACE)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 533247049722) != 0):
                self.state = 124
                self.statement()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(Dart2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Dart2Parser.INT, 0)

        def DOUBLE(self):
            return self.getToken(Dart2Parser.DOUBLE, 0)

        def BOOL(self):
            return self.getToken(Dart2Parser.BOOL, 0)

        def STRING(self):
            return self.getToken(Dart2Parser.STRING, 0)

        def VOID(self):
            return self.getToken(Dart2Parser.VOID, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = Dart2Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Dart2Parser.PrimaryContext,0)


        def assignment(self):
            return self.getTypedRuleContext(Dart2Parser.AssignmentContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def PLUS(self):
            return self.getToken(Dart2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Dart2Parser.MINUS, 0)

        def MULT(self):
            return self.getToken(Dart2Parser.MULT, 0)

        def DIV(self):
            return self.getToken(Dart2Parser.DIV, 0)

        def EQ(self):
            return self.getToken(Dart2Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(Dart2Parser.NEQ, 0)

        def LT(self):
            return self.getToken(Dart2Parser.LT, 0)

        def LTE(self):
            return self.getToken(Dart2Parser.LTE, 0)

        def GT(self):
            return self.getToken(Dart2Parser.GT, 0)

        def GTE(self):
            return self.getToken(Dart2Parser.GTE, 0)

        def AND(self):
            return self.getToken(Dart2Parser.AND, 0)

        def OR(self):
            return self.getToken(Dart2Parser.OR, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Dart2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 135
                self.primary()
                pass

            elif la_ == 2:
                self.state = 136
                self.assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 140
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 141
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 143
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 146
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.expression(3)
                        pass

             
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = Dart2Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(Dart2Parser.ID)
            self.state = 154
            self.match(Dart2Parser.ASSIGN)
            self.state = 155
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(Dart2Parser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(Dart2Parser.FunctionCallContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = Dart2Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primary)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(Dart2Parser.LPAREN)
                self.state = 158
                self.expression(0)
                self.state = 159
                self.match(Dart2Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(Dart2Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Dart2Parser.ArgumentListContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = Dart2Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(Dart2Parser.ID)
            self.state = 167
            self.match(Dart2Parser.LPAREN)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532710162432) != 0):
                self.state = 168
                self.argumentList()


            self.state = 171
            self.match(Dart2Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = Dart2Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.expression(0)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 174
                self.match(Dart2Parser.COMMA)
                self.state = 175
                self.expression(0)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(Dart2Parser.INT_LITERAL, 0)

        def DOUBLE_LITERAL(self):
            return self.getToken(Dart2Parser.DOUBLE_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(Dart2Parser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(Dart2Parser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = Dart2Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




