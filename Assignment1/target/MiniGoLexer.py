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
        buf.write("\u01c8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\7\5\u0086\n\5\f\5\16\5\u0089\13\5\3\5\5\5\u008c")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6\u0095\n\6\f\6\16")
        buf.write("\6\u0098\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b\u00a2")
        buf.write("\n\b\r\b\16\b\u00a3\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0127\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\5\36\u012e\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u013c\n\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\6\60\u015f\n\60\r\60\16\60\u0160\3\60\3\60\6")
        buf.write("\60\u0165\n\60\r\60\16\60\u0166\5\60\u0169\n\60\3\60\3")
        buf.write("\60\5\60\u016d\n\60\3\60\6\60\u0170\n\60\r\60\16\60\u0171")
        buf.write("\5\60\u0174\n\60\3\61\3\61\3\61\7\61\u0179\n\61\f\61\16")
        buf.write("\61\u017c\13\61\5\61\u017e\n\61\3\62\3\62\3\62\6\62\u0183")
        buf.write("\n\62\r\62\16\62\u0184\3\63\3\63\3\63\6\63\u018a\n\63")
        buf.write("\r\63\16\63\u018b\3\64\3\64\3\64\6\64\u0191\n\64\r\64")
        buf.write("\16\64\u0192\3\65\3\65\3\65\3\65\5\65\u0199\n\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\78\u01a3\n8\f8\168\u01a6")
        buf.write("\138\38\38\39\39\79\u01ac\n9\f9\169\u01af\139\3:\3:\3")
        buf.write(";\3;\3;\7;\u01b6\n;\f;\16;\u01b9\13;\3;\3;\3;\3;\3<\3")
        buf.write("<\3<\7<\u01c2\n<\f<\16<\u01c5\13<\3<\3<\3\u0096\2=\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\60a\2c\2e\2g\2i\61k\2m\2o\62q\63s\64u\65")
        buf.write("w\66\3\2\23\3\2\f\f\3\3\f\f\5\2\13\13\17\17\"\"\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3")
        buf.write("\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$^^ppttvv\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\2\u01e5\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2_\3\2\2\2\2i\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2")
        buf.write("\2\2\5|\3\2\2\2\7\177\3\2\2\2\t\u0081\3\2\2\2\13\u008f")
        buf.write("\3\2\2\2\r\u009e\3\2\2\2\17\u00a1\3\2\2\2\21\u00a7\3\2")
        buf.write("\2\2\23\u00aa\3\2\2\2\25\u00af\3\2\2\2\27\u00b3\3\2\2")
        buf.write("\2\31\u00ba\3\2\2\2\33\u00bf\3\2\2\2\35\u00c4\3\2\2\2")
        buf.write("\37\u00cb\3\2\2\2!\u00d5\3\2\2\2#\u00dc\3\2\2\2%\u00e0")
        buf.write("\3\2\2\2\'\u00e6\3\2\2\2)\u00ee\3\2\2\2+\u00f4\3\2\2\2")
        buf.write("-\u00f8\3\2\2\2/\u0101\3\2\2\2\61\u0107\3\2\2\2\63\u010d")
        buf.write("\3\2\2\2\65\u0111\3\2\2\2\67\u0116\3\2\2\29\u0126\3\2")
        buf.write("\2\2;\u012d\3\2\2\2=\u013b\3\2\2\2?\u013d\3\2\2\2A\u013f")
        buf.write("\3\2\2\2C\u0141\3\2\2\2E\u0143\3\2\2\2G\u0145\3\2\2\2")
        buf.write("I\u0147\3\2\2\2K\u0149\3\2\2\2M\u014b\3\2\2\2O\u014d\3")
        buf.write("\2\2\2Q\u014f\3\2\2\2S\u0151\3\2\2\2U\u0153\3\2\2\2W\u0155")
        buf.write("\3\2\2\2Y\u0157\3\2\2\2[\u0159\3\2\2\2]\u015b\3\2\2\2")
        buf.write("_\u015e\3\2\2\2a\u017d\3\2\2\2c\u017f\3\2\2\2e\u0186\3")
        buf.write("\2\2\2g\u018d\3\2\2\2i\u0198\3\2\2\2k\u019a\3\2\2\2m\u019c")
        buf.write("\3\2\2\2o\u019f\3\2\2\2q\u01a9\3\2\2\2s\u01b0\3\2\2\2")
        buf.write("u\u01b2\3\2\2\2w\u01be\3\2\2\2yz\7~\2\2z{\7~\2\2{\4\3")
        buf.write("\2\2\2|}\7(\2\2}~\7(\2\2~\6\3\2\2\2\177\u0080\7#\2\2\u0080")
        buf.write("\b\3\2\2\2\u0081\u0082\7\61\2\2\u0082\u0083\7\61\2\2\u0083")
        buf.write("\u0087\3\2\2\2\u0084\u0086\n\2\2\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c")
        buf.write("\t\3\2\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\b\5\2\2\u008e\n\3\2\2\2\u008f\u0090\7\61\2\2\u0090")
        buf.write("\u0091\7,\2\2\u0091\u0096\3\2\2\2\u0092\u0095\5\13\6\2")
        buf.write("\u0093\u0095\13\2\2\2\u0094\u0092\3\2\2\2\u0094\u0093")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0097\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0099\u009a\7,\2\2\u009a\u009b\7\61\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009d\b\6\2\2\u009d\f\3\2\2\2\u009e\u009f")
        buf.write("\7\f\2\2\u009f\16\3\2\2\2\u00a0\u00a2\t\4\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\b\2\2")
        buf.write("\u00a6\20\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7h\2")
        buf.write("\2\u00a9\22\3\2\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7n")
        buf.write("\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7g\2\2\u00ae\24\3")
        buf.write("\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7t\2\2\u00b2\26\3\2\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7p\2\2\u00b9\30\3\2\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7e\2\2\u00be\32\3\2\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7{\2\2\u00c1\u00c2\7r\2\2\u00c2\u00c3\7g\2\2\u00c3\34")
        buf.write("\3\2\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\36\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7e\2\2\u00d3\u00d4\7g\2\2\u00d4 \3\2\2\2\u00d5\u00d6")
        buf.write("\7u\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7i\2\2\u00db\"")
        buf.write("\3\2\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df$\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5&\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed(\3")
        buf.write("\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7v\2\2\u00f3*\3")
        buf.write("\2\2\2\u00f4\u00f5\7x\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100.\3\2\2\2\u0101\u0102\7d\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7m\2\2\u0106\60\3\2\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7p\2\2\u010a\u010b\7i\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\62\3\2\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7k\2\2\u010f\u0110\7n\2\2\u0110\64\3\2\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7t\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115\66\3\2\2\2\u0116\u0117\7h\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b8\3\2\2\2\u011c\u011d\7?\2\2\u011d\u0127")
        buf.write("\7?\2\2\u011e\u011f\7#\2\2\u011f\u0127\7?\2\2\u0120\u0127")
        buf.write("\7>\2\2\u0121\u0122\7>\2\2\u0122\u0127\7?\2\2\u0123\u0127")
        buf.write("\7@\2\2\u0124\u0125\7@\2\2\u0125\u0127\7?\2\2\u0126\u011c")
        buf.write("\3\2\2\2\u0126\u011e\3\2\2\2\u0126\u0120\3\2\2\2\u0126")
        buf.write("\u0121\3\2\2\2\u0126\u0123\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0127:\3\2\2\2\u0128\u0129\7(\2\2\u0129\u012e\7(\2\2")
        buf.write("\u012a\u012b\7~\2\2\u012b\u012e\7~\2\2\u012c\u012e\7#")
        buf.write("\2\2\u012d\u0128\3\2\2\2\u012d\u012a\3\2\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e<\3\2\2\2\u012f\u0130\7<\2\2\u0130\u013c")
        buf.write("\7?\2\2\u0131\u0132\7-\2\2\u0132\u013c\7?\2\2\u0133\u0134")
        buf.write("\7/\2\2\u0134\u013c\7?\2\2\u0135\u0136\7,\2\2\u0136\u013c")
        buf.write("\7?\2\2\u0137\u0138\7\61\2\2\u0138\u013c\7?\2\2\u0139")
        buf.write("\u013a\7\'\2\2\u013a\u013c\7?\2\2\u013b\u012f\3\2\2\2")
        buf.write("\u013b\u0131\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0135\3")
        buf.write("\2\2\2\u013b\u0137\3\2\2\2\u013b\u0139\3\2\2\2\u013c>")
        buf.write("\3\2\2\2\u013d\u013e\7\60\2\2\u013e@\3\2\2\2\u013f\u0140")
        buf.write("\7?\2\2\u0140B\3\2\2\2\u0141\u0142\7-\2\2\u0142D\3\2\2")
        buf.write("\2\u0143\u0144\7/\2\2\u0144F\3\2\2\2\u0145\u0146\7,\2")
        buf.write("\2\u0146H\3\2\2\2\u0147\u0148\7\61\2\2\u0148J\3\2\2\2")
        buf.write("\u0149\u014a\7\'\2\2\u014aL\3\2\2\2\u014b\u014c\7*\2\2")
        buf.write("\u014cN\3\2\2\2\u014d\u014e\7+\2\2\u014eP\3\2\2\2\u014f")
        buf.write("\u0150\7]\2\2\u0150R\3\2\2\2\u0151\u0152\7_\2\2\u0152")
        buf.write("T\3\2\2\2\u0153\u0154\7}\2\2\u0154V\3\2\2\2\u0155\u0156")
        buf.write("\7\177\2\2\u0156X\3\2\2\2\u0157\u0158\7.\2\2\u0158Z\3")
        buf.write("\2\2\2\u0159\u015a\7=\2\2\u015a\\\3\2\2\2\u015b\u015c")
        buf.write("\t\5\2\2\u015c^\3\2\2\2\u015d\u015f\5]/\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0168\7\60\2")
        buf.write("\2\u0163\u0165\5]/\2\u0164\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0169")
        buf.write("\3\2\2\2\u0168\u0164\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u0173\3\2\2\2\u016a\u016c\t\6\2\2\u016b\u016d\t\7\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3")
        buf.write("\2\2\2\u016e\u0170\5]/\2\u016f\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0174\3\2\2\2\u0173\u016a\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174`\3\2\2\2\u0175\u017e\7\62\2\2\u0176\u017a\t\b\2")
        buf.write("\2\u0177\u0179\t\5\2\2\u0178\u0177\3\2\2\2\u0179\u017c")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u0175\3\2\2\2")
        buf.write("\u017d\u0176\3\2\2\2\u017eb\3\2\2\2\u017f\u0180\7\62\2")
        buf.write("\2\u0180\u0182\t\t\2\2\u0181\u0183\t\n\2\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185d\3\2\2\2\u0186\u0187\7\62\2\2\u0187")
        buf.write("\u0189\t\13\2\2\u0188\u018a\t\f\2\2\u0189\u0188\3\2\2")
        buf.write("\2\u018a\u018b\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018cf\3\2\2\2\u018d\u018e\7\62\2\2\u018e\u0190")
        buf.write("\t\r\2\2\u018f\u0191\t\16\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193h\3\2\2\2\u0194\u0199\5a\61\2\u0195\u0199\5c\62")
        buf.write("\2\u0196\u0199\5e\63\2\u0197\u0199\5g\64\2\u0198\u0194")
        buf.write("\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199j\3\2\2\2\u019a\u019b\n\17\2\2\u019b")
        buf.write("l\3\2\2\2\u019c\u019d\7^\2\2\u019d\u019e\t\20\2\2\u019e")
        buf.write("n\3\2\2\2\u019f\u01a4\7$\2\2\u01a0\u01a3\5k\66\2\u01a1")
        buf.write("\u01a3\5m\67\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3")
        buf.write("\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8")
        buf.write("\7$\2\2\u01a8p\3\2\2\2\u01a9\u01ad\t\21\2\2\u01aa\u01ac")
        buf.write("\t\22\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aer\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b1\13\2\2\2\u01b1t\3\2\2\2\u01b2")
        buf.write("\u01b7\7$\2\2\u01b3\u01b6\5k\66\2\u01b4\u01b6\5m\67\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3")
        buf.write("\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\7^\2\2\u01bb")
        buf.write("\u01bc\n\20\2\2\u01bc\u01bd\b;\3\2\u01bdv\3\2\2\2\u01be")
        buf.write("\u01c3\7$\2\2\u01bf\u01c2\5k\66\2\u01c0\u01c2\5m\67\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3")
        buf.write("\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\b<\4\2\u01c7")
        buf.write("x\3\2\2\2\36\2\u0087\u008b\u0094\u0096\u00a3\u0126\u012d")
        buf.write("\u013b\u0160\u0166\u0168\u016c\u0171\u0173\u017a\u017d")
        buf.write("\u0184\u018b\u0192\u0198\u01a2\u01a4\u01ad\u01b5\u01b7")
        buf.write("\u01c1\u01c3\5\b\2\2\3;\2\3<\3")
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
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
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
     


