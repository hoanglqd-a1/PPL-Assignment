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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\5\6-\n\6\3\6\3\6\5\6\61\n\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\6\b@\n")
        buf.write("\b\r\b\16\bA\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\nO\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\fY\n")
        buf.write("\f\3\f\3\f\3\f\5\f^\n\f\3\f\3\f\5\fb\n\f\3\f\3\f\3\f\5")
        buf.write("\fg\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\4\3\2\16")
        buf.write("\21\4\2\30\31,.\2h\2\31\3\2\2\2\4\"\3\2\2\2\6$\3\2\2\2")
        buf.write("\b&\3\2\2\2\n(\3\2\2\2\f\64\3\2\2\2\16:\3\2\2\2\20F\3")
        buf.write("\2\2\2\22N\3\2\2\2\24P\3\2\2\2\26S\3\2\2\2\30\32\5\4\3")
        buf.write("\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37#\5\26")
        buf.write("\f\2 #\5\n\6\2!#\5\f\7\2\"\37\3\2\2\2\" \3\2\2\2\"!\3")
        buf.write("\2\2\2#\5\3\2\2\2$%\t\2\2\2%\7\3\2\2\2&\'\t\3\2\2\'\t")
        buf.write("\3\2\2\2()\7\23\2\2)\60\7/\2\2*\61\5\6\4\2+-\5\6\4\2,")
        buf.write("+\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\36\2\2/\61\5\b\5\2\60")
        buf.write("*\3\2\2\2\60,\3\2\2\2\61\62\3\2\2\2\62\63\7+\2\2\63\13")
        buf.write("\3\2\2\2\64\65\7\22\2\2\65\66\7/\2\2\66\67\7\36\2\2\67")
        buf.write("8\5\b\5\289\7+\2\29\r\3\2\2\2:;\7\23\2\2;?\7/\2\2<=\7")
        buf.write("&\2\2=>\7-\2\2>@\7\'\2\2?<\3\2\2\2@A\3\2\2\2A?\3\2\2\2")
        buf.write("AB\3\2\2\2BC\3\2\2\2CD\5\6\4\2DE\7+\2\2E\17\3\2\2\2FG")
        buf.write("\7/\2\2GH\5\6\4\2H\21\3\2\2\2IJ\5\20\t\2JK\7*\2\2KL\5")
        buf.write("\22\n\2LO\3\2\2\2MO\5\20\t\2NI\3\2\2\2NM\3\2\2\2O\23\3")
        buf.write("\2\2\2PQ\7/\2\2QR\7/\2\2R\25\3\2\2\2SX\7\n\2\2TU\7$\2")
        buf.write("\2UV\5\24\13\2VW\7%\2\2WY\3\2\2\2XT\3\2\2\2XY\3\2\2\2")
        buf.write("YZ\3\2\2\2Z[\7/\2\2[]\7$\2\2\\^\5\22\n\2]\\\3\2\2\2]^")
        buf.write("\3\2\2\2^_\3\2\2\2_a\7%\2\2`b\5\6\4\2a`\3\2\2\2ab\3\2")
        buf.write("\2\2bc\3\2\2\2cd\7(\2\2df\7)\2\2eg\7+\2\2fe\3\2\2\2fg")
        buf.write("\3\2\2\2g\27\3\2\2\2\f\33\",\60ANX]af")
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
                     "<INVALID>", "<INVALID>", "'.'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "NL", "WS", "COMMENT", "IF_", "ELSE_", 
                      "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
                      "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", 
                      "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", "TRUE_", 
                      "FALSE_", "OP2", "OP3", "OP4", "OP5", "ASSIGN", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", 
                      "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", 
                      "INTEGER", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_data_type = 2
    RULE_value = 3
    RULE_vardecl = 4
    RULE_constdecl = 5
    RULE_arraydecl = 6
    RULE_parameter = 7
    RULE_parameterlst = 8
    RULE_receiver = 9
    RULE_funcdecl = 10

    ruleNames =  [ "program", "decl", "data_type", "value", "vardecl", "constdecl", 
                   "arraydecl", "parameter", "parameterlst", "receiver", 
                   "funcdecl" ]

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
    OP2=24
    OP3=25
    OP4=26
    OP5=27
    ASSIGN=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    LPAREN=34
    RPAREN=35
    LSB=36
    RSB=37
    LCB=38
    RCB=39
    COMMA=40
    SEMICOLON=41
    FLOAT=42
    INTEGER=43
    STRING=44
    ID=45
    ERROR_CHAR=46
    ILLEGAL_ESCAPE=47
    UNCLOSE_STRING=48

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.decl()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_))) != 0)):
                    break

            self.state = 27
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


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.vardecl()
                pass
            elif token in [MiniGoParser.CONST_]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.constdecl()
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_(self):
            return self.getToken(MiniGoParser.INT_, 0)

        def FLOAT_(self):
            return self.getToken(MiniGoParser.FLOAT_, 0)

        def STRING_(self):
            return self.getToken(MiniGoParser.STRING_, 0)

        def BOOLEAN_(self):
            return self.getToken(MiniGoParser.BOOLEAN_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def TRUE_(self):
            return self.getToken(MiniGoParser.TRUE_, 0)

        def FALSE_(self):
            return self.getToken(MiniGoParser.FALSE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING))) != 0)):
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MiniGoParser.VAR_)
            self.state = 39
            self.match(MiniGoParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 40
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 41
                    self.data_type()


                self.state = 44
                self.match(MiniGoParser.ASSIGN)
                self.state = 45
                self.value()
                pass


            self.state = 48
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_(self):
            return self.getToken(MiniGoParser.CONST_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MiniGoParser.CONST_)
            self.state = 51
            self.match(MiniGoParser.ID)
            self.state = 52
            self.match(MiniGoParser.ASSIGN)
            self.state = 53
            self.value()
            self.state = 54
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTEGER)
            else:
                return self.getToken(MiniGoParser.INTEGER, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiniGoParser.VAR_)
            self.state = 57
            self.match(MiniGoParser.ID)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.match(MiniGoParser.LSB)
                self.state = 59
                self.match(MiniGoParser.INTEGER)
                self.state = 60
                self.match(MiniGoParser.RSB)
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 65
            self.data_type()
            self.state = 66
            self.match(MiniGoParser.SEMICOLON)
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MiniGoParser.ID)
            self.state = 69
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlst" ):
                return visitor.visitParameterlst(self)
            else:
                return visitor.visitChildren(self)




    def parameterlst(self):

        localctx = MiniGoParser.ParameterlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterlst)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.parameter()
                self.state = 72
                self.match(MiniGoParser.COMMA)
                self.state = 73
                self.parameterlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MiniGoParser.ID)
            self.state = 79
            self.match(MiniGoParser.ID)
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


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
        self.enterRule(localctx, 20, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MiniGoParser.FUNC_)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 82
                self.match(MiniGoParser.LPAREN)
                self.state = 83
                self.receiver()
                self.state = 84
                self.match(MiniGoParser.RPAREN)


            self.state = 88
            self.match(MiniGoParser.ID)
            self.state = 89
            self.match(MiniGoParser.LPAREN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 90
                self.parameterlst()


            self.state = 93
            self.match(MiniGoParser.RPAREN)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 94
                self.data_type()


            self.state = 97
            self.match(MiniGoParser.LCB)
            self.state = 98
            self.match(MiniGoParser.RCB)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 99
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





