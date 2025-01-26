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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01e6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\6\2Z\n\2\r")
        buf.write("\2\16\2[\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3e\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\5\3\5\3\5")
        buf.write("\7\5v\n\5\f\5\16\5y\13\5\3\6\3\6\3\6\7\6~\n\6\f\6\16\6")
        buf.write("\u0081\13\6\3\7\3\7\3\7\7\7\u0086\n\7\f\7\16\7\u0089\13")
        buf.write("\7\3\b\3\b\3\b\3\b\5\b\u008f\n\b\3\b\7\b\u0092\n\b\f\b")
        buf.write("\16\b\u0095\13\b\3\t\3\t\3\t\7\t\u009a\n\t\f\t\16\t\u009d")
        buf.write("\13\t\3\n\5\n\u00a0\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00af\n\13\f\13")
        buf.write("\16\13\u00b2\13\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ba\n")
        buf.write("\f\3\r\3\r\3\r\7\r\u00bf\n\r\f\r\16\r\u00c2\13\r\5\r\u00c4")
        buf.write("\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00d1\n\20\3\20\3\20\5\20\u00d5\n\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\6\22\u00e5\n\22\r\22\16\22\u00e6\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00f1\n\23\3\24\3")
        buf.write("\24\3\24\7\24\u00f6\n\24\f\24\16\24\u00f9\13\24\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u0103\n\26\3\26")
        buf.write("\3\26\3\26\5\26\u0108\n\26\3\26\3\26\5\26\u010c\n\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0119\n\27\f\27\16\27\u011c\13\27\3\27\3\27\5\27")
        buf.write("\u0120\n\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u0129")
        buf.write("\n\30\3\30\7\30\u012c\n\30\f\30\16\30\u012f\13\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\5\31\u0136\n\31\3\31\3\31\3\31\5")
        buf.write("\31\u013b\n\31\7\31\u013d\n\31\f\31\16\31\u0140\13\31")
        buf.write("\3\32\3\32\3\32\5\32\u0145\n\32\3\32\3\32\5\32\u0149\n")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0152\n\33")
        buf.write("\3\33\7\33\u0155\n\33\f\33\16\33\u0158\13\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0165")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0170\n\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\7\37\u0179")
        buf.write("\n\37\f\37\16\37\u017c\13\37\3\37\5\37\u017f\n\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 ")
        buf.write("\u0192\n \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3%\5%\u01a9\n%\3%\7%\u01ac\n%\f%\16")
        buf.write("%\u01af\13%\3&\3&\5&\u01b3\n&\3\'\3\'\3\'\3\'\7\'\u01b9")
        buf.write("\n\'\f\'\16\'\u01bc\13\'\5\'\u01be\n\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\6(\u01c6\n(\r(\16(\u01c7\3(\3(\3(\3)\3)\3)\5)\u01d0")
        buf.write("\n)\3)\3)\3*\3*\3+\3+\3+\3+\3+\3+\5+\u01dc\n+\3,\6,\u01df")
        buf.write("\n,\r,\16,\u01e0\3,\5,\u01e4\n,\3,\2\2-\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTV\2\6\3\2%\'\4\2\5\5$$\3\2\22\25\4\2\b\b//\2\u01ff")
        buf.write("\2Y\3\2\2\2\4d\3\2\2\2\6p\3\2\2\2\br\3\2\2\2\nz\3\2\2")
        buf.write("\2\f\u0082\3\2\2\2\16\u008a\3\2\2\2\20\u0096\3\2\2\2\22")
        buf.write("\u009f\3\2\2\2\24\u00a3\3\2\2\2\26\u00b9\3\2\2\2\30\u00c3")
        buf.write("\3\2\2\2\32\u00c5\3\2\2\2\34\u00c7\3\2\2\2\36\u00cc\3")
        buf.write("\2\2\2 \u00d8\3\2\2\2\"\u00de\3\2\2\2$\u00ed\3\2\2\2&")
        buf.write("\u00f2\3\2\2\2(\u00fa\3\2\2\2*\u00fd\3\2\2\2,\u0112\3")
        buf.write("\2\2\2.\u0123\3\2\2\2\60\u0133\3\2\2\2\62\u0141\3\2\2")
        buf.write("\2\64\u014c\3\2\2\2\66\u015c\3\2\2\28\u0166\3\2\2\2:\u0171")
        buf.write("\3\2\2\2<\u0176\3\2\2\2>\u0182\3\2\2\2@\u0198\3\2\2\2")
        buf.write("B\u019b\3\2\2\2D\u019e\3\2\2\2F\u01a4\3\2\2\2H\u01a8\3")
        buf.write("\2\2\2J\u01b2\3\2\2\2L\u01b4\3\2\2\2N\u01c5\3\2\2\2P\u01cc")
        buf.write("\3\2\2\2R\u01d3\3\2\2\2T\u01db\3\2\2\2V\u01e3\3\2\2\2")
        buf.write("XZ\5\4\3\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\")
        buf.write("]\3\2\2\2]^\7\2\2\3^\3\3\2\2\2_e\5\b\5\2`e\5\6\4\2ae\5")
        buf.write("*\26\2be\5.\30\2ce\5\64\33\2d_\3\2\2\2d`\3\2\2\2da\3\2")
        buf.write("\2\2db\3\2\2\2dc\3\2\2\2e\5\3\2\2\2fq\5\34\17\2gq\5\36")
        buf.write("\20\2hq\5\"\22\2iq\5 \21\2jq\5<\37\2kq\5> \2lq\5B\"\2")
        buf.write("mq\5@!\2nq\5D#\2oq\5F$\2pf\3\2\2\2pg\3\2\2\2ph\3\2\2\2")
        buf.write("pi\3\2\2\2pj\3\2\2\2pk\3\2\2\2pl\3\2\2\2pm\3\2\2\2pn\3")
        buf.write("\2\2\2po\3\2\2\2q\7\3\2\2\2rw\5\n\6\2st\7\3\2\2tv\5\n")
        buf.write("\6\2us\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\t\3\2\2")
        buf.write("\2yw\3\2\2\2z\177\5\f\7\2{|\7\4\2\2|~\5\f\7\2}{\3\2\2")
        buf.write("\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\13\3\2\2\2\u0081\177\3\2\2\2\u0082\u0087\5\16\b\2\u0083")
        buf.write("\u0084\7\36\2\2\u0084\u0086\5\16\b\2\u0085\u0083\3\2\2")
        buf.write("\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\r\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u0093")
        buf.write("\5\20\t\2\u008b\u008f\7#\2\2\u008c\u008f\3\2\2\2\u008d")
        buf.write("\u008f\7$\2\2\u008e\u008b\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\5")
        buf.write("\20\t\2\u0091\u008e\3\2\2\2\u0092\u0095\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\17\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0096\u009b\5\22\n\2\u0097\u0098\t\2\2")
        buf.write("\2\u0098\u009a\5\22\n\2\u0099\u0097\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\21\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\t\3\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a2\5\24\13\2\u00a2\23\3\2\2\2\u00a3\u00b0\5")
        buf.write("\26\f\2\u00a4\u00a5\7!\2\2\u00a5\u00af\7\63\2\2\u00a6")
        buf.write("\u00a7\7*\2\2\u00a7\u00a8\5\b\5\2\u00a8\u00a9\7+\2\2\u00a9")
        buf.write("\u00af\3\2\2\2\u00aa\u00ab\7(\2\2\u00ab\u00ac\5\30\r\2")
        buf.write("\u00ac\u00ad\7)\2\2\u00ad\u00af\3\2\2\2\u00ae\u00a4\3")
        buf.write("\2\2\2\u00ae\u00a6\3\2\2\2\u00ae\u00aa\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\25\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7(\2\2\u00b4")
        buf.write("\u00b5\5\b\5\2\u00b5\u00b6\7)\2\2\u00b6\u00ba\3\2\2\2")
        buf.write("\u00b7\u00ba\7\63\2\2\u00b8\u00ba\5T+\2\u00b9\u00b3\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\27")
        buf.write("\3\2\2\2\u00bb\u00c0\5\b\5\2\u00bc\u00bd\7.\2\2\u00bd")
        buf.write("\u00bf\5\b\5\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c4\3")
        buf.write("\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00bb\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\31\3\2\2\2\u00c5\u00c6\5\24\13\2\u00c6")
        buf.write("\33\3\2\2\2\u00c7\u00c8\5\32\16\2\u00c8\u00c9\7 \2\2\u00c9")
        buf.write("\u00ca\5\b\5\2\u00ca\u00cb\5V,\2\u00cb\35\3\2\2\2\u00cc")
        buf.write("\u00cd\7\27\2\2\u00cd\u00d4\7\63\2\2\u00ce\u00d5\5R*\2")
        buf.write("\u00cf\u00d1\5R*\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2")
        buf.write("\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7\"\2\2\u00d3\u00d5")
        buf.write("\5\b\5\2\u00d4\u00ce\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\5V,\2\u00d7\37\3\2\2\2\u00d8")
        buf.write("\u00d9\7\26\2\2\u00d9\u00da\7\63\2\2\u00da\u00db\7\"\2")
        buf.write("\2\u00db\u00dc\5\b\5\2\u00dc\u00dd\5V,\2\u00dd!\3\2\2")
        buf.write("\2\u00de\u00df\7\27\2\2\u00df\u00e4\7\63\2\2\u00e0\u00e1")
        buf.write("\7*\2\2\u00e1\u00e2\5\b\5\2\u00e2\u00e3\7+\2\2\u00e3\u00e5")
        buf.write("\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\5R*\2\u00e9\u00ea\7\"\2\2\u00ea\u00eb\5N")
        buf.write("(\2\u00eb\u00ec\5V,\2\u00ec#\3\2\2\2\u00ed\u00f0\7\63")
        buf.write("\2\2\u00ee\u00f1\5R*\2\u00ef\u00f1\7\63\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1%\3\2\2\2\u00f2\u00f7")
        buf.write("\5$\23\2\u00f3\u00f4\7.\2\2\u00f4\u00f6\5$\23\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8\'\3\2\2\2\u00f9\u00f7\3\2\2")
        buf.write("\2\u00fa\u00fb\7\63\2\2\u00fb\u00fc\7\63\2\2\u00fc)\3")
        buf.write("\2\2\2\u00fd\u0102\7\16\2\2\u00fe\u00ff\7(\2\2\u00ff\u0100")
        buf.write("\5(\25\2\u0100\u0101\7)\2\2\u0101\u0103\3\2\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0105\7\63\2\2\u0105\u0107\7(\2\2\u0106\u0108\5")
        buf.write("&\24\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010b\7)\2\2\u010a\u010c\5R*\2\u010b\u010a")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010e\7,\2\2\u010e\u010f\5H%\2\u010f\u0110\7-\2\2\u0110")
        buf.write("\u0111\5V,\2\u0111+\3\2\2\2\u0112\u011f\7\63\2\2\u0113")
        buf.write("\u011a\5R*\2\u0114\u0115\7*\2\2\u0115\u0116\5\b\5\2\u0116")
        buf.write("\u0117\7+\2\2\u0117\u0119\3\2\2\2\u0118\u0114\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011b\u0120\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u0120")
        buf.write("\7\63\2\2\u011e\u0120\7\21\2\2\u011f\u0113\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0122\5V,\2\u0122-\3\2\2\2\u0123\u0124\7\17\2\2")
        buf.write("\u0124\u0125\7\63\2\2\u0125\u0126\7\20\2\2\u0126\u0128")
        buf.write("\7,\2\2\u0127\u0129\5V,\2\u0128\u0127\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129\u012d\3\2\2\2\u012a\u012c\5,\27\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u012d\3")
        buf.write("\2\2\2\u0130\u0131\7-\2\2\u0131\u0132\5V,\2\u0132/\3\2")
        buf.write("\2\2\u0133\u0135\7\63\2\2\u0134\u0136\5R*\2\u0135\u0134")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u013e\3\2\2\2\u0137")
        buf.write("\u0138\7.\2\2\u0138\u013a\7\63\2\2\u0139\u013b\5R*\2\u013a")
        buf.write("\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2")
        buf.write("\u013c\u0137\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\61\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0142\7\63\2\2\u0142\u0144\7(\2\2\u0143")
        buf.write("\u0145\5\60\31\2\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2")
        buf.write("\2\u0145\u0146\3\2\2\2\u0146\u0148\7)\2\2\u0147\u0149")
        buf.write("\5R*\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014b\5V,\2\u014b\63\3\2\2\2\u014c\u014d")
        buf.write("\7\17\2\2\u014d\u014e\7\63\2\2\u014e\u014f\7\21\2\2\u014f")
        buf.write("\u0151\7,\2\2\u0150\u0152\5V,\2\u0151\u0150\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0156\3\2\2\2\u0153\u0155\5\62\32")
        buf.write("\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0159\u015a\7-\2\2\u015a\u015b\5V,\2\u015b")
        buf.write("\65\3\2\2\2\u015c\u015d\7\n\2\2\u015d\u015e\7(\2\2\u015e")
        buf.write("\u015f\5\b\5\2\u015f\u0160\7)\2\2\u0160\u0161\7,\2\2\u0161")
        buf.write("\u0162\5H%\2\u0162\u0164\7-\2\2\u0163\u0165\5V,\2\u0164")
        buf.write("\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\67\3\2\2\2\u0166")
        buf.write("\u0167\7\13\2\2\u0167\u0168\7\n\2\2\u0168\u0169\7(\2\2")
        buf.write("\u0169\u016a\5\b\5\2\u016a\u016b\7)\2\2\u016b\u016c\7")
        buf.write(",\2\2\u016c\u016d\5H%\2\u016d\u016f\7-\2\2\u016e\u0170")
        buf.write("\5V,\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u01709")
        buf.write("\3\2\2\2\u0171\u0172\7\13\2\2\u0172\u0173\7,\2\2\u0173")
        buf.write("\u0174\5H%\2\u0174\u0175\7-\2\2\u0175;\3\2\2\2\u0176\u017a")
        buf.write("\5\66\34\2\u0177\u0179\58\35\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f\5")
        buf.write(":\36\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\5V,\2\u0181=\3\2\2\2\u0182\u0191")
        buf.write("\7\f\2\2\u0183\u0192\5\b\5\2\u0184\u0185\5\34\17\2\u0185")
        buf.write("\u0186\5\b\5\2\u0186\u0187\7/\2\2\u0187\u0188\5\32\16")
        buf.write("\2\u0188\u0189\5\34\17\2\u0189\u018a\5\b\5\2\u018a\u0192")
        buf.write("\3\2\2\2\u018b\u018c\7\63\2\2\u018c\u018d\7.\2\2\u018d")
        buf.write("\u018e\7\63\2\2\u018e\u018f\7 \2\2\u018f\u0190\7\32\2")
        buf.write("\2\u0190\u0192\7\63\2\2\u0191\u0183\3\2\2\2\u0191\u0184")
        buf.write("\3\2\2\2\u0191\u018b\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\7,\2\2\u0194\u0195\5H%\2\u0195\u0196\7-\2\2\u0196")
        buf.write("\u0197\5V,\2\u0197?\3\2\2\2\u0198\u0199\7\31\2\2\u0199")
        buf.write("\u019a\5V,\2\u019aA\3\2\2\2\u019b\u019c\7\30\2\2\u019c")
        buf.write("\u019d\5V,\2\u019dC\3\2\2\2\u019e\u019f\5\24\13\2\u019f")
        buf.write("\u01a0\7(\2\2\u01a0\u01a1\5\30\r\2\u01a1\u01a2\7)\2\2")
        buf.write("\u01a2\u01a3\5V,\2\u01a3E\3\2\2\2\u01a4\u01a5\7\r\2\2")
        buf.write("\u01a5\u01a6\5V,\2\u01a6G\3\2\2\2\u01a7\u01a9\5V,\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ad\3\2\2\2")
        buf.write("\u01aa\u01ac\5\6\4\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeI")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b3\5\b\5\2\u01b1")
        buf.write("\u01b3\5L\'\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2")
        buf.write("\u01b3K\3\2\2\2\u01b4\u01bd\7,\2\2\u01b5\u01ba\5J&\2\u01b6")
        buf.write("\u01b7\7.\2\2\u01b7\u01b9\5J&\2\u01b8\u01b6\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01b5\3")
        buf.write("\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0")
        buf.write("\7-\2\2\u01c0M\3\2\2\2\u01c1\u01c2\7*\2\2\u01c2\u01c3")
        buf.write("\5\b\5\2\u01c3\u01c4\7+\2\2\u01c4\u01c6\3\2\2\2\u01c5")
        buf.write("\u01c1\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\5")
        buf.write("R*\2\u01ca\u01cb\5L\'\2\u01cbO\3\2\2\2\u01cc\u01cd\7\63")
        buf.write("\2\2\u01cd\u01cf\7,\2\2\u01ce\u01d0\5&\24\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d2\7-\2\2\u01d2Q\3\2\2\2\u01d3\u01d4\t\4\2\2\u01d4")
        buf.write("S\3\2\2\2\u01d5\u01dc\7\61\2\2\u01d6\u01dc\7\60\2\2\u01d7")
        buf.write("\u01dc\7\62\2\2\u01d8\u01dc\7\34\2\2\u01d9\u01dc\7\35")
        buf.write("\2\2\u01da\u01dc\5P)\2\u01db\u01d5\3\2\2\2\u01db\u01d6")
        buf.write("\3\2\2\2\u01db\u01d7\3\2\2\2\u01db\u01d8\3\2\2\2\u01db")
        buf.write("\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dcU\3\2\2\2\u01dd")
        buf.write("\u01df\t\5\2\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e4\3")
        buf.write("\2\2\2\u01e2\u01e4\7\2\2\3\u01e3\u01de\3\2\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4W\3\2\2\2\63[dpw\177\u0087\u008e\u0093\u009b")
        buf.write("\u009f\u00ae\u00b0\u00b9\u00c0\u00c3\u00d0\u00d4\u00e6")
        buf.write("\u00f0\u00f7\u0102\u0107\u010b\u011a\u011f\u0128\u012d")
        buf.write("\u0135\u013a\u013e\u0144\u0148\u0151\u0156\u0164\u016f")
        buf.write("\u017a\u017e\u0191\u01a8\u01ad\u01b2\u01ba\u01bd\u01c7")
        buf.write("\u01cf\u01db\u01e0\u01e3")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'||'", "'&&'", "'!'", "<INVALID>", "<INVALID>", 
                     "'\n'", "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "<INVALID>", "'.'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", 
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
    RULE_blockcode = 35
    RULE_arr_elem = 36
    RULE_arr_elem_list = 37
    RULE_arr_literal = 38
    RULE_struct_literal = 39
    RULE_data_type = 40
    RULE_literal = 41
    RULE_end_stm = 42

    ruleNames =  [ "program", "decl", "statement", "expr0", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr_list", 
                   "lhs", "assigning", "vardecl", "constdecl", "arraydecl", 
                   "parameter", "parameterlst", "receiver", "funcdecl", 
                   "fielddecl", "structdecl", "method_para_list", "methoddecl", 
                   "interfacedecl", "if_", "elseif_", "else_", "ifelse_stat", 
                   "forloop_stat", "break_stat", "continue_stat", "funccall_stat", 
                   "return_stat", "blockcode", "arr_elem", "arr_elem_list", 
                   "arr_literal", "struct_literal", "data_type", "literal", 
                   "end_stm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SINGLE_LINE_CMT=4
    MULTI_LINE_CMT=5
    NL=6
    WS=7
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
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.decl()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.FUNC_) | (1 << MiniGoParser.TYPE_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 91
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expr0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.funcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 106
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 107
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 108
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 109
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
            self.state = 112
            self.expr1()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 113
                self.match(MiniGoParser.T__0)
                self.state = 114
                self.expr1()
                self.state = 119
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
            self.state = 120
            self.expr2()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1:
                self.state = 121
                self.match(MiniGoParser.T__1)
                self.state = 122
                self.expr2()
                self.state = 127
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
            self.state = 128
            self.expr3()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMPARISON_OP:
                self.state = 129
                self.match(MiniGoParser.COMPARISON_OP)
                self.state = 130
                self.expr3()
                self.state = 135
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
            self.state = 136
            self.expr4()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 137
                        self.match(MiniGoParser.ADD)
                        pass

                    elif la_ == 2:
                        pass

                    elif la_ == 3:
                        self.state = 139
                        self.match(MiniGoParser.SUB)
                        pass


                    self.state = 142
                    self.expr4() 
                self.state = 147
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
            self.state = 148
            self.expr5()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 149
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.expr5()
                self.state = 155
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
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__2 or _la==MiniGoParser.SUB:
                self.state = 156
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 159
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
            self.state = 161
            self.expr7()
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.OP5]:
                        self.state = 162
                        self.match(MiniGoParser.OP5)
                        self.state = 163
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LSB]:
                        self.state = 164
                        self.match(MiniGoParser.LSB)
                        self.state = 165
                        self.expr0()
                        self.state = 166
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.LPAREN]:
                        self.state = 168
                        self.match(MiniGoParser.LPAREN)
                        self.state = 169
                        self.expr_list()
                        self.state = 170
                        self.match(MiniGoParser.RPAREN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 176
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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(MiniGoParser.LPAREN)
                self.state = 178
                self.expr0()
                self.state = 179
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
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
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 185
                self.expr0()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 186
                    self.match(MiniGoParser.COMMA)
                    self.state = 187
                    self.expr0()
                    self.state = 192
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
            self.state = 195
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
            self.state = 197
            self.lhs()
            self.state = 198
            self.match(MiniGoParser.ASSIGN1)
            self.state = 199
            self.expr0()
            self.state = 200
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
            self.state = 202
            self.match(MiniGoParser.VAR_)
            self.state = 203
            self.match(MiniGoParser.ID)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 204
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 205
                    self.data_type()


                self.state = 208
                self.match(MiniGoParser.ASSIGN)
                self.state = 209
                self.expr0()
                pass


            self.state = 212
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
            self.state = 214
            self.match(MiniGoParser.CONST_)
            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 216
            self.match(MiniGoParser.ASSIGN)
            self.state = 217
            self.expr0()
            self.state = 218
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
            self.state = 220
            self.match(MiniGoParser.VAR_)
            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 226 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 222
                self.match(MiniGoParser.LSB)
                self.state = 223
                self.expr0()
                self.state = 224
                self.match(MiniGoParser.RSB)
                self.state = 228 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 230
            self.data_type()
            self.state = 231
            self.match(MiniGoParser.ASSIGN)
            self.state = 232
            self.arr_literal()
            self.state = 233
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
            self.state = 235
            self.match(MiniGoParser.ID)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.state = 236
                self.data_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 237
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
            self.state = 240
            self.parameter()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 241
                self.match(MiniGoParser.COMMA)
                self.state = 242
                self.parameter()
                self.state = 247
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
            self.state = 248
            self.match(MiniGoParser.ID)
            self.state = 249
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
            self.state = 251
            self.match(MiniGoParser.FUNC_)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 252
                self.match(MiniGoParser.LPAREN)
                self.state = 253
                self.receiver()
                self.state = 254
                self.match(MiniGoParser.RPAREN)


            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 259
            self.match(MiniGoParser.LPAREN)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 260
                self.parameterlst()


            self.state = 263
            self.match(MiniGoParser.RPAREN)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 264
                self.data_type()


            self.state = 267
            self.match(MiniGoParser.LCB)
            self.state = 268
            self.blockcode()
            self.state = 269
            self.match(MiniGoParser.RCB)
            self.state = 270
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
            self.state = 272
            self.match(MiniGoParser.ID)
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.state = 273
                self.data_type()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LSB:
                    self.state = 274
                    self.match(MiniGoParser.LSB)
                    self.state = 275
                    self.expr0()
                    self.state = 276
                    self.match(MiniGoParser.RSB)
                    self.state = 282
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.ID]:
                self.state = 283
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INTERFACE_]:
                self.state = 284
                self.match(MiniGoParser.INTERFACE_)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 287
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
            self.state = 289
            self.match(MiniGoParser.TYPE_)
            self.state = 290
            self.match(MiniGoParser.ID)
            self.state = 291
            self.match(MiniGoParser.STRUCT_)
            self.state = 292
            self.match(MiniGoParser.LCB)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 293
                self.end_stm()


            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 296
                self.fielddecl()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(MiniGoParser.RCB)
            self.state = 303
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
            self.state = 305
            self.match(MiniGoParser.ID)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 306
                self.data_type()


            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 309
                self.match(MiniGoParser.COMMA)
                self.state = 310
                self.match(MiniGoParser.ID)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 311
                    self.data_type()


                self.state = 318
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
            self.state = 319
            self.match(MiniGoParser.ID)
            self.state = 320
            self.match(MiniGoParser.LPAREN)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 321
                self.method_para_list()


            self.state = 324
            self.match(MiniGoParser.RPAREN)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 325
                self.data_type()


            self.state = 328
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
            self.state = 330
            self.match(MiniGoParser.TYPE_)
            self.state = 331
            self.match(MiniGoParser.ID)
            self.state = 332
            self.match(MiniGoParser.INTERFACE_)
            self.state = 333
            self.match(MiniGoParser.LCB)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 334
                self.end_stm()


            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 337
                self.methoddecl()
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 343
            self.match(MiniGoParser.RCB)
            self.state = 344
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
            self.state = 346
            self.match(MiniGoParser.IF_)
            self.state = 347
            self.match(MiniGoParser.LPAREN)
            self.state = 348
            self.expr0()
            self.state = 349
            self.match(MiniGoParser.RPAREN)
            self.state = 350
            self.match(MiniGoParser.LCB)
            self.state = 351
            self.blockcode()
            self.state = 352
            self.match(MiniGoParser.RCB)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 353
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
            self.state = 356
            self.match(MiniGoParser.ELSE_)
            self.state = 357
            self.match(MiniGoParser.IF_)
            self.state = 358
            self.match(MiniGoParser.LPAREN)
            self.state = 359
            self.expr0()
            self.state = 360
            self.match(MiniGoParser.RPAREN)
            self.state = 361
            self.match(MiniGoParser.LCB)
            self.state = 362
            self.blockcode()
            self.state = 363
            self.match(MiniGoParser.RCB)
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 364
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
            self.state = 367
            self.match(MiniGoParser.ELSE_)
            self.state = 368
            self.match(MiniGoParser.LCB)
            self.state = 369
            self.blockcode()
            self.state = 370
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
            self.state = 372
            self.if_()
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 373
                    self.elseif_() 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE_:
                self.state = 379
                self.else_()


            self.state = 382
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

        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

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
        self.enterRule(localctx, 60, self.RULE_forloop_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.FOR_)
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 385
                self.expr0()
                pass

            elif la_ == 2:
                self.state = 386
                self.assigning()
                self.state = 387
                self.expr0()
                self.state = 388
                self.match(MiniGoParser.SEMICOLON)
                self.state = 389
                self.lhs()
                self.state = 390
                self.assigning()
                self.state = 391
                self.expr0()
                pass

            elif la_ == 3:
                self.state = 393
                self.match(MiniGoParser.ID)
                self.state = 394
                self.match(MiniGoParser.COMMA)
                self.state = 395
                self.match(MiniGoParser.ID)
                self.state = 396
                self.match(MiniGoParser.ASSIGN1)
                self.state = 397
                self.match(MiniGoParser.RANGE_)
                self.state = 398
                self.match(MiniGoParser.ID)
                pass


            self.state = 401
            self.match(MiniGoParser.LCB)
            self.state = 402
            self.blockcode()
            self.state = 403
            self.match(MiniGoParser.RCB)
            self.state = 404
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
            self.state = 406
            self.match(MiniGoParser.BREAK_)
            self.state = 407
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
            self.state = 409
            self.match(MiniGoParser.CONTINUE_)
            self.state = 410
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
            self.state = 412
            self.expr6()
            self.state = 413
            self.match(MiniGoParser.LPAREN)
            self.state = 414
            self.expr_list()
            self.state = 415
            self.match(MiniGoParser.RPAREN)
            self.state = 416
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
        self.enterRule(localctx, 68, self.RULE_return_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MiniGoParser.RETURN_)
            self.state = 419
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
        self.enterRule(localctx, 70, self.RULE_blockcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 421
                self.end_stm()


            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF_) | (1 << MiniGoParser.FOR_) | (1 << MiniGoParser.RETURN_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.CONTINUE_) | (1 << MiniGoParser.BREAK_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 424
                self.statement()
                self.state = 429
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
        self.enterRule(localctx, 72, self.RULE_arr_elem)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__2, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.expr0()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
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
        self.enterRule(localctx, 74, self.RULE_arr_elem_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.LCB)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 435
                self.arr_elem()
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 436
                    self.match(MiniGoParser.COMMA)
                    self.state = 437
                    self.arr_elem()
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 445
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
        self.enterRule(localctx, 76, self.RULE_arr_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 447
                self.match(MiniGoParser.LSB)
                self.state = 448
                self.expr0()
                self.state = 449
                self.match(MiniGoParser.RSB)
                self.state = 453 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 455
            self.data_type()
            self.state = 456
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
        self.enterRule(localctx, 78, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.ID)
            self.state = 459
            self.match(MiniGoParser.LCB)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 460
                self.parameterlst()


            self.state = 463
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
        self.enterRule(localctx, 80, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
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
        self.enterRule(localctx, 82, self.RULE_literal)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
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
        self.enterRule(localctx, 84, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NL, MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 476 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 475
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 478 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
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





