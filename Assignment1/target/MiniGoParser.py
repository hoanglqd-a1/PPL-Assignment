# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2")
        buf.write(" \2\13\3\2\2\2\4\23\3\2\2\2\6\25\3\2\2\2\b\32\3\2\2\2")
        buf.write("\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16")
        buf.write("\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\24")
        buf.write("\5\b\5\2\22\24\5\6\4\2\23\21\3\2\2\2\23\22\3\2\2\2\24")
        buf.write("\5\3\2\2\2\25\26\7\23\2\2\26\27\7*\2\2\27\30\7\17\2\2")
        buf.write("\30\31\7&\2\2\31\7\3\2\2\2\32\33\7\n\2\2\33\34\7*\2\2")
        buf.write("\34\35\7\37\2\2\35\36\7 \2\2\36\37\7#\2\2\37 \7$\2\2 ")
        buf.write("!\7&\2\2!\t\3\2\2\2\4\r\23")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "<INVALID>", "<INVALID>", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "NL", "WS", "COMMENT", "IF_", "ELSE_", 
                      "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
                      "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", 
                      "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", "TRUE_", 
                      "FALSE_", "OP1", "OP2", "OP3", "OP4", "OP5", "LPAREN", 
                      "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                      "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl" ]

    EOF = Token.EOF
    NL=1
    WS=2
    COMMENT=3
    IF_=4
    ELSE_=5
    FOR_=6
    RETURN_=7
    FUNC_=8
    TYPE_=9
    STRUCT_=10
    INTERFACE_=11
    STRING_=12
    INT_=13
    FLOAT_=14
    BOOLEAN_=15
    CONST_=16
    VAR_=17
    CONTINUE_=18
    BREAK_=19
    RANGE_=20
    NIL_=21
    TRUE_=22
    FALSE_=23
    OP1=24
    OP2=25
    OP3=26
    OP4=27
    OP5=28
    LPAREN=29
    RPAREN=30
    LSB=31
    RSB=32
    LCB=33
    RCB=34
    COMMA=35
    SEMICOLON=36
    FLOAT=37
    INTEGER=38
    STRING=39
    ID=40
    ERROR_CHAR=41
    ILLEGAL_ESCAPE=42
    UNCLOSE_STRING=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.decl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.FUNC_ or _la==MiniGoParser.VAR_):
                    break

            self.state = 13
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.vardecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_(self):
            return self.getToken(MiniGoParser.INT_, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(MiniGoParser.VAR_)
            self.state = 20
            self.match(MiniGoParser.ID)
            self.state = 21
            self.match(MiniGoParser.INT_)
            self.state = 22
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_(self):
            return self.getToken(MiniGoParser.FUNC_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MiniGoParser.FUNC_)
            self.state = 25
            self.match(MiniGoParser.ID)
            self.state = 26
            self.match(MiniGoParser.LPAREN)
            self.state = 27
            self.match(MiniGoParser.RPAREN)
            self.state = 28
            self.match(MiniGoParser.LCB)
            self.state = 29
            self.match(MiniGoParser.RCB)
            self.state = 30
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





