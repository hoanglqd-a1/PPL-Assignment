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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u01a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\3\6\3w\n\3\r\3\16\3x\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u0083\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0104\n\31\3\32\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u010b\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0117\n\33\3\34\3\34\3\35\3\35\3\36\3")
        buf.write("\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\6,\u013a\n,\r")
        buf.write(",\16,\u013b\3,\3,\6,\u0140\n,\r,\16,\u0141\5,\u0144\n")
        buf.write(",\3,\3,\5,\u0148\n,\3,\6,\u014b\n,\r,\16,\u014c\5,\u014f")
        buf.write("\n,\3-\3-\3-\7-\u0154\n-\f-\16-\u0157\13-\5-\u0159\n-")
        buf.write("\3.\3.\3.\6.\u015e\n.\r.\16.\u015f\3/\3/\3/\6/\u0165\n")
        buf.write("/\r/\16/\u0166\3\60\3\60\3\60\6\60\u016c\n\60\r\60\16")
        buf.write("\60\u016d\3\61\3\61\3\61\3\61\5\61\u0174\n\61\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\7\64\u017e\n\64\f\64\16")
        buf.write("\64\u0181\13\64\3\64\3\64\3\65\3\65\7\65\u0187\n\65\f")
        buf.write("\65\16\65\u018a\13\65\3\66\3\66\3\67\3\67\3\67\7\67\u0191")
        buf.write("\n\67\f\67\16\67\u0194\13\67\3\67\3\67\3\67\3\67\38\3")
        buf.write("8\38\78\u019d\n8\f8\168\u01a0\138\38\38\2\29\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U\2W")
        buf.write(",Y\2[\2]\2_\2a-c\2e\2g.i/k\60m\61o\62\3\2\21\5\2\13\13")
        buf.write("\17\17\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2")
        buf.write("\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2")
        buf.write("$$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u01be\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2W\3\2")
        buf.write("\2\2\2a\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5v\3\2\2\2\7\u0082\3\2\2")
        buf.write("\2\t\u0084\3\2\2\2\13\u0087\3\2\2\2\r\u008c\3\2\2\2\17")
        buf.write("\u0090\3\2\2\2\21\u0097\3\2\2\2\23\u009c\3\2\2\2\25\u00a1")
        buf.write("\3\2\2\2\27\u00a8\3\2\2\2\31\u00b2\3\2\2\2\33\u00b9\3")
        buf.write("\2\2\2\35\u00bd\3\2\2\2\37\u00c3\3\2\2\2!\u00cb\3\2\2")
        buf.write("\2#\u00d1\3\2\2\2%\u00d5\3\2\2\2\'\u00de\3\2\2\2)\u00e4")
        buf.write("\3\2\2\2+\u00ea\3\2\2\2-\u00ee\3\2\2\2/\u00f3\3\2\2\2")
        buf.write("\61\u0103\3\2\2\2\63\u010a\3\2\2\2\65\u0116\3\2\2\2\67")
        buf.write("\u0118\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011e\3")
        buf.write("\2\2\2?\u0120\3\2\2\2A\u0122\3\2\2\2C\u0124\3\2\2\2E\u0126")
        buf.write("\3\2\2\2G\u0128\3\2\2\2I\u012a\3\2\2\2K\u012c\3\2\2\2")
        buf.write("M\u012e\3\2\2\2O\u0130\3\2\2\2Q\u0132\3\2\2\2S\u0134\3")
        buf.write("\2\2\2U\u0136\3\2\2\2W\u0139\3\2\2\2Y\u0158\3\2\2\2[\u015a")
        buf.write("\3\2\2\2]\u0161\3\2\2\2_\u0168\3\2\2\2a\u0173\3\2\2\2")
        buf.write("c\u0175\3\2\2\2e\u0177\3\2\2\2g\u017a\3\2\2\2i\u0184\3")
        buf.write("\2\2\2k\u018b\3\2\2\2m\u018d\3\2\2\2o\u0199\3\2\2\2qr")
        buf.write("\7\f\2\2rs\3\2\2\2st\b\2\2\2t\4\3\2\2\2uw\t\2\2\2vu\3")
        buf.write("\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\b\3\2")
        buf.write("\2{\6\3\2\2\2|}\7^\2\2}\u0083\7^\2\2~\177\7^\2\2\177\u0083")
        buf.write("\7,\2\2\u0080\u0081\7,\2\2\u0081\u0083\7^\2\2\u0082|\3")
        buf.write("\2\2\2\u0082~\3\2\2\2\u0082\u0080\3\2\2\2\u0083\b\3\2")
        buf.write("\2\2\u0084\u0085\7k\2\2\u0085\u0086\7h\2\2\u0086\n\3\2")
        buf.write("\2\2\u0087\u0088\7g\2\2\u0088\u0089\7n\2\2\u0089\u008a")
        buf.write("\7u\2\2\u008a\u008b\7g\2\2\u008b\f\3\2\2\2\u008c\u008d")
        buf.write("\7h\2\2\u008d\u008e\7q\2\2\u008e\u008f\7t\2\2\u008f\16")
        buf.write("\3\2\2\2\u0090\u0091\7t\2\2\u0091\u0092\7g\2\2\u0092\u0093")
        buf.write("\7v\2\2\u0093\u0094\7w\2\2\u0094\u0095\7t\2\2\u0095\u0096")
        buf.write("\7p\2\2\u0096\20\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b\7e\2\2\u009b\22")
        buf.write("\3\2\2\2\u009c\u009d\7v\2\2\u009d\u009e\7{\2\2\u009e\u009f")
        buf.write("\7r\2\2\u009f\u00a0\7g\2\2\u00a0\24\3\2\2\2\u00a1\u00a2")
        buf.write("\7u\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7\7v\2\2\u00a7\26")
        buf.write("\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7h\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\30\3\2\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7i\2\2\u00b8\32\3\2\2\2\u00b9\u00ba")
        buf.write("\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\34")
        buf.write("\3\2\2\2\u00bd\u00be\7h\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\36")
        buf.write("\3\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7q\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7p\2\2\u00ca \3\2\2\2\u00cb\u00cc")
        buf.write("\7e\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7u\2\2\u00cf\u00d0\7v\2\2\u00d0\"\3\2\2\2\u00d1\u00d2")
        buf.write("\7x\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7t\2\2\u00d4$\3")
        buf.write("\2\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7g\2\2\u00dd&\3")
        buf.write("\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7m\2\2\u00e3(\3")
        buf.write("\2\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7i\2\2\u00e8\u00e9\7g\2\2\u00e9*\3")
        buf.write("\2\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed,\3\2\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2.\3")
        buf.write("\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7g\2\2\u00f8\60")
        buf.write("\3\2\2\2\u00f9\u00fa\7?\2\2\u00fa\u0104\7?\2\2\u00fb\u00fc")
        buf.write("\7#\2\2\u00fc\u0104\7?\2\2\u00fd\u0104\7>\2\2\u00fe\u00ff")
        buf.write("\7>\2\2\u00ff\u0104\7?\2\2\u0100\u0104\7@\2\2\u0101\u0102")
        buf.write("\7@\2\2\u0102\u0104\7?\2\2\u0103\u00f9\3\2\2\2\u0103\u00fb")
        buf.write("\3\2\2\2\u0103\u00fd\3\2\2\2\u0103\u00fe\3\2\2\2\u0103")
        buf.write("\u0100\3\2\2\2\u0103\u0101\3\2\2\2\u0104\62\3\2\2\2\u0105")
        buf.write("\u0106\7(\2\2\u0106\u010b\7(\2\2\u0107\u0108\7~\2\2\u0108")
        buf.write("\u010b\7~\2\2\u0109\u010b\7#\2\2\u010a\u0105\3\2\2\2\u010a")
        buf.write("\u0107\3\2\2\2\u010a\u0109\3\2\2\2\u010b\64\3\2\2\2\u010c")
        buf.write("\u010d\7-\2\2\u010d\u0117\7?\2\2\u010e\u010f\7/\2\2\u010f")
        buf.write("\u0117\7?\2\2\u0110\u0111\7,\2\2\u0111\u0117\7?\2\2\u0112")
        buf.write("\u0113\7\61\2\2\u0113\u0117\7?\2\2\u0114\u0115\7\'\2\2")
        buf.write("\u0115\u0117\7?\2\2\u0116\u010c\3\2\2\2\u0116\u010e\3")
        buf.write("\2\2\2\u0116\u0110\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\66\3\2\2\2\u0118\u0119\7\60\2\2\u01198")
        buf.write("\3\2\2\2\u011a\u011b\7?\2\2\u011b:\3\2\2\2\u011c\u011d")
        buf.write("\7-\2\2\u011d<\3\2\2\2\u011e\u011f\7/\2\2\u011f>\3\2\2")
        buf.write("\2\u0120\u0121\7,\2\2\u0121@\3\2\2\2\u0122\u0123\7\61")
        buf.write("\2\2\u0123B\3\2\2\2\u0124\u0125\7\'\2\2\u0125D\3\2\2\2")
        buf.write("\u0126\u0127\7*\2\2\u0127F\3\2\2\2\u0128\u0129\7+\2\2")
        buf.write("\u0129H\3\2\2\2\u012a\u012b\7]\2\2\u012bJ\3\2\2\2\u012c")
        buf.write("\u012d\7_\2\2\u012dL\3\2\2\2\u012e\u012f\7}\2\2\u012f")
        buf.write("N\3\2\2\2\u0130\u0131\7\177\2\2\u0131P\3\2\2\2\u0132\u0133")
        buf.write("\7.\2\2\u0133R\3\2\2\2\u0134\u0135\7=\2\2\u0135T\3\2\2")
        buf.write("\2\u0136\u0137\t\3\2\2\u0137V\3\2\2\2\u0138\u013a\5U+")
        buf.write("\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u0143\7\60\2\2\u013e\u0140\5U+\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142\u0144\3\2\2\2\u0143\u013f\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u014e\3\2\2\2\u0145\u0147\t\4\2\2\u0146")
        buf.write("\u0148\t\5\2\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u014b\5U+\2\u014a\u0149\3\2")
        buf.write("\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u0145\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014fX\3\2\2\2\u0150\u0159\7\62\2\2\u0151")
        buf.write("\u0155\t\6\2\2\u0152\u0154\t\3\2\2\u0153\u0152\3\2\2\2")
        buf.write("\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0150")
        buf.write("\3\2\2\2\u0158\u0151\3\2\2\2\u0159Z\3\2\2\2\u015a\u015b")
        buf.write("\7\62\2\2\u015b\u015d\t\7\2\2\u015c\u015e\t\b\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\\\3\2\2\2\u0161\u0162\7\62")
        buf.write("\2\2\u0162\u0164\t\t\2\2\u0163\u0165\t\n\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167^\3\2\2\2\u0168\u0169\7\62\2\2\u0169")
        buf.write("\u016b\t\13\2\2\u016a\u016c\t\f\2\2\u016b\u016a\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e`\3\2\2\2\u016f\u0174\5Y-\2\u0170\u0174")
        buf.write("\5[.\2\u0171\u0174\5]/\2\u0172\u0174\5_\60\2\u0173\u016f")
        buf.write("\3\2\2\2\u0173\u0170\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174b\3\2\2\2\u0175\u0176\n\r\2\2\u0176")
        buf.write("d\3\2\2\2\u0177\u0178\7^\2\2\u0178\u0179\t\16\2\2\u0179")
        buf.write("f\3\2\2\2\u017a\u017f\7$\2\2\u017b\u017e\5c\62\2\u017c")
        buf.write("\u017e\5e\63\2\u017d\u017b\3\2\2\2\u017d\u017c\3\2\2\2")
        buf.write("\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183")
        buf.write("\7$\2\2\u0183h\3\2\2\2\u0184\u0188\t\17\2\2\u0185\u0187")
        buf.write("\t\20\2\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189j\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018b\u018c\13\2\2\2\u018cl\3\2\2\2\u018d")
        buf.write("\u0192\7$\2\2\u018e\u0191\5c\62\2\u018f\u0191\5e\63\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196\7^\2\2\u0196")
        buf.write("\u0197\n\16\2\2\u0197\u0198\b\67\3\2\u0198n\3\2\2\2\u0199")
        buf.write("\u019e\7$\2\2\u019a\u019d\5c\62\2\u019b\u019d\5e\63\2")
        buf.write("\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d\u01a0\3")
        buf.write("\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b8\4\2\u01a2")
        buf.write("p\3\2\2\2\33\2x\u0082\u0103\u010a\u0116\u013b\u0141\u0143")
        buf.write("\u0147\u014c\u014e\u0155\u0158\u015f\u0166\u016d\u0173")
        buf.write("\u017d\u017f\u0188\u0190\u0192\u019c\u019e\5\b\2\2\3\67")
        buf.write("\2\38\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NL = 1
    WS = 2
    COMMENT = 3
    IF_ = 4
    ELSE_ = 5
    FOR_ = 6
    RETURN_ = 7
    FUNC_ = 8
    TYPE_ = 9
    STRUCT_ = 10
    INTERFACE_ = 11
    STRING_ = 12
    INT_ = 13
    FLOAT_ = 14
    BOOLEAN_ = 15
    CONST_ = 16
    VAR_ = 17
    CONTINUE_ = 18
    BREAK_ = 19
    RANGE_ = 20
    NIL_ = 21
    TRUE_ = 22
    FALSE_ = 23
    OP2 = 24
    OP3 = 25
    OP4 = 26
    OP5 = 27
    ASSIGN = 28
    ADD = 29
    SUB = 30
    MUL = 31
    DIV = 32
    MOD = 33
    LPAREN = 34
    RPAREN = 35
    LSB = 36
    RSB = 37
    LCB = 38
    RCB = 39
    COMMA = 40
    SEMICOLON = 41
    FLOAT = 42
    INTEGER = 43
    STRING = 44
    ID = 45
    ERROR_CHAR = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "COMMENT", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
            "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
            "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
            "NIL_", "TRUE_", "FALSE_", "OP2", "OP3", "OP4", "OP5", "ASSIGN", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", 
            "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", 
            "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "NL", "WS", "COMMENT", "IF_", "ELSE_", "FOR_", "RETURN_", 
                  "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", 
                  "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                  "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "OP2", 
                  "OP3", "OP4", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", 
                  "COMMA", "SEMICOLON", "Digit", "FLOAT", "DecInt", "BinInt", 
                  "OctInt", "HexInt", "INTEGER", "Char", "EscapeChar", "STRING", 
                  "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.UNCLOSE_STRING_action 
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
     


