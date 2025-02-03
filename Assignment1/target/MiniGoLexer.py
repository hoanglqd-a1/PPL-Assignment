# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\7\5\u0088\n\5\f\5\16\5\u008b\13\5\3\5\5\5")
        buf.write("\u008e\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6\u0097\n\6\f")
        buf.write("\6\16\6\u009a\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b")
        buf.write("\u00a4\n\b\r\b\16\b\u00a5\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0129\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0130\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u013c\n\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\6\61\u0162\n\61\r\61\16\61\u0163")
        buf.write("\3\61\3\61\6\61\u0168\n\61\r\61\16\61\u0169\5\61\u016c")
        buf.write("\n\61\3\61\3\61\5\61\u0170\n\61\3\61\6\61\u0173\n\61\r")
        buf.write("\61\16\61\u0174\5\61\u0177\n\61\3\62\3\62\3\62\7\62\u017c")
        buf.write("\n\62\f\62\16\62\u017f\13\62\5\62\u0181\n\62\3\63\3\63")
        buf.write("\3\63\6\63\u0186\n\63\r\63\16\63\u0187\3\64\3\64\3\64")
        buf.write("\6\64\u018d\n\64\r\64\16\64\u018e\3\65\3\65\3\65\6\65")
        buf.write("\u0194\n\65\r\65\16\65\u0195\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u019c\n\66\3\67\3\67\38\38\38\39\39\39\79\u01a6\n9\f")
        buf.write("9\169\u01a9\139\39\39\3:\3:\7:\u01af\n:\f:\16:\u01b2\13")
        buf.write(":\3;\3;\3<\3<\3<\7<\u01b9\n<\f<\16<\u01bc\13<\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\7=\u01c5\n=\f=\16=\u01c8\13=\3=\3=\3\u0098")
        buf.write("\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\2a\61c\2e\2g\2i\2k\62m\2o\2q\63")
        buf.write("s\64u\65w\66y\67\3\2\23\3\2\f\f\3\3\f\f\5\2\13\13\17\17")
        buf.write("\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62\63")
        buf.write("\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$^^p")
        buf.write("pttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u01e7\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2a\3\2\2\2")
        buf.write("\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\3{\3\2\2\2\5~\3\2\2\2\7\u0081\3\2\2\2\t")
        buf.write("\u0083\3\2\2\2\13\u0091\3\2\2\2\r\u00a0\3\2\2\2\17\u00a3")
        buf.write("\3\2\2\2\21\u00a9\3\2\2\2\23\u00ac\3\2\2\2\25\u00b1\3")
        buf.write("\2\2\2\27\u00b5\3\2\2\2\31\u00bc\3\2\2\2\33\u00c1\3\2")
        buf.write("\2\2\35\u00c6\3\2\2\2\37\u00cd\3\2\2\2!\u00d7\3\2\2\2")
        buf.write("#\u00de\3\2\2\2%\u00e2\3\2\2\2\'\u00e8\3\2\2\2)\u00f0")
        buf.write("\3\2\2\2+\u00f6\3\2\2\2-\u00fa\3\2\2\2/\u0103\3\2\2\2")
        buf.write("\61\u0109\3\2\2\2\63\u010f\3\2\2\2\65\u0113\3\2\2\2\67")
        buf.write("\u0118\3\2\2\29\u0128\3\2\2\2;\u012f\3\2\2\2=\u013b\3")
        buf.write("\2\2\2?\u013d\3\2\2\2A\u0140\3\2\2\2C\u0142\3\2\2\2E\u0144")
        buf.write("\3\2\2\2G\u0146\3\2\2\2I\u0148\3\2\2\2K\u014a\3\2\2\2")
        buf.write("M\u014c\3\2\2\2O\u014e\3\2\2\2Q\u0150\3\2\2\2S\u0152\3")
        buf.write("\2\2\2U\u0154\3\2\2\2W\u0156\3\2\2\2Y\u0158\3\2\2\2[\u015a")
        buf.write("\3\2\2\2]\u015c\3\2\2\2_\u015e\3\2\2\2a\u0161\3\2\2\2")
        buf.write("c\u0180\3\2\2\2e\u0182\3\2\2\2g\u0189\3\2\2\2i\u0190\3")
        buf.write("\2\2\2k\u019b\3\2\2\2m\u019d\3\2\2\2o\u019f\3\2\2\2q\u01a2")
        buf.write("\3\2\2\2s\u01ac\3\2\2\2u\u01b3\3\2\2\2w\u01b5\3\2\2\2")
        buf.write("y\u01c1\3\2\2\2{|\7~\2\2|}\7~\2\2}\4\3\2\2\2~\177\7(\2")
        buf.write("\2\177\u0080\7(\2\2\u0080\6\3\2\2\2\u0081\u0082\7#\2\2")
        buf.write("\u0082\b\3\2\2\2\u0083\u0084\7\61\2\2\u0084\u0085\7\61")
        buf.write("\2\2\u0085\u0089\3\2\2\2\u0086\u0088\n\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0090\b\5\2\2\u0090\n\3\2\2\2\u0091\u0092")
        buf.write("\7\61\2\2\u0092\u0093\7,\2\2\u0093\u0098\3\2\2\2\u0094")
        buf.write("\u0097\5\13\6\2\u0095\u0097\13\2\2\2\u0096\u0094\3\2\2")
        buf.write("\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u009c\7,\2\2\u009c\u009d\7\61\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009f\b\6\2\2\u009f\f\3\2\2")
        buf.write("\2\u00a0\u00a1\7\f\2\2\u00a1\16\3\2\2\2\u00a2\u00a4\t")
        buf.write("\4\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a8\b\b\2\2\u00a8\20\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa")
        buf.write("\u00ab\7h\2\2\u00ab\22\3\2\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\24\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\26\3\2\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7w\2\2\u00b9")
        buf.write("\u00ba\7t\2\2\u00ba\u00bb\7p\2\2\u00bb\30\3\2\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7e\2\2\u00c0\32\3\2\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7{\2\2\u00c3\u00c4\7r\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\34\3\2\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7e\2\2\u00cb")
        buf.write("\u00cc\7v\2\2\u00cc\36\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7e\2\2\u00d5\u00d6\7g\2\2\u00d6 \3\2\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da")
        buf.write("\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7i\2\2\u00dd")
        buf.write("\"\3\2\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0")
        buf.write("\u00e1\7v\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3")
        buf.write("\u00e4\7n\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7c\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7&\3\2\2\2\u00e8\u00e9\7d\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7n\2\2\u00ec")
        buf.write("\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("(\3\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("*\3\2\2\2\u00f6\u00f7\7x\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9,\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe")
        buf.write("\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102.\3\2\2\2\u0103\u0104\7d\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105\u0106\7g\2\2\u0106\u0107\7c\2\2\u0107")
        buf.write("\u0108\7m\2\2\u0108\60\3\2\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7c\2\2\u010b\u010c\7p\2\2\u010c\u010d\7i\2\2\u010d")
        buf.write("\u010e\7g\2\2\u010e\62\3\2\2\2\u010f\u0110\7p\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7n\2\2\u0112\64\3\2\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\u0115\7t\2\2\u0115\u0116\7w\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117\66\3\2\2\2\u0118\u0119\7h\2\2\u0119")
        buf.write("\u011a\7c\2\2\u011a\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d8\3\2\2\2\u011e\u011f\7?\2\2\u011f")
        buf.write("\u0129\7?\2\2\u0120\u0121\7#\2\2\u0121\u0129\7?\2\2\u0122")
        buf.write("\u0129\7>\2\2\u0123\u0124\7>\2\2\u0124\u0129\7?\2\2\u0125")
        buf.write("\u0129\7@\2\2\u0126\u0127\7@\2\2\u0127\u0129\7?\2\2\u0128")
        buf.write("\u011e\3\2\2\2\u0128\u0120\3\2\2\2\u0128\u0122\3\2\2\2")
        buf.write("\u0128\u0123\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0129:\3\2\2\2\u012a\u012b\7(\2\2\u012b\u0130\7")
        buf.write("(\2\2\u012c\u012d\7~\2\2\u012d\u0130\7~\2\2\u012e\u0130")
        buf.write("\7#\2\2\u012f\u012a\3\2\2\2\u012f\u012c\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130<\3\2\2\2\u0131\u0132\7-\2\2\u0132")
        buf.write("\u013c\7?\2\2\u0133\u0134\7/\2\2\u0134\u013c\7?\2\2\u0135")
        buf.write("\u0136\7,\2\2\u0136\u013c\7?\2\2\u0137\u0138\7\61\2\2")
        buf.write("\u0138\u013c\7?\2\2\u0139\u013a\7\'\2\2\u013a\u013c\7")
        buf.write("?\2\2\u013b\u0131\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0135")
        buf.write("\3\2\2\2\u013b\u0137\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write(">\3\2\2\2\u013d\u013e\7<\2\2\u013e\u013f\7?\2\2\u013f")
        buf.write("@\3\2\2\2\u0140\u0141\7\60\2\2\u0141B\3\2\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143D\3\2\2\2\u0144\u0145\7-\2\2\u0145F\3\2\2")
        buf.write("\2\u0146\u0147\7/\2\2\u0147H\3\2\2\2\u0148\u0149\7,\2")
        buf.write("\2\u0149J\3\2\2\2\u014a\u014b\7\61\2\2\u014bL\3\2\2\2")
        buf.write("\u014c\u014d\7\'\2\2\u014dN\3\2\2\2\u014e\u014f\7*\2\2")
        buf.write("\u014fP\3\2\2\2\u0150\u0151\7+\2\2\u0151R\3\2\2\2\u0152")
        buf.write("\u0153\7]\2\2\u0153T\3\2\2\2\u0154\u0155\7_\2\2\u0155")
        buf.write("V\3\2\2\2\u0156\u0157\7}\2\2\u0157X\3\2\2\2\u0158\u0159")
        buf.write("\7\177\2\2\u0159Z\3\2\2\2\u015a\u015b\7.\2\2\u015b\\\3")
        buf.write("\2\2\2\u015c\u015d\7=\2\2\u015d^\3\2\2\2\u015e\u015f\t")
        buf.write("\5\2\2\u015f`\3\2\2\2\u0160\u0162\5_\60\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u016b\7\60\2")
        buf.write("\2\u0166\u0168\5_\60\2\u0167\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016c\3\2\2\2\u016b\u0167\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u0176\3\2\2\2\u016d\u016f\t\6\2\2\u016e\u0170\t")
        buf.write("\7\2\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172")
        buf.write("\3\2\2\2\u0171\u0173\5_\60\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0177\3\2\2\2\u0176\u016d\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177b\3\2\2\2\u0178\u0181\7\62\2\2\u0179\u017d")
        buf.write("\t\b\2\2\u017a\u017c\t\5\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0178\3")
        buf.write("\2\2\2\u0180\u0179\3\2\2\2\u0181d\3\2\2\2\u0182\u0183")
        buf.write("\7\62\2\2\u0183\u0185\t\t\2\2\u0184\u0186\t\n\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188f\3\2\2\2\u0189\u018a\7\62\2")
        buf.write("\2\u018a\u018c\t\13\2\2\u018b\u018d\t\f\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018fh\3\2\2\2\u0190\u0191\7\62\2\2\u0191")
        buf.write("\u0193\t\r\2\2\u0192\u0194\t\16\2\2\u0193\u0192\3\2\2")
        buf.write("\2\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196j\3\2\2\2\u0197\u019c\5c\62\2\u0198\u019c")
        buf.write("\5e\63\2\u0199\u019c\5g\64\2\u019a\u019c\5i\65\2\u019b")
        buf.write("\u0197\3\2\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019a\3\2\2\2\u019cl\3\2\2\2\u019d\u019e\n\17\2")
        buf.write("\2\u019en\3\2\2\2\u019f\u01a0\7^\2\2\u01a0\u01a1\t\20")
        buf.write("\2\2\u01a1p\3\2\2\2\u01a2\u01a7\7$\2\2\u01a3\u01a6\5m")
        buf.write("\67\2\u01a4\u01a6\5o8\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u01ab\7$\2\2\u01abr\3\2\2\2\u01ac\u01b0\t\21\2")
        buf.write("\2\u01ad\u01af\t\22\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("t\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\13\2\2\2\u01b4")
        buf.write("v\3\2\2\2\u01b5\u01ba\7$\2\2\u01b6\u01b9\5m\67\2\u01b7")
        buf.write("\u01b9\5o8\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\7")
        buf.write("^\2\2\u01be\u01bf\n\20\2\2\u01bf\u01c0\b<\3\2\u01c0x\3")
        buf.write("\2\2\2\u01c1\u01c6\7$\2\2\u01c2\u01c5\5m\67\2\u01c3\u01c5")
        buf.write("\5o8\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7")
        buf.write("\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\b=\4\2")
        buf.write("\u01caz\3\2\2\2\36\2\u0089\u008d\u0096\u0098\u00a5\u0128")
        buf.write("\u012f\u013b\u0163\u0169\u016b\u016f\u0174\u0176\u017d")
        buf.write("\u0180\u0187\u018e\u0195\u019b\u01a5\u01a7\u01b0\u01b8")
        buf.write("\u01ba\u01c4\u01c6\5\b\2\2\3<\2\3=\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    SINGLE_LINE_CMT = 4
    MULTI_LINE_CMT = 5
    NL = 6
    WS = 7
    IF_ = 8
    ELSE_ = 9
    FOR_ = 10
    RETURN_ = 11
    FUNC_ = 12
    TYPE_ = 13
    STRUCT_ = 14
    INTERFACE_ = 15
    STRING_ = 16
    INT_ = 17
    FLOAT_ = 18
    BOOLEAN_ = 19
    CONST_ = 20
    VAR_ = 21
    CONTINUE_ = 22
    BREAK_ = 23
    RANGE_ = 24
    NIL_ = 25
    TRUE_ = 26
    FALSE_ = 27
    COMPARISON_OP = 28
    BOOLEAN_OP = 29
    UPT_ASSIGN = 30
    ASSIGN = 31
    DOT = 32
    INIT = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    MOD = 38
    LPAREN = 39
    RPAREN = 40
    LSB = 41
    RSB = 42
    LCB = 43
    RCB = 44
    COMMA = 45
    SEMICOLON = 46
    FLOAT = 47
    INTEGER = 48
    STRING = 49
    ID = 50
    ERROR_CHAR = 51
    ILLEGAL_ESCAPE = 52
    UNCLOSE_STRING = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'!'", "'\n'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'nil'", "'true'", "'false'", "':='", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "BOOLEAN_OP", "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                  "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                  "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
                  "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                  "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "BOOLEAN_OP", 
                  "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", 
                  "RCB", "COMMA", "SEMICOLON", "Digit", "FLOAT", "DecInt", 
                  "BinInt", "OctInt", "HexInt", "INTEGER", "Char", "EscapeChar", 
                  "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.split("\\n")[0][1:]
     


