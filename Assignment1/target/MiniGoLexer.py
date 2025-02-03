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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u008c\n\6\f\6\16\6\u008f")
        buf.write("\13\6\3\6\5\6\u0092\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7\u009b\n\7\f\7\16\7\u009e\13\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\6\t\u00a8\n\t\r\t\16\t\u00a9\3\t\3\t\3\n\3")
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
        buf.write("\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0134\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0140")
        buf.write("\n \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\6\62\u0166\n\62\r\62\16\62\u0167\3")
        buf.write("\62\3\62\6\62\u016c\n\62\r\62\16\62\u016d\5\62\u0170\n")
        buf.write("\62\3\62\3\62\5\62\u0174\n\62\3\62\6\62\u0177\n\62\r\62")
        buf.write("\16\62\u0178\5\62\u017b\n\62\3\63\3\63\3\63\7\63\u0180")
        buf.write("\n\63\f\63\16\63\u0183\13\63\5\63\u0185\n\63\3\64\3\64")
        buf.write("\3\64\6\64\u018a\n\64\r\64\16\64\u018b\3\65\3\65\3\65")
        buf.write("\6\65\u0191\n\65\r\65\16\65\u0192\3\66\3\66\3\66\6\66")
        buf.write("\u0198\n\66\r\66\16\66\u0199\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u01a0\n\67\38\38\39\39\39\3:\3:\3:\7:\u01aa\n:\f:\16")
        buf.write(":\u01ad\13:\3:\3:\3;\3;\7;\u01b3\n;\f;\16;\u01b6\13;\3")
        buf.write("<\3<\3=\3=\3=\7=\u01bd\n=\f=\16=\u01c0\13=\3=\3=\3=\3")
        buf.write("=\3>\3>\3>\7>\u01c9\n>\f>\16>\u01cc\13>\3>\3>\3\u009c")
        buf.write("\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\2c\62e\2g\2i\2k\2m\63o\2q\2")
        buf.write("s\64u\65w\66y\67{8\3\2\23\3\2\f\f\3\3\f\f\5\2\13\13\17")
        buf.write("\17\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62")
        buf.write("\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$")
        buf.write("^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u01eb\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2c\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3}\3\2\2\2\5\u0080\3\2\2")
        buf.write("\2\7\u0083\3\2\2\2\t\u0085\3\2\2\2\13\u0087\3\2\2\2\r")
        buf.write("\u0095\3\2\2\2\17\u00a4\3\2\2\2\21\u00a7\3\2\2\2\23\u00ad")
        buf.write("\3\2\2\2\25\u00b0\3\2\2\2\27\u00b5\3\2\2\2\31\u00b9\3")
        buf.write("\2\2\2\33\u00c0\3\2\2\2\35\u00c5\3\2\2\2\37\u00ca\3\2")
        buf.write("\2\2!\u00d1\3\2\2\2#\u00db\3\2\2\2%\u00e2\3\2\2\2\'\u00e6")
        buf.write("\3\2\2\2)\u00ec\3\2\2\2+\u00f4\3\2\2\2-\u00fa\3\2\2\2")
        buf.write("/\u00fe\3\2\2\2\61\u0107\3\2\2\2\63\u010d\3\2\2\2\65\u0113")
        buf.write("\3\2\2\2\67\u0117\3\2\2\29\u011c\3\2\2\2;\u012c\3\2\2")
        buf.write("\2=\u0133\3\2\2\2?\u013f\3\2\2\2A\u0141\3\2\2\2C\u0144")
        buf.write("\3\2\2\2E\u0146\3\2\2\2G\u0148\3\2\2\2I\u014a\3\2\2\2")
        buf.write("K\u014c\3\2\2\2M\u014e\3\2\2\2O\u0150\3\2\2\2Q\u0152\3")
        buf.write("\2\2\2S\u0154\3\2\2\2U\u0156\3\2\2\2W\u0158\3\2\2\2Y\u015a")
        buf.write("\3\2\2\2[\u015c\3\2\2\2]\u015e\3\2\2\2_\u0160\3\2\2\2")
        buf.write("a\u0162\3\2\2\2c\u0165\3\2\2\2e\u0184\3\2\2\2g\u0186\3")
        buf.write("\2\2\2i\u018d\3\2\2\2k\u0194\3\2\2\2m\u019f\3\2\2\2o\u01a1")
        buf.write("\3\2\2\2q\u01a3\3\2\2\2s\u01a6\3\2\2\2u\u01b0\3\2\2\2")
        buf.write("w\u01b7\3\2\2\2y\u01b9\3\2\2\2{\u01c5\3\2\2\2}~\7~\2\2")
        buf.write("~\177\7~\2\2\177\4\3\2\2\2\u0080\u0081\7(\2\2\u0081\u0082")
        buf.write("\7(\2\2\u0082\6\3\2\2\2\u0083\u0084\7#\2\2\u0084\b\3\2")
        buf.write("\2\2\u0085\u0086\7<\2\2\u0086\n\3\2\2\2\u0087\u0088\7")
        buf.write("\61\2\2\u0088\u0089\7\61\2\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u008c\n\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0091\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0092\t\3\2\2\u0091\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\b\6\2\2\u0094")
        buf.write("\f\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097\7,\2\2\u0097")
        buf.write("\u009c\3\2\2\2\u0098\u009b\5\r\7\2\u0099\u009b\13\2\2")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u009e")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d")
        buf.write("\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7,\2\2")
        buf.write("\u00a0\u00a1\7\61\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\b\7\2\2\u00a3\16\3\2\2\2\u00a4\u00a5\7\f\2\2\u00a5\20")
        buf.write("\3\2\2\2\u00a6\u00a8\t\4\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ac\b\t\2\2\u00ac\22\3\2")
        buf.write("\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7h\2\2\u00af\24\3")
        buf.write("\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\26\3\2\2\2\u00b5\u00b6")
        buf.write("\7h\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7t\2\2\u00b8\30")
        buf.write("\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\32\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7w\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\34")
        buf.write("\3\2\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7{\2\2\u00c7\u00c8")
        buf.write("\7r\2\2\u00c8\u00c9\7g\2\2\u00c9\36\3\2\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce")
        buf.write("\7w\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0\7v\2\2\u00d0 \3")
        buf.write("\2\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\"\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7i\2\2\u00e1$\3\2\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5&\3")
        buf.write("\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7v\2\2\u00eb(\3")
        buf.write("\2\2\2\u00ec\u00ed\7d\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7p\2\2\u00f3*\3\2\2\2\u00f4\u00f5")
        buf.write("\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7v\2\2\u00f9,\3\2\2\2\u00fa\u00fb")
        buf.write("\7x\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7t\2\2\u00fd.\3")
        buf.write("\2\2\2\u00fe\u00ff\7e\2\2\u00ff\u0100\7q\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u0102\7v\2\2\u0102\u0103\7k\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7w\2\2\u0105\u0106\7g\2\2\u0106\60")
        buf.write("\3\2\2\2\u0107\u0108\7d\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\u010b\7c\2\2\u010b\u010c\7m\2\2\u010c\62")
        buf.write("\3\2\2\2\u010d\u010e\7t\2\2\u010e\u010f\7c\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\u0111\7i\2\2\u0111\u0112\7g\2\2\u0112\64")
        buf.write("\3\2\2\2\u0113\u0114\7p\2\2\u0114\u0115\7k\2\2\u0115\u0116")
        buf.write("\7n\2\2\u0116\66\3\2\2\2\u0117\u0118\7v\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b\7g\2\2\u011b8\3")
        buf.write("\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7c\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7u\2\2\u0120\u0121\7g\2\2\u0121:\3")
        buf.write("\2\2\2\u0122\u0123\7?\2\2\u0123\u012d\7?\2\2\u0124\u0125")
        buf.write("\7#\2\2\u0125\u012d\7?\2\2\u0126\u012d\7>\2\2\u0127\u0128")
        buf.write("\7>\2\2\u0128\u012d\7?\2\2\u0129\u012d\7@\2\2\u012a\u012b")
        buf.write("\7@\2\2\u012b\u012d\7?\2\2\u012c\u0122\3\2\2\2\u012c\u0124")
        buf.write("\3\2\2\2\u012c\u0126\3\2\2\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012d<\3\2\2\2\u012e")
        buf.write("\u012f\7(\2\2\u012f\u0134\7(\2\2\u0130\u0131\7~\2\2\u0131")
        buf.write("\u0134\7~\2\2\u0132\u0134\7#\2\2\u0133\u012e\3\2\2\2\u0133")
        buf.write("\u0130\3\2\2\2\u0133\u0132\3\2\2\2\u0134>\3\2\2\2\u0135")
        buf.write("\u0136\7-\2\2\u0136\u0140\7?\2\2\u0137\u0138\7/\2\2\u0138")
        buf.write("\u0140\7?\2\2\u0139\u013a\7,\2\2\u013a\u0140\7?\2\2\u013b")
        buf.write("\u013c\7\61\2\2\u013c\u0140\7?\2\2\u013d\u013e\7\'\2\2")
        buf.write("\u013e\u0140\7?\2\2\u013f\u0135\3\2\2\2\u013f\u0137\3")
        buf.write("\2\2\2\u013f\u0139\3\2\2\2\u013f\u013b\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140@\3\2\2\2\u0141\u0142\7<\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143B\3\2\2\2\u0144\u0145\7\60\2\2\u0145D\3\2")
        buf.write("\2\2\u0146\u0147\7?\2\2\u0147F\3\2\2\2\u0148\u0149\7-")
        buf.write("\2\2\u0149H\3\2\2\2\u014a\u014b\7/\2\2\u014bJ\3\2\2\2")
        buf.write("\u014c\u014d\7,\2\2\u014dL\3\2\2\2\u014e\u014f\7\61\2")
        buf.write("\2\u014fN\3\2\2\2\u0150\u0151\7\'\2\2\u0151P\3\2\2\2\u0152")
        buf.write("\u0153\7*\2\2\u0153R\3\2\2\2\u0154\u0155\7+\2\2\u0155")
        buf.write("T\3\2\2\2\u0156\u0157\7]\2\2\u0157V\3\2\2\2\u0158\u0159")
        buf.write("\7_\2\2\u0159X\3\2\2\2\u015a\u015b\7}\2\2\u015bZ\3\2\2")
        buf.write("\2\u015c\u015d\7\177\2\2\u015d\\\3\2\2\2\u015e\u015f\7")
        buf.write(".\2\2\u015f^\3\2\2\2\u0160\u0161\7=\2\2\u0161`\3\2\2\2")
        buf.write("\u0162\u0163\t\5\2\2\u0163b\3\2\2\2\u0164\u0166\5a\61")
        buf.write("\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016f\7\60\2\2\u016a\u016c\5a\61\2\u016b\u016a\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016b\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u017a\3\2\2\2\u0171\u0173\t\6\2\2")
        buf.write("\u0172\u0174\t\7\2\2\u0173\u0172\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0174\u0176\3\2\2\2\u0175\u0177\5a\61\2\u0176\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0171\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bd\3\2\2\2\u017c\u0185\7\62\2")
        buf.write("\2\u017d\u0181\t\b\2\2\u017e\u0180\t\5\2\2\u017f\u017e")
        buf.write("\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0184\u017c\3\2\2\2\u0184\u017d\3\2\2\2\u0185f\3\2\2")
        buf.write("\2\u0186\u0187\7\62\2\2\u0187\u0189\t\t\2\2\u0188\u018a")
        buf.write("\t\n\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018ch\3\2\2\2\u018d")
        buf.write("\u018e\7\62\2\2\u018e\u0190\t\13\2\2\u018f\u0191\t\f\2")
        buf.write("\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193j\3\2\2\2\u0194\u0195")
        buf.write("\7\62\2\2\u0195\u0197\t\r\2\2\u0196\u0198\t\16\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019al\3\2\2\2\u019b\u01a0\5e\63")
        buf.write("\2\u019c\u01a0\5g\64\2\u019d\u01a0\5i\65\2\u019e\u01a0")
        buf.write("\5k\66\2\u019f\u019b\3\2\2\2\u019f\u019c\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u01a0n\3\2\2\2\u01a1")
        buf.write("\u01a2\n\17\2\2\u01a2p\3\2\2\2\u01a3\u01a4\7^\2\2\u01a4")
        buf.write("\u01a5\t\20\2\2\u01a5r\3\2\2\2\u01a6\u01ab\7$\2\2\u01a7")
        buf.write("\u01aa\5o8\2\u01a8\u01aa\5q9\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ae\u01af\7$\2\2\u01aft\3\2\2\2\u01b0\u01b4\t")
        buf.write("\21\2\2\u01b1\u01b3\t\22\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5v\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\13\2\2")
        buf.write("\2\u01b8x\3\2\2\2\u01b9\u01be\7$\2\2\u01ba\u01bd\5o8\2")
        buf.write("\u01bb\u01bd\5q9\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2")
        buf.write("\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c2\7^\2\2\u01c2\u01c3\n\20\2\2\u01c3\u01c4\b=\3\2")
        buf.write("\u01c4z\3\2\2\2\u01c5\u01ca\7$\2\2\u01c6\u01c9\5o8\2\u01c7")
        buf.write("\u01c9\5q9\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\b")
        buf.write(">\4\2\u01ce|\3\2\2\2\36\2\u008d\u0091\u009a\u009c\u00a9")
        buf.write("\u012c\u0133\u013f\u0167\u016d\u016f\u0173\u0178\u017a")
        buf.write("\u0181\u0184\u018b\u0192\u0199\u019f\u01a9\u01ab\u01b4")
        buf.write("\u01bc\u01be\u01c8\u01ca\5\b\2\2\3=\2\3>\3")
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
    BOOLEAN_OP = 30
    UPT_ASSIGN = 31
    ASSIGN = 32
    DOT = 33
    INIT = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    MOD = 39
    LPAREN = 40
    RPAREN = 41
    LSB = 42
    RSB = 43
    LCB = 44
    RCB = 45
    COMMA = 46
    SEMICOLON = 47
    FLOAT = 48
    INTEGER = 49
    STRING = 50
    ID = 51
    ERROR_CHAR = 52
    ILLEGAL_ESCAPE = 53
    UNCLOSE_STRING = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'!'", "':'", "'\n'", "'if'", "'else'", "'for'", 
            "'return'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'", "':='", 
            "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "BOOLEAN_OP", "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
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
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
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
     


