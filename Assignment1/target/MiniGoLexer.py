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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01c3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\6\6\u0085\n\6\r\6\16\6\u0086\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\7\7\u008f\n\7\f\7\16\7\u0092\13\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\b\u009b\n\b\f\b\16\b\u009e\13\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u0122\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u0129\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u0137\n\37\3 \3 \3!\3!")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\6\60\u015a\n\60")
        buf.write("\r\60\16\60\u015b\3\60\3\60\6\60\u0160\n\60\r\60\16\60")
        buf.write("\u0161\5\60\u0164\n\60\3\60\3\60\5\60\u0168\n\60\3\60")
        buf.write("\6\60\u016b\n\60\r\60\16\60\u016c\5\60\u016f\n\60\3\61")
        buf.write("\3\61\3\61\7\61\u0174\n\61\f\61\16\61\u0177\13\61\5\61")
        buf.write("\u0179\n\61\3\62\3\62\3\62\6\62\u017e\n\62\r\62\16\62")
        buf.write("\u017f\3\63\3\63\3\63\6\63\u0185\n\63\r\63\16\63\u0186")
        buf.write("\3\64\3\64\3\64\6\64\u018c\n\64\r\64\16\64\u018d\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u0194\n\65\3\66\3\66\3\67\3\67\3")
        buf.write("\67\38\38\38\78\u019e\n8\f8\168\u01a1\138\38\38\39\39")
        buf.write("\79\u01a7\n9\f9\169\u01aa\139\3:\3:\3;\3;\3;\7;\u01b1")
        buf.write("\n;\f;\16;\u01b4\13;\3;\3;\3;\3;\3<\3<\3<\7<\u01bd\n<")
        buf.write("\f<\16<\u01c0\13<\3<\3<\3\u009c\2=\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\60")
        buf.write("a\2c\2e\2g\2i\61k\2m\2o\62q\63s\64u\65w\66\3\2\22\5\2")
        buf.write("\13\13\17\17\"\"\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CH")
        buf.write("ch\4\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u01e0")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2_\3\2")
        buf.write("\2\2\2i\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5|\3\2\2\2\7\177\3\2\2\2")
        buf.write("\t\u0081\3\2\2\2\13\u0084\3\2\2\2\r\u008a\3\2\2\2\17\u0095")
        buf.write("\3\2\2\2\21\u00a2\3\2\2\2\23\u00a5\3\2\2\2\25\u00aa\3")
        buf.write("\2\2\2\27\u00ae\3\2\2\2\31\u00b5\3\2\2\2\33\u00ba\3\2")
        buf.write("\2\2\35\u00bf\3\2\2\2\37\u00c6\3\2\2\2!\u00d0\3\2\2\2")
        buf.write("#\u00d7\3\2\2\2%\u00db\3\2\2\2\'\u00e1\3\2\2\2)\u00e9")
        buf.write("\3\2\2\2+\u00ef\3\2\2\2-\u00f3\3\2\2\2/\u00fc\3\2\2\2")
        buf.write("\61\u0102\3\2\2\2\63\u0108\3\2\2\2\65\u010c\3\2\2\2\67")
        buf.write("\u0111\3\2\2\29\u0121\3\2\2\2;\u0128\3\2\2\2=\u0136\3")
        buf.write("\2\2\2?\u0138\3\2\2\2A\u013a\3\2\2\2C\u013c\3\2\2\2E\u013e")
        buf.write("\3\2\2\2G\u0140\3\2\2\2I\u0142\3\2\2\2K\u0144\3\2\2\2")
        buf.write("M\u0146\3\2\2\2O\u0148\3\2\2\2Q\u014a\3\2\2\2S\u014c\3")
        buf.write("\2\2\2U\u014e\3\2\2\2W\u0150\3\2\2\2Y\u0152\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0159\3\2\2\2a\u0178\3\2\2\2")
        buf.write("c\u017a\3\2\2\2e\u0181\3\2\2\2g\u0188\3\2\2\2i\u0193\3")
        buf.write("\2\2\2k\u0195\3\2\2\2m\u0197\3\2\2\2o\u019a\3\2\2\2q\u01a4")
        buf.write("\3\2\2\2s\u01ab\3\2\2\2u\u01ad\3\2\2\2w\u01b9\3\2\2\2")
        buf.write("yz\7~\2\2z{\7~\2\2{\4\3\2\2\2|}\7(\2\2}~\7(\2\2~\6\3\2")
        buf.write("\2\2\177\u0080\7#\2\2\u0080\b\3\2\2\2\u0081\u0082\7\f")
        buf.write("\2\2\u0082\n\3\2\2\2\u0083\u0085\t\2\2\2\u0084\u0083\3")
        buf.write("\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\6\2\2\u0089")
        buf.write("\f\3\2\2\2\u008a\u008b\7\61\2\2\u008b\u008c\7\61\2\2\u008c")
        buf.write("\u0090\3\2\2\2\u008d\u008f\n\3\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094")
        buf.write("\7\f\2\2\u0094\16\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097")
        buf.write("\7,\2\2\u0097\u009c\3\2\2\2\u0098\u009b\13\2\2\2\u0099")
        buf.write("\u009b\5\17\b\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2")
        buf.write("\2\u009b\u009e\3\2\2\2\u009c\u009d\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f")
        buf.write("\u00a0\7,\2\2\u00a0\u00a1\7\61\2\2\u00a1\20\3\2\2\2\u00a2")
        buf.write("\u00a3\7k\2\2\u00a3\u00a4\7h\2\2\u00a4\22\3\2\2\2\u00a5")
        buf.write("\u00a6\7g\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8")
        buf.write("\u00a9\7g\2\2\u00a9\24\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab")
        buf.write("\u00ac\7q\2\2\u00ac\u00ad\7t\2\2\u00ad\26\3\2\2\2\u00ae")
        buf.write("\u00af\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7v\2\2\u00b1")
        buf.write("\u00b2\7w\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7p\2\2\u00b4")
        buf.write("\30\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7w\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7e\2\2\u00b9\32\3\2\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7{\2\2\u00bc\u00bd\7r\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\34\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7w\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\36\3\2\2\2\u00c6")
        buf.write("\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9")
        buf.write("\u00ca\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7h\2\2\u00cc")
        buf.write("\u00cd\7c\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write(" \3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7i\2\2\u00d6\"\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da$\3\2\2\2\u00db")
        buf.write("\u00dc\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0&\3\2\2\2\u00e1")
        buf.write("\u00e2\7d\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7n\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8(\3\2\2\2\u00e9\u00ea\7e\2\2\u00ea")
        buf.write("\u00eb\7q\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7u\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee*\3\2\2\2\u00ef\u00f0\7x\2\2\u00f0")
        buf.write("\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2,\3\2\2\2\u00f3")
        buf.write("\u00f4\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7g\2\2\u00fb.\3\2\2\2\u00fc")
        buf.write("\u00fd\7d\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7m\2\2\u0101\60\3\2\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105")
        buf.write("\u0106\7i\2\2\u0106\u0107\7g\2\2\u0107\62\3\2\2\2\u0108")
        buf.write("\u0109\7p\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\64\3\2\2\2\u010c\u010d\7v\2\2\u010d\u010e\7t\2\2\u010e")
        buf.write("\u010f\7w\2\2\u010f\u0110\7g\2\2\u0110\66\3\2\2\2\u0111")
        buf.write("\u0112\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114")
        buf.write("\u0115\7u\2\2\u0115\u0116\7g\2\2\u01168\3\2\2\2\u0117")
        buf.write("\u0118\7?\2\2\u0118\u0122\7?\2\2\u0119\u011a\7#\2\2\u011a")
        buf.write("\u0122\7?\2\2\u011b\u0122\7>\2\2\u011c\u011d\7>\2\2\u011d")
        buf.write("\u0122\7?\2\2\u011e\u0122\7@\2\2\u011f\u0120\7@\2\2\u0120")
        buf.write("\u0122\7?\2\2\u0121\u0117\3\2\2\2\u0121\u0119\3\2\2\2")
        buf.write("\u0121\u011b\3\2\2\2\u0121\u011c\3\2\2\2\u0121\u011e\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0122:\3\2\2\2\u0123\u0124")
        buf.write("\7(\2\2\u0124\u0129\7(\2\2\u0125\u0126\7~\2\2\u0126\u0129")
        buf.write("\7~\2\2\u0127\u0129\7#\2\2\u0128\u0123\3\2\2\2\u0128\u0125")
        buf.write("\3\2\2\2\u0128\u0127\3\2\2\2\u0129<\3\2\2\2\u012a\u012b")
        buf.write("\7<\2\2\u012b\u0137\7?\2\2\u012c\u012d\7-\2\2\u012d\u0137")
        buf.write("\7?\2\2\u012e\u012f\7/\2\2\u012f\u0137\7?\2\2\u0130\u0131")
        buf.write("\7,\2\2\u0131\u0137\7?\2\2\u0132\u0133\7\61\2\2\u0133")
        buf.write("\u0137\7?\2\2\u0134\u0135\7\'\2\2\u0135\u0137\7?\2\2\u0136")
        buf.write("\u012a\3\2\2\2\u0136\u012c\3\2\2\2\u0136\u012e\3\2\2\2")
        buf.write("\u0136\u0130\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0134\3")
        buf.write("\2\2\2\u0137>\3\2\2\2\u0138\u0139\7\60\2\2\u0139@\3\2")
        buf.write("\2\2\u013a\u013b\7?\2\2\u013bB\3\2\2\2\u013c\u013d\7-")
        buf.write("\2\2\u013dD\3\2\2\2\u013e\u013f\7/\2\2\u013fF\3\2\2\2")
        buf.write("\u0140\u0141\7,\2\2\u0141H\3\2\2\2\u0142\u0143\7\61\2")
        buf.write("\2\u0143J\3\2\2\2\u0144\u0145\7\'\2\2\u0145L\3\2\2\2\u0146")
        buf.write("\u0147\7*\2\2\u0147N\3\2\2\2\u0148\u0149\7+\2\2\u0149")
        buf.write("P\3\2\2\2\u014a\u014b\7]\2\2\u014bR\3\2\2\2\u014c\u014d")
        buf.write("\7_\2\2\u014dT\3\2\2\2\u014e\u014f\7}\2\2\u014fV\3\2\2")
        buf.write("\2\u0150\u0151\7\177\2\2\u0151X\3\2\2\2\u0152\u0153\7")
        buf.write(".\2\2\u0153Z\3\2\2\2\u0154\u0155\7=\2\2\u0155\\\3\2\2")
        buf.write("\2\u0156\u0157\t\4\2\2\u0157^\3\2\2\2\u0158\u015a\5]/")
        buf.write("\2\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u0163\7\60\2\2\u015e\u0160\5]/\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3")
        buf.write("\2\2\2\u0162\u0164\3\2\2\2\u0163\u015f\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u016e\3\2\2\2\u0165\u0167\t\5\2\2\u0166")
        buf.write("\u0168\t\6\2\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168\u016a\3\2\2\2\u0169\u016b\5]/\2\u016a\u0169\3\2")
        buf.write("\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0165\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f`\3\2\2\2\u0170\u0179\7\62\2\2\u0171")
        buf.write("\u0175\t\7\2\2\u0172\u0174\t\4\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0170")
        buf.write("\3\2\2\2\u0178\u0171\3\2\2\2\u0179b\3\2\2\2\u017a\u017b")
        buf.write("\7\62\2\2\u017b\u017d\t\b\2\2\u017c\u017e\t\t\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180d\3\2\2\2\u0181\u0182\7\62\2")
        buf.write("\2\u0182\u0184\t\n\2\2\u0183\u0185\t\13\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187f\3\2\2\2\u0188\u0189\7\62\2\2\u0189")
        buf.write("\u018b\t\f\2\2\u018a\u018c\t\r\2\2\u018b\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018eh\3\2\2\2\u018f\u0194\5a\61\2\u0190\u0194")
        buf.write("\5c\62\2\u0191\u0194\5e\63\2\u0192\u0194\5g\64\2\u0193")
        buf.write("\u018f\3\2\2\2\u0193\u0190\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0192\3\2\2\2\u0194j\3\2\2\2\u0195\u0196\n\16\2")
        buf.write("\2\u0196l\3\2\2\2\u0197\u0198\7^\2\2\u0198\u0199\t\17")
        buf.write("\2\2\u0199n\3\2\2\2\u019a\u019f\7$\2\2\u019b\u019e\5k")
        buf.write("\66\2\u019c\u019e\5m\67\2\u019d\u019b\3\2\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a2\u01a3\7$\2\2\u01a3p\3\2\2\2\u01a4\u01a8\t\20\2")
        buf.write("\2\u01a5\u01a7\t\21\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("r\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\13\2\2\2\u01ac")
        buf.write("t\3\2\2\2\u01ad\u01b2\7$\2\2\u01ae\u01b1\5k\66\2\u01af")
        buf.write("\u01b1\5m\67\2\u01b0\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2")
        buf.write("\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6")
        buf.write("\7^\2\2\u01b6\u01b7\n\17\2\2\u01b7\u01b8\b;\3\2\u01b8")
        buf.write("v\3\2\2\2\u01b9\u01be\7$\2\2\u01ba\u01bd\5k\66\2\u01bb")
        buf.write("\u01bd\5m\67\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2")
        buf.write("\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2")
        buf.write("\b<\4\2\u01c2x\3\2\2\2\35\2\u0086\u0090\u009a\u009c\u0121")
        buf.write("\u0128\u0136\u015b\u0161\u0163\u0167\u016c\u016e\u0175")
        buf.write("\u0178\u017f\u0186\u018d\u0193\u019d\u019f\u01a8\u01b0")
        buf.write("\u01b2\u01bc\u01be\5\b\2\2\3;\2\3<\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NL = 4
    WS = 5
    SINGLE_LINE_CMT = 6
    MULTI_LINE_CMT = 7
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
    OP3 = 29
    ASSIGN1 = 30
    OP5 = 31
    ASSIGN = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    LPAREN = 38
    RPAREN = 39
    LSB = 40
    RSB = 41
    LCB = 42
    RCB = 43
    COMMA = 44
    SEMICOLON = 45
    FLOAT = 46
    INTEGER = 47
    STRING = 48
    ID = 49
    ERROR_CHAR = 50
    ILLEGAL_ESCAPE = 51
    UNCLOSE_STRING = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'!'", "'\n'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'nil'", "'true'", "'false'", "'.'", "'='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NL", "WS", "SINGLE_LINE_CMT", 
                  "MULTI_LINE_CMT", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
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
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.UNCLOSE_STRING_action 
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
     


