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
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u008b\n\6\f\6\16\6\u008e")
        buf.write("\13\6\3\6\5\6\u0091\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7\u009a\n\7\f\7\16\7\u009d\13\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\6\t\u00a7\n\t\r\t\16\t\u00a8\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u012c\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0133\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u0141\n \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\6\61\u0164\n\61\r\61\16\61\u0165\3\61")
        buf.write("\3\61\6\61\u016a\n\61\r\61\16\61\u016b\5\61\u016e\n\61")
        buf.write("\3\61\3\61\5\61\u0172\n\61\3\61\6\61\u0175\n\61\r\61\16")
        buf.write("\61\u0176\5\61\u0179\n\61\3\62\3\62\3\62\7\62\u017e\n")
        buf.write("\62\f\62\16\62\u0181\13\62\5\62\u0183\n\62\3\63\3\63\3")
        buf.write("\63\6\63\u0188\n\63\r\63\16\63\u0189\3\64\3\64\3\64\6")
        buf.write("\64\u018f\n\64\r\64\16\64\u0190\3\65\3\65\3\65\6\65\u0196")
        buf.write("\n\65\r\65\16\65\u0197\3\66\3\66\3\66\3\66\5\66\u019e")
        buf.write("\n\66\3\67\3\67\38\38\38\39\39\39\79\u01a8\n9\f9\169\u01ab")
        buf.write("\139\39\39\3:\3:\7:\u01b1\n:\f:\16:\u01b4\13:\3;\3;\3")
        buf.write("<\3<\3<\7<\u01bb\n<\f<\16<\u01be\13<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\7=\u01c7\n=\f=\16=\u01ca\13=\3=\3=\3\u009b\2>\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\2a\61c\2e\2g\2i\2k\62m\2o\2q\63s\64u\65")
        buf.write("w\66y\67\3\2\23\3\2\f\f\3\3\f\f\5\2\13\13\17\17\"\"\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62\63\4\2Q")
        buf.write("Qqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$^^ppttvv")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\2\u01ea\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2a\3\2\2\2\2k")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\3{\3\2\2\2\5~\3\2\2\2\7\u0081\3\2\2\2\t\u0083")
        buf.write("\3\2\2\2\13\u0086\3\2\2\2\r\u0094\3\2\2\2\17\u00a3\3\2")
        buf.write("\2\2\21\u00a6\3\2\2\2\23\u00ac\3\2\2\2\25\u00af\3\2\2")
        buf.write("\2\27\u00b4\3\2\2\2\31\u00b8\3\2\2\2\33\u00bf\3\2\2\2")
        buf.write("\35\u00c4\3\2\2\2\37\u00c9\3\2\2\2!\u00d0\3\2\2\2#\u00da")
        buf.write("\3\2\2\2%\u00e1\3\2\2\2\'\u00e5\3\2\2\2)\u00eb\3\2\2\2")
        buf.write("+\u00f3\3\2\2\2-\u00f9\3\2\2\2/\u00fd\3\2\2\2\61\u0106")
        buf.write("\3\2\2\2\63\u010c\3\2\2\2\65\u0112\3\2\2\2\67\u0116\3")
        buf.write("\2\2\29\u011b\3\2\2\2;\u012b\3\2\2\2=\u0132\3\2\2\2?\u0140")
        buf.write("\3\2\2\2A\u0142\3\2\2\2C\u0144\3\2\2\2E\u0146\3\2\2\2")
        buf.write("G\u0148\3\2\2\2I\u014a\3\2\2\2K\u014c\3\2\2\2M\u014e\3")
        buf.write("\2\2\2O\u0150\3\2\2\2Q\u0152\3\2\2\2S\u0154\3\2\2\2U\u0156")
        buf.write("\3\2\2\2W\u0158\3\2\2\2Y\u015a\3\2\2\2[\u015c\3\2\2\2")
        buf.write("]\u015e\3\2\2\2_\u0160\3\2\2\2a\u0163\3\2\2\2c\u0182\3")
        buf.write("\2\2\2e\u0184\3\2\2\2g\u018b\3\2\2\2i\u0192\3\2\2\2k\u019d")
        buf.write("\3\2\2\2m\u019f\3\2\2\2o\u01a1\3\2\2\2q\u01a4\3\2\2\2")
        buf.write("s\u01ae\3\2\2\2u\u01b5\3\2\2\2w\u01b7\3\2\2\2y\u01c3\3")
        buf.write("\2\2\2{|\7~\2\2|}\7~\2\2}\4\3\2\2\2~\177\7(\2\2\177\u0080")
        buf.write("\7(\2\2\u0080\6\3\2\2\2\u0081\u0082\7#\2\2\u0082\b\3\2")
        buf.write("\2\2\u0083\u0084\7<\2\2\u0084\u0085\7?\2\2\u0085\n\3\2")
        buf.write("\2\2\u0086\u0087\7\61\2\2\u0087\u0088\7\61\2\2\u0088\u008c")
        buf.write("\3\2\2\2\u0089\u008b\n\2\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0091\t")
        buf.write("\3\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093")
        buf.write("\b\6\2\2\u0093\f\3\2\2\2\u0094\u0095\7\61\2\2\u0095\u0096")
        buf.write("\7,\2\2\u0096\u009b\3\2\2\2\u0097\u009a\5\r\7\2\u0098")
        buf.write("\u009a\13\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2")
        buf.write("\2\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u009f\7,\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a2\b\7\2\2\u00a2\16\3\2\2\2\u00a3\u00a4\7\f")
        buf.write("\2\2\u00a4\20\3\2\2\2\u00a5\u00a7\t\4\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\b\t\2\2")
        buf.write("\u00ab\22\3\2\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7h\2")
        buf.write("\2\u00ae\24\3\2\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7n")
        buf.write("\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\26\3")
        buf.write("\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\30\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7p\2\2\u00be\32\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7e\2\2\u00c3\34\3\2\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7{\2\2\u00c6\u00c7\7r\2\2\u00c7\u00c8\7g\2\2\u00c8\36")
        buf.write("\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf \3\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7e\2\2\u00d8\u00d9\7g\2\2\u00d9\"\3\2\2\2\u00da\u00db")
        buf.write("\7u\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7i\2\2\u00e0$\3")
        buf.write("\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4&\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea(\3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7p\2\2\u00f2*\3")
        buf.write("\2\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8,\3")
        buf.write("\2\2\2\u00f9\u00fa\7x\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc.\3\2\2\2\u00fd\u00fe\7e\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7w\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\60\3\2\2\2\u0106\u0107\7d\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7g\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7m\2\2\u010b\62\3\2\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7p\2\2\u010f\u0110\7i\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111\64\3\2\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7n\2\2\u0115\66\3\2\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\u0118\7t\2\2\u0118\u0119\7w\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a8\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120:\3\2\2\2\u0121\u0122\7?\2\2\u0122\u012c")
        buf.write("\7?\2\2\u0123\u0124\7#\2\2\u0124\u012c\7?\2\2\u0125\u012c")
        buf.write("\7>\2\2\u0126\u0127\7>\2\2\u0127\u012c\7?\2\2\u0128\u012c")
        buf.write("\7@\2\2\u0129\u012a\7@\2\2\u012a\u012c\7?\2\2\u012b\u0121")
        buf.write("\3\2\2\2\u012b\u0123\3\2\2\2\u012b\u0125\3\2\2\2\u012b")
        buf.write("\u0126\3\2\2\2\u012b\u0128\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012c<\3\2\2\2\u012d\u012e\7(\2\2\u012e\u0133\7(\2\2")
        buf.write("\u012f\u0130\7~\2\2\u0130\u0133\7~\2\2\u0131\u0133\7#")
        buf.write("\2\2\u0132\u012d\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0131")
        buf.write("\3\2\2\2\u0133>\3\2\2\2\u0134\u0135\7<\2\2\u0135\u0141")
        buf.write("\7?\2\2\u0136\u0137\7-\2\2\u0137\u0141\7?\2\2\u0138\u0139")
        buf.write("\7/\2\2\u0139\u0141\7?\2\2\u013a\u013b\7,\2\2\u013b\u0141")
        buf.write("\7?\2\2\u013c\u013d\7\61\2\2\u013d\u0141\7?\2\2\u013e")
        buf.write("\u013f\7\'\2\2\u013f\u0141\7?\2\2\u0140\u0134\3\2\2\2")
        buf.write("\u0140\u0136\3\2\2\2\u0140\u0138\3\2\2\2\u0140\u013a\3")
        buf.write("\2\2\2\u0140\u013c\3\2\2\2\u0140\u013e\3\2\2\2\u0141@")
        buf.write("\3\2\2\2\u0142\u0143\7\60\2\2\u0143B\3\2\2\2\u0144\u0145")
        buf.write("\7?\2\2\u0145D\3\2\2\2\u0146\u0147\7-\2\2\u0147F\3\2\2")
        buf.write("\2\u0148\u0149\7/\2\2\u0149H\3\2\2\2\u014a\u014b\7,\2")
        buf.write("\2\u014bJ\3\2\2\2\u014c\u014d\7\61\2\2\u014dL\3\2\2\2")
        buf.write("\u014e\u014f\7\'\2\2\u014fN\3\2\2\2\u0150\u0151\7*\2\2")
        buf.write("\u0151P\3\2\2\2\u0152\u0153\7+\2\2\u0153R\3\2\2\2\u0154")
        buf.write("\u0155\7]\2\2\u0155T\3\2\2\2\u0156\u0157\7_\2\2\u0157")
        buf.write("V\3\2\2\2\u0158\u0159\7}\2\2\u0159X\3\2\2\2\u015a\u015b")
        buf.write("\7\177\2\2\u015bZ\3\2\2\2\u015c\u015d\7.\2\2\u015d\\\3")
        buf.write("\2\2\2\u015e\u015f\7=\2\2\u015f^\3\2\2\2\u0160\u0161\t")
        buf.write("\5\2\2\u0161`\3\2\2\2\u0162\u0164\5_\60\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u016d\7\60\2")
        buf.write("\2\u0168\u016a\5_\60\2\u0169\u0168\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016e\3\2\2\2\u016d\u0169\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u0178\3\2\2\2\u016f\u0171\t\6\2\2\u0170\u0172\t")
        buf.write("\7\2\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174")
        buf.write("\3\2\2\2\u0173\u0175\5_\60\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u0179\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179b\3\2\2\2\u017a\u0183\7\62\2\2\u017b\u017f")
        buf.write("\t\b\2\2\u017c\u017e\t\5\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u017a\3")
        buf.write("\2\2\2\u0182\u017b\3\2\2\2\u0183d\3\2\2\2\u0184\u0185")
        buf.write("\7\62\2\2\u0185\u0187\t\t\2\2\u0186\u0188\t\n\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018af\3\2\2\2\u018b\u018c\7\62\2")
        buf.write("\2\u018c\u018e\t\13\2\2\u018d\u018f\t\f\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191h\3\2\2\2\u0192\u0193\7\62\2\2\u0193")
        buf.write("\u0195\t\r\2\2\u0194\u0196\t\16\2\2\u0195\u0194\3\2\2")
        buf.write("\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198j\3\2\2\2\u0199\u019e\5c\62\2\u019a\u019e")
        buf.write("\5e\63\2\u019b\u019e\5g\64\2\u019c\u019e\5i\65\2\u019d")
        buf.write("\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019el\3\2\2\2\u019f\u01a0\n\17\2")
        buf.write("\2\u01a0n\3\2\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a3\t\20")
        buf.write("\2\2\u01a3p\3\2\2\2\u01a4\u01a9\7$\2\2\u01a5\u01a8\5m")
        buf.write("\67\2\u01a6\u01a8\5o8\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ac\u01ad\7$\2\2\u01adr\3\2\2\2\u01ae\u01b2\t\21\2")
        buf.write("\2\u01af\u01b1\t\22\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("t\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\13\2\2\2\u01b6")
        buf.write("v\3\2\2\2\u01b7\u01bc\7$\2\2\u01b8\u01bb\5m\67\2\u01b9")
        buf.write("\u01bb\5o8\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\7")
        buf.write("^\2\2\u01c0\u01c1\n\20\2\2\u01c1\u01c2\b<\3\2\u01c2x\3")
        buf.write("\2\2\2\u01c3\u01c8\7$\2\2\u01c4\u01c7\5m\67\2\u01c5\u01c7")
        buf.write("\5o8\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\b=\4\2")
        buf.write("\u01ccz\3\2\2\2\36\2\u008c\u0090\u0099\u009b\u00a8\u012b")
        buf.write("\u0132\u0140\u0165\u016b\u016d\u0171\u0176\u0178\u017f")
        buf.write("\u0182\u0189\u0190\u0197\u019d\u01a7\u01a9\u01b2\u01ba")
        buf.write("\u01bc\u01c6\u01c8\5\b\2\2\3<\2\3=\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SINGLE_LINE_CMT = 5
    MULTI_LINE_CMT = 6
    NL = 7
    WS = 8
    IF_ = 9
    ELSE_ = 10
    FOR_ = 11
    RETURN_ = 12
    FUNC_ = 13
    TYPE_ = 14
    STRUCT_ = 15
    INTERFACE_ = 16
    STRING_ = 17
    INT_ = 18
    FLOAT_ = 19
    BOOLEAN_ = 20
    CONST_ = 21
    VAR_ = 22
    CONTINUE_ = 23
    BREAK_ = 24
    RANGE_ = 25
    NIL_ = 26
    TRUE_ = 27
    FALSE_ = 28
    COMPARISON_OP = 29
    OP3 = 30
    ASSIGN1 = 31
    OP5 = 32
    ASSIGN = 33
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
            "'||'", "'&&'", "'!'", "':='", "'\n'", "'if'", "'else'", "'for'", 
            "'return'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                  "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                  "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
                  "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                  "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "OP3", "ASSIGN1", 
                  "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", 
                  "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                  "Digit", "FLOAT", "DecInt", "BinInt", "OctInt", "HexInt", 
                  "INTEGER", "Char", "EscapeChar", "STRING", "ID", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
     


