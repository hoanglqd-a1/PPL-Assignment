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
        buf.write("\u01c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\7\7\u008f\n\7\f\7\16\7\u0092\13\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\7\b\u009d\n\b\f\b\16\b\u00a0\13\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0126\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u013b\n")
        buf.write("\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\6\60\u015e\n\60\r\60\16\60\u015f\3\60\3\60\6\60\u0164")
        buf.write("\n\60\r\60\16\60\u0165\5\60\u0168\n\60\3\60\3\60\5\60")
        buf.write("\u016c\n\60\3\60\6\60\u016f\n\60\r\60\16\60\u0170\5\60")
        buf.write("\u0173\n\60\3\61\3\61\3\61\7\61\u0178\n\61\f\61\16\61")
        buf.write("\u017b\13\61\5\61\u017d\n\61\3\62\3\62\3\62\6\62\u0182")
        buf.write("\n\62\r\62\16\62\u0183\3\63\3\63\3\63\6\63\u0189\n\63")
        buf.write("\r\63\16\63\u018a\3\64\3\64\3\64\6\64\u0190\n\64\r\64")
        buf.write("\16\64\u0191\3\65\3\65\3\65\3\65\5\65\u0198\n\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\78\u01a2\n8\f8\168\u01a5")
        buf.write("\138\38\38\39\39\79\u01ab\n9\f9\169\u01ae\139\3:\3:\3")
        buf.write(";\3;\3;\7;\u01b5\n;\f;\16;\u01b8\13;\3;\3;\3;\3;\3<\3")
        buf.write("<\3<\7<\u01c1\n<\f<\16<\u01c4\13<\3<\3<\3\u009e\2=\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\60a\2c\2e\2g\2i\61k\2m\2o\62q\63s\64u\65")
        buf.write("w\66\3\2\22\5\2\13\13\17\17\"\"\4\2\f\f\17\17\3\2\62;")
        buf.write("\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2")
        buf.write("\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$^^ppttvv\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\2\u01e4\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2_\3\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2")
        buf.write("\5|\3\2\2\2\7\177\3\2\2\2\t\u0081\3\2\2\2\13\u0084\3\2")
        buf.write("\2\2\r\u008a\3\2\2\2\17\u0097\3\2\2\2\21\u00a6\3\2\2\2")
        buf.write("\23\u00a9\3\2\2\2\25\u00ae\3\2\2\2\27\u00b2\3\2\2\2\31")
        buf.write("\u00b9\3\2\2\2\33\u00be\3\2\2\2\35\u00c3\3\2\2\2\37\u00ca")
        buf.write("\3\2\2\2!\u00d4\3\2\2\2#\u00db\3\2\2\2%\u00df\3\2\2\2")
        buf.write("\'\u00e5\3\2\2\2)\u00ed\3\2\2\2+\u00f3\3\2\2\2-\u00f7")
        buf.write("\3\2\2\2/\u0100\3\2\2\2\61\u0106\3\2\2\2\63\u010c\3\2")
        buf.write("\2\2\65\u0110\3\2\2\2\67\u0115\3\2\2\29\u0125\3\2\2\2")
        buf.write(";\u012c\3\2\2\2=\u013a\3\2\2\2?\u013c\3\2\2\2A\u013e\3")
        buf.write("\2\2\2C\u0140\3\2\2\2E\u0142\3\2\2\2G\u0144\3\2\2\2I\u0146")
        buf.write("\3\2\2\2K\u0148\3\2\2\2M\u014a\3\2\2\2O\u014c\3\2\2\2")
        buf.write("Q\u014e\3\2\2\2S\u0150\3\2\2\2U\u0152\3\2\2\2W\u0154\3")
        buf.write("\2\2\2Y\u0156\3\2\2\2[\u0158\3\2\2\2]\u015a\3\2\2\2_\u015d")
        buf.write("\3\2\2\2a\u017c\3\2\2\2c\u017e\3\2\2\2e\u0185\3\2\2\2")
        buf.write("g\u018c\3\2\2\2i\u0197\3\2\2\2k\u0199\3\2\2\2m\u019b\3")
        buf.write("\2\2\2o\u019e\3\2\2\2q\u01a8\3\2\2\2s\u01af\3\2\2\2u\u01b1")
        buf.write("\3\2\2\2w\u01bd\3\2\2\2yz\7~\2\2z{\7~\2\2{\4\3\2\2\2|")
        buf.write("}\7(\2\2}~\7(\2\2~\6\3\2\2\2\177\u0080\7#\2\2\u0080\b")
        buf.write("\3\2\2\2\u0081\u0082\7\f\2\2\u0082\n\3\2\2\2\u0083\u0085")
        buf.write("\t\2\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\b\6\2\2\u0089\f\3\2\2\2\u008a\u008b\7\61")
        buf.write("\2\2\u008b\u008c\7\61\2\2\u008c\u0090\3\2\2\2\u008d\u008f")
        buf.write("\n\3\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2")
        buf.write("\u0092\u0090\3\2\2\2\u0093\u0094\7\f\2\2\u0094\u0095\3")
        buf.write("\2\2\2\u0095\u0096\b\7\3\2\u0096\16\3\2\2\2\u0097\u0098")
        buf.write("\7\61\2\2\u0098\u0099\7,\2\2\u0099\u009e\3\2\2\2\u009a")
        buf.write("\u009d\13\2\2\2\u009b\u009d\5\17\b\2\u009c\u009a\3\2\2")
        buf.write("\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\7,\2\2\u00a2\u00a3\7\61\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b\b\3\2\u00a5\20\3\2")
        buf.write("\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7h\2\2\u00a8\22\3")
        buf.write("\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\24\3\2\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7t\2\2\u00b1\26")
        buf.write("\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\30\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb")
        buf.write("\7w\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7e\2\2\u00bd\32")
        buf.write("\3\2\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7{\2\2\u00c0\u00c1")
        buf.write("\7r\2\2\u00c1\u00c2\7g\2\2\u00c2\34\3\2\2\2\u00c3\u00c4")
        buf.write("\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9\7v\2\2\u00c9\36")
        buf.write("\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7e\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3 \3\2\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7i\2\2\u00da\"\3\2\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de$\3")
        buf.write("\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7v\2\2\u00e4&\3")
        buf.write("\2\2\2\u00e5\u00e6\7d\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb")
        buf.write("\7c\2\2\u00eb\u00ec\7p\2\2\u00ec(\3\2\2\2\u00ed\u00ee")
        buf.write("\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7u\2\2\u00f1\u00f2\7v\2\2\u00f2*\3\2\2\2\u00f3\u00f4")
        buf.write("\7x\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7t\2\2\u00f6,\3")
        buf.write("\2\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff.\3")
        buf.write("\2\2\2\u0100\u0101\7d\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7c\2\2\u0104\u0105\7m\2\2\u0105\60")
        buf.write("\3\2\2\2\u0106\u0107\7t\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7i\2\2\u010a\u010b\7g\2\2\u010b\62")
        buf.write("\3\2\2\2\u010c\u010d\7p\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\64\3\2\2\2\u0110\u0111\7v\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7w\2\2\u0113\u0114\7g\2\2\u0114\66")
        buf.write("\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117\7c\2\2\u0117\u0118")
        buf.write("\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a8\3")
        buf.write("\2\2\2\u011b\u011c\7?\2\2\u011c\u0126\7?\2\2\u011d\u011e")
        buf.write("\7#\2\2\u011e\u0126\7?\2\2\u011f\u0126\7>\2\2\u0120\u0121")
        buf.write("\7>\2\2\u0121\u0126\7?\2\2\u0122\u0126\7@\2\2\u0123\u0124")
        buf.write("\7@\2\2\u0124\u0126\7?\2\2\u0125\u011b\3\2\2\2\u0125\u011d")
        buf.write("\3\2\2\2\u0125\u011f\3\2\2\2\u0125\u0120\3\2\2\2\u0125")
        buf.write("\u0122\3\2\2\2\u0125\u0123\3\2\2\2\u0126:\3\2\2\2\u0127")
        buf.write("\u0128\7(\2\2\u0128\u012d\7(\2\2\u0129\u012a\7~\2\2\u012a")
        buf.write("\u012d\7~\2\2\u012b\u012d\7#\2\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u0129\3\2\2\2\u012c\u012b\3\2\2\2\u012d<\3\2\2\2\u012e")
        buf.write("\u012f\7<\2\2\u012f\u013b\7?\2\2\u0130\u0131\7-\2\2\u0131")
        buf.write("\u013b\7?\2\2\u0132\u0133\7/\2\2\u0133\u013b\7?\2\2\u0134")
        buf.write("\u0135\7,\2\2\u0135\u013b\7?\2\2\u0136\u0137\7\61\2\2")
        buf.write("\u0137\u013b\7?\2\2\u0138\u0139\7\'\2\2\u0139\u013b\7")
        buf.write("?\2\2\u013a\u012e\3\2\2\2\u013a\u0130\3\2\2\2\u013a\u0132")
        buf.write("\3\2\2\2\u013a\u0134\3\2\2\2\u013a\u0136\3\2\2\2\u013a")
        buf.write("\u0138\3\2\2\2\u013b>\3\2\2\2\u013c\u013d\7\60\2\2\u013d")
        buf.write("@\3\2\2\2\u013e\u013f\7?\2\2\u013fB\3\2\2\2\u0140\u0141")
        buf.write("\7-\2\2\u0141D\3\2\2\2\u0142\u0143\7/\2\2\u0143F\3\2\2")
        buf.write("\2\u0144\u0145\7,\2\2\u0145H\3\2\2\2\u0146\u0147\7\61")
        buf.write("\2\2\u0147J\3\2\2\2\u0148\u0149\7\'\2\2\u0149L\3\2\2\2")
        buf.write("\u014a\u014b\7*\2\2\u014bN\3\2\2\2\u014c\u014d\7+\2\2")
        buf.write("\u014dP\3\2\2\2\u014e\u014f\7]\2\2\u014fR\3\2\2\2\u0150")
        buf.write("\u0151\7_\2\2\u0151T\3\2\2\2\u0152\u0153\7}\2\2\u0153")
        buf.write("V\3\2\2\2\u0154\u0155\7\177\2\2\u0155X\3\2\2\2\u0156\u0157")
        buf.write("\7.\2\2\u0157Z\3\2\2\2\u0158\u0159\7=\2\2\u0159\\\3\2")
        buf.write("\2\2\u015a\u015b\t\4\2\2\u015b^\3\2\2\2\u015c\u015e\5")
        buf.write("]/\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0167\7\60\2\2\u0162\u0164\5]/\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166\u0168\3\2\2\2\u0167\u0163\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0172\3\2\2\2\u0169\u016b\t\5\2\2\u016a")
        buf.write("\u016c\t\6\2\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016e\3\2\2\2\u016d\u016f\5]/\2\u016e\u016d\3\2")
        buf.write("\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0169\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173`\3\2\2\2\u0174\u017d\7\62\2\2\u0175")
        buf.write("\u0179\t\7\2\2\u0176\u0178\t\4\2\2\u0177\u0176\3\2\2\2")
        buf.write("\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3")
        buf.write("\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u0174")
        buf.write("\3\2\2\2\u017c\u0175\3\2\2\2\u017db\3\2\2\2\u017e\u017f")
        buf.write("\7\62\2\2\u017f\u0181\t\b\2\2\u0180\u0182\t\t\2\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184d\3\2\2\2\u0185\u0186\7\62\2")
        buf.write("\2\u0186\u0188\t\n\2\2\u0187\u0189\t\13\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bf\3\2\2\2\u018c\u018d\7\62\2\2\u018d")
        buf.write("\u018f\t\f\2\2\u018e\u0190\t\r\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192h\3\2\2\2\u0193\u0198\5a\61\2\u0194\u0198")
        buf.write("\5c\62\2\u0195\u0198\5e\63\2\u0196\u0198\5g\64\2\u0197")
        buf.write("\u0193\3\2\2\2\u0197\u0194\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0196\3\2\2\2\u0198j\3\2\2\2\u0199\u019a\n\16\2")
        buf.write("\2\u019al\3\2\2\2\u019b\u019c\7^\2\2\u019c\u019d\t\17")
        buf.write("\2\2\u019dn\3\2\2\2\u019e\u01a3\7$\2\2\u019f\u01a2\5k")
        buf.write("\66\2\u01a0\u01a2\5m\67\2\u01a1\u019f\3\2\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a7\7$\2\2\u01a7p\3\2\2\2\u01a8\u01ac\t\20\2")
        buf.write("\2\u01a9\u01ab\t\21\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("r\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\13\2\2\2\u01b0")
        buf.write("t\3\2\2\2\u01b1\u01b6\7$\2\2\u01b2\u01b5\5k\66\2\u01b3")
        buf.write("\u01b5\5m\67\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba")
        buf.write("\7^\2\2\u01ba\u01bb\n\17\2\2\u01bb\u01bc\b;\4\2\u01bc")
        buf.write("v\3\2\2\2\u01bd\u01c2\7$\2\2\u01be\u01c1\5k\66\2\u01bf")
        buf.write("\u01c1\5m\67\2\u01c0\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3")
        buf.write("\2\2\2\u01c3\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6")
        buf.write("\b<\5\2\u01c6x\3\2\2\2\35\2\u0086\u0090\u009c\u009e\u0125")
        buf.write("\u012c\u013a\u015f\u0165\u0167\u016b\u0170\u0172\u0179")
        buf.write("\u017c\u0183\u018a\u0191\u0197\u01a1\u01a3\u01ac\u01b4")
        buf.write("\u01b6\u01c0\u01c2\6\b\2\2\2\3\2\3;\2\3<\3")
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
     


