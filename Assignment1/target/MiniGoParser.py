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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u0206\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\6\2b\n\2\r\2\16\2c\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4x\n\4\3\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080\13\5")
        buf.write("\3\6\3\6\3\6\7\6\u0085\n\6\f\6\16\6\u0088\13\6\3\7\3\7")
        buf.write("\3\7\7\7\u008d\n\7\f\7\16\7\u0090\13\7\3\b\3\b\3\b\7\b")
        buf.write("\u0095\n\b\f\b\16\b\u0098\13\b\3\t\3\t\3\t\7\t\u009d\n")
        buf.write("\t\f\t\16\t\u00a0\13\t\3\n\5\n\u00a3\n\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00b2\n\13\f\13\16\13\u00b5\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00bd\n\f\3\r\3\r\3\r\7\r\u00c2\n\r\f\r\16\r")
        buf.write("\u00c5\13\r\5\r\u00c7\n\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u00d4\n\20\3\20\3\20\5")
        buf.write("\20\u00d8\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\6\22\u00e8\n\22\r\22\16")
        buf.write("\22\u00e9\3\22\3\22\3\22\5\22\u00ef\n\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\5\23\u00f6\n\23\3\24\3\24\3\24\7\24\u00fb\n")
        buf.write("\24\f\24\16\24\u00fe\13\24\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0108\n\26\3\26\3\26\3\26\5\26\u010d")
        buf.write("\n\26\3\26\3\26\5\26\u0111\n\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u011e\n\27\f\27")
        buf.write("\16\27\u0121\13\27\3\27\3\27\5\27\u0125\n\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u012e\n\30\3\30\7\30\u0131")
        buf.write("\n\30\f\30\16\30\u0134\13\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\5\31\u013b\n\31\3\31\3\31\3\31\5\31\u0140\n\31\7\31\u0142")
        buf.write("\n\31\f\31\16\31\u0145\13\31\3\32\3\32\3\32\5\32\u014a")
        buf.write("\n\32\3\32\3\32\5\32\u014e\n\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0157\n\33\3\33\7\33\u015a\n\33\f\33")
        buf.write("\16\33\u015d\13\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u016a\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0175\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\7\37\u017e\n\37\f\37\16\37\u0181")
        buf.write("\13\37\3\37\5\37\u0184\n\37\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u019b\n \5")
        buf.write(" \u019d\n \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\5$\u01b2\n$\3$\3$\3%\3%\3&\5&\u01b9\n")
        buf.write("&\3&\7&\u01bc\n&\f&\16&\u01bf\13&\3\'\3\'\5\'\u01c3\n")
        buf.write("\'\3(\3(\3(\3(\7(\u01c9\n(\f(\16(\u01cc\13(\5(\u01ce\n")
        buf.write("(\3(\3(\3)\3)\3)\3)\6)\u01d6\n)\r)\16)\u01d7\3)\3)\3)")
        buf.write("\3*\3*\3*\3*\3+\3+\3+\7+\u01e4\n+\f+\16+\u01e7\13+\3,")
        buf.write("\3,\3,\5,\u01ec\n,\3,\3,\3-\3-\3.\3.\5.\u01f4\n.\3/\3")
        buf.write("/\3/\3/\3/\3/\5/\u01fc\n/\3\60\6\60\u01ff\n\60\r\60\16")
        buf.write("\60\u0200\3\60\5\60\u0204\n\60\3\60\2\2\61\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^\2\b\3\2%&\3\2\')\4\2\5\5&&\3\2!\"\3\2")
        buf.write("\23\26\4\2\t\t\61\61\2\u021d\2a\3\2\2\2\4k\3\2\2\2\6w")
        buf.write("\3\2\2\2\by\3\2\2\2\n\u0081\3\2\2\2\f\u0089\3\2\2\2\16")
        buf.write("\u0091\3\2\2\2\20\u0099\3\2\2\2\22\u00a2\3\2\2\2\24\u00a6")
        buf.write("\3\2\2\2\26\u00bc\3\2\2\2\30\u00c6\3\2\2\2\32\u00c8\3")
        buf.write("\2\2\2\34\u00ca\3\2\2\2\36\u00cf\3\2\2\2 \u00db\3\2\2")
        buf.write("\2\"\u00e1\3\2\2\2$\u00f2\3\2\2\2&\u00f7\3\2\2\2(\u00ff")
        buf.write("\3\2\2\2*\u0102\3\2\2\2,\u0117\3\2\2\2.\u0128\3\2\2\2")
        buf.write("\60\u0138\3\2\2\2\62\u0146\3\2\2\2\64\u0151\3\2\2\2\66")
        buf.write("\u0161\3\2\2\28\u016b\3\2\2\2:\u0176\3\2\2\2<\u017b\3")
        buf.write("\2\2\2>\u0187\3\2\2\2@\u01a3\3\2\2\2B\u01a6\3\2\2\2D\u01a9")
        buf.write("\3\2\2\2F\u01af\3\2\2\2H\u01b5\3\2\2\2J\u01b8\3\2\2\2")
        buf.write("L\u01c2\3\2\2\2N\u01c4\3\2\2\2P\u01d5\3\2\2\2R\u01dc\3")
        buf.write("\2\2\2T\u01e0\3\2\2\2V\u01e8\3\2\2\2X\u01ef\3\2\2\2Z\u01f3")
        buf.write("\3\2\2\2\\\u01fb\3\2\2\2^\u0203\3\2\2\2`b\5\4\3\2a`\3")
        buf.write("\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\2\2")
        buf.write("\3f\3\3\2\2\2gl\5\6\4\2hl\5*\26\2il\5.\30\2jl\5\64\33")
        buf.write("\2kg\3\2\2\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2l\5\3\2\2\2")
        buf.write("mx\5\34\17\2nx\5\36\20\2ox\5\"\22\2px\5 \21\2qx\5<\37")
        buf.write("\2rx\5> \2sx\5B\"\2tx\5@!\2ux\5D#\2vx\5F$\2wm\3\2\2\2")
        buf.write("wn\3\2\2\2wo\3\2\2\2wp\3\2\2\2wq\3\2\2\2wr\3\2\2\2ws\3")
        buf.write("\2\2\2wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2x\7\3\2\2\2y~\5\n")
        buf.write("\6\2z{\7\3\2\2{}\5\n\6\2|z\3\2\2\2}\u0080\3\2\2\2~|\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\t\3\2\2\2\u0080~\3\2\2\2\u0081")
        buf.write("\u0086\5\f\7\2\u0082\u0083\7\4\2\2\u0083\u0085\5\f\7\2")
        buf.write("\u0084\u0082\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3")
        buf.write("\2\2\2\u0086\u0087\3\2\2\2\u0087\13\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0089\u008e\5\16\b\2\u008a\u008b\7\37\2\2\u008b")
        buf.write("\u008d\5\16\b\2\u008c\u008a\3\2\2\2\u008d\u0090\3\2\2")
        buf.write("\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\r\3\2")
        buf.write("\2\2\u0090\u008e\3\2\2\2\u0091\u0096\5\20\t\2\u0092\u0093")
        buf.write("\t\2\2\2\u0093\u0095\5\20\t\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\17\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009e\5\22")
        buf.write("\n\2\u009a\u009b\t\3\2\2\u009b\u009d\5\22\n\2\u009c\u009a")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\21\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a3\t\4\2\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a5\5\24\13\2\u00a5\23\3")
        buf.write("\2\2\2\u00a6\u00b3\5\26\f\2\u00a7\u00a8\7#\2\2\u00a8\u00b2")
        buf.write("\7\65\2\2\u00a9\u00aa\7,\2\2\u00aa\u00ab\5\b\5\2\u00ab")
        buf.write("\u00ac\7-\2\2\u00ac\u00b2\3\2\2\2\u00ad\u00ae\7*\2\2\u00ae")
        buf.write("\u00af\5\30\r\2\u00af\u00b0\7+\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00a7\3\2\2\2\u00b1\u00a9\3\2\2\2\u00b1\u00ad\3")
        buf.write("\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\25\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\7*\2\2\u00b7\u00b8\5\b\5\2\u00b8\u00b9\7+\2\2\u00b9\u00bd")
        buf.write("\3\2\2\2\u00ba\u00bd\7\65\2\2\u00bb\u00bd\5\\/\2\u00bc")
        buf.write("\u00b6\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\27\3\2\2\2\u00be\u00c3\5\b\5\2\u00bf\u00c0\7\60")
        buf.write("\2\2\u00c0\u00c2\5\b\5\2\u00c1\u00bf\3\2\2\2\u00c2\u00c5")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00be\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\31\3\2\2\2\u00c8\u00c9\5\24")
        buf.write("\13\2\u00c9\33\3\2\2\2\u00ca\u00cb\5\32\16\2\u00cb\u00cc")
        buf.write("\5H%\2\u00cc\u00cd\5\b\5\2\u00cd\u00ce\5^\60\2\u00ce\35")
        buf.write("\3\2\2\2\u00cf\u00d0\7\30\2\2\u00d0\u00d7\7\65\2\2\u00d1")
        buf.write("\u00d8\5Z.\2\u00d2\u00d4\5Z.\2\u00d3\u00d2\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\7$\2\2")
        buf.write("\u00d6\u00d8\5\b\5\2\u00d7\u00d1\3\2\2\2\u00d7\u00d3\3")
        buf.write("\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\5^\60\2\u00da\37")
        buf.write("\3\2\2\2\u00db\u00dc\7\27\2\2\u00dc\u00dd\7\65\2\2\u00dd")
        buf.write("\u00de\7$\2\2\u00de\u00df\5\b\5\2\u00df\u00e0\5^\60\2")
        buf.write("\u00e0!\3\2\2\2\u00e1\u00e2\7\30\2\2\u00e2\u00e7\7\65")
        buf.write("\2\2\u00e3\u00e4\7,\2\2\u00e4\u00e5\5\b\5\2\u00e5\u00e6")
        buf.write("\7-\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00ee\5Z.\2\u00ec\u00ed\7$")
        buf.write("\2\2\u00ed\u00ef\5P)\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\5^\60\2\u00f1")
        buf.write("#\3\2\2\2\u00f2\u00f5\7\65\2\2\u00f3\u00f6\5Z.\2\u00f4")
        buf.write("\u00f6\7\65\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2")
        buf.write("\2\u00f6%\3\2\2\2\u00f7\u00fc\5$\23\2\u00f8\u00f9\7\60")
        buf.write("\2\2\u00f9\u00fb\5$\23\2\u00fa\u00f8\3\2\2\2\u00fb\u00fe")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\'\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\7\65\2\2\u0100")
        buf.write("\u0101\7\65\2\2\u0101)\3\2\2\2\u0102\u0107\7\17\2\2\u0103")
        buf.write("\u0104\7*\2\2\u0104\u0105\5(\25\2\u0105\u0106\7+\2\2\u0106")
        buf.write("\u0108\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010a\7\65\2\2\u010a\u010c")
        buf.write("\7*\2\2\u010b\u010d\5&\24\2\u010c\u010b\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\7+\2\2")
        buf.write("\u010f\u0111\5Z.\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2")
        buf.write("\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7.\2\2\u0113\u0114")
        buf.write("\5J&\2\u0114\u0115\7/\2\2\u0115\u0116\5^\60\2\u0116+\3")
        buf.write("\2\2\2\u0117\u0124\7\65\2\2\u0118\u011f\5Z.\2\u0119\u011a")
        buf.write("\7,\2\2\u011a\u011b\5\b\5\2\u011b\u011c\7-\2\2\u011c\u011e")
        buf.write("\3\2\2\2\u011d\u0119\3\2\2\2\u011e\u0121\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0125\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0122\u0125\7\65\2\2\u0123\u0125")
        buf.write("\7\22\2\2\u0124\u0118\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\5^\60\2")
        buf.write("\u0127-\3\2\2\2\u0128\u0129\7\20\2\2\u0129\u012a\7\65")
        buf.write("\2\2\u012a\u012b\7\21\2\2\u012b\u012d\7.\2\2\u012c\u012e")
        buf.write("\5^\60\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u0132\3\2\2\2\u012f\u0131\5,\27\2\u0130\u012f\3\2\2\2")
        buf.write("\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136")
        buf.write("\7/\2\2\u0136\u0137\5^\60\2\u0137/\3\2\2\2\u0138\u013a")
        buf.write("\7\65\2\2\u0139\u013b\5Z.\2\u013a\u0139\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u0143\3\2\2\2\u013c\u013d\7\60\2")
        buf.write("\2\u013d\u013f\7\65\2\2\u013e\u0140\5Z.\2\u013f\u013e")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141")
        buf.write("\u013c\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\61\3\2\2\2\u0145\u0143\3\2")
        buf.write("\2\2\u0146\u0147\7\65\2\2\u0147\u0149\7*\2\2\u0148\u014a")
        buf.write("\5\60\31\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\7+\2\2\u014c\u014e\5Z.\2\u014d")
        buf.write("\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\5^\60\2\u0150\63\3\2\2\2\u0151\u0152\7\20")
        buf.write("\2\2\u0152\u0153\7\65\2\2\u0153\u0154\7\22\2\2\u0154\u0156")
        buf.write("\7.\2\2\u0155\u0157\5^\60\2\u0156\u0155\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u015b\3\2\2\2\u0158\u015a\5\62\32")
        buf.write("\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015e\u015f\7/\2\2\u015f\u0160\5^\60\2")
        buf.write("\u0160\65\3\2\2\2\u0161\u0162\7\13\2\2\u0162\u0163\7*")
        buf.write("\2\2\u0163\u0164\5\b\5\2\u0164\u0165\7+\2\2\u0165\u0166")
        buf.write("\7.\2\2\u0166\u0167\5J&\2\u0167\u0169\7/\2\2\u0168\u016a")
        buf.write("\5^\60\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\67\3\2\2\2\u016b\u016c\7\f\2\2\u016c\u016d\7\13\2\2\u016d")
        buf.write("\u016e\7*\2\2\u016e\u016f\5\b\5\2\u016f\u0170\7+\2\2\u0170")
        buf.write("\u0171\7.\2\2\u0171\u0172\5J&\2\u0172\u0174\7/\2\2\u0173")
        buf.write("\u0175\5^\60\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u01759\3\2\2\2\u0176\u0177\7\f\2\2\u0177\u0178\7.\2\2")
        buf.write("\u0178\u0179\5J&\2\u0179\u017a\7/\2\2\u017a;\3\2\2\2\u017b")
        buf.write("\u017f\5\66\34\2\u017c\u017e\58\35\2\u017d\u017c\3\2\2")
        buf.write("\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("\u0184\5:\36\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\5^\60\2\u0186=\3\2\2")
        buf.write("\2\u0187\u019c\7\r\2\2\u0188\u019d\5\b\5\2\u0189\u018a")
        buf.write("\7\65\2\2\u018a\u018b\7\"\2\2\u018b\u018c\5\b\5\2\u018c")
        buf.write("\u018d\7\61\2\2\u018d\u018e\5\b\5\2\u018e\u018f\7\61\2")
        buf.write("\2\u018f\u0190\7\65\2\2\u0190\u0191\7!\2\2\u0191\u0192")
        buf.write("\5\b\5\2\u0192\u019d\3\2\2\2\u0193\u0194\7\65\2\2\u0194")
        buf.write("\u0195\7\60\2\2\u0195\u0196\7\65\2\2\u0196\u0197\7\"\2")
        buf.write("\2\u0197\u019a\7\33\2\2\u0198\u019b\7\65\2\2\u0199\u019b")
        buf.write("\5P)\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u0188\3\2\2\2\u019c\u0189\3\2\2\2\u019c")
        buf.write("\u0193\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\7.\2\2")
        buf.write("\u019f\u01a0\5J&\2\u01a0\u01a1\7/\2\2\u01a1\u01a2\5^\60")
        buf.write("\2\u01a2?\3\2\2\2\u01a3\u01a4\7\32\2\2\u01a4\u01a5\5^")
        buf.write("\60\2\u01a5A\3\2\2\2\u01a6\u01a7\7\31\2\2\u01a7\u01a8")
        buf.write("\5^\60\2\u01a8C\3\2\2\2\u01a9\u01aa\5\24\13\2\u01aa\u01ab")
        buf.write("\7*\2\2\u01ab\u01ac\5\30\r\2\u01ac\u01ad\7+\2\2\u01ad")
        buf.write("\u01ae\5^\60\2\u01aeE\3\2\2\2\u01af\u01b1\7\16\2\2\u01b0")
        buf.write("\u01b2\5\b\5\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b4\5^\60\2\u01b4G\3\2\2")
        buf.write("\2\u01b5\u01b6\t\5\2\2\u01b6I\3\2\2\2\u01b7\u01b9\5^\60")
        buf.write("\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bd")
        buf.write("\3\2\2\2\u01ba\u01bc\5\6\4\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01beK\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c3\5\b\5")
        buf.write("\2\u01c1\u01c3\5N(\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3")
        buf.write("\2\2\2\u01c3M\3\2\2\2\u01c4\u01cd\7.\2\2\u01c5\u01ca\5")
        buf.write("L\'\2\u01c6\u01c7\7\60\2\2\u01c7\u01c9\5L\'\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cd\u01c5\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3")
        buf.write("\2\2\2\u01cf\u01d0\7/\2\2\u01d0O\3\2\2\2\u01d1\u01d2\7")
        buf.write(",\2\2\u01d2\u01d3\5\b\5\2\u01d3\u01d4\7-\2\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01da\5Z.\2\u01da\u01db\5N(\2\u01dbQ\3\2\2\2\u01dc")
        buf.write("\u01dd\7\65\2\2\u01dd\u01de\7\6\2\2\u01de\u01df\5\\/\2")
        buf.write("\u01dfS\3\2\2\2\u01e0\u01e5\5R*\2\u01e1\u01e2\7\60\2\2")
        buf.write("\u01e2\u01e4\5R*\2\u01e3\u01e1\3\2\2\2\u01e4\u01e7\3\2")
        buf.write("\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6U\3")
        buf.write("\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\7\65\2\2\u01e9")
        buf.write("\u01eb\7.\2\2\u01ea\u01ec\5T+\2\u01eb\u01ea\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\7/\2\2")
        buf.write("\u01eeW\3\2\2\2\u01ef\u01f0\t\6\2\2\u01f0Y\3\2\2\2\u01f1")
        buf.write("\u01f4\5X-\2\u01f2\u01f4\7\65\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f4[\3\2\2\2\u01f5\u01fc\7\63\2")
        buf.write("\2\u01f6\u01fc\7\62\2\2\u01f7\u01fc\7\64\2\2\u01f8\u01fc")
        buf.write("\7\35\2\2\u01f9\u01fc\7\36\2\2\u01fa\u01fc\5V,\2\u01fb")
        buf.write("\u01f5\3\2\2\2\u01fb\u01f6\3\2\2\2\u01fb\u01f7\3\2\2\2")
        buf.write("\u01fb\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3")
        buf.write("\2\2\2\u01fc]\3\2\2\2\u01fd\u01ff\t\7\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0204\7\2\2\3")
        buf.write("\u0203\u01fe\3\2\2\2\u0203\u0202\3\2\2\2\u0204_\3\2\2")
        buf.write("\2\67ckw~\u0086\u008e\u0096\u009e\u00a2\u00b1\u00b3\u00bc")
        buf.write("\u00c3\u00c6\u00d3\u00d7\u00e9\u00ee\u00f5\u00fc\u0107")
        buf.write("\u010c\u0110\u011f\u0124\u012d\u0132\u013a\u013f\u0143")
        buf.write("\u0149\u014d\u0156\u015b\u0169\u0174\u017f\u0183\u019a")
        buf.write("\u019c\u01b1\u01b8\u01bd\u01c2\u01ca\u01cd\u01d7\u01e5")
        buf.write("\u01eb\u01f3\u01fb\u0200\u0203")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'||'", "'&&'", "'!'", "':'", "<INVALID>", 
                     "<INVALID>", "'\n'", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':='", "'.'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
                      "BOOLEAN_OP", "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", 
                      "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                      "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
    RULE_funcdecl = 20
    RULE_fielddecl = 21
    RULE_structdecl = 22
    RULE_method_para_list = 23
    RULE_methoddecl = 24
    RULE_interfacedecl = 25
    RULE_if_ = 26
    RULE_elseif_ = 27
    RULE_else_ = 28
    RULE_ifelse_stat = 29
    RULE_forloop_stat = 30
    RULE_break_stat = 31
    RULE_continue_stat = 32
    RULE_funccall_stat = 33
    RULE_return_stat = 34
    RULE_assign = 35
    RULE_blockcode = 36
    RULE_arr_elem = 37
    RULE_arr_elem_list = 38
    RULE_arr_literal = 39
    RULE_struct_para = 40
    RULE_struct_para_lst = 41
    RULE_struct_literal = 42
    RULE_primitive_data_type = 43
    RULE_data_type = 44
    RULE_literal = 45
    RULE_end_stm = 46

    ruleNames =  [ "program", "decl", "statement", "expr0", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr_list", 
                   "lhs", "assigning", "vardecl", "constdecl", "arraydecl", 
                   "parameter", "parameterlst", "receiver", "funcdecl", 
                   "fielddecl", "structdecl", "method_para_list", "methoddecl", 
                   "interfacedecl", "if_", "elseif_", "else_", "ifelse_stat", 
                   "forloop_stat", "break_stat", "continue_stat", "funccall_stat", 
                   "return_stat", "assign", "blockcode", "arr_elem", "arr_elem_list", 
                   "arr_literal", "struct_para", "struct_para_lst", "struct_literal", 
                   "primitive_data_type", "data_type", "literal", "end_stm" ]

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
    BOOLEAN_OP=30
    UPT_ASSIGN=31
    ASSIGN=32
    DOT=33
    INIT=34
    ADD=35
    SUB=36
    MUL=37
    DIV=38
    MOD=39
    LPAREN=40
    RPAREN=41
    LSB=42
    RSB=43
    LCB=44
    RCB=45
    COMMA=46
    SEMICOLON=47
    FLOAT=48
    INTEGER=49
    STRING=50
    ID=51
    ERROR_CHAR=52
    ILLEGAL_ESCAPE=53
    UNCLOSE_STRING=54

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
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.decl()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.FUNC_) | (1 << MiniGoParser.TYPE_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 99
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.structdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 113
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 115
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 116
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
            self.state = 119
            self.expr1()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 120
                self.match(MiniGoParser.T__0)
                self.state = 121
                self.expr1()
                self.state = 126
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
            self.state = 127
            self.expr2()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1:
                self.state = 128
                self.match(MiniGoParser.T__1)
                self.state = 129
                self.expr2()
                self.state = 134
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
            self.state = 135
            self.expr3()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMPARISON_OP:
                self.state = 136
                self.match(MiniGoParser.COMPARISON_OP)
                self.state = 137
                self.expr3()
                self.state = 142
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.expr4()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ADD or _la==MiniGoParser.SUB:
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.expr4()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 151
            self.expr5()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 152
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self.expr5()
                self.state = 158
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
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__2 or _la==MiniGoParser.SUB:
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 162
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


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

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
            self.state = 164
            self.expr7()
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 165
                        self.match(MiniGoParser.DOT)
                        self.state = 166
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LSB]:
                        self.state = 167
                        self.match(MiniGoParser.LSB)
                        self.state = 168
                        self.expr0()
                        self.state = 169
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.LPAREN]:
                        self.state = 171
                        self.match(MiniGoParser.LPAREN)
                        self.state = 172
                        self.expr_list()
                        self.state = 173
                        self.match(MiniGoParser.RPAREN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 179
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr7)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(MiniGoParser.LPAREN)
                self.state = 181
                self.expr0()
                self.state = 182
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
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
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 188
                self.expr0()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 189
                    self.match(MiniGoParser.COMMA)
                    self.state = 190
                    self.expr0()
                    self.state = 195
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
            self.state = 198
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


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


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
            self.state = 200
            self.lhs()
            self.state = 201
            self.assign()
            self.state = 202
            self.expr0()
            self.state = 203
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


        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

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
            self.state = 205
            self.match(MiniGoParser.VAR_)
            self.state = 206
            self.match(MiniGoParser.ID)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 207
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 208
                    self.data_type()


                self.state = 211
                self.match(MiniGoParser.INIT)
                self.state = 212
                self.expr0()
                pass


            self.state = 215
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

        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

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
            self.state = 217
            self.match(MiniGoParser.CONST_)
            self.state = 218
            self.match(MiniGoParser.ID)
            self.state = 219
            self.match(MiniGoParser.INIT)
            self.state = 220
            self.expr0()
            self.state = 221
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

        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


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
            self.state = 223
            self.match(MiniGoParser.VAR_)
            self.state = 224
            self.match(MiniGoParser.ID)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 225
                self.match(MiniGoParser.LSB)
                self.state = 226
                self.expr0()
                self.state = 227
                self.match(MiniGoParser.RSB)
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 233
            self.data_type()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.INIT:
                self.state = 234
                self.match(MiniGoParser.INIT)
                self.state = 235
                self.arr_literal()


            self.state = 238
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
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 241
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 242
                self.match(MiniGoParser.ID)
                pass


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
            self.state = 245
            self.parameter()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 246
                self.match(MiniGoParser.COMMA)
                self.state = 247
                self.parameter()
                self.state = 252
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
            self.state = 253
            self.match(MiniGoParser.ID)
            self.state = 254
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

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


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
        self.enterRule(localctx, 40, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.FUNC_)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 257
                self.match(MiniGoParser.LPAREN)
                self.state = 258
                self.receiver()
                self.state = 259
                self.match(MiniGoParser.RPAREN)


            self.state = 263
            self.match(MiniGoParser.ID)
            self.state = 264
            self.match(MiniGoParser.LPAREN)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 265
                self.parameterlst()


            self.state = 268
            self.match(MiniGoParser.RPAREN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 269
                self.data_type()


            self.state = 272
            self.match(MiniGoParser.LCB)
            self.state = 273
            self.blockcode()
            self.state = 274
            self.match(MiniGoParser.RCB)
            self.state = 275
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
        self.enterRule(localctx, 42, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.ID)
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 278
                self.data_type()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LSB:
                    self.state = 279
                    self.match(MiniGoParser.LSB)
                    self.state = 280
                    self.expr0()
                    self.state = 281
                    self.match(MiniGoParser.RSB)
                    self.state = 287
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 288
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.state = 289
                self.match(MiniGoParser.INTERFACE_)
                pass


            self.state = 292
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
        self.enterRule(localctx, 44, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniGoParser.TYPE_)
            self.state = 295
            self.match(MiniGoParser.ID)
            self.state = 296
            self.match(MiniGoParser.STRUCT_)
            self.state = 297
            self.match(MiniGoParser.LCB)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 298
                self.end_stm()


            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 301
                self.fielddecl()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
            self.match(MiniGoParser.RCB)
            self.state = 308
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
        self.enterRule(localctx, 46, self.RULE_method_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MiniGoParser.ID)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 311
                self.data_type()


            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 314
                self.match(MiniGoParser.COMMA)
                self.state = 315
                self.match(MiniGoParser.ID)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 316
                    self.data_type()


                self.state = 323
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
        self.enterRule(localctx, 48, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MiniGoParser.ID)
            self.state = 325
            self.match(MiniGoParser.LPAREN)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 326
                self.method_para_list()


            self.state = 329
            self.match(MiniGoParser.RPAREN)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 330
                self.data_type()


            self.state = 333
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
        self.enterRule(localctx, 50, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.TYPE_)
            self.state = 336
            self.match(MiniGoParser.ID)
            self.state = 337
            self.match(MiniGoParser.INTERFACE_)
            self.state = 338
            self.match(MiniGoParser.LCB)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 339
                self.end_stm()


            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 342
                self.methoddecl()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 348
            self.match(MiniGoParser.RCB)
            self.state = 349
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
        self.enterRule(localctx, 52, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.IF_)
            self.state = 352
            self.match(MiniGoParser.LPAREN)
            self.state = 353
            self.expr0()
            self.state = 354
            self.match(MiniGoParser.RPAREN)
            self.state = 355
            self.match(MiniGoParser.LCB)
            self.state = 356
            self.blockcode()
            self.state = 357
            self.match(MiniGoParser.RCB)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 358
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
        self.enterRule(localctx, 54, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.ELSE_)
            self.state = 362
            self.match(MiniGoParser.IF_)
            self.state = 363
            self.match(MiniGoParser.LPAREN)
            self.state = 364
            self.expr0()
            self.state = 365
            self.match(MiniGoParser.RPAREN)
            self.state = 366
            self.match(MiniGoParser.LCB)
            self.state = 367
            self.blockcode()
            self.state = 368
            self.match(MiniGoParser.RCB)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 369
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
        self.enterRule(localctx, 56, self.RULE_else_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MiniGoParser.ELSE_)
            self.state = 373
            self.match(MiniGoParser.LCB)
            self.state = 374
            self.blockcode()
            self.state = 375
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
        self.enterRule(localctx, 58, self.RULE_ifelse_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.if_()
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 378
                    self.elseif_() 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE_:
                self.state = 384
                self.else_()


            self.state = 387
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


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_stat" ):
                return visitor.visitForloop_stat(self)
            else:
                return visitor.visitChildren(self)




    def forloop_stat(self):

        localctx = MiniGoParser.Forloop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forloop_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.FOR_)
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 390
                self.expr0()
                pass

            elif la_ == 2:
                self.state = 391
                self.match(MiniGoParser.ID)
                self.state = 392
                self.match(MiniGoParser.ASSIGN)
                self.state = 393
                self.expr0()
                self.state = 394
                self.match(MiniGoParser.SEMICOLON)
                self.state = 395
                self.expr0()
                self.state = 396
                self.match(MiniGoParser.SEMICOLON)
                self.state = 397
                self.match(MiniGoParser.ID)
                self.state = 398
                self.match(MiniGoParser.UPT_ASSIGN)
                self.state = 399
                self.expr0()
                pass

            elif la_ == 3:
                self.state = 401
                self.match(MiniGoParser.ID)
                self.state = 402
                self.match(MiniGoParser.COMMA)
                self.state = 403
                self.match(MiniGoParser.ID)
                self.state = 404
                self.match(MiniGoParser.ASSIGN)
                self.state = 405
                self.match(MiniGoParser.RANGE_)
                self.state = 408
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 406
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.LSB]:
                    self.state = 407
                    self.arr_literal()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self.state = 412
            self.match(MiniGoParser.LCB)
            self.state = 413
            self.blockcode()
            self.state = 414
            self.match(MiniGoParser.RCB)
            self.state = 415
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
        self.enterRule(localctx, 62, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(MiniGoParser.BREAK_)
            self.state = 418
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
        self.enterRule(localctx, 64, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.CONTINUE_)
            self.state = 421
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
        self.enterRule(localctx, 66, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expr6()
            self.state = 424
            self.match(MiniGoParser.LPAREN)
            self.state = 425
            self.expr_list()
            self.state = 426
            self.match(MiniGoParser.RPAREN)
            self.state = 427
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


        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




    def return_stat(self):

        localctx = MiniGoParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.RETURN_)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 430
                self.expr0()


            self.state = 433
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UPT_ASSIGN or _la==MiniGoParser.ASSIGN):
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
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 437
                self.end_stm()


            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 440
                self.statement()
                self.state = 445
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
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__2, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.expr0()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
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
            self.state = 450
            self.match(MiniGoParser.LCB)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 451
                self.arr_elem()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 452
                    self.match(MiniGoParser.COMMA)
                    self.state = 453
                    self.arr_elem()
                    self.state = 458
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 461
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
            self.state = 467 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 463
                self.match(MiniGoParser.LSB)
                self.state = 464
                self.expr0()
                self.state = 465
                self.match(MiniGoParser.RSB)
                self.state = 469 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 471
            self.data_type()
            self.state = 472
            self.arr_elem_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_para" ):
                return visitor.visitStruct_para(self)
            else:
                return visitor.visitChildren(self)




    def struct_para(self):

        localctx = MiniGoParser.Struct_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.ID)
            self.state = 475
            self.match(MiniGoParser.T__3)
            self.state = 476
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_para_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_paraContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_paraContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_para_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_para_lst" ):
                return visitor.visitStruct_para_lst(self)
            else:
                return visitor.visitChildren(self)




    def struct_para_lst(self):

        localctx = MiniGoParser.Struct_para_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_para_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.struct_para()
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 479
                self.match(MiniGoParser.COMMA)
                self.state = 480
                self.struct_para()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def struct_para_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_para_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(MiniGoParser.ID)
            self.state = 487
            self.match(MiniGoParser.LCB)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 488
                self.struct_para_lst()


            self.state = 491
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_data_typeContext(ParserRuleContext):
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
            return MiniGoParser.RULE_primitive_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_data_type" ):
                return visitor.visitPrimitive_data_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_data_type(self):

        localctx = MiniGoParser.Primitive_data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_primitive_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_data_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_data_type)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.primitive_data_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self.enterRule(localctx, 90, self.RULE_literal)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 501
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 502
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 503
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 504
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
        self.enterRule(localctx, 92, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NL, MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 507
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 510 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
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





