# Generated from c:/coding/PPL/Assignment1/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,52,301,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,4,0,60,8,0,11,0,12,0,61,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,
        5,1,5,5,5,85,8,5,10,5,12,5,88,9,5,1,6,1,6,1,6,5,6,93,8,6,10,6,12,
        6,96,9,6,1,7,1,7,1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,1,
        8,3,8,110,8,8,1,8,5,8,113,8,8,10,8,12,8,116,9,8,1,9,1,9,1,9,5,9,
        121,8,9,10,9,12,9,124,9,9,1,10,3,10,127,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,142,8,11,10,11,
        12,11,145,9,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,153,8,12,1,13,
        1,13,1,13,5,13,158,8,13,10,13,12,13,161,9,13,3,13,163,8,13,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,176,8,16,
        1,16,1,16,3,16,180,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,4,18,195,8,18,11,18,12,18,196,1,18,1,18,
        1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,210,8,20,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,220,8,22,1,22,1,22,1,22,
        3,22,225,8,22,1,22,1,22,3,22,229,8,22,1,22,1,22,1,22,1,22,1,23,1,
        23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,244,8,24,1,24,5,24,247,
        8,24,10,24,12,24,250,9,24,1,24,1,24,1,24,1,25,1,25,3,25,257,8,25,
        1,25,1,25,1,25,3,25,262,8,25,5,25,264,8,25,10,25,12,25,267,9,25,
        1,26,1,26,1,26,3,26,272,8,26,1,26,1,26,3,26,276,8,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,3,27,285,8,27,1,27,5,27,288,8,27,10,27,12,
        27,291,9,27,1,27,1,27,1,27,1,28,4,28,297,8,28,11,28,12,28,298,1,
        28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,0,6,1,0,16,19,2,0,26,27,46,48,1,0,6,7,
        1,0,35,37,2,0,3,3,34,34,2,0,4,4,45,45,311,0,59,1,0,0,0,2,73,1,0,
        0,0,4,75,1,0,0,0,6,77,1,0,0,0,8,79,1,0,0,0,10,81,1,0,0,0,12,89,1,
        0,0,0,14,97,1,0,0,0,16,105,1,0,0,0,18,117,1,0,0,0,20,126,1,0,0,0,
        22,130,1,0,0,0,24,152,1,0,0,0,26,162,1,0,0,0,28,164,1,0,0,0,30,166,
        1,0,0,0,32,171,1,0,0,0,34,183,1,0,0,0,36,189,1,0,0,0,38,201,1,0,
        0,0,40,209,1,0,0,0,42,211,1,0,0,0,44,214,1,0,0,0,46,234,1,0,0,0,
        48,238,1,0,0,0,50,254,1,0,0,0,52,268,1,0,0,0,54,279,1,0,0,0,56,296,
        1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,
        61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,74,3,10,
        5,0,66,74,3,8,4,0,67,74,3,30,15,0,68,74,3,32,16,0,69,74,3,34,17,
        0,70,74,3,44,22,0,71,74,3,48,24,0,72,74,3,54,27,0,73,65,1,0,0,0,
        73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,
        0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,7,0,0,0,76,
        5,1,0,0,0,77,78,7,1,0,0,78,7,1,0,0,0,79,80,7,2,0,0,80,9,1,0,0,0,
        81,86,3,12,6,0,82,83,5,1,0,0,83,85,3,12,6,0,84,82,1,0,0,0,85,88,
        1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,11,1,0,0,0,88,86,1,0,0,0,
        89,94,3,14,7,0,90,91,5,2,0,0,91,93,3,14,7,0,92,90,1,0,0,0,93,96,
        1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,13,1,0,0,0,96,94,1,0,0,0,
        97,102,3,16,8,0,98,99,5,28,0,0,99,101,3,16,8,0,100,98,1,0,0,0,101,
        104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,15,1,0,0,0,104,102,
        1,0,0,0,105,114,3,18,9,0,106,110,5,33,0,0,107,110,1,0,0,0,108,110,
        5,34,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,0,110,111,
        1,0,0,0,111,113,3,18,9,0,112,109,1,0,0,0,113,116,1,0,0,0,114,112,
        1,0,0,0,114,115,1,0,0,0,115,17,1,0,0,0,116,114,1,0,0,0,117,122,3,
        20,10,0,118,119,7,3,0,0,119,121,3,20,10,0,120,118,1,0,0,0,121,124,
        1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,19,1,0,0,0,124,122,1,
        0,0,0,125,127,7,4,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,
        0,0,0,128,129,3,22,11,0,129,21,1,0,0,0,130,143,3,24,12,0,131,132,
        5,31,0,0,132,142,5,49,0,0,133,134,5,40,0,0,134,135,3,10,5,0,135,
        136,5,41,0,0,136,142,1,0,0,0,137,138,5,38,0,0,138,139,3,26,13,0,
        139,140,5,39,0,0,140,142,1,0,0,0,141,131,1,0,0,0,141,133,1,0,0,0,
        141,137,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,
        144,23,1,0,0,0,145,143,1,0,0,0,146,147,5,38,0,0,147,148,3,10,5,0,
        148,149,5,39,0,0,149,153,1,0,0,0,150,153,5,49,0,0,151,153,3,6,3,
        0,152,146,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,25,1,0,0,0,
        154,159,3,10,5,0,155,156,5,44,0,0,156,158,3,10,5,0,157,155,1,0,0,
        0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,163,1,0,0,
        0,161,159,1,0,0,0,162,154,1,0,0,0,162,163,1,0,0,0,163,27,1,0,0,0,
        164,165,3,22,11,0,165,29,1,0,0,0,166,167,3,28,14,0,167,168,5,30,
        0,0,168,169,3,10,5,0,169,170,3,56,28,0,170,31,1,0,0,0,171,172,5,
        21,0,0,172,179,5,49,0,0,173,180,3,4,2,0,174,176,3,4,2,0,175,174,
        1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,5,32,0,0,178,180,
        3,10,5,0,179,173,1,0,0,0,179,175,1,0,0,0,180,181,1,0,0,0,181,182,
        3,56,28,0,182,33,1,0,0,0,183,184,5,20,0,0,184,185,5,49,0,0,185,186,
        5,32,0,0,186,187,3,10,5,0,187,188,3,56,28,0,188,35,1,0,0,0,189,190,
        5,21,0,0,190,194,5,49,0,0,191,192,5,40,0,0,192,193,5,47,0,0,193,
        195,5,41,0,0,194,191,1,0,0,0,195,196,1,0,0,0,196,194,1,0,0,0,196,
        197,1,0,0,0,197,198,1,0,0,0,198,199,3,4,2,0,199,200,3,56,28,0,200,
        37,1,0,0,0,201,202,5,49,0,0,202,203,3,4,2,0,203,39,1,0,0,0,204,205,
        3,38,19,0,205,206,5,44,0,0,206,207,3,40,20,0,207,210,1,0,0,0,208,
        210,3,38,19,0,209,204,1,0,0,0,209,208,1,0,0,0,210,41,1,0,0,0,211,
        212,5,49,0,0,212,213,5,49,0,0,213,43,1,0,0,0,214,219,5,12,0,0,215,
        216,5,38,0,0,216,217,3,42,21,0,217,218,5,39,0,0,218,220,1,0,0,0,
        219,215,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,222,5,49,0,0,
        222,224,5,38,0,0,223,225,3,40,20,0,224,223,1,0,0,0,224,225,1,0,0,
        0,225,226,1,0,0,0,226,228,5,39,0,0,227,229,3,4,2,0,228,227,1,0,0,
        0,228,229,1,0,0,0,229,230,1,0,0,0,230,231,5,42,0,0,231,232,5,43,
        0,0,232,233,3,56,28,0,233,45,1,0,0,0,234,235,5,49,0,0,235,236,3,
        4,2,0,236,237,3,56,28,0,237,47,1,0,0,0,238,239,5,13,0,0,239,240,
        5,49,0,0,240,241,5,14,0,0,241,243,5,42,0,0,242,244,3,56,28,0,243,
        242,1,0,0,0,243,244,1,0,0,0,244,248,1,0,0,0,245,247,3,46,23,0,246,
        245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,
        251,1,0,0,0,250,248,1,0,0,0,251,252,5,43,0,0,252,253,3,56,28,0,253,
        49,1,0,0,0,254,256,5,49,0,0,255,257,3,4,2,0,256,255,1,0,0,0,256,
        257,1,0,0,0,257,265,1,0,0,0,258,259,5,44,0,0,259,261,5,49,0,0,260,
        262,3,4,2,0,261,260,1,0,0,0,261,262,1,0,0,0,262,264,1,0,0,0,263,
        258,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,
        51,1,0,0,0,267,265,1,0,0,0,268,269,5,49,0,0,269,271,5,38,0,0,270,
        272,3,50,25,0,271,270,1,0,0,0,271,272,1,0,0,0,272,273,1,0,0,0,273,
        275,5,39,0,0,274,276,3,4,2,0,275,274,1,0,0,0,275,276,1,0,0,0,276,
        277,1,0,0,0,277,278,3,56,28,0,278,53,1,0,0,0,279,280,5,13,0,0,280,
        281,5,49,0,0,281,282,5,15,0,0,282,284,5,42,0,0,283,285,3,56,28,0,
        284,283,1,0,0,0,284,285,1,0,0,0,285,289,1,0,0,0,286,288,3,52,26,
        0,287,286,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,
        0,290,292,1,0,0,0,291,289,1,0,0,0,292,293,5,43,0,0,293,294,3,56,
        28,0,294,55,1,0,0,0,295,297,7,5,0,0,296,295,1,0,0,0,297,298,1,0,
        0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,57,1,0,0,0,31,61,73,86,94,
        102,109,114,122,126,141,143,152,159,162,175,179,196,209,219,224,
        228,243,248,256,261,265,271,275,284,289,298
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'||'", "'&&'", "'!'", "'\\n'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'nil'", 
                     "'true'", "'false'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NL", "WS", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "IF_", 
                      "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                      "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                      "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                      "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "OP3", 
                      "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", 
                      "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
                      "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_data_type = 2
    RULE_literal = 3
    RULE_comment = 4
    RULE_expr0 = 5
    RULE_expr1 = 6
    RULE_expr2 = 7
    RULE_expr3 = 8
    RULE_expr4 = 9
    RULE_expr5 = 10
    RULE_expr6 = 11
    RULE_expr7 = 12
    RULE_expr_list = 13
    RULE_lhs = 14
    RULE_assigning = 15
    RULE_vardecl = 16
    RULE_constdecl = 17
    RULE_arraydecl = 18
    RULE_parameter = 19
    RULE_parameterlst = 20
    RULE_receiver = 21
    RULE_funcdecl = 22
    RULE_fielddecl = 23
    RULE_structdecl = 24
    RULE_method_para_list = 25
    RULE_methoddecl = 26
    RULE_interfacedecl = 27
    RULE_end_stm = 28

    ruleNames =  [ "program", "decl", "data_type", "literal", "comment", 
                   "expr0", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr_list", "lhs", "assigning", "vardecl", 
                   "constdecl", "arraydecl", "parameter", "parameterlst", 
                   "receiver", "funcdecl", "fielddecl", "structdecl", "method_para_list", 
                   "methoddecl", "interfacedecl", "end_stm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NL=4
    WS=5
    SINGLE_LINE_CMT=6
    MULTI_LINE_CMT=7
    IF_=8
    ELSE_=9
    FOR_=10
    RETURN_=11
    FUNC_=12
    TYPE_=13
    STRUCT_=14
    INTERFACE_=15
    STRING_=16
    INT_=17
    FLOAT_=18
    BOOLEAN_=19
    CONST_=20
    VAR_=21
    CONTINUE_=22
    BREAK_=23
    RANGE_=24
    NIL_=25
    TRUE_=26
    FALSE_=27
    COMPARISON_OP=28
    OP3=29
    ASSIGN1=30
    OP5=31
    ASSIGN=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    LPAREN=38
    RPAREN=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    COMMA=44
    SEMICOLON=45
    FLOAT=46
    INTEGER=47
    STRING=48
    ID=49
    ERROR_CHAR=50
    ILLEGAL_ESCAPE=51
    UNCLOSE_STRING=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.decl()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1055823424925896) != 0)):
                    break

            self.state = 63
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

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def comment(self):
            return self.getTypedRuleContext(MiniGoParser.CommentContext,0)


        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.expr0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.comment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.assigning()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.vardecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.constdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.funcdecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.structdecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.interfacedecl()
                pass


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




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
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


    class LiteralContext(ParserRuleContext):
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
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581410570240) != 0)):
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_CMT(self):
            return self.getToken(MiniGoParser.SINGLE_LINE_CMT, 0)

        def MULTI_LINE_CMT(self):
            return self.getToken(MiniGoParser.MULTI_LINE_CMT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_comment




    def comment(self):

        localctx = MiniGoParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr1Context,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr0




    def expr0(self):

        localctx = MiniGoParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expr1()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 82
                self.match(MiniGoParser.T__0)
                self.state = 83
                self.expr1()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr2Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr2Context,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1




    def expr1(self):

        localctx = MiniGoParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expr2()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 90
                self.match(MiniGoParser.T__1)
                self.state = 91
                self.expr2()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr3Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr3Context,i)


        def COMPARISON_OP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMPARISON_OP)
            else:
                return self.getToken(MiniGoParser.COMPARISON_OP, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2




    def expr2(self):

        localctx = MiniGoParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expr3()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 98
                self.match(MiniGoParser.COMPARISON_OP)
                self.state = 99
                self.expr3()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr4Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr4Context,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ADD)
            else:
                return self.getToken(MiniGoParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SUB)
            else:
                return self.getToken(MiniGoParser.SUB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3




    def expr3(self):

        localctx = MiniGoParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expr4()
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 106
                        self.match(MiniGoParser.ADD)
                        pass

                    elif la_ == 2:
                        pass

                    elif la_ == 3:
                        self.state = 108
                        self.match(MiniGoParser.SUB)
                        pass


                    self.state = 111
                    self.expr4() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr5Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr5Context,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MUL)
            else:
                return self.getToken(MiniGoParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DIV)
            else:
                return self.getToken(MiniGoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MOD)
            else:
                return self.getToken(MiniGoParser.MOD, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4




    def expr4(self):

        localctx = MiniGoParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expr5()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0):
                self.state = 118
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.expr5()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==34:
                self.state = 125
                _la = self._input.LA(1)
                if not(_la==3 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 128
            self.expr6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def OP5(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OP5)
            else:
                return self.getToken(MiniGoParser.OP5, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr_listContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expr7()
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [31]:
                        self.state = 131
                        self.match(MiniGoParser.OP5)
                        self.state = 132
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [40]:
                        self.state = 133
                        self.match(MiniGoParser.LSB)
                        self.state = 134
                        self.expr0()
                        self.state = 135
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [38]:
                        self.state = 137
                        self.match(MiniGoParser.LPAREN)
                        self.state = 138
                        self.expr_list()
                        self.state = 139
                        self.match(MiniGoParser.RPAREN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr7)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MiniGoParser.LPAREN)
                self.state = 147
                self.expr0()
                self.state = 148
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(MiniGoParser.ID)
                pass
            elif token in [26, 27, 46, 47, 48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.literal()
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1055823421767688) != 0):
                self.state = 154
                self.expr0()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 155
                    self.match(MiniGoParser.COMMA)
                    self.state = 156
                    self.expr0()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.expr6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning




    def assigning(self):

        localctx = MiniGoParser.AssigningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.lhs()
            self.state = 167
            self.match(MiniGoParser.ASSIGN1)
            self.state = 168
            self.expr0()
            self.state = 169
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MiniGoParser.VAR_)
            self.state = 172
            self.match(MiniGoParser.ID)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 173
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                    self.state = 174
                    self.data_type()


                self.state = 177
                self.match(MiniGoParser.ASSIGN)
                self.state = 178
                self.expr0()
                pass


            self.state = 181
            self.end_stm()
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

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.CONST_)
            self.state = 184
            self.match(MiniGoParser.ID)
            self.state = 185
            self.match(MiniGoParser.ASSIGN)
            self.state = 186
            self.expr0()
            self.state = 187
            self.end_stm()
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.VAR_)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 194 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 191
                self.match(MiniGoParser.LSB)
                self.state = 192
                self.match(MiniGoParser.INTEGER)
                self.state = 193
                self.match(MiniGoParser.RSB)
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==40):
                    break

            self.state = 198
            self.data_type()
            self.state = 199
            self.end_stm()
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




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.ID)
            self.state = 202
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




    def parameterlst(self):

        localctx = MiniGoParser.ParameterlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameterlst)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.parameter()
                self.state = 205
                self.match(MiniGoParser.COMMA)
                self.state = 206
                self.parameterlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
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




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.ID)
            self.state = 212
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MiniGoParser.FUNC_)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 215
                self.match(MiniGoParser.LPAREN)
                self.state = 216
                self.receiver()
                self.state = 217
                self.match(MiniGoParser.RPAREN)


            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 222
            self.match(MiniGoParser.LPAREN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 223
                self.parameterlst()


            self.state = 226
            self.match(MiniGoParser.RPAREN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 227
                self.data_type()


            self.state = 230
            self.match(MiniGoParser.LCB)
            self.state = 231
            self.match(MiniGoParser.RCB)
            self.state = 232
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.ID)
            self.state = 235
            self.data_type()
            self.state = 236
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT_(self):
            return self.getToken(MiniGoParser.STRUCT_, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_stmContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_stmContext,i)


        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.TYPE_)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 240
            self.match(MiniGoParser.STRUCT_)
            self.state = 241
            self.match(MiniGoParser.LCB)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==45:
                self.state = 242
                self.end_stm()


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 245
                self.fielddecl()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(MiniGoParser.RCB)
            self.state = 252
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def data_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Data_typeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Data_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_para_list




    def method_para_list(self):

        localctx = MiniGoParser.Method_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.ID)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 255
                self.data_type()


            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 258
                self.match(MiniGoParser.COMMA)
                self.state = 259
                self.match(MiniGoParser.ID)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                    self.state = 260
                    self.data_type()


                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def method_para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_para_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.ID)
            self.state = 269
            self.match(MiniGoParser.LPAREN)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 270
                self.method_para_list()


            self.state = 273
            self.match(MiniGoParser.RPAREN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 274
                self.data_type()


            self.state = 277
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_stmContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_stmContext,i)


        def methoddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethoddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.TYPE_)
            self.state = 280
            self.match(MiniGoParser.ID)
            self.state = 281
            self.match(MiniGoParser.INTERFACE_)
            self.state = 282
            self.match(MiniGoParser.LCB)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==45:
                self.state = 283
                self.end_stm()


            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 286
                self.methoddecl()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 292
            self.match(MiniGoParser.RCB)
            self.state = 293
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stm




    def end_stm(self):

        localctx = MiniGoParser.End_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==4 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==45):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





