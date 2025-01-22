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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-")
        buf.write("\u0190\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\3\6\3m\n\3\r\3\16\3n\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4y\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u00fc\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0103\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0110\n\34\3\35\3")
        buf.write("\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\6\'\u0127\n\'\r\'\16\'\u0128\3\'\3\'")
        buf.write("\6\'\u012d\n\'\r\'\16\'\u012e\5\'\u0131\n\'\3\'\3\'\5")
        buf.write("\'\u0135\n\'\3\'\6\'\u0138\n\'\r\'\16\'\u0139\5\'\u013c")
        buf.write("\n\'\3(\3(\3(\7(\u0141\n(\f(\16(\u0144\13(\5(\u0146\n")
        buf.write("(\3)\3)\3)\6)\u014b\n)\r)\16)\u014c\3*\3*\3*\6*\u0152")
        buf.write("\n*\r*\16*\u0153\3+\3+\3+\6+\u0159\n+\r+\16+\u015a\3,")
        buf.write("\3,\3,\3,\5,\u0161\n,\3-\3-\3.\3.\3.\3/\3/\3/\7/\u016b")
        buf.write("\n/\f/\16/\u016e\13/\3/\3/\3\60\3\60\7\60\u0174\n\60\f")
        buf.write("\60\16\60\u0177\13\60\3\61\3\61\3\62\3\62\3\62\7\62\u017e")
        buf.write("\n\62\f\62\16\62\u0181\13\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\7\63\u018a\n\63\f\63\16\63\u018d\13\63\3\63")
        buf.write("\3\63\2\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\2M\'O\2Q\2S\2U\2W(Y\2[\2])_*a+c,e-\3\2\22\5\2")
        buf.write("\13\13\17\17\"\"\6\2\'\',-//\61\61\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZz")
        buf.write("z\5\2\62;CHch\4\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\2\u01ac\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2M\3\2\2\2\2W\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3g\3\2\2\2\5")
        buf.write("l\3\2\2\2\7x\3\2\2\2\tz\3\2\2\2\13}\3\2\2\2\r\u0082\3")
        buf.write("\2\2\2\17\u0086\3\2\2\2\21\u008d\3\2\2\2\23\u0092\3\2")
        buf.write("\2\2\25\u0097\3\2\2\2\27\u009e\3\2\2\2\31\u00a8\3\2\2")
        buf.write("\2\33\u00af\3\2\2\2\35\u00b3\3\2\2\2\37\u00b9\3\2\2\2")
        buf.write("!\u00c1\3\2\2\2#\u00c7\3\2\2\2%\u00cb\3\2\2\2\'\u00d4")
        buf.write("\3\2\2\2)\u00da\3\2\2\2+\u00e0\3\2\2\2-\u00e4\3\2\2\2")
        buf.write("/\u00e9\3\2\2\2\61\u00ef\3\2\2\2\63\u00fb\3\2\2\2\65\u0102")
        buf.write("\3\2\2\2\67\u010f\3\2\2\29\u0111\3\2\2\2;\u0113\3\2\2")
        buf.write("\2=\u0115\3\2\2\2?\u0117\3\2\2\2A\u0119\3\2\2\2C\u011b")
        buf.write("\3\2\2\2E\u011d\3\2\2\2G\u011f\3\2\2\2I\u0121\3\2\2\2")
        buf.write("K\u0123\3\2\2\2M\u0126\3\2\2\2O\u0145\3\2\2\2Q\u0147\3")
        buf.write("\2\2\2S\u014e\3\2\2\2U\u0155\3\2\2\2W\u0160\3\2\2\2Y\u0162")
        buf.write("\3\2\2\2[\u0164\3\2\2\2]\u0167\3\2\2\2_\u0171\3\2\2\2")
        buf.write("a\u0178\3\2\2\2c\u017a\3\2\2\2e\u0186\3\2\2\2gh\7\f\2")
        buf.write("\2hi\3\2\2\2ij\b\2\2\2j\4\3\2\2\2km\t\2\2\2lk\3\2\2\2")
        buf.write("mn\3\2\2\2nl\3\2\2\2no\3\2\2\2op\3\2\2\2pq\b\3\2\2q\6")
        buf.write("\3\2\2\2rs\7^\2\2sy\7^\2\2tu\7^\2\2uy\7,\2\2vw\7,\2\2")
        buf.write("wy\7^\2\2xr\3\2\2\2xt\3\2\2\2xv\3\2\2\2y\b\3\2\2\2z{\7")
        buf.write("k\2\2{|\7h\2\2|\n\3\2\2\2}~\7g\2\2~\177\7n\2\2\177\u0080")
        buf.write("\7u\2\2\u0080\u0081\7g\2\2\u0081\f\3\2\2\2\u0082\u0083")
        buf.write("\7h\2\2\u0083\u0084\7q\2\2\u0084\u0085\7t\2\2\u0085\16")
        buf.write("\3\2\2\2\u0086\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088\u0089")
        buf.write("\7v\2\2\u0089\u008a\7w\2\2\u008a\u008b\7t\2\2\u008b\u008c")
        buf.write("\7p\2\2\u008c\20\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f")
        buf.write("\7w\2\2\u008f\u0090\7p\2\2\u0090\u0091\7e\2\2\u0091\22")
        buf.write("\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094\7{\2\2\u0094\u0095")
        buf.write("\7r\2\2\u0095\u0096\7g\2\2\u0096\24\3\2\2\2\u0097\u0098")
        buf.write("\7u\2\2\u0098\u0099\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7e\2\2\u009c\u009d\7v\2\2\u009d\26")
        buf.write("\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7h\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\30\3\2\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7i\2\2\u00ae\32\3\2\2\2\u00af\u00b0")
        buf.write("\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\34")
        buf.write("\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\36")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7p\2\2\u00c0 \3\2\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7u\2\2\u00c5\u00c6\7v\2\2\u00c6\"\3\2\2\2\u00c7\u00c8")
        buf.write("\7x\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7t\2\2\u00ca$\3")
        buf.write("\2\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7g\2\2\u00d3&\3")
        buf.write("\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7m\2\2\u00d9(\3")
        buf.write("\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7i\2\2\u00de\u00df\7g\2\2\u00df*\3")
        buf.write("\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3,\3\2\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7g\2\2\u00e8.\3")
        buf.write("\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7g\2\2\u00ee\60")
        buf.write("\3\2\2\2\u00ef\u00f0\t\3\2\2\u00f0\62\3\2\2\2\u00f1\u00f2")
        buf.write("\7?\2\2\u00f2\u00fc\7?\2\2\u00f3\u00f4\7#\2\2\u00f4\u00fc")
        buf.write("\7?\2\2\u00f5\u00fc\7>\2\2\u00f6\u00f7\7>\2\2\u00f7\u00fc")
        buf.write("\7?\2\2\u00f8\u00fc\7@\2\2\u00f9\u00fa\7@\2\2\u00fa\u00fc")
        buf.write("\7?\2\2\u00fb\u00f1\3\2\2\2\u00fb\u00f3\3\2\2\2\u00fb")
        buf.write("\u00f5\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb\u00f8\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7(\2")
        buf.write("\2\u00fe\u0103\7(\2\2\u00ff\u0100\7~\2\2\u0100\u0103\7")
        buf.write("~\2\2\u0101\u0103\7#\2\2\u0102\u00fd\3\2\2\2\u0102\u00ff")
        buf.write("\3\2\2\2\u0102\u0101\3\2\2\2\u0103\66\3\2\2\2\u0104\u0110")
        buf.write("\7?\2\2\u0105\u0106\7-\2\2\u0106\u0110\7?\2\2\u0107\u0108")
        buf.write("\7/\2\2\u0108\u0110\7?\2\2\u0109\u010a\7,\2\2\u010a\u0110")
        buf.write("\7?\2\2\u010b\u010c\7\61\2\2\u010c\u0110\7?\2\2\u010d")
        buf.write("\u010e\7\'\2\2\u010e\u0110\7?\2\2\u010f\u0104\3\2\2\2")
        buf.write("\u010f\u0105\3\2\2\2\u010f\u0107\3\2\2\2\u010f\u0109\3")
        buf.write("\2\2\2\u010f\u010b\3\2\2\2\u010f\u010d\3\2\2\2\u01108")
        buf.write("\3\2\2\2\u0111\u0112\7\60\2\2\u0112:\3\2\2\2\u0113\u0114")
        buf.write("\7*\2\2\u0114<\3\2\2\2\u0115\u0116\7+\2\2\u0116>\3\2\2")
        buf.write("\2\u0117\u0118\7]\2\2\u0118@\3\2\2\2\u0119\u011a\7_\2")
        buf.write("\2\u011aB\3\2\2\2\u011b\u011c\7}\2\2\u011cD\3\2\2\2\u011d")
        buf.write("\u011e\7\177\2\2\u011eF\3\2\2\2\u011f\u0120\7.\2\2\u0120")
        buf.write("H\3\2\2\2\u0121\u0122\7=\2\2\u0122J\3\2\2\2\u0123\u0124")
        buf.write("\t\4\2\2\u0124L\3\2\2\2\u0125\u0127\5K&\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0130\7\60\2")
        buf.write("\2\u012b\u012d\5K&\2\u012c\u012b\3\2\2\2\u012d\u012e\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131")
        buf.write("\3\2\2\2\u0130\u012c\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u013b\3\2\2\2\u0132\u0134\t\5\2\2\u0133\u0135\t\6\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3")
        buf.write("\2\2\2\u0136\u0138\5K&\2\u0137\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013c\3\2\2\2\u013b\u0132\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013cN\3\2\2\2\u013d\u0146\7\62\2\2\u013e\u0142\t\7\2")
        buf.write("\2\u013f\u0141\t\4\2\2\u0140\u013f\3\2\2\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u013d\3\2\2\2")
        buf.write("\u0145\u013e\3\2\2\2\u0146P\3\2\2\2\u0147\u0148\7\62\2")
        buf.write("\2\u0148\u014a\t\b\2\2\u0149\u014b\t\t\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014dR\3\2\2\2\u014e\u014f\7\62\2\2\u014f")
        buf.write("\u0151\t\n\2\2\u0150\u0152\t\13\2\2\u0151\u0150\3\2\2")
        buf.write("\2\u0152\u0153\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154T\3\2\2\2\u0155\u0156\7\62\2\2\u0156\u0158")
        buf.write("\t\f\2\2\u0157\u0159\t\r\2\2\u0158\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015bV\3\2\2\2\u015c\u0161\5O(\2\u015d\u0161\5Q)\2\u015e")
        buf.write("\u0161\5S*\2\u015f\u0161\5U+\2\u0160\u015c\3\2\2\2\u0160")
        buf.write("\u015d\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161X\3\2\2\2\u0162\u0163\n\16\2\2\u0163Z\3\2\2\2\u0164")
        buf.write("\u0165\7^\2\2\u0165\u0166\t\17\2\2\u0166\\\3\2\2\2\u0167")
        buf.write("\u016c\7$\2\2\u0168\u016b\5Y-\2\u0169\u016b\5[.\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3")
        buf.write("\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\7$\2\2\u0170^\3")
        buf.write("\2\2\2\u0171\u0175\t\20\2\2\u0172\u0174\t\21\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176`\3\2\2\2\u0177\u0175\3\2\2")
        buf.write("\2\u0178\u0179\13\2\2\2\u0179b\3\2\2\2\u017a\u017f\7$")
        buf.write("\2\2\u017b\u017e\5Y-\2\u017c\u017e\5[.\2\u017d\u017b\3")
        buf.write("\2\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0183\7^\2\2\u0183\u0184\n\17\2\2")
        buf.write("\u0184\u0185\b\62\3\2\u0185d\3\2\2\2\u0186\u018b\7$\2")
        buf.write("\2\u0187\u018a\5Y-\2\u0188\u018a\5[.\2\u0189\u0187\3\2")
        buf.write("\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\b\63\4\2\u018ff\3\2\2\2\33")
        buf.write("\2nx\u00fb\u0102\u010f\u0128\u012e\u0130\u0134\u0139\u013b")
        buf.write("\u0142\u0145\u014c\u0153\u015a\u0160\u016a\u016c\u0175")
        buf.write("\u017d\u017f\u0189\u018b\5\b\2\2\3\62\2\3\63\3")
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
    OP1 = 24
    OP2 = 25
    OP3 = 26
    OP4 = 27
    OP5 = 28
    LPAREN = 29
    RPAREN = 30
    LSB = 31
    RSB = 32
    LCB = 33
    RCB = 34
    COMMA = 35
    SEMICOLON = 36
    FLOAT = 37
    INTEGER = 38
    STRING = 39
    ID = 40
    ERROR_CHAR = 41
    ILLEGAL_ESCAPE = 42
    UNCLOSE_STRING = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'.'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "COMMENT", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
            "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
            "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
            "NIL_", "TRUE_", "FALSE_", "OP1", "OP2", "OP3", "OP4", "OP5", 
            "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
            "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "NL", "WS", "COMMENT", "IF_", "ELSE_", "FOR_", "RETURN_", 
                  "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", 
                  "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                  "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "OP1", 
                  "OP2", "OP3", "OP4", "OP5", "LPAREN", "RPAREN", "LSB", 
                  "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "Digit", "FLOAT", 
                  "DecInt", "BinInt", "OctInt", "HexInt", "INTEGER", "Char", 
                  "EscapeChar", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

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
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
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
     


