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
        buf.write("\u0214\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\7\2\u0080\n\2\f\2\16")
        buf.write("\2\u0083\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\u008c\n")
        buf.write("\3\f\3\16\3\u008f\13\3\3\3\3\3\3\3\3\3\3\3\3\4\5\4\u0097")
        buf.write("\n\4\3\4\3\4\3\4\3\5\6\5\u009d\n\5\r\5\16\5\u009e\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u014c\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0167\n\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\6\61\u01a1\n\61\r\61\16\61\u01a2\3\61\3\61\6\61\u01a7")
        buf.write("\n\61\r\61\16\61\u01a8\5\61\u01ab\n\61\3\61\3\61\5\61")
        buf.write("\u01af\n\61\3\61\6\61\u01b2\n\61\r\61\16\61\u01b3\5\61")
        buf.write("\u01b6\n\61\3\61\3\61\3\62\3\62\3\62\7\62\u01bd\n\62\f")
        buf.write("\62\16\62\u01c0\13\62\5\62\u01c2\n\62\3\63\3\63\3\63\6")
        buf.write("\63\u01c7\n\63\r\63\16\63\u01c8\3\64\3\64\3\64\6\64\u01ce")
        buf.write("\n\64\r\64\16\64\u01cf\3\65\3\65\3\65\6\65\u01d5\n\65")
        buf.write("\r\65\16\65\u01d6\3\66\3\66\3\66\3\66\5\66\u01dd\n\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\38\39\39\39\79\u01e9\n9\f9")
        buf.write("\169\u01ec\139\39\39\39\3:\3:\7:\u01f3\n:\f:\16:\u01f6")
        buf.write("\13:\3:\3:\3;\3;\3;\3<\3<\3<\7<\u0200\n<\f<\16<\u0203")
        buf.write("\13<\3<\3<\3<\3<\3<\3=\3=\3=\7=\u020d\n=\f=\16=\u0210")
        buf.write("\13=\3=\3=\3=\3\u008d\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\61c\2e")
        buf.write("\2g\2i\2k\62m\2o\2q\63s\64u\65w\66y\67\3\2\22\3\2\f\f")
        buf.write("\5\2\13\13\17\17\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4")
        buf.write("\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4")
        buf.write("\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u022f")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2a\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{\3\2\2\2\5\u0086\3\2\2")
        buf.write("\2\7\u0096\3\2\2\2\t\u009c\3\2\2\2\13\u00a2\3\2\2\2\r")
        buf.write("\u00a7\3\2\2\2\17\u00ae\3\2\2\2\21\u00b4\3\2\2\2\23\u00bd")
        buf.write("\3\2\2\2\25\u00c4\3\2\2\2\27\u00cb\3\2\2\2\31\u00d4\3")
        buf.write("\2\2\2\33\u00e0\3\2\2\2\35\u00e9\3\2\2\2\37\u00ef\3\2")
        buf.write("\2\2!\u00f7\3\2\2\2#\u0101\3\2\2\2%\u0109\3\2\2\2\'\u010f")
        buf.write("\3\2\2\2)\u011a\3\2\2\2+\u0122\3\2\2\2-\u012a\3\2\2\2")
        buf.write("/\u0130\3\2\2\2\61\u0137\3\2\2\2\63\u014b\3\2\2\2\65\u014d")
        buf.write("\3\2\2\2\67\u0152\3\2\2\29\u0157\3\2\2\2;\u0166\3\2\2")
        buf.write("\2=\u0168\3\2\2\2?\u016d\3\2\2\2A\u0170\3\2\2\2C\u0173")
        buf.write("\3\2\2\2E\u0176\3\2\2\2G\u0179\3\2\2\2I\u017c\3\2\2\2")
        buf.write("K\u017f\3\2\2\2M\u0182\3\2\2\2O\u0185\3\2\2\2Q\u0188\3")
        buf.write("\2\2\2S\u018b\3\2\2\2U\u018e\3\2\2\2W\u0191\3\2\2\2Y\u0194")
        buf.write("\3\2\2\2[\u0197\3\2\2\2]\u019a\3\2\2\2_\u019d\3\2\2\2")
        buf.write("a\u01a0\3\2\2\2c\u01c1\3\2\2\2e\u01c3\3\2\2\2g\u01ca\3")
        buf.write("\2\2\2i\u01d1\3\2\2\2k\u01dc\3\2\2\2m\u01e0\3\2\2\2o\u01e2")
        buf.write("\3\2\2\2q\u01e5\3\2\2\2s\u01f0\3\2\2\2u\u01f9\3\2\2\2")
        buf.write("w\u01fc\3\2\2\2y\u0209\3\2\2\2{|\7\61\2\2|}\7\61\2\2}")
        buf.write("\u0081\3\2\2\2~\u0080\n\2\2\2\177~\3\2\2\2\u0080\u0083")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\b\2\2\2\u0085")
        buf.write("\4\3\2\2\2\u0086\u0087\7\61\2\2\u0087\u0088\7,\2\2\u0088")
        buf.write("\u008d\3\2\2\2\u0089\u008c\5\5\3\2\u008a\u008c\13\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7,\2\2")
        buf.write("\u0091\u0092\7\61\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write("\b\3\2\2\u0094\6\3\2\2\2\u0095\u0097\7\17\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\7\f\2\2\u0099\u009a\b\4\3\2\u009a\b\3\2\2\2\u009b")
        buf.write("\u009d\t\3\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a1\b\5\2\2\u00a1\n\3\2\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\b\6\4\2\u00a6\f\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7n\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ad\b\7\5\2\u00ad\16\3\2\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\b\b\6\2\u00b3\20\3\2\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7w\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\b\t\7\2\u00bc\22\3\2\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7e\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\n\b\2\u00c3")
        buf.write("\24\3\2\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7{\2\2\u00c6")
        buf.write("\u00c7\7r\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00ca\b\13\t\2\u00ca\26\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7w\2\2\u00cf")
        buf.write("\u00d0\7e\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\b\f\n\2\u00d3\30\3\2\2\2\u00d4\u00d5\7k\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7g\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7e\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00df\b\r\13\2\u00df\32\3\2\2\2\u00e0\u00e1\7u\2\2\u00e1")
        buf.write("\u00e2\7v\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7k\2\2\u00e4")
        buf.write("\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e8\b\16\f\2\u00e8\34\3\2\2\2\u00e9\u00ea\7k\2\2\u00ea")
        buf.write("\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00ee\b\17\r\2\u00ee\36\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0")
        buf.write("\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\b\20\16")
        buf.write("\2\u00f6 \3\2\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7q\2")
        buf.write("\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7")
        buf.write("g\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\b\21\17\2\u0100\"\3\2\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7u\2\2\u0105\u0106\7v\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write("\b\22\20\2\u0108$\3\2\2\2\u0109\u010a\7x\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7t\2\2\u010c\u010d\3\2\2\2\u010d\u010e")
        buf.write("\b\23\21\2\u010e&\3\2\2\2\u010f\u0110\7e\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7p\2\2\u0112\u0113\7v\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116\7w\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\3\2\2\2\u0118\u0119\b\24\22\2\u0119")
        buf.write("(\3\2\2\2\u011a\u011b\7d\2\2\u011b\u011c\7t\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d\u011e\7c\2\2\u011e\u011f\7m\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\b\25\23\2\u0121*\3\2\2\2\u0122")
        buf.write("\u0123\7t\2\2\u0123\u0124\7c\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\u0126\7i\2\2\u0126\u0127\7g\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u0129\b\26\24\2\u0129,\3\2\2\2\u012a\u012b\7p\2\2\u012b")
        buf.write("\u012c\7k\2\2\u012c\u012d\7n\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012f\b\27\25\2\u012f.\3\2\2\2\u0130\u0131\7v\2\2\u0131")
        buf.write("\u0132\7t\2\2\u0132\u0133\7w\2\2\u0133\u0134\7g\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\b\30\26\2\u0136\60\3\2\2\2")
        buf.write("\u0137\u0138\7h\2\2\u0138\u0139\7c\2\2\u0139\u013a\7n")
        buf.write("\2\2\u013a\u013b\7u\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013e\b\31\27\2\u013e\62\3\2\2\2\u013f")
        buf.write("\u0140\7?\2\2\u0140\u014c\7?\2\2\u0141\u0142\7#\2\2\u0142")
        buf.write("\u014c\7?\2\2\u0143\u014c\7>\2\2\u0144\u0145\7>\2\2\u0145")
        buf.write("\u014c\7?\2\2\u0146\u014c\7@\2\2\u0147\u0148\7@\2\2\u0148")
        buf.write("\u0149\7?\2\2\u0149\u014a\3\2\2\2\u014a\u014c\b\32\30")
        buf.write("\2\u014b\u013f\3\2\2\2\u014b\u0141\3\2\2\2\u014b\u0143")
        buf.write("\3\2\2\2\u014b\u0144\3\2\2\2\u014b\u0146\3\2\2\2\u014b")
        buf.write("\u0147\3\2\2\2\u014c\64\3\2\2\2\u014d\u014e\7(\2\2\u014e")
        buf.write("\u014f\7(\2\2\u014f\u0150\3\2\2\2\u0150\u0151\b\33\31")
        buf.write("\2\u0151\66\3\2\2\2\u0152\u0153\7~\2\2\u0153\u0154\7~")
        buf.write("\2\2\u0154\u0155\3\2\2\2\u0155\u0156\b\34\32\2\u01568")
        buf.write("\3\2\2\2\u0157\u0158\7#\2\2\u0158\u0159\b\35\33\2\u0159")
        buf.write(":\3\2\2\2\u015a\u015b\7-\2\2\u015b\u0167\7?\2\2\u015c")
        buf.write("\u015d\7/\2\2\u015d\u0167\7?\2\2\u015e\u015f\7,\2\2\u015f")
        buf.write("\u0167\7?\2\2\u0160\u0161\7\61\2\2\u0161\u0167\7?\2\2")
        buf.write("\u0162\u0163\7\'\2\2\u0163\u0164\7?\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0167\b\36\34\2\u0166\u015a\3\2\2\2\u0166")
        buf.write("\u015c\3\2\2\2\u0166\u015e\3\2\2\2\u0166\u0160\3\2\2\2")
        buf.write("\u0166\u0162\3\2\2\2\u0167<\3\2\2\2\u0168\u0169\7<\2\2")
        buf.write("\u0169\u016a\7?\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b")
        buf.write("\37\35\2\u016c>\3\2\2\2\u016d\u016e\7\60\2\2\u016e\u016f")
        buf.write("\b \36\2\u016f@\3\2\2\2\u0170\u0171\7?\2\2\u0171\u0172")
        buf.write("\b!\37\2\u0172B\3\2\2\2\u0173\u0174\7-\2\2\u0174\u0175")
        buf.write("\b\" \2\u0175D\3\2\2\2\u0176\u0177\7/\2\2\u0177\u0178")
        buf.write("\b#!\2\u0178F\3\2\2\2\u0179\u017a\7,\2\2\u017a\u017b\b")
        buf.write("$\"\2\u017bH\3\2\2\2\u017c\u017d\7\61\2\2\u017d\u017e")
        buf.write("\b%#\2\u017eJ\3\2\2\2\u017f\u0180\7\'\2\2\u0180\u0181")
        buf.write("\b&$\2\u0181L\3\2\2\2\u0182\u0183\7*\2\2\u0183\u0184\b")
        buf.write("\'%\2\u0184N\3\2\2\2\u0185\u0186\7+\2\2\u0186\u0187\b")
        buf.write("(&\2\u0187P\3\2\2\2\u0188\u0189\7]\2\2\u0189\u018a\b)")
        buf.write("\'\2\u018aR\3\2\2\2\u018b\u018c\7_\2\2\u018c\u018d\b*")
        buf.write("(\2\u018dT\3\2\2\2\u018e\u018f\7}\2\2\u018f\u0190\b+)")
        buf.write("\2\u0190V\3\2\2\2\u0191\u0192\7\177\2\2\u0192\u0193\b")
        buf.write(",*\2\u0193X\3\2\2\2\u0194\u0195\7.\2\2\u0195\u0196\b-")
        buf.write("+\2\u0196Z\3\2\2\2\u0197\u0198\7=\2\2\u0198\u0199\b.,")
        buf.write("\2\u0199\\\3\2\2\2\u019a\u019b\7<\2\2\u019b\u019c\b/-")
        buf.write("\2\u019c^\3\2\2\2\u019d\u019e\t\4\2\2\u019e`\3\2\2\2\u019f")
        buf.write("\u01a1\5_\60\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01aa\7\60\2\2\u01a5\u01a7\5_\60\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a6\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01b5\3\2\2\2\u01ac\u01ae")
        buf.write("\t\5\2\2\u01ad\u01af\t\6\2\2\u01ae\u01ad\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2\5_\60\2")
        buf.write("\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01ac")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7")
        buf.write("\u01b8\b\61.\2\u01b8b\3\2\2\2\u01b9\u01c2\7\62\2\2\u01ba")
        buf.write("\u01be\t\7\2\2\u01bb\u01bd\t\4\2\2\u01bc\u01bb\3\2\2\2")
        buf.write("\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01b9")
        buf.write("\3\2\2\2\u01c1\u01ba\3\2\2\2\u01c2d\3\2\2\2\u01c3\u01c4")
        buf.write("\7\62\2\2\u01c4\u01c6\t\b\2\2\u01c5\u01c7\t\t\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9f\3\2\2\2\u01ca\u01cb\7\62\2")
        buf.write("\2\u01cb\u01cd\t\n\2\2\u01cc\u01ce\t\13\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0h\3\2\2\2\u01d1\u01d2\7\62\2\2\u01d2")
        buf.write("\u01d4\t\f\2\2\u01d3\u01d5\t\r\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3")
        buf.write("\2\2\2\u01d7j\3\2\2\2\u01d8\u01dd\5c\62\2\u01d9\u01dd")
        buf.write("\5e\63\2\u01da\u01dd\5g\64\2\u01db\u01dd\5i\65\2\u01dc")
        buf.write("\u01d8\3\2\2\2\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\b")
        buf.write("\66/\2\u01dfl\3\2\2\2\u01e0\u01e1\n\16\2\2\u01e1n\3\2")
        buf.write("\2\2\u01e2\u01e3\7^\2\2\u01e3\u01e4\t\17\2\2\u01e4p\3")
        buf.write("\2\2\2\u01e5\u01ea\7$\2\2\u01e6\u01e9\5m\67\2\u01e7\u01e9")
        buf.write("\5o8\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u01ed\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7$\2\2")
        buf.write("\u01ee\u01ef\b9\60\2\u01efr\3\2\2\2\u01f0\u01f4\t\20\2")
        buf.write("\2\u01f1\u01f3\t\21\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\b:\61\2")
        buf.write("\u01f8t\3\2\2\2\u01f9\u01fa\13\2\2\2\u01fa\u01fb\b;\62")
        buf.write("\2\u01fbv\3\2\2\2\u01fc\u0201\7$\2\2\u01fd\u0200\5m\67")
        buf.write("\2\u01fe\u0200\5o8\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3")
        buf.write("\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0204")
        buf.write("\u0205\7^\2\2\u0205\u0206\n\17\2\2\u0206\u0207\b<\63\2")
        buf.write("\u0207\u0208\b<\64\2\u0208x\3\2\2\2\u0209\u020e\7$\2\2")
        buf.write("\u020a\u020d\5m\67\2\u020b\u020d\5o8\2\u020c\u020a\3\2")
        buf.write("\2\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0211\u0212\b=\65\2\u0212\u0213\b=\66\2")
        buf.write("\u0213z\3\2\2\2\35\2\u0081\u008b\u008d\u0096\u009e\u014b")
        buf.write("\u0166\u01a2\u01a8\u01aa\u01ae\u01b3\u01b5\u01be\u01c1")
        buf.write("\u01c8\u01cf\u01d6\u01dc\u01e8\u01ea\u01f4\u01ff\u0201")
        buf.write("\u020c\u020e\67\b\2\2\3\4\2\3\6\3\3\7\4\3\b\5\3\t\6\3")
        buf.write("\n\7\3\13\b\3\f\t\3\r\n\3\16\13\3\17\f\3\20\r\3\21\16")
        buf.write("\3\22\17\3\23\20\3\24\21\3\25\22\3\26\23\3\27\24\3\30")
        buf.write("\25\3\31\26\3\32\27\3\33\30\3\34\31\3\35\32\3\36\33\3")
        buf.write("\37\34\3 \35\3!\36\3\"\37\3# \3$!\3%\"\3&#\3\'$\3(%\3")
        buf.write(")&\3*\'\3+(\3,)\3-*\3.+\3/,\3\61-\3\66.\39/\3:\60\3;\61")
        buf.write("\3<\62\3<\63\3=\64\3=\65")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_LINE_CMT = 1
    MULTI_LINE_CMT = 2
    NL = 3
    WS = 4
    IF_ = 5
    ELSE_ = 6
    FOR_ = 7
    RETURN_ = 8
    FUNC_ = 9
    TYPE_ = 10
    STRUCT_ = 11
    INTERFACE_ = 12
    STRING_ = 13
    INT_ = 14
    FLOAT_ = 15
    BOOLEAN_ = 16
    CONST_ = 17
    VAR_ = 18
    CONTINUE_ = 19
    BREAK_ = 20
    RANGE_ = 21
    NIL_ = 22
    TRUE_ = 23
    FALSE_ = 24
    COMPARISON_OP = 25
    AND = 26
    OR = 27
    NOT = 28
    UPT_ASSIGN = 29
    ASSIGN = 30
    DOT = 31
    EQUAL = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    LCB = 42
    RCB = 43
    COMMA = 44
    SEMICOLON = 45
    COLON = 46
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
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'&&'", "'||'", "'!'", "':='", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "AND", "OR", "NOT", "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", "FLOAT", "INTEGER", 
            "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", 
                  "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                  "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                  "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", 
                  "TRUE_", "FALSE_", "COMPARISON_OP", "AND", "OR", "NOT", 
                  "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "LP", "RP", "LSB", "RSB", "LCB", 
                  "RCB", "COMMA", "SEMICOLON", "COLON", "Digit", "FLOAT", 
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


    lastTokenType = None

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
            actions[2] = self.NL_action 
            actions[4] = self.IF__action 
            actions[5] = self.ELSE__action 
            actions[6] = self.FOR__action 
            actions[7] = self.RETURN__action 
            actions[8] = self.FUNC__action 
            actions[9] = self.TYPE__action 
            actions[10] = self.STRUCT__action 
            actions[11] = self.INTERFACE__action 
            actions[12] = self.STRING__action 
            actions[13] = self.INT__action 
            actions[14] = self.FLOAT__action 
            actions[15] = self.BOOLEAN__action 
            actions[16] = self.CONST__action 
            actions[17] = self.VAR__action 
            actions[18] = self.CONTINUE__action 
            actions[19] = self.BREAK__action 
            actions[20] = self.RANGE__action 
            actions[21] = self.NIL__action 
            actions[22] = self.TRUE__action 
            actions[23] = self.FALSE__action 
            actions[24] = self.COMPARISON_OP_action 
            actions[25] = self.AND_action 
            actions[26] = self.OR_action 
            actions[27] = self.NOT_action 
            actions[28] = self.UPT_ASSIGN_action 
            actions[29] = self.ASSIGN_action 
            actions[30] = self.DOT_action 
            actions[31] = self.EQUAL_action 
            actions[32] = self.ADD_action 
            actions[33] = self.SUB_action 
            actions[34] = self.MUL_action 
            actions[35] = self.DIV_action 
            actions[36] = self.MOD_action 
            actions[37] = self.LP_action 
            actions[38] = self.RP_action 
            actions[39] = self.LSB_action 
            actions[40] = self.RSB_action 
            actions[41] = self.LCB_action 
            actions[42] = self.RCB_action 
            actions[43] = self.COMMA_action 
            actions[44] = self.SEMICOLON_action 
            actions[45] = self.COLON_action 
            actions[47] = self.FLOAT_action 
            actions[52] = self.INTEGER_action 
            actions[55] = self.STRING_action 
            actions[56] = self.ID_action 
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RP', 'RSB', 'RCB']:
                self.text = ';'
                self.type = self.SEMICOLON
                self.lastTokenType = 'SEMICOLON'
            else:
                self.skip()

     

    def IF__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.lastTokenType = 'IF_'
     

    def ELSE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.lastTokenType = 'ELSE_'
     

    def FOR__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.lastTokenType = 'FOR_'
     

    def RETURN__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.lastTokenType = 'RETURN_'
     

    def FUNC__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.lastTokenType = 'FUNC_'
     

    def TYPE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.lastTokenType = 'TYPE_'
     

    def STRUCT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.lastTokenType = 'STRUCT_'
     

    def INTERFACE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            self.lastTokenType = 'INTERFACE_'
     

    def STRING__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            self.lastTokenType = 'STRING_'
     

    def INT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
            self.lastTokenType = 'INT_'
     

    def FLOAT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
            self.lastTokenType = 'FLOAT_'
     

    def BOOLEAN__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:
            self.lastTokenType = 'BOOLEAN_'
     

    def CONST__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 13:
            self.lastTokenType = 'CONST_'
     

    def VAR__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 14:
            self.lastTokenType = 'VAR_'
     

    def CONTINUE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 15:
            self.lastTokenType = 'CONTINUE_'
     

    def BREAK__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 16:
            self.lastTokenType = 'BREAK_'
     

    def RANGE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 17:
            self.lastTokenType = 'RANGE_'
     

    def NIL__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 18:
            self.lastTokenType = 'NIL_'
     

    def TRUE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 19:
            self.lastTokenType = 'TRUE_'
     

    def FALSE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 20:
            self.lastTokenType = 'FALSE_'
     

    def COMPARISON_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 21:
            self.lastTypeToken = 'COMPARISON_OP'
     

    def AND_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTypeToken = 'AND'
     

    def OR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTypeToken = 'OR'
     

    def NOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTypeToken = 'NOT'
     

    def UPT_ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'UPT_ASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'DOT'
     

    def EQUAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'EQUAL'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'MOD'
     

    def LP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'LP'
     

    def RP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'RP'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'SEMICOLON'
     

    def COLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'COLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 46:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 48:
            self.text = self.text[1:]
     

        if actionIndex == 49:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 50:
            self.text = self.text.replace('\r','\n').split('\n')[0][1:]
     

        if actionIndex == 51:
            self.lastTokenType = 'UNCLOSE_STRING'
     


