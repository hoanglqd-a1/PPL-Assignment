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
        buf.write("\u0215\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\u009b\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\6\t")
        buf.write("\u00a6\n\t\r\t\16\t\u00a7\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0155\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u015d\n\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u016b\n \3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\6\62\u01a2\n\62\r\62\16\62\u01a3\3\62\3\62\6\62")
        buf.write("\u01a8\n\62\r\62\16\62\u01a9\5\62\u01ac\n\62\3\62\3\62")
        buf.write("\5\62\u01b0\n\62\3\62\6\62\u01b3\n\62\r\62\16\62\u01b4")
        buf.write("\5\62\u01b7\n\62\3\62\3\62\3\63\3\63\3\63\7\63\u01be\n")
        buf.write("\63\f\63\16\63\u01c1\13\63\5\63\u01c3\n\63\3\64\3\64\3")
        buf.write("\64\6\64\u01c8\n\64\r\64\16\64\u01c9\3\65\3\65\3\65\6")
        buf.write("\65\u01cf\n\65\r\65\16\65\u01d0\3\66\3\66\3\66\6\66\u01d6")
        buf.write("\n\66\r\66\16\66\u01d7\3\67\3\67\3\67\3\67\5\67\u01de")
        buf.write("\n\67\3\67\3\67\38\38\39\39\39\3:\3:\3:\7:\u01ea\n:\f")
        buf.write(":\16:\u01ed\13:\3:\3:\3:\3;\3;\7;\u01f4\n;\f;\16;\u01f7")
        buf.write("\13;\3;\3;\3<\3<\3<\3=\3=\3=\7=\u0201\n=\f=\16=\u0204")
        buf.write("\13=\3=\3=\3=\3=\3=\3>\3>\3>\7>\u020e\n>\f>\16>\u0211")
        buf.write("\13>\3>\3>\3>\3\u0099\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\62")
        buf.write("e\2g\2i\2k\2m\63o\2q\2s\64u\65w\66y\67{8\3\2\22\3\2\f")
        buf.write("\f\5\2\13\13\17\17\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CH")
        buf.write("ch\4\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u0231")
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
        buf.write("\2\2\2_\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3}\3\2\2\2\5\u0080")
        buf.write("\3\2\2\2\7\u0083\3\2\2\2\t\u0085\3\2\2\2\13\u0087\3\2")
        buf.write("\2\2\r\u0092\3\2\2\2\17\u00a1\3\2\2\2\21\u00a5\3\2\2\2")
        buf.write("\23\u00ab\3\2\2\2\25\u00b0\3\2\2\2\27\u00b7\3\2\2\2\31")
        buf.write("\u00bd\3\2\2\2\33\u00c6\3\2\2\2\35\u00cd\3\2\2\2\37\u00d4")
        buf.write("\3\2\2\2!\u00dd\3\2\2\2#\u00e9\3\2\2\2%\u00f2\3\2\2\2")
        buf.write("\'\u00f8\3\2\2\2)\u0100\3\2\2\2+\u010a\3\2\2\2-\u0112")
        buf.write("\3\2\2\2/\u0118\3\2\2\2\61\u0123\3\2\2\2\63\u012b\3\2")
        buf.write("\2\2\65\u0133\3\2\2\2\67\u0139\3\2\2\29\u0140\3\2\2\2")
        buf.write(";\u0154\3\2\2\2=\u015c\3\2\2\2?\u016a\3\2\2\2A\u016c\3")
        buf.write("\2\2\2C\u0171\3\2\2\2E\u0174\3\2\2\2G\u0177\3\2\2\2I\u017a")
        buf.write("\3\2\2\2K\u017d\3\2\2\2M\u0180\3\2\2\2O\u0183\3\2\2\2")
        buf.write("Q\u0186\3\2\2\2S\u0189\3\2\2\2U\u018c\3\2\2\2W\u018f\3")
        buf.write("\2\2\2Y\u0192\3\2\2\2[\u0195\3\2\2\2]\u0198\3\2\2\2_\u019b")
        buf.write("\3\2\2\2a\u019e\3\2\2\2c\u01a1\3\2\2\2e\u01c2\3\2\2\2")
        buf.write("g\u01c4\3\2\2\2i\u01cb\3\2\2\2k\u01d2\3\2\2\2m\u01dd\3")
        buf.write("\2\2\2o\u01e1\3\2\2\2q\u01e3\3\2\2\2s\u01e6\3\2\2\2u\u01f1")
        buf.write("\3\2\2\2w\u01fa\3\2\2\2y\u01fd\3\2\2\2{\u020a\3\2\2\2")
        buf.write("}~\7~\2\2~\177\7~\2\2\177\4\3\2\2\2\u0080\u0081\7(\2\2")
        buf.write("\u0081\u0082\7(\2\2\u0082\6\3\2\2\2\u0083\u0084\7#\2\2")
        buf.write("\u0084\b\3\2\2\2\u0085\u0086\7<\2\2\u0086\n\3\2\2\2\u0087")
        buf.write("\u0088\7\61\2\2\u0088\u0089\7\61\2\2\u0089\u008d\3\2\2")
        buf.write("\2\u008a\u008c\n\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\6\2\2")
        buf.write("\u0091\f\3\2\2\2\u0092\u0093\7\61\2\2\u0093\u0094\7,\2")
        buf.write("\2\u0094\u0099\3\2\2\2\u0095\u0098\5\r\7\2\u0096\u0098")
        buf.write("\13\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u009a\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7")
        buf.write(",\2\2\u009d\u009e\7\61\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\b\7\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7\f\2\2\u00a2\u00a3")
        buf.write("\b\b\3\2\u00a3\20\3\2\2\2\u00a4\u00a6\t\3\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b\t\2\2")
        buf.write("\u00aa\22\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7h\2")
        buf.write("\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\b\n\4\2\u00af\24\3")
        buf.write("\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\b\13\5\2\u00b6\26\3\2\2\2\u00b7\u00b8\7h\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc")
        buf.write("\b\f\6\2\u00bc\30\3\2\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5")
        buf.write("\b\r\7\2\u00c5\32\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb\u00cc\b\16\b\2\u00cc\34\3\2\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7{\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b\17\t\2\u00d3")
        buf.write("\36\3\2\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6\7v\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7e\2\2\u00d9")
        buf.write("\u00da\7v\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\b\20\n\2")
        buf.write("\u00dc \3\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2")
        buf.write("\u00df\u00e0\7v\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7t")
        buf.write("\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8")
        buf.write("\b\21\13\2\u00e8\"\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7i\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1")
        buf.write("\b\22\f\2\u00f1$\3\2\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\b\23\r\2\u00f7&\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7n\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7v\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\b\24\16\2\u00ff")
        buf.write("(\3\2\2\2\u0100\u0101\7d\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7q\2\2\u0103\u0104\7n\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\u0106\7c\2\2\u0106\u0107\7p\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\b\25\17\2\u0109*\3\2\2\2\u010a\u010b\7e\2\2\u010b")
        buf.write("\u010c\7q\2\2\u010c\u010d\7p\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\3\2\2\2\u0110\u0111\b\26\20")
        buf.write("\2\u0111,\3\2\2\2\u0112\u0113\7x\2\2\u0113\u0114\7c\2")
        buf.write("\2\u0114\u0115\7t\2\2\u0115\u0116\3\2\2\2\u0116\u0117")
        buf.write("\b\27\21\2\u0117.\3\2\2\2\u0118\u0119\7e\2\2\u0119\u011a")
        buf.write("\7q\2\2\u011a\u011b\7p\2\2\u011b\u011c\7v\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7w\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\3\2\2\2\u0121\u0122\b\30\22\2\u0122")
        buf.write("\60\3\2\2\2\u0123\u0124\7d\2\2\u0124\u0125\7t\2\2\u0125")
        buf.write("\u0126\7g\2\2\u0126\u0127\7c\2\2\u0127\u0128\7m\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012a\b\31\23\2\u012a\62\3\2\2\2")
        buf.write("\u012b\u012c\7t\2\2\u012c\u012d\7c\2\2\u012d\u012e\7p")
        buf.write("\2\2\u012e\u012f\7i\2\2\u012f\u0130\7g\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0132\b\32\24\2\u0132\64\3\2\2\2\u0133")
        buf.write("\u0134\7p\2\2\u0134\u0135\7k\2\2\u0135\u0136\7n\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\b\33\25\2\u0138\66\3\2\2\2")
        buf.write("\u0139\u013a\7v\2\2\u013a\u013b\7t\2\2\u013b\u013c\7w")
        buf.write("\2\2\u013c\u013d\7g\2\2\u013d\u013e\3\2\2\2\u013e\u013f")
        buf.write("\b\34\26\2\u013f8\3\2\2\2\u0140\u0141\7h\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\3\2\2\2\u0146\u0147\b\35\27\2\u0147")
        buf.write(":\3\2\2\2\u0148\u0149\7?\2\2\u0149\u0155\7?\2\2\u014a")
        buf.write("\u014b\7#\2\2\u014b\u0155\7?\2\2\u014c\u0155\7>\2\2\u014d")
        buf.write("\u014e\7>\2\2\u014e\u0155\7?\2\2\u014f\u0155\7@\2\2\u0150")
        buf.write("\u0151\7@\2\2\u0151\u0152\7?\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0155\b\36\30\2\u0154\u0148\3\2\2\2\u0154\u014a\3\2\2")
        buf.write("\2\u0154\u014c\3\2\2\2\u0154\u014d\3\2\2\2\u0154\u014f")
        buf.write("\3\2\2\2\u0154\u0150\3\2\2\2\u0155<\3\2\2\2\u0156\u0157")
        buf.write("\7(\2\2\u0157\u015d\7(\2\2\u0158\u0159\7~\2\2\u0159\u015d")
        buf.write("\7~\2\2\u015a\u015b\7#\2\2\u015b\u015d\b\37\31\2\u015c")
        buf.write("\u0156\3\2\2\2\u015c\u0158\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015d>\3\2\2\2\u015e\u015f\7-\2\2\u015f\u016b\7?\2\2")
        buf.write("\u0160\u0161\7/\2\2\u0161\u016b\7?\2\2\u0162\u0163\7,")
        buf.write("\2\2\u0163\u016b\7?\2\2\u0164\u0165\7\61\2\2\u0165\u016b")
        buf.write("\7?\2\2\u0166\u0167\7\'\2\2\u0167\u0168\7?\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016b\b \32\2\u016a\u015e\3\2\2\2\u016a")
        buf.write("\u0160\3\2\2\2\u016a\u0162\3\2\2\2\u016a\u0164\3\2\2\2")
        buf.write("\u016a\u0166\3\2\2\2\u016b@\3\2\2\2\u016c\u016d\7<\2\2")
        buf.write("\u016d\u016e\7?\2\2\u016e\u016f\3\2\2\2\u016f\u0170\b")
        buf.write("!\33\2\u0170B\3\2\2\2\u0171\u0172\7\60\2\2\u0172\u0173")
        buf.write("\b\"\34\2\u0173D\3\2\2\2\u0174\u0175\7?\2\2\u0175\u0176")
        buf.write("\b#\35\2\u0176F\3\2\2\2\u0177\u0178\7-\2\2\u0178\u0179")
        buf.write("\b$\36\2\u0179H\3\2\2\2\u017a\u017b\7/\2\2\u017b\u017c")
        buf.write("\b%\37\2\u017cJ\3\2\2\2\u017d\u017e\7,\2\2\u017e\u017f")
        buf.write("\b& \2\u017fL\3\2\2\2\u0180\u0181\7\61\2\2\u0181\u0182")
        buf.write("\b\'!\2\u0182N\3\2\2\2\u0183\u0184\7\'\2\2\u0184\u0185")
        buf.write("\b(\"\2\u0185P\3\2\2\2\u0186\u0187\7*\2\2\u0187\u0188")
        buf.write("\b)#\2\u0188R\3\2\2\2\u0189\u018a\7+\2\2\u018a\u018b\b")
        buf.write("*$\2\u018bT\3\2\2\2\u018c\u018d\7]\2\2\u018d\u018e\b+")
        buf.write("%\2\u018eV\3\2\2\2\u018f\u0190\7_\2\2\u0190\u0191\b,&")
        buf.write("\2\u0191X\3\2\2\2\u0192\u0193\7}\2\2\u0193\u0194\b-\'")
        buf.write("\2\u0194Z\3\2\2\2\u0195\u0196\7\177\2\2\u0196\u0197\b")
        buf.write(".(\2\u0197\\\3\2\2\2\u0198\u0199\7.\2\2\u0199\u019a\b")
        buf.write("/)\2\u019a^\3\2\2\2\u019b\u019c\7=\2\2\u019c\u019d\b\60")
        buf.write("*\2\u019d`\3\2\2\2\u019e\u019f\t\4\2\2\u019fb\3\2\2\2")
        buf.write("\u01a0\u01a2\5a\61\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01ab\7\60\2\2\u01a6\u01a8\5a\61\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a7\3")
        buf.write("\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01b6\3\2\2\2\u01ad\u01af")
        buf.write("\t\5\2\2\u01ae\u01b0\t\6\2\2\u01af\u01ae\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3\5a\61\2")
        buf.write("\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01ad")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\b\62+\2\u01b9d\3\2\2\2\u01ba\u01c3\7\62\2\2\u01bb")
        buf.write("\u01bf\t\7\2\2\u01bc\u01be\t\4\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01ba")
        buf.write("\3\2\2\2\u01c2\u01bb\3\2\2\2\u01c3f\3\2\2\2\u01c4\u01c5")
        buf.write("\7\62\2\2\u01c5\u01c7\t\b\2\2\u01c6\u01c8\t\t\2\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01cah\3\2\2\2\u01cb\u01cc\7\62\2")
        buf.write("\2\u01cc\u01ce\t\n\2\2\u01cd\u01cf\t\13\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1j\3\2\2\2\u01d2\u01d3\7\62\2\2\u01d3")
        buf.write("\u01d5\t\f\2\2\u01d4\u01d6\t\r\2\2\u01d5\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8l\3\2\2\2\u01d9\u01de\5e\63\2\u01da\u01de")
        buf.write("\5g\64\2\u01db\u01de\5i\65\2\u01dc\u01de\5k\66\2\u01dd")
        buf.write("\u01d9\3\2\2\2\u01dd\u01da\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\b")
        buf.write("\67,\2\u01e0n\3\2\2\2\u01e1\u01e2\n\16\2\2\u01e2p\3\2")
        buf.write("\2\2\u01e3\u01e4\7^\2\2\u01e4\u01e5\t\17\2\2\u01e5r\3")
        buf.write("\2\2\2\u01e6\u01eb\7$\2\2\u01e7\u01ea\5o8\2\u01e8\u01ea")
        buf.write("\5q9\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01ed")
        buf.write("\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ee\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\7$\2\2")
        buf.write("\u01ef\u01f0\b:-\2\u01f0t\3\2\2\2\u01f1\u01f5\t\20\2\2")
        buf.write("\u01f2\u01f4\t\21\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\b;.\2\u01f9")
        buf.write("v\3\2\2\2\u01fa\u01fb\13\2\2\2\u01fb\u01fc\b</\2\u01fc")
        buf.write("x\3\2\2\2\u01fd\u0202\7$\2\2\u01fe\u0201\5o8\2\u01ff\u0201")
        buf.write("\5q9\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0204")
        buf.write("\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0205\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0206\7^\2\2")
        buf.write("\u0206\u0207\n\17\2\2\u0207\u0208\b=\60\2\u0208\u0209")
        buf.write("\b=\61\2\u0209z\3\2\2\2\u020a\u020f\7$\2\2\u020b\u020e")
        buf.write("\5o8\2\u020c\u020e\5q9\2\u020d\u020b\3\2\2\2\u020d\u020c")
        buf.write("\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0212\u0213\b>\62\2\u0213\u0214\b>\63\2\u0214|\3\2\2")
        buf.write("\2\35\2\u008d\u0097\u0099\u00a7\u0154\u015c\u016a\u01a3")
        buf.write("\u01a9\u01ab\u01af\u01b4\u01b6\u01bf\u01c2\u01c9\u01d0")
        buf.write("\u01d7\u01dd\u01e9\u01eb\u01f5\u0200\u0202\u020d\u020f")
        buf.write("\64\b\2\2\3\b\2\3\n\3\3\13\4\3\f\5\3\r\6\3\16\7\3\17\b")
        buf.write("\3\20\t\3\21\n\3\22\13\3\23\f\3\24\r\3\25\16\3\26\17\3")
        buf.write("\27\20\3\30\21\3\31\22\3\32\23\3\33\24\3\34\25\3\35\26")
        buf.write("\3\36\27\3\37\30\3 \31\3!\32\3\"\33\3#\34\3$\35\3%\36")
        buf.write("\3&\37\3\' \3(!\3)\"\3*#\3+$\3,%\3-&\3.\'\3/(\3\60)\3")
        buf.write("\62*\3\67+\3:,\3;-\3<.\3=/\3=\60\3>\61\3>\62")
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
    EQUAL = 34
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
            "BOOLEAN_OP", "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                  "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                  "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
                  "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                  "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "BOOLEAN_OP", 
                  "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", 
                  "LCB", "RCB", "COMMA", "SEMICOLON", "Digit", "FLOAT", 
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
            actions[6] = self.NL_action 
            actions[8] = self.IF__action 
            actions[9] = self.ELSE__action 
            actions[10] = self.FOR__action 
            actions[11] = self.RETURN__action 
            actions[12] = self.FUNC__action 
            actions[13] = self.TYPE__action 
            actions[14] = self.STRUCT__action 
            actions[15] = self.INTERFACE__action 
            actions[16] = self.STRING__action 
            actions[17] = self.INT__action 
            actions[18] = self.FLOAT__action 
            actions[19] = self.BOOLEAN__action 
            actions[20] = self.CONST__action 
            actions[21] = self.VAR__action 
            actions[22] = self.CONTINUE__action 
            actions[23] = self.BREAK__action 
            actions[24] = self.RANGE__action 
            actions[25] = self.NIL__action 
            actions[26] = self.TRUE__action 
            actions[27] = self.FALSE__action 
            actions[28] = self.COMPARISON_OP_action 
            actions[29] = self.BOOLEAN_OP_action 
            actions[30] = self.UPT_ASSIGN_action 
            actions[31] = self.ASSIGN_action 
            actions[32] = self.DOT_action 
            actions[33] = self.EQUAL_action 
            actions[34] = self.ADD_action 
            actions[35] = self.SUB_action 
            actions[36] = self.MUL_action 
            actions[37] = self.DIV_action 
            actions[38] = self.MOD_action 
            actions[39] = self.LPAREN_action 
            actions[40] = self.RPAREN_action 
            actions[41] = self.LSB_action 
            actions[42] = self.RSB_action 
            actions[43] = self.LCB_action 
            actions[44] = self.RCB_action 
            actions[45] = self.COMMA_action 
            actions[46] = self.SEMICOLON_action 
            actions[48] = self.FLOAT_action 
            actions[53] = self.INTEGER_action 
            actions[56] = self.STRING_action 
            actions[57] = self.ID_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RPAREN', 'RSB', 'RCB']:
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
     

    def BOOLEAN_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTokenType = 'BOOLEAN_OP'
     

    def UPT_ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTokenType = 'UPT_ASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'DOT'
     

    def EQUAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'EQUAL'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'MOD'
     

    def LPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'LPAREN'
     

    def RPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'RPAREN'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'SEMICOLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.text = self.text[1:]
     

        if actionIndex == 46:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.text = self.text.replace('\r','\n').split('\n')[0][1:]
     

        if actionIndex == 48:
            self.lastTokenType = 'UNCLOSE_STRING'
     


