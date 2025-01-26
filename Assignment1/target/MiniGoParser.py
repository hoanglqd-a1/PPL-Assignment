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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\6\2")
        buf.write("\\\n\2\r\2\16\2]\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3g\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4s\n\4\3\5")
        buf.write("\3\5\3\5\7\5x\n\5\f\5\16\5{\13\5\3\6\3\6\3\6\7\6\u0080")
        buf.write("\n\6\f\6\16\6\u0083\13\6\3\7\3\7\3\7\7\7\u0088\n\7\f\7")
        buf.write("\16\7\u008b\13\7\3\b\3\b\3\b\3\b\5\b\u0091\n\b\3\b\7\b")
        buf.write("\u0094\n\b\f\b\16\b\u0097\13\b\3\t\3\t\3\t\7\t\u009c\n")
        buf.write("\t\f\t\16\t\u009f\13\t\3\n\5\n\u00a2\n\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00b1\n\13\f\13\16\13\u00b4\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00bc\n\f\3\r\3\r\3\r\7\r\u00c1\n\r\f\r\16\r")
        buf.write("\u00c4\13\r\5\r\u00c6\n\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u00d3\n\20\3\20\3\20\5")
        buf.write("\20\u00d7\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\6\22\u00e7\n\22\r\22\16")
        buf.write("\22\u00e8\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23")
        buf.write("\u00f3\n\23\3\24\3\24\3\24\7\24\u00f8\n\24\f\24\16\24")
        buf.write("\u00fb\13\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0107\n\27\3\27\3\27\3\27\5\27\u010c\n\27")
        buf.write("\3\27\3\27\5\27\u0110\n\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u011d\n\30\f\30\16\30")
        buf.write("\u0120\13\30\3\30\3\30\5\30\u0124\n\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u012d\n\31\3\31\7\31\u0130\n")
        buf.write("\31\f\31\16\31\u0133\13\31\3\31\3\31\3\31\3\32\3\32\5")
        buf.write("\32\u013a\n\32\3\32\3\32\3\32\5\32\u013f\n\32\7\32\u0141")
        buf.write("\n\32\f\32\16\32\u0144\13\32\3\33\3\33\3\33\5\33\u0149")
        buf.write("\n\33\3\33\3\33\5\33\u014d\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0156\n\34\3\34\7\34\u0159\n\34\f\34")
        buf.write("\16\34\u015c\13\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u0169\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u0174\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \7 \u017d\n \f \16 \u0180\13 \3 ")
        buf.write("\5 \u0183\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\5!\u0196\n!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\5&\u01ad\n&\3&\7&\u01b0")
        buf.write("\n&\f&\16&\u01b3\13&\3\'\3\'\5\'\u01b7\n\'\3(\3(\3(\3")
        buf.write("(\7(\u01bd\n(\f(\16(\u01c0\13(\5(\u01c2\n(\3(\3(\3)\3")
        buf.write(")\3)\3)\6)\u01ca\n)\r)\16)\u01cb\3)\3)\3)\3*\3*\3*\5*")
        buf.write("\u01d4\n*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\5,\u01e0\n,\3")
        buf.write("-\6-\u01e3\n-\r-\16-\u01e4\3-\5-\u01e8\n-\3-\2\2.\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVX\2\6\3\2&(\4\2\5\5%%\3\2\23\26\4\2")
        buf.write("\t\t\60\60\2\u0202\2[\3\2\2\2\4f\3\2\2\2\6r\3\2\2\2\b")
        buf.write("t\3\2\2\2\n|\3\2\2\2\f\u0084\3\2\2\2\16\u008c\3\2\2\2")
        buf.write("\20\u0098\3\2\2\2\22\u00a1\3\2\2\2\24\u00a5\3\2\2\2\26")
        buf.write("\u00bb\3\2\2\2\30\u00c5\3\2\2\2\32\u00c7\3\2\2\2\34\u00c9")
        buf.write("\3\2\2\2\36\u00ce\3\2\2\2 \u00da\3\2\2\2\"\u00e0\3\2\2")
        buf.write("\2$\u00ef\3\2\2\2&\u00f4\3\2\2\2(\u00fc\3\2\2\2*\u00ff")
        buf.write("\3\2\2\2,\u0101\3\2\2\2.\u0116\3\2\2\2\60\u0127\3\2\2")
        buf.write("\2\62\u0137\3\2\2\2\64\u0145\3\2\2\2\66\u0150\3\2\2\2")
        buf.write("8\u0160\3\2\2\2:\u016a\3\2\2\2<\u0175\3\2\2\2>\u017a\3")
        buf.write("\2\2\2@\u0186\3\2\2\2B\u019c\3\2\2\2D\u019f\3\2\2\2F\u01a2")
        buf.write("\3\2\2\2H\u01a8\3\2\2\2J\u01ac\3\2\2\2L\u01b6\3\2\2\2")
        buf.write("N\u01b8\3\2\2\2P\u01c9\3\2\2\2R\u01d0\3\2\2\2T\u01d7\3")
        buf.write("\2\2\2V\u01df\3\2\2\2X\u01e7\3\2\2\2Z\\\5\4\3\2[Z\3\2")
        buf.write("\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\2\2")
        buf.write("\3`\3\3\2\2\2ag\5\b\5\2bg\5\6\4\2cg\5,\27\2dg\5\60\31")
        buf.write("\2eg\5\66\34\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2\2")
        buf.write("fe\3\2\2\2g\5\3\2\2\2hs\5\34\17\2is\5\36\20\2js\5\"\22")
        buf.write("\2ks\5 \21\2ls\5> \2ms\5@!\2ns\5D#\2os\5B\"\2ps\5F$\2")
        buf.write("qs\5H%\2rh\3\2\2\2ri\3\2\2\2rj\3\2\2\2rk\3\2\2\2rl\3\2")
        buf.write("\2\2rm\3\2\2\2rn\3\2\2\2ro\3\2\2\2rp\3\2\2\2rq\3\2\2\2")
        buf.write("s\7\3\2\2\2ty\5\n\6\2uv\7\3\2\2vx\5\n\6\2wu\3\2\2\2x{")
        buf.write("\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\t\3\2\2\2{y\3\2\2\2|\u0081")
        buf.write("\5\f\7\2}~\7\4\2\2~\u0080\5\f\7\2\177}\3\2\2\2\u0080\u0083")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\13")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0089\5\16\b\2\u0085")
        buf.write("\u0086\7\37\2\2\u0086\u0088\5\16\b\2\u0087\u0085\3\2\2")
        buf.write("\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\r\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u0095")
        buf.write("\5\20\t\2\u008d\u0091\7$\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u0091\7%\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\5")
        buf.write("\20\t\2\u0093\u0090\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\17\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0098\u009d\5\22\n\2\u0099\u009a\t\2\2")
        buf.write("\2\u009a\u009c\5\22\n\2\u009b\u0099\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\21\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2\t\3\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\5\24\13\2\u00a4\23\3\2\2\2\u00a5\u00b2\5")
        buf.write("\26\f\2\u00a6\u00a7\7\"\2\2\u00a7\u00b1\7\64\2\2\u00a8")
        buf.write("\u00a9\7+\2\2\u00a9\u00aa\5\b\5\2\u00aa\u00ab\7,\2\2\u00ab")
        buf.write("\u00b1\3\2\2\2\u00ac\u00ad\7)\2\2\u00ad\u00ae\5\30\r\2")
        buf.write("\u00ae\u00af\7*\2\2\u00af\u00b1\3\2\2\2\u00b0\u00a6\3")
        buf.write("\2\2\2\u00b0\u00a8\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\25\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7)\2\2\u00b6")
        buf.write("\u00b7\5\b\5\2\u00b7\u00b8\7*\2\2\u00b8\u00bc\3\2\2\2")
        buf.write("\u00b9\u00bc\7\64\2\2\u00ba\u00bc\5V,\2\u00bb\u00b5\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\27")
        buf.write("\3\2\2\2\u00bd\u00c2\5\b\5\2\u00be\u00bf\7/\2\2\u00bf")
        buf.write("\u00c1\5\b\5\2\u00c0\u00be\3\2\2\2\u00c1\u00c4\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c6\3")
        buf.write("\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00bd\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\31\3\2\2\2\u00c7\u00c8\5\24\13\2\u00c8")
        buf.write("\33\3\2\2\2\u00c9\u00ca\5\32\16\2\u00ca\u00cb\7!\2\2\u00cb")
        buf.write("\u00cc\5\b\5\2\u00cc\u00cd\5X-\2\u00cd\35\3\2\2\2\u00ce")
        buf.write("\u00cf\7\30\2\2\u00cf\u00d6\7\64\2\2\u00d0\u00d7\5T+\2")
        buf.write("\u00d1\u00d3\5T+\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2")
        buf.write("\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7#\2\2\u00d5\u00d7")
        buf.write("\5\b\5\2\u00d6\u00d0\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\5X-\2\u00d9\37\3\2\2\2\u00da")
        buf.write("\u00db\7\27\2\2\u00db\u00dc\7\64\2\2\u00dc\u00dd\7#\2")
        buf.write("\2\u00dd\u00de\5\b\5\2\u00de\u00df\5X-\2\u00df!\3\2\2")
        buf.write("\2\u00e0\u00e1\7\30\2\2\u00e1\u00e6\7\64\2\2\u00e2\u00e3")
        buf.write("\7+\2\2\u00e3\u00e4\5\b\5\2\u00e4\u00e5\7,\2\2\u00e5\u00e7")
        buf.write("\3\2\2\2\u00e6\u00e2\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\5T+\2\u00eb\u00ec\7#\2\2\u00ec\u00ed\5P)")
        buf.write("\2\u00ed\u00ee\5X-\2\u00ee#\3\2\2\2\u00ef\u00f2\7\64\2")
        buf.write("\2\u00f0\u00f3\5T+\2\u00f1\u00f3\7\64\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3%\3\2\2\2\u00f4\u00f9")
        buf.write("\5$\23\2\u00f5\u00f6\7/\2\2\u00f6\u00f8\5$\23\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\'\3\2\2\2\u00fb\u00f9\3\2\2")
        buf.write("\2\u00fc\u00fd\7\64\2\2\u00fd\u00fe\7\64\2\2\u00fe)\3")
        buf.write("\2\2\2\u00ff\u0100\3\2\2\2\u0100+\3\2\2\2\u0101\u0106")
        buf.write("\7\17\2\2\u0102\u0103\7)\2\2\u0103\u0104\5(\25\2\u0104")
        buf.write("\u0105\7*\2\2\u0105\u0107\3\2\2\2\u0106\u0102\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7")
        buf.write("\64\2\2\u0109\u010b\7)\2\2\u010a\u010c\5&\24\2\u010b\u010a")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010f\7*\2\2\u010e\u0110\5T+\2\u010f\u010e\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\7-\2\2")
        buf.write("\u0112\u0113\5*\26\2\u0113\u0114\7.\2\2\u0114\u0115\5")
        buf.write("X-\2\u0115-\3\2\2\2\u0116\u0123\7\64\2\2\u0117\u011e\5")
        buf.write("T+\2\u0118\u0119\7+\2\2\u0119\u011a\5\b\5\2\u011a\u011b")
        buf.write("\7,\2\2\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f\u0124\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0124\7")
        buf.write("\64\2\2\u0122\u0124\7\22\2\2\u0123\u0117\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0126\5X-\2\u0126/\3\2\2\2\u0127\u0128\7\20\2\2")
        buf.write("\u0128\u0129\7\64\2\2\u0129\u012a\7\21\2\2\u012a\u012c")
        buf.write("\7-\2\2\u012b\u012d\5X-\2\u012c\u012b\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u0131\3\2\2\2\u012e\u0130\5.\30\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0134\u0135\7.\2\2\u0135\u0136\5X-\2\u0136\61\3")
        buf.write("\2\2\2\u0137\u0139\7\64\2\2\u0138\u013a\5T+\2\u0139\u0138")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0142\3\2\2\2\u013b")
        buf.write("\u013c\7/\2\2\u013c\u013e\7\64\2\2\u013d\u013f\5T+\2\u013e")
        buf.write("\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2")
        buf.write("\u0140\u013b\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\63\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0146\7\64\2\2\u0146\u0148\7)\2\2\u0147")
        buf.write("\u0149\5\62\32\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2")
        buf.write("\2\u0149\u014a\3\2\2\2\u014a\u014c\7*\2\2\u014b\u014d")
        buf.write("\5T+\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\5X-\2\u014f\65\3\2\2\2\u0150\u0151")
        buf.write("\7\20\2\2\u0151\u0152\7\64\2\2\u0152\u0153\7\22\2\2\u0153")
        buf.write("\u0155\7-\2\2\u0154\u0156\5X-\2\u0155\u0154\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u015a\3\2\2\2\u0157\u0159\5\64\33")
        buf.write("\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015d\u015e\7.\2\2\u015e\u015f\5X-\2\u015f")
        buf.write("\67\3\2\2\2\u0160\u0161\7\13\2\2\u0161\u0162\7)\2\2\u0162")
        buf.write("\u0163\5\b\5\2\u0163\u0164\7*\2\2\u0164\u0165\7-\2\2\u0165")
        buf.write("\u0166\5J&\2\u0166\u0168\7.\2\2\u0167\u0169\5X-\2\u0168")
        buf.write("\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u01699\3\2\2\2\u016a")
        buf.write("\u016b\7\f\2\2\u016b\u016c\7\13\2\2\u016c\u016d\7)\2\2")
        buf.write("\u016d\u016e\5\b\5\2\u016e\u016f\7*\2\2\u016f\u0170\7")
        buf.write("-\2\2\u0170\u0171\5J&\2\u0171\u0173\7.\2\2\u0172\u0174")
        buf.write("\5X-\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174;")
        buf.write("\3\2\2\2\u0175\u0176\7\f\2\2\u0176\u0177\7-\2\2\u0177")
        buf.write("\u0178\5J&\2\u0178\u0179\7.\2\2\u0179=\3\2\2\2\u017a\u017e")
        buf.write("\58\35\2\u017b\u017d\5:\36\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0183\5")
        buf.write("<\37\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0185\5X-\2\u0185?\3\2\2\2\u0186\u0195")
        buf.write("\7\r\2\2\u0187\u0196\5\b\5\2\u0188\u0189\5\34\17\2\u0189")
        buf.write("\u018a\5\b\5\2\u018a\u018b\7\60\2\2\u018b\u018c\5\32\16")
        buf.write("\2\u018c\u018d\5\34\17\2\u018d\u018e\5\b\5\2\u018e\u0196")
        buf.write("\3\2\2\2\u018f\u0190\7\64\2\2\u0190\u0191\7/\2\2\u0191")
        buf.write("\u0192\7\64\2\2\u0192\u0193\7\6\2\2\u0193\u0194\7\33\2")
        buf.write("\2\u0194\u0196\7\64\2\2\u0195\u0187\3\2\2\2\u0195\u0188")
        buf.write("\3\2\2\2\u0195\u018f\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0198\7-\2\2\u0198\u0199\5J&\2\u0199\u019a\7.\2\2\u019a")
        buf.write("\u019b\5X-\2\u019bA\3\2\2\2\u019c\u019d\7\32\2\2\u019d")
        buf.write("\u019e\5X-\2\u019eC\3\2\2\2\u019f\u01a0\7\31\2\2\u01a0")
        buf.write("\u01a1\5X-\2\u01a1E\3\2\2\2\u01a2\u01a3\5\24\13\2\u01a3")
        buf.write("\u01a4\7)\2\2\u01a4\u01a5\5\30\r\2\u01a5\u01a6\7*\2\2")
        buf.write("\u01a6\u01a7\5X-\2\u01a7G\3\2\2\2\u01a8\u01a9\7\16\2\2")
        buf.write("\u01a9\u01aa\5X-\2\u01aaI\3\2\2\2\u01ab\u01ad\5X-\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b1\3\2\2\2")
        buf.write("\u01ae\u01b0\5\6\4\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2K")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b7\5\b\5\2\u01b5")
        buf.write("\u01b7\5N(\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write("M\3\2\2\2\u01b8\u01c1\7-\2\2\u01b9\u01be\5L\'\2\u01ba")
        buf.write("\u01bb\7/\2\2\u01bb\u01bd\5L\'\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01b9\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4")
        buf.write("\7.\2\2\u01c4O\3\2\2\2\u01c5\u01c6\7+\2\2\u01c6\u01c7")
        buf.write("\5\b\5\2\u01c7\u01c8\7,\2\2\u01c8\u01ca\3\2\2\2\u01c9")
        buf.write("\u01c5\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\5")
        buf.write("T+\2\u01ce\u01cf\5N(\2\u01cfQ\3\2\2\2\u01d0\u01d1\7\64")
        buf.write("\2\2\u01d1\u01d3\7-\2\2\u01d2\u01d4\5&\24\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d6\7.\2\2\u01d6S\3\2\2\2\u01d7\u01d8\t\4\2\2\u01d8")
        buf.write("U\3\2\2\2\u01d9\u01e0\7\62\2\2\u01da\u01e0\7\61\2\2\u01db")
        buf.write("\u01e0\7\63\2\2\u01dc\u01e0\7\35\2\2\u01dd\u01e0\7\36")
        buf.write("\2\2\u01de\u01e0\5R*\2\u01df\u01d9\3\2\2\2\u01df\u01da")
        buf.write("\3\2\2\2\u01df\u01db\3\2\2\2\u01df\u01dc\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0W\3\2\2\2\u01e1")
        buf.write("\u01e3\t\5\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e8\3")
        buf.write("\2\2\2\u01e6\u01e8\7\2\2\3\u01e7\u01e2\3\2\2\2\u01e7\u01e6")
        buf.write("\3\2\2\2\u01e8Y\3\2\2\2\63]fry\u0081\u0089\u0090\u0095")
        buf.write("\u009d\u00a1\u00b0\u00b2\u00bb\u00c2\u00c5\u00d2\u00d6")
        buf.write("\u00e8\u00f2\u00f9\u0106\u010b\u010f\u011e\u0123\u012c")
        buf.write("\u0131\u0139\u013e\u0142\u0148\u014c\u0155\u015a\u0168")
        buf.write("\u0173\u017e\u0182\u0195\u01ac\u01b1\u01b6\u01be\u01c1")
        buf.write("\u01cb\u01d3\u01df\u01e4\u01e7")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'||'", "'&&'", "'!'", "':='", "<INVALID>", 
                     "<INVALID>", "'\n'", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
                      "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", 
                      "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
                      "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_statement = 2
    RULE_expr0 = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_expr3 = 6
    RULE_expr4 = 7
    RULE_expr5 = 8
    RULE_expr6 = 9
    RULE_expr7 = 10
    RULE_expr_list = 11
    RULE_lhs = 12
    RULE_assigning = 13
    RULE_vardecl = 14
    RULE_constdecl = 15
    RULE_arraydecl = 16
    RULE_parameter = 17
    RULE_parameterlst = 18
    RULE_receiver = 19
    RULE_func_body = 20
    RULE_funcdecl = 21
    RULE_fielddecl = 22
    RULE_structdecl = 23
    RULE_method_para_list = 24
    RULE_methoddecl = 25
    RULE_interfacedecl = 26
    RULE_if_ = 27
    RULE_elseif_ = 28
    RULE_else_ = 29
    RULE_ifelse_stat = 30
    RULE_forloop_stat = 31
    RULE_break_stat = 32
    RULE_continue_stat = 33
    RULE_funccall_stat = 34
    RULE_return_stat = 35
    RULE_blockcode = 36
    RULE_arr_elem = 37
    RULE_arr_elem_list = 38
    RULE_arr_literal = 39
    RULE_struct_literal = 40
    RULE_data_type = 41
    RULE_literal = 42
    RULE_end_stm = 43

    ruleNames =  [ "program", "decl", "statement", "expr0", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr_list", 
                   "lhs", "assigning", "vardecl", "constdecl", "arraydecl", 
                   "parameter", "parameterlst", "receiver", "func_body", 
                   "funcdecl", "fielddecl", "structdecl", "method_para_list", 
                   "methoddecl", "interfacedecl", "if_", "elseif_", "else_", 
                   "ifelse_stat", "forloop_stat", "break_stat", "continue_stat", 
                   "funccall_stat", "return_stat", "blockcode", "arr_elem", 
                   "arr_elem_list", "arr_literal", "struct_literal", "data_type", 
                   "literal", "end_stm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SINGLE_LINE_CMT=5
    MULTI_LINE_CMT=6
    NL=7
    WS=8
    IF_=9
    ELSE_=10
    FOR_=11
    RETURN_=12
    FUNC_=13
    TYPE_=14
    STRUCT_=15
    INTERFACE_=16
    STRING_=17
    INT_=18
    FLOAT_=19
    BOOLEAN_=20
    CONST_=21
    VAR_=22
    CONTINUE_=23
    BREAK_=24
    RANGE_=25
    NIL_=26
    TRUE_=27
    FALSE_=28
    COMPARISON_OP=29
    OP3=30
    ASSIGN1=31
    OP5=32
    ASSIGN=33
    ADD=34
    SUB=35
    MUL=36
    DIV=37
    MOD=38
    LPAREN=39
    RPAREN=40
    LSB=41
    RSB=42
    LCB=43
    RCB=44
    COMMA=45
    SEMICOLON=46
    FLOAT=47
    INTEGER=48
    STRING=49
    ID=50
    ERROR_CHAR=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53

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
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self.decl()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.FUNC_) | (1 << MiniGoParser.TYPE_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 93
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


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.expr0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.funcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.interfacedecl()
                pass


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

        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def ifelse_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_statContext,0)


        def forloop_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statContext,0)


        def funccall_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 111
                self.return_stat()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)




    def expr0(self):

        localctx = MiniGoParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expr1()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 115
                self.match(MiniGoParser.T__0)
                self.state = 116
                self.expr1()
                self.state = 121
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MiniGoParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.expr2()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1:
                self.state = 123
                self.match(MiniGoParser.T__1)
                self.state = 124
                self.expr2()
                self.state = 129
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = MiniGoParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expr3()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMPARISON_OP:
                self.state = 131
                self.match(MiniGoParser.COMPARISON_OP)
                self.state = 132
                self.expr3()
                self.state = 137
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = MiniGoParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expr4()
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 139
                        self.match(MiniGoParser.ADD)
                        pass

                    elif la_ == 2:
                        pass

                    elif la_ == 3:
                        self.state = 141
                        self.match(MiniGoParser.SUB)
                        pass


                    self.state = 144
                    self.expr4() 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MiniGoParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expr5()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 151
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.expr5()
                self.state = 157
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__2 or _la==MiniGoParser.SUB:
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 161
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.expr7()
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 174
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.OP5]:
                        self.state = 164
                        self.match(MiniGoParser.OP5)
                        self.state = 165
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LSB]:
                        self.state = 166
                        self.match(MiniGoParser.LSB)
                        self.state = 167
                        self.expr0()
                        self.state = 168
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.LPAREN]:
                        self.state = 170
                        self.match(MiniGoParser.LPAREN)
                        self.state = 171
                        self.expr_list()
                        self.state = 172
                        self.match(MiniGoParser.RPAREN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr7)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(MiniGoParser.LPAREN)
                self.state = 180
                self.expr0()
                self.state = 181
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.literal()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 187
                self.expr0()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 188
                    self.match(MiniGoParser.COMMA)
                    self.state = 189
                    self.expr0()
                    self.state = 194
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigning" ):
                return visitor.visitAssigning(self)
            else:
                return visitor.visitChildren(self)




    def assigning(self):

        localctx = MiniGoParser.AssigningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.lhs()
            self.state = 200
            self.match(MiniGoParser.ASSIGN1)
            self.state = 201
            self.expr0()
            self.state = 202
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.VAR_)
            self.state = 205
            self.match(MiniGoParser.ID)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 206
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 207
                    self.data_type()


                self.state = 210
                self.match(MiniGoParser.ASSIGN)
                self.state = 211
                self.expr0()
                pass


            self.state = 214
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.CONST_)
            self.state = 217
            self.match(MiniGoParser.ID)
            self.state = 218
            self.match(MiniGoParser.ASSIGN)
            self.state = 219
            self.expr0()
            self.state = 220
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


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.VAR_)
            self.state = 223
            self.match(MiniGoParser.ID)
            self.state = 228 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 224
                self.match(MiniGoParser.LSB)
                self.state = 225
                self.expr0()
                self.state = 226
                self.match(MiniGoParser.RSB)
                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 232
            self.data_type()
            self.state = 233
            self.match(MiniGoParser.ASSIGN)
            self.state = 234
            self.arr_literal()
            self.state = 235
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

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
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MiniGoParser.ID)
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.state = 238
                self.data_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 239
                self.match(MiniGoParser.ID)
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


    class ParameterlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlst" ):
                return visitor.visitParameterlst(self)
            else:
                return visitor.visitChildren(self)




    def parameterlst(self):

        localctx = MiniGoParser.ParameterlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameterlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.parameter()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 243
                self.match(MiniGoParser.COMMA)
                self.state = 244
                self.parameter()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 38, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = MiniGoParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def func_body(self):
            return self.getTypedRuleContext(MiniGoParser.Func_bodyContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MiniGoParser.FUNC_)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 256
                self.match(MiniGoParser.LPAREN)
                self.state = 257
                self.receiver()
                self.state = 258
                self.match(MiniGoParser.RPAREN)


            self.state = 262
            self.match(MiniGoParser.ID)
            self.state = 263
            self.match(MiniGoParser.LPAREN)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 264
                self.parameterlst()


            self.state = 267
            self.match(MiniGoParser.RPAREN)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 268
                self.data_type()


            self.state = 271
            self.match(MiniGoParser.LCB)
            self.state = 272
            self.func_body()
            self.state = 273
            self.match(MiniGoParser.RCB)
            self.state = 274
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

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

        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.ID)
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.state = 277
                self.data_type()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LSB:
                    self.state = 278
                    self.match(MiniGoParser.LSB)
                    self.state = 279
                    self.expr0()
                    self.state = 280
                    self.match(MiniGoParser.RSB)
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.ID]:
                self.state = 287
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INTERFACE_]:
                self.state = 288
                self.match(MiniGoParser.INTERFACE_)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 291
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.TYPE_)
            self.state = 294
            self.match(MiniGoParser.ID)
            self.state = 295
            self.match(MiniGoParser.STRUCT_)
            self.state = 296
            self.match(MiniGoParser.LCB)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 297
                self.end_stm()


            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 300
                self.fielddecl()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(MiniGoParser.RCB)
            self.state = 307
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_para_list" ):
                return visitor.visitMethod_para_list(self)
            else:
                return visitor.visitChildren(self)




    def method_para_list(self):

        localctx = MiniGoParser.Method_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MiniGoParser.ID)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 310
                self.data_type()


            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 313
                self.match(MiniGoParser.COMMA)
                self.state = 314
                self.match(MiniGoParser.ID)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 315
                    self.data_type()


                self.state = 322
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.ID)
            self.state = 324
            self.match(MiniGoParser.LPAREN)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 325
                self.method_para_list()


            self.state = 328
            self.match(MiniGoParser.RPAREN)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 329
                self.data_type()


            self.state = 332
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.TYPE_)
            self.state = 335
            self.match(MiniGoParser.ID)
            self.state = 336
            self.match(MiniGoParser.INTERFACE_)
            self.state = 337
            self.match(MiniGoParser.LCB)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 338
                self.end_stm()


            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 341
                self.methoddecl()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 347
            self.match(MiniGoParser.RCB)
            self.state = 348
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_" ):
                return visitor.visitIf_(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = MiniGoParser.If_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.IF_)
            self.state = 351
            self.match(MiniGoParser.LPAREN)
            self.state = 352
            self.expr0()
            self.state = 353
            self.match(MiniGoParser.RPAREN)
            self.state = 354
            self.match(MiniGoParser.LCB)
            self.state = 355
            self.blockcode()
            self.state = 356
            self.match(MiniGoParser.RCB)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 357
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_" ):
                return visitor.visitElseif_(self)
            else:
                return visitor.visitChildren(self)




    def elseif_(self):

        localctx = MiniGoParser.Elseif_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.ELSE_)
            self.state = 361
            self.match(MiniGoParser.IF_)
            self.state = 362
            self.match(MiniGoParser.LPAREN)
            self.state = 363
            self.expr0()
            self.state = 364
            self.match(MiniGoParser.RPAREN)
            self.state = 365
            self.match(MiniGoParser.LCB)
            self.state = 366
            self.blockcode()
            self.state = 367
            self.match(MiniGoParser.RCB)
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 368
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_" ):
                return visitor.visitElse_(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = MiniGoParser.Else_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MiniGoParser.ELSE_)
            self.state = 372
            self.match(MiniGoParser.LCB)
            self.state = 373
            self.blockcode()
            self.state = 374
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelse_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(MiniGoParser.If_Context,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def elseif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Elseif_Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Elseif_Context,i)


        def else_(self):
            return self.getTypedRuleContext(MiniGoParser.Else_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse_stat" ):
                return visitor.visitIfelse_stat(self)
            else:
                return visitor.visitChildren(self)




    def ifelse_stat(self):

        localctx = MiniGoParser.Ifelse_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifelse_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.if_()
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 377
                    self.elseif_() 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE_:
                self.state = 383
                self.else_()


            self.state = 386
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def assigning(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssigningContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssigningContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_stat" ):
                return visitor.visitForloop_stat(self)
            else:
                return visitor.visitChildren(self)




    def forloop_stat(self):

        localctx = MiniGoParser.Forloop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forloop_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MiniGoParser.FOR_)
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 389
                self.expr0()
                pass

            elif la_ == 2:
                self.state = 390
                self.assigning()
                self.state = 391
                self.expr0()
                self.state = 392
                self.match(MiniGoParser.SEMICOLON)
                self.state = 393
                self.lhs()
                self.state = 394
                self.assigning()
                self.state = 395
                self.expr0()
                pass

            elif la_ == 3:
                self.state = 397
                self.match(MiniGoParser.ID)
                self.state = 398
                self.match(MiniGoParser.COMMA)
                self.state = 399
                self.match(MiniGoParser.ID)
                self.state = 400
                self.match(MiniGoParser.T__3)
                self.state = 401
                self.match(MiniGoParser.RANGE_)
                self.state = 402
                self.match(MiniGoParser.ID)
                pass


            self.state = 405
            self.match(MiniGoParser.LCB)
            self.state = 406
            self.blockcode()
            self.state = 407
            self.match(MiniGoParser.RCB)
            self.state = 408
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stat" ):
                return visitor.visitBreak_stat(self)
            else:
                return visitor.visitChildren(self)




    def break_stat(self):

        localctx = MiniGoParser.Break_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(MiniGoParser.BREAK_)
            self.state = 411
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(MiniGoParser.CONTINUE_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stat" ):
                return visitor.visitContinue_stat(self)
            else:
                return visitor.visitChildren(self)




    def continue_stat(self):

        localctx = MiniGoParser.Continue_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(MiniGoParser.CONTINUE_)
            self.state = 414
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_stat" ):
                return visitor.visitFunccall_stat(self)
            else:
                return visitor.visitChildren(self)




    def funccall_stat(self):

        localctx = MiniGoParser.Funccall_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr6()
            self.state = 417
            self.match(MiniGoParser.LPAREN)
            self.state = 418
            self.expr_list()
            self.state = 419
            self.match(MiniGoParser.RPAREN)
            self.state = 420
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(MiniGoParser.RETURN_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




    def return_stat(self):

        localctx = MiniGoParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.RETURN_)
            self.state = 423
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcode" ):
                return visitor.visitBlockcode(self)
            else:
                return visitor.visitChildren(self)




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_blockcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 425
                self.end_stm()


            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 428
                self.statement()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def arr_elem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem" ):
                return visitor.visitArr_elem(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem(self):

        localctx = MiniGoParser.Arr_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arr_elem)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__2, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.expr0()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.arr_elem_list()
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


    class Arr_elem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def arr_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_elemContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_elemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_elem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem_list" ):
                return visitor.visitArr_elem_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem_list(self):

        localctx = MiniGoParser.Arr_elem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arr_elem_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.LCB)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 439
                self.arr_elem()
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 440
                    self.match(MiniGoParser.COMMA)
                    self.state = 441
                    self.arr_elem()
                    self.state = 446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 449
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def arr_elem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_listContext,0)


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_literal" ):
                return visitor.visitArr_literal(self)
            else:
                return visitor.visitChildren(self)




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arr_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 451
                self.match(MiniGoParser.LSB)
                self.state = 452
                self.expr0()
                self.state = 453
                self.match(MiniGoParser.RSB)
                self.state = 457 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 459
            self.data_type()
            self.state = 460
            self.arr_elem_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(MiniGoParser.ID)
            self.state = 463
            self.match(MiniGoParser.LCB)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 464
                self.parameterlst()


            self.state = 467
            self.match(MiniGoParser.RCB)
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
        self.enterRule(localctx, 82, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
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

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_literal)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 474
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 475
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 476
                self.struct_literal()
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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_stm" ):
                return visitor.visitEnd_stm(self)
            else:
                return visitor.visitChildren(self)




    def end_stm(self):

        localctx = MiniGoParser.End_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NL, MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 479
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 482 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.match(MiniGoParser.EOF)
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





