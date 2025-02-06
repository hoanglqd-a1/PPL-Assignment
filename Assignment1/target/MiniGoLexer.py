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
        buf.write("\u01cc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7\u0098\n\7\f\7\16")
        buf.write("\7\u009b\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\6\t\u00a5")
        buf.write("\n\t\r\t\16\t\u00a6\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012a")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0131\n\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u013d\n \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\6\62")
        buf.write("\u0163\n\62\r\62\16\62\u0164\3\62\3\62\6\62\u0169\n\62")
        buf.write("\r\62\16\62\u016a\5\62\u016d\n\62\3\62\3\62\5\62\u0171")
        buf.write("\n\62\3\62\6\62\u0174\n\62\r\62\16\62\u0175\5\62\u0178")
        buf.write("\n\62\3\63\3\63\3\63\7\63\u017d\n\63\f\63\16\63\u0180")
        buf.write("\13\63\5\63\u0182\n\63\3\64\3\64\3\64\6\64\u0187\n\64")
        buf.write("\r\64\16\64\u0188\3\65\3\65\3\65\6\65\u018e\n\65\r\65")
        buf.write("\16\65\u018f\3\66\3\66\3\66\6\66\u0195\n\66\r\66\16\66")
        buf.write("\u0196\3\67\3\67\3\67\3\67\5\67\u019d\n\67\38\38\39\3")
        buf.write("9\39\3:\3:\3:\7:\u01a7\n:\f:\16:\u01aa\13:\3:\3:\3;\3")
        buf.write(";\7;\u01b0\n;\f;\16;\u01b3\13;\3<\3<\3=\3=\3=\7=\u01ba")
        buf.write("\n=\f=\16=\u01bd\13=\3=\3=\3=\3=\3>\3>\3>\7>\u01c6\n>")
        buf.write("\f>\16>\u01c9\13>\3>\3>\3\u0099\2?\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\2c\62e\2g\2i\2k\2m\63o\2q\2s\64u\65w\66y\67{8\3\2")
        buf.write("\22\3\2\f\f\5\2\13\13\17\17\"\"\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5")
        buf.write("\2\62;CHch\4\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\2\u01e8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3")
        buf.write("}\3\2\2\2\5\u0080\3\2\2\2\7\u0083\3\2\2\2\t\u0085\3\2")
        buf.write("\2\2\13\u0087\3\2\2\2\r\u0092\3\2\2\2\17\u00a1\3\2\2\2")
        buf.write("\21\u00a4\3\2\2\2\23\u00aa\3\2\2\2\25\u00ad\3\2\2\2\27")
        buf.write("\u00b2\3\2\2\2\31\u00b6\3\2\2\2\33\u00bd\3\2\2\2\35\u00c2")
        buf.write("\3\2\2\2\37\u00c7\3\2\2\2!\u00ce\3\2\2\2#\u00d8\3\2\2")
        buf.write("\2%\u00df\3\2\2\2\'\u00e3\3\2\2\2)\u00e9\3\2\2\2+\u00f1")
        buf.write("\3\2\2\2-\u00f7\3\2\2\2/\u00fb\3\2\2\2\61\u0104\3\2\2")
        buf.write("\2\63\u010a\3\2\2\2\65\u0110\3\2\2\2\67\u0114\3\2\2\2")
        buf.write("9\u0119\3\2\2\2;\u0129\3\2\2\2=\u0130\3\2\2\2?\u013c\3")
        buf.write("\2\2\2A\u013e\3\2\2\2C\u0141\3\2\2\2E\u0143\3\2\2\2G\u0145")
        buf.write("\3\2\2\2I\u0147\3\2\2\2K\u0149\3\2\2\2M\u014b\3\2\2\2")
        buf.write("O\u014d\3\2\2\2Q\u014f\3\2\2\2S\u0151\3\2\2\2U\u0153\3")
        buf.write("\2\2\2W\u0155\3\2\2\2Y\u0157\3\2\2\2[\u0159\3\2\2\2]\u015b")
        buf.write("\3\2\2\2_\u015d\3\2\2\2a\u015f\3\2\2\2c\u0162\3\2\2\2")
        buf.write("e\u0181\3\2\2\2g\u0183\3\2\2\2i\u018a\3\2\2\2k\u0191\3")
        buf.write("\2\2\2m\u019c\3\2\2\2o\u019e\3\2\2\2q\u01a0\3\2\2\2s\u01a3")
        buf.write("\3\2\2\2u\u01ad\3\2\2\2w\u01b4\3\2\2\2y\u01b6\3\2\2\2")
        buf.write("{\u01c2\3\2\2\2}~\7~\2\2~\177\7~\2\2\177\4\3\2\2\2\u0080")
        buf.write("\u0081\7(\2\2\u0081\u0082\7(\2\2\u0082\6\3\2\2\2\u0083")
        buf.write("\u0084\7#\2\2\u0084\b\3\2\2\2\u0085\u0086\7<\2\2\u0086")
        buf.write("\n\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7\61\2\2\u0089")
        buf.write("\u008d\3\2\2\2\u008a\u008c\n\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3")
        buf.write("\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091")
        buf.write("\b\6\2\2\u0091\f\3\2\2\2\u0092\u0093\7\61\2\2\u0093\u0094")
        buf.write("\7,\2\2\u0094\u0099\3\2\2\2\u0095\u0098\5\r\7\2\u0096")
        buf.write("\u0098\13\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\u009b\3\2\2\2\u0099\u009a\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\b\7\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7\f")
        buf.write("\2\2\u00a2\20\3\2\2\2\u00a3\u00a5\t\3\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\b\t\2\2")
        buf.write("\u00a9\22\3\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7h\2")
        buf.write("\2\u00ac\24\3\2\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7n")
        buf.write("\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1\7g\2\2\u00b1\26\3")
        buf.write("\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\30\3\2\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7p\2\2\u00bc\32\3\2\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7e\2\2\u00c1\34\3\2\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4")
        buf.write("\7{\2\2\u00c4\u00c5\7r\2\2\u00c5\u00c6\7g\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd \3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7g\2\2\u00d7\"\3\2\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7i\2\2\u00de$\3")
        buf.write("\2\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2&\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8(\3\2\2\2\u00e9\u00ea\7d\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7p\2\2\u00f0*\3")
        buf.write("\2\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6\7v\2\2\u00f6,\3")
        buf.write("\2\2\2\u00f7\u00f8\7x\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa.\3\2\2\2\u00fb\u00fc\7e\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\60\3\2\2\2\u0104\u0105\7d\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7g\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7m\2\2\u0109\62\3\2\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7p\2\2\u010d\u010e\7i\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\64\3\2\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7n\2\2\u0113\66\3\2\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\u0116\7t\2\2\u0116\u0117\7w\2\2\u0117\u0118")
        buf.write("\7g\2\2\u01188\3\2\2\2\u0119\u011a\7h\2\2\u011a\u011b")
        buf.write("\7c\2\2\u011b\u011c\7n\2\2\u011c\u011d\7u\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e:\3\2\2\2\u011f\u0120\7?\2\2\u0120\u012a")
        buf.write("\7?\2\2\u0121\u0122\7#\2\2\u0122\u012a\7?\2\2\u0123\u012a")
        buf.write("\7>\2\2\u0124\u0125\7>\2\2\u0125\u012a\7?\2\2\u0126\u012a")
        buf.write("\7@\2\2\u0127\u0128\7@\2\2\u0128\u012a\7?\2\2\u0129\u011f")
        buf.write("\3\2\2\2\u0129\u0121\3\2\2\2\u0129\u0123\3\2\2\2\u0129")
        buf.write("\u0124\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u012a<\3\2\2\2\u012b\u012c\7(\2\2\u012c\u0131\7(\2\2")
        buf.write("\u012d\u012e\7~\2\2\u012e\u0131\7~\2\2\u012f\u0131\7#")
        buf.write("\2\2\u0130\u012b\3\2\2\2\u0130\u012d\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131>\3\2\2\2\u0132\u0133\7-\2\2\u0133\u013d")
        buf.write("\7?\2\2\u0134\u0135\7/\2\2\u0135\u013d\7?\2\2\u0136\u0137")
        buf.write("\7,\2\2\u0137\u013d\7?\2\2\u0138\u0139\7\61\2\2\u0139")
        buf.write("\u013d\7?\2\2\u013a\u013b\7\'\2\2\u013b\u013d\7?\2\2\u013c")
        buf.write("\u0132\3\2\2\2\u013c\u0134\3\2\2\2\u013c\u0136\3\2\2\2")
        buf.write("\u013c\u0138\3\2\2\2\u013c\u013a\3\2\2\2\u013d@\3\2\2")
        buf.write("\2\u013e\u013f\7<\2\2\u013f\u0140\7?\2\2\u0140B\3\2\2")
        buf.write("\2\u0141\u0142\7\60\2\2\u0142D\3\2\2\2\u0143\u0144\7?")
        buf.write("\2\2\u0144F\3\2\2\2\u0145\u0146\7-\2\2\u0146H\3\2\2\2")
        buf.write("\u0147\u0148\7/\2\2\u0148J\3\2\2\2\u0149\u014a\7,\2\2")
        buf.write("\u014aL\3\2\2\2\u014b\u014c\7\61\2\2\u014cN\3\2\2\2\u014d")
        buf.write("\u014e\7\'\2\2\u014eP\3\2\2\2\u014f\u0150\7*\2\2\u0150")
        buf.write("R\3\2\2\2\u0151\u0152\7+\2\2\u0152T\3\2\2\2\u0153\u0154")
        buf.write("\7]\2\2\u0154V\3\2\2\2\u0155\u0156\7_\2\2\u0156X\3\2\2")
        buf.write("\2\u0157\u0158\7}\2\2\u0158Z\3\2\2\2\u0159\u015a\7\177")
        buf.write("\2\2\u015a\\\3\2\2\2\u015b\u015c\7.\2\2\u015c^\3\2\2\2")
        buf.write("\u015d\u015e\7=\2\2\u015e`\3\2\2\2\u015f\u0160\t\4\2\2")
        buf.write("\u0160b\3\2\2\2\u0161\u0163\5a\61\2\u0162\u0161\3\2\2")
        buf.write("\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u016c\7\60\2\2\u0167")
        buf.write("\u0169\5a\61\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3")
        buf.write("\2\2\2\u016c\u0168\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u0177")
        buf.write("\3\2\2\2\u016e\u0170\t\5\2\2\u016f\u0171\t\6\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2")
        buf.write("\u0172\u0174\5a\61\2\u0173\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178")
        buf.write("\3\2\2\2\u0177\u016e\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("d\3\2\2\2\u0179\u0182\7\62\2\2\u017a\u017e\t\7\2\2\u017b")
        buf.write("\u017d\t\4\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0182\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0181\u0179\3\2\2\2\u0181\u017a")
        buf.write("\3\2\2\2\u0182f\3\2\2\2\u0183\u0184\7\62\2\2\u0184\u0186")
        buf.write("\t\b\2\2\u0185\u0187\t\t\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189h\3\2\2\2\u018a\u018b\7\62\2\2\u018b\u018d\t\n\2")
        buf.write("\2\u018c\u018e\t\13\2\2\u018d\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("j\3\2\2\2\u0191\u0192\7\62\2\2\u0192\u0194\t\f\2\2\u0193")
        buf.write("\u0195\t\r\2\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197l\3\2\2")
        buf.write("\2\u0198\u019d\5e\63\2\u0199\u019d\5g\64\2\u019a\u019d")
        buf.write("\5i\65\2\u019b\u019d\5k\66\2\u019c\u0198\3\2\2\2\u019c")
        buf.write("\u0199\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019dn\3\2\2\2\u019e\u019f\n\16\2\2\u019fp\3\2\2\2\u01a0")
        buf.write("\u01a1\7^\2\2\u01a1\u01a2\t\17\2\2\u01a2r\3\2\2\2\u01a3")
        buf.write("\u01a8\7$\2\2\u01a4\u01a7\5o8\2\u01a5\u01a7\5q9\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3")
        buf.write("\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7$\2\2\u01act\3")
        buf.write("\2\2\2\u01ad\u01b1\t\20\2\2\u01ae\u01b0\t\21\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2v\3\2\2\2\u01b3\u01b1\3\2\2")
        buf.write("\2\u01b4\u01b5\13\2\2\2\u01b5x\3\2\2\2\u01b6\u01bb\7$")
        buf.write("\2\2\u01b7\u01ba\5o8\2\u01b8\u01ba\5q9\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c0\n\17\2\2")
        buf.write("\u01c0\u01c1\b=\3\2\u01c1z\3\2\2\2\u01c2\u01c7\7$\2\2")
        buf.write("\u01c3\u01c6\5o8\2\u01c4\u01c6\5q9\2\u01c5\u01c3\3\2\2")
        buf.write("\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01ca\u01cb\b>\4\2\u01cb|\3\2\2\2\35\2")
        buf.write("\u008d\u0097\u0099\u00a6\u0129\u0130\u013c\u0164\u016a")
        buf.write("\u016c\u0170\u0175\u0177\u017e\u0181\u0188\u018f\u0196")
        buf.write("\u019c\u01a6\u01a8\u01b1\u01b9\u01bb\u01c5\u01c7\5\b\2")
        buf.write("\2\3=\2\3>\3")
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
            self.text = self.text.replace('\r','\n').split('\n')[0][1:]
     


