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
        4,1,43,229,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,67,
        8,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,77,8,3,10,3,12,3,80,9,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,102,8,5,1,6,1,6,1,6,1,6,3,6,108,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,9,6,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,138,8,9,1,
        10,1,10,1,10,3,10,143,8,10,1,10,1,10,1,11,1,11,1,11,5,11,150,8,11,
        10,11,12,11,153,9,11,1,12,1,12,1,13,1,13,1,13,3,13,160,8,13,1,13,
        1,13,1,13,3,13,165,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        174,8,14,1,15,1,15,1,15,3,15,179,8,15,1,15,1,15,3,15,183,8,15,1,
        15,1,15,3,15,187,8,15,1,15,1,15,1,15,1,16,1,16,3,16,194,8,16,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,3,20,214,8,20,1,21,1,21,5,21,218,8,21,10,21,
        12,21,221,9,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,0,1,12,24,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,
        6,1,0,9,13,1,0,14,17,1,0,19,24,1,0,25,26,1,0,27,28,1,0,36,39,236,
        0,51,1,0,0,0,2,62,1,0,0,0,4,71,1,0,0,0,6,73,1,0,0,0,8,81,1,0,0,0,
        10,101,1,0,0,0,12,107,1,0,0,0,14,123,1,0,0,0,16,126,1,0,0,0,18,137,
        1,0,0,0,20,139,1,0,0,0,22,146,1,0,0,0,24,154,1,0,0,0,26,159,1,0,
        0,0,28,166,1,0,0,0,30,175,1,0,0,0,32,193,1,0,0,0,34,195,1,0,0,0,
        36,197,1,0,0,0,38,203,1,0,0,0,40,211,1,0,0,0,42,215,1,0,0,0,44,224,
        1,0,0,0,46,226,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,
        51,49,1,0,0,0,51,52,1,0,0,0,52,57,1,0,0,0,53,51,1,0,0,0,54,56,3,
        10,5,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,
        60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,63,3,4,2,
        0,63,64,5,40,0,0,64,66,5,29,0,0,65,67,3,6,3,0,66,65,1,0,0,0,66,67,
        1,0,0,0,67,68,1,0,0,0,68,69,5,30,0,0,69,70,3,42,21,0,70,3,1,0,0,
        0,71,72,7,0,0,0,72,5,1,0,0,0,73,78,3,8,4,0,74,75,5,34,0,0,75,77,
        3,8,4,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,
        79,7,1,0,0,0,80,78,1,0,0,0,81,82,3,44,22,0,82,83,5,40,0,0,83,9,1,
        0,0,0,84,85,3,26,13,0,85,86,5,33,0,0,86,102,1,0,0,0,87,88,3,46,23,
        0,88,89,5,33,0,0,89,102,1,0,0,0,90,102,3,28,14,0,91,102,3,30,15,
        0,92,102,3,36,18,0,93,102,3,38,19,0,94,95,3,40,20,0,95,96,5,33,0,
        0,96,102,1,0,0,0,97,102,3,42,21,0,98,99,3,12,6,0,99,100,5,33,0,0,
        100,102,1,0,0,0,101,84,1,0,0,0,101,87,1,0,0,0,101,90,1,0,0,0,101,
        91,1,0,0,0,101,92,1,0,0,0,101,93,1,0,0,0,101,94,1,0,0,0,101,97,1,
        0,0,0,101,98,1,0,0,0,102,11,1,0,0,0,103,104,6,6,-1,0,104,108,3,18,
        9,0,105,108,3,16,8,0,106,108,3,14,7,0,107,103,1,0,0,0,107,105,1,
        0,0,0,107,106,1,0,0,0,108,120,1,0,0,0,109,110,10,5,0,0,110,111,7,
        1,0,0,111,119,3,12,6,6,112,113,10,4,0,0,113,114,7,2,0,0,114,119,
        3,12,6,5,115,116,10,3,0,0,116,117,7,3,0,0,117,119,3,12,6,4,118,109,
        1,0,0,0,118,112,1,0,0,0,118,115,1,0,0,0,119,122,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,13,1,0,0,0,122,120,1,0,0,0,123,124,3,
        18,9,0,124,125,7,4,0,0,125,15,1,0,0,0,126,127,5,40,0,0,127,128,5,
        18,0,0,128,129,3,12,6,0,129,17,1,0,0,0,130,131,5,29,0,0,131,132,
        3,12,6,0,132,133,5,30,0,0,133,138,1,0,0,0,134,138,5,40,0,0,135,138,
        3,24,12,0,136,138,3,20,10,0,137,130,1,0,0,0,137,134,1,0,0,0,137,
        135,1,0,0,0,137,136,1,0,0,0,138,19,1,0,0,0,139,140,5,40,0,0,140,
        142,5,29,0,0,141,143,3,22,11,0,142,141,1,0,0,0,142,143,1,0,0,0,143,
        144,1,0,0,0,144,145,5,30,0,0,145,21,1,0,0,0,146,151,3,12,6,0,147,
        148,5,34,0,0,148,150,3,12,6,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,23,1,0,0,0,153,151,1,0,0,0,154,155,
        7,5,0,0,155,25,1,0,0,0,156,160,5,7,0,0,157,160,5,8,0,0,158,160,3,
        44,22,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,161,
        1,0,0,0,161,164,5,40,0,0,162,163,5,18,0,0,163,165,3,12,6,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,27,1,0,0,0,166,167,5,1,0,0,167,168,5,
        29,0,0,168,169,3,12,6,0,169,170,5,30,0,0,170,173,3,10,5,0,171,172,
        5,2,0,0,172,174,3,10,5,0,173,171,1,0,0,0,173,174,1,0,0,0,174,29,
        1,0,0,0,175,176,5,3,0,0,176,178,5,29,0,0,177,179,3,32,16,0,178,177,
        1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,5,33,0,0,181,183,
        3,12,6,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,186,
        5,33,0,0,185,187,3,34,17,0,186,185,1,0,0,0,186,187,1,0,0,0,187,188,
        1,0,0,0,188,189,5,30,0,0,189,190,3,10,5,0,190,31,1,0,0,0,191,194,
        3,26,13,0,192,194,3,46,23,0,193,191,1,0,0,0,193,192,1,0,0,0,194,
        33,1,0,0,0,195,196,3,46,23,0,196,35,1,0,0,0,197,198,5,4,0,0,198,
        199,5,29,0,0,199,200,3,12,6,0,200,201,5,30,0,0,201,202,3,10,5,0,
        202,37,1,0,0,0,203,204,5,5,0,0,204,205,3,10,5,0,205,206,5,4,0,0,
        206,207,5,29,0,0,207,208,3,12,6,0,208,209,5,30,0,0,209,210,5,33,
        0,0,210,39,1,0,0,0,211,213,5,6,0,0,212,214,3,12,6,0,213,212,1,0,
        0,0,213,214,1,0,0,0,214,41,1,0,0,0,215,219,5,31,0,0,216,218,3,10,
        5,0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,
        0,0,220,222,1,0,0,0,221,219,1,0,0,0,222,223,5,32,0,0,223,43,1,0,
        0,0,224,225,7,0,0,0,225,45,1,0,0,0,226,227,3,12,6,0,227,47,1,0,0,
        0,20,51,57,66,78,101,107,118,120,137,142,151,159,164,173,178,182,
        186,193,213,219
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
                     "'>='", "'&&'", "'||'", "'++'", "'--'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "WHILE", "DO", "RETURN", 
                      "VAR", "FINAL", "BOOL", "INT", "DOUBLE", "STRING", 
                      "VOID", "PLUS", "MINUS", "MULT", "DIV", "ASSIGN", 
                      "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "PLUS_PLUS", "MINUS_MINUS", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMI", "COMMA", "DOT", "BOOL_LITERAL", 
                      "INT_LITERAL", "DOUBLE_LITERAL", "STRING_LITERAL", 
                      "ID", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_functionDeclaration = 1
    RULE_functionType = 2
    RULE_parameterList = 3
    RULE_parameter = 4
    RULE_statement = 5
    RULE_expression = 6
    RULE_postfixExpression = 7
    RULE_assignment = 8
    RULE_primary = 9
    RULE_functionCall = 10
    RULE_argumentList = 11
    RULE_literal = 12
    RULE_variableDeclaration = 13
    RULE_ifStatement = 14
    RULE_forStatement = 15
    RULE_forInitializer = 16
    RULE_forIterator = 17
    RULE_whileStatement = 18
    RULE_doWhileStatement = 19
    RULE_returnStatement = 20
    RULE_block = 21
    RULE_type = 22
    RULE_expressionStatement = 23

    ruleNames =  [ "program", "functionDeclaration", "functionType", "parameterList", 
                   "parameter", "statement", "expression", "postfixExpression", 
                   "assignment", "primary", "functionCall", "argumentList", 
                   "literal", "variableDeclaration", "ifStatement", "forStatement", 
                   "forInitializer", "forIterator", "whileStatement", "doWhileStatement", 
                   "returnStatement", "block", "type", "expressionStatement" ]

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
    PLUS_PLUS=27
    MINUS_MINUS=28
    LPAREN=29
    RPAREN=30
    LBRACE=31
    RBRACE=32
    SEMI=33
    COMMA=34
    DOT=35
    BOOL_LITERAL=36
    INT_LITERAL=37
    DOUBLE_LITERAL=38
    STRING_LITERAL=39
    ID=40
    LINE_COMMENT=41
    BLOCK_COMMENT=42
    WS=43

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

        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.FunctionDeclarationContext,i)


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
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self.functionDeclaration() 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2132988149754) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(Dart2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionType(self):
            return self.getTypedRuleContext(Dart2Parser.FunctionTypeContext,0)


        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(Dart2Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = Dart2Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.functionType()
            self.state = 63
            self.match(Dart2Parser.ID)
            self.state = 64
            self.match(Dart2Parser.LPAREN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0):
                self.state = 65
                self.parameterList()


            self.state = 68
            self.match(Dart2Parser.RPAREN)
            self.state = 69
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(Dart2Parser.VOID, 0)

        def INT(self):
            return self.getToken(Dart2Parser.INT, 0)

        def DOUBLE(self):
            return self.getToken(Dart2Parser.DOUBLE, 0)

        def BOOL(self):
            return self.getToken(Dart2Parser.BOOL, 0)

        def STRING(self):
            return self.getToken(Dart2Parser.STRING, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_functionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionType" ):
                listener.enterFunctionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionType" ):
                listener.exitFunctionType(self)




    def functionType(self):

        localctx = Dart2Parser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
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


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = Dart2Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.parameter()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 74
                self.match(Dart2Parser.COMMA)
                self.state = 75
                self.parameter()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = Dart2Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.type_()
            self.state = 82
            self.match(Dart2Parser.ID)
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


        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


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
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.variableDeclaration()
                self.state = 85
                self.match(Dart2Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.expressionStatement()
                self.state = 88
                self.match(Dart2Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.doWhileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.returnStatement()
                self.state = 95
                self.match(Dart2Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 97
                self.block()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 98
                self.expression(0)
                self.state = 99
                self.match(Dart2Parser.SEMI)
                pass


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


        def postfixExpression(self):
            return self.getTypedRuleContext(Dart2Parser.PostfixExpressionContext,0)


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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 104
                self.primary()
                pass

            elif la_ == 2:
                self.state = 105
                self.assignment()
                pass

            elif la_ == 3:
                self.state = 106
                self.postfixExpression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 118
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 109
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 110
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 111
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 114
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 116
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 117
                        self.expression(4)
                        pass

             
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Dart2Parser.PrimaryContext,0)


        def PLUS_PLUS(self):
            return self.getToken(Dart2Parser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(Dart2Parser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpression" ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpression" ):
                listener.exitPostfixExpression(self)




    def postfixExpression(self):

        localctx = Dart2Parser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.primary()
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(Dart2Parser.ID)
            self.state = 127
            self.match(Dart2Parser.ASSIGN)
            self.state = 128
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
        self.enterRule(localctx, 18, self.RULE_primary)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(Dart2Parser.LPAREN)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(Dart2Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(Dart2Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
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
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(Dart2Parser.ID)
            self.state = 140
            self.match(Dart2Parser.LPAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130840649728) != 0):
                self.state = 141
                self.argumentList()


            self.state = 144
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
        self.enterRule(localctx, 22, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expression(0)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 147
                self.match(Dart2Parser.COMMA)
                self.state = 148
                self.expression(0)
                self.state = 153
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
        self.enterRule(localctx, 24, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 156
                self.match(Dart2Parser.VAR)
                pass
            elif token in [8]:
                self.state = 157
                self.match(Dart2Parser.FINAL)
                pass
            elif token in [9, 10, 11, 12, 13]:
                self.state = 158
                self.type_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(Dart2Parser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 162
                self.match(Dart2Parser.ASSIGN)
                self.state = 163
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
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(Dart2Parser.IF)
            self.state = 167
            self.match(Dart2Parser.LPAREN)
            self.state = 168
            self.expression(0)
            self.state = 169
            self.match(Dart2Parser.RPAREN)
            self.state = 170
            self.statement()
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 171
                self.match(Dart2Parser.ELSE)
                self.state = 172
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
        self.enterRule(localctx, 30, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(Dart2Parser.FOR)
            self.state = 176
            self.match(Dart2Parser.LPAREN)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130840665984) != 0):
                self.state = 177
                self.forInitializer()


            self.state = 180
            self.match(Dart2Parser.SEMI)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130840649728) != 0):
                self.state = 181
                self.expression(0)


            self.state = 184
            self.match(Dart2Parser.SEMI)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130840649728) != 0):
                self.state = 185
                self.forIterator()


            self.state = 188
            self.match(Dart2Parser.RPAREN)
            self.state = 189
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
        self.enterRule(localctx, 32, self.RULE_forInitializer)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.variableDeclaration()
                pass
            elif token in [29, 36, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
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
        self.enterRule(localctx, 34, self.RULE_forIterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 36, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(Dart2Parser.WHILE)
            self.state = 198
            self.match(Dart2Parser.LPAREN)
            self.state = 199
            self.expression(0)
            self.state = 200
            self.match(Dart2Parser.RPAREN)
            self.state = 201
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
        self.enterRule(localctx, 38, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(Dart2Parser.DO)
            self.state = 204
            self.statement()
            self.state = 205
            self.match(Dart2Parser.WHILE)
            self.state = 206
            self.match(Dart2Parser.LPAREN)
            self.state = 207
            self.expression(0)
            self.state = 208
            self.match(Dart2Parser.RPAREN)
            self.state = 209
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
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(Dart2Parser.RETURN)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130840649728) != 0):
                self.state = 212
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
        self.enterRule(localctx, 42, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(Dart2Parser.LBRACE)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2132988149754) != 0):
                self.state = 216
                self.statement()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
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
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
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
        self.enterRule(localctx, 46, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.expression(0)
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
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




