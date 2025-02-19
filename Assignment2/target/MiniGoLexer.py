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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u023c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\7\2\u0092\n\2\f\2")
        buf.write("\16\2\u0095\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\u009e")
        buf.write("\n\3\f\3\16\3\u00a1\13\3\3\3\3\3\3\3\3\3\3\3\3\4\5\4\u00a9")
        buf.write("\n\4\3\4\3\4\3\4\3\5\6\5\u00af\n\5\r\5\16\5\u00b0\3\5")
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
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\3:\6:\u01ca\n:\r:\16:\u01cb\3:\3:\6:\u01d0\n:")
        buf.write("\r:\16:\u01d1\5:\u01d4\n:\3:\3:\5:\u01d8\n:\3:\6:\u01db")
        buf.write("\n:\r:\16:\u01dc\5:\u01df\n:\3:\3:\3;\3;\3;\7;\u01e6\n")
        buf.write(";\f;\16;\u01e9\13;\5;\u01eb\n;\3<\3<\3<\6<\u01f0\n<\r")
        buf.write("<\16<\u01f1\3=\3=\3=\6=\u01f7\n=\r=\16=\u01f8\3>\3>\3")
        buf.write(">\6>\u01fe\n>\r>\16>\u01ff\3?\3?\3?\3?\5?\u0206\n?\3?")
        buf.write("\3?\3@\3@\3A\3A\3A\3B\3B\3B\7B\u0212\nB\fB\16B\u0215\13")
        buf.write("B\3B\3B\3B\3C\3C\7C\u021c\nC\fC\16C\u021f\13C\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3E\7E\u0229\nE\fE\16E\u022c\13E\3E\3E\3")
        buf.write("E\3E\3F\3F\3F\7F\u0235\nF\fF\16F\u0238\13F\3F\3F\3F\3")
        buf.write("\u009f\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q\2s:u\2w\2y\2{\2};\177\2\u0081\2\u0083<\u0085")
        buf.write("=\u0087>\u0089?\u008b@\3\2\22\3\2\f\f\5\2\13\13\16\17")
        buf.write("\"\"\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2DDdd\3\2\62\63")
        buf.write("\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\5\2\f\f$$^^\7\2$")
        buf.write("$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u024e\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2")
        buf.write("\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5")
        buf.write("\u0098\3\2\2\2\7\u00a8\3\2\2\2\t\u00ae\3\2\2\2\13\u00b4")
        buf.write("\3\2\2\2\r\u00b9\3\2\2\2\17\u00c0\3\2\2\2\21\u00c6\3\2")
        buf.write("\2\2\23\u00cf\3\2\2\2\25\u00d6\3\2\2\2\27\u00dd\3\2\2")
        buf.write("\2\31\u00e6\3\2\2\2\33\u00f2\3\2\2\2\35\u00fb\3\2\2\2")
        buf.write("\37\u0101\3\2\2\2!\u0109\3\2\2\2#\u0113\3\2\2\2%\u011b")
        buf.write("\3\2\2\2\'\u0121\3\2\2\2)\u012c\3\2\2\2+\u0134\3\2\2\2")
        buf.write("-\u013c\3\2\2\2/\u0142\3\2\2\2\61\u0149\3\2\2\2\63\u0151")
        buf.write("\3\2\2\2\65\u0156\3\2\2\2\67\u015b\3\2\2\29\u015e\3\2")
        buf.write("\2\2;\u0163\3\2\2\2=\u0166\3\2\2\2?\u016b\3\2\2\2A\u0170")
        buf.write("\3\2\2\2C\u0175\3\2\2\2E\u0178\3\2\2\2G\u017d\3\2\2\2")
        buf.write("I\u0182\3\2\2\2K\u0187\3\2\2\2M\u018c\3\2\2\2O\u0191\3")
        buf.write("\2\2\2Q\u0196\3\2\2\2S\u0199\3\2\2\2U\u019c\3\2\2\2W\u019f")
        buf.write("\3\2\2\2Y\u01a2\3\2\2\2[\u01a5\3\2\2\2]\u01a8\3\2\2\2")
        buf.write("_\u01ab\3\2\2\2a\u01ae\3\2\2\2c\u01b1\3\2\2\2e\u01b4\3")
        buf.write("\2\2\2g\u01b7\3\2\2\2i\u01ba\3\2\2\2k\u01bd\3\2\2\2m\u01c0")
        buf.write("\3\2\2\2o\u01c3\3\2\2\2q\u01c6\3\2\2\2s\u01c9\3\2\2\2")
        buf.write("u\u01ea\3\2\2\2w\u01ec\3\2\2\2y\u01f3\3\2\2\2{\u01fa\3")
        buf.write("\2\2\2}\u0205\3\2\2\2\177\u0209\3\2\2\2\u0081\u020b\3")
        buf.write("\2\2\2\u0083\u020e\3\2\2\2\u0085\u0219\3\2\2\2\u0087\u0222")
        buf.write("\3\2\2\2\u0089\u0225\3\2\2\2\u008b\u0231\3\2\2\2\u008d")
        buf.write("\u008e\7\61\2\2\u008e\u008f\7\61\2\2\u008f\u0093\3\2\2")
        buf.write("\2\u0090\u0092\n\2\2\2\u0091\u0090\3\2\2\2\u0092\u0095")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\b\2\2\2")
        buf.write("\u0097\4\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a\7,\2")
        buf.write("\2\u009a\u009f\3\2\2\2\u009b\u009e\5\5\3\2\u009c\u009e")
        buf.write("\13\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7")
        buf.write(",\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\b\3\2\2\u00a6\6\3\2\2\2\u00a7\u00a9\7\17\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00ab\7\f\2\2\u00ab\u00ac\b\4\3\2\u00ac\b\3\2\2\2\u00ad")
        buf.write("\u00af\t\3\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2\u00b3\b\5\2\2\u00b3\n\3\2\2\2\u00b4\u00b5")
        buf.write("\7k\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8")
        buf.write("\b\6\4\2\u00b8\f\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00bf\b\7\5\2\u00bf\16\3\2\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\b\b\6\2\u00c5\20\3\2\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7w\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00ce\b\t\7\2\u00ce\22\3\2\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7e\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\b\n\b\2\u00d5")
        buf.write("\24\3\2\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7{\2\2\u00d8")
        buf.write("\u00d9\7r\2\2\u00d9\u00da\7g\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dc\b\13\t\2\u00dc\26\3\2\2\2\u00dd\u00de\7u\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7w\2\2\u00e1")
        buf.write("\u00e2\7e\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e5\b\f\n\2\u00e5\30\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7g\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7c\2\2\u00ed")
        buf.write("\u00ee\7e\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\b\r\13\2\u00f1\32\3\2\2\2\u00f2\u00f3\7u\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7k\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fa\b\16\f\2\u00fa\34\3\2\2\2\u00fb\u00fc\7k\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\b\17\r\2\u0100\36\3\2\2\2\u0101\u0102\7h\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7q\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7v\2\2\u0106\u0107\3\2\2\2\u0107\u0108\b\20\16")
        buf.write("\2\u0108 \3\2\2\2\u0109\u010a\7d\2\2\u010a\u010b\7q\2")
        buf.write("\2\u010b\u010c\7q\2\2\u010c\u010d\7n\2\2\u010d\u010e\7")
        buf.write("g\2\2\u010e\u010f\7c\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0112\b\21\17\2\u0112\"\3\2\2\2\u0113\u0114")
        buf.write("\7e\2\2\u0114\u0115\7q\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7u\2\2\u0117\u0118\7v\2\2\u0118\u0119\3\2\2\2\u0119\u011a")
        buf.write("\b\22\20\2\u011a$\3\2\2\2\u011b\u011c\7x\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7t\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write("\b\23\21\2\u0120&\3\2\2\2\u0121\u0122\7e\2\2\u0122\u0123")
        buf.write("\7q\2\2\u0123\u0124\7p\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7w\2\2\u0128\u0129")
        buf.write("\7g\2\2\u0129\u012a\3\2\2\2\u012a\u012b\b\24\22\2\u012b")
        buf.write("(\3\2\2\2\u012c\u012d\7d\2\2\u012d\u012e\7t\2\2\u012e")
        buf.write("\u012f\7g\2\2\u012f\u0130\7c\2\2\u0130\u0131\7m\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0133\b\25\23\2\u0133*\3\2\2\2\u0134")
        buf.write("\u0135\7t\2\2\u0135\u0136\7c\2\2\u0136\u0137\7p\2\2\u0137")
        buf.write("\u0138\7i\2\2\u0138\u0139\7g\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\b\26\24\2\u013b,\3\2\2\2\u013c\u013d\7p\2\2\u013d")
        buf.write("\u013e\7k\2\2\u013e\u013f\7n\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0141\b\27\25\2\u0141.\3\2\2\2\u0142\u0143\7v\2\2\u0143")
        buf.write("\u0144\7t\2\2\u0144\u0145\7w\2\2\u0145\u0146\7g\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0148\b\30\26\2\u0148\60\3\2\2\2")
        buf.write("\u0149\u014a\7h\2\2\u014a\u014b\7c\2\2\u014b\u014c\7n")
        buf.write("\2\2\u014c\u014d\7u\2\2\u014d\u014e\7g\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\b\31\27\2\u0150\62\3\2\2\2\u0151")
        buf.write("\u0152\7?\2\2\u0152\u0153\7?\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0155\b\32\30\2\u0155\64\3\2\2\2\u0156\u0157\7#\2\2\u0157")
        buf.write("\u0158\7?\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b\33\31")
        buf.write("\2\u015a\66\3\2\2\2\u015b\u015c\7>\2\2\u015c\u015d\b\34")
        buf.write("\32\2\u015d8\3\2\2\2\u015e\u015f\7>\2\2\u015f\u0160\7")
        buf.write("?\2\2\u0160\u0161\3\2\2\2\u0161\u0162\b\35\33\2\u0162")
        buf.write(":\3\2\2\2\u0163\u0164\7@\2\2\u0164\u0165\b\36\34\2\u0165")
        buf.write("<\3\2\2\2\u0166\u0167\7@\2\2\u0167\u0168\7?\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\b\37\35\2\u016a>\3\2\2\2\u016b")
        buf.write("\u016c\7(\2\2\u016c\u016d\7(\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\b \36\2\u016f@\3\2\2\2\u0170\u0171\7~\2\2\u0171")
        buf.write("\u0172\7~\2\2\u0172\u0173\3\2\2\2\u0173\u0174\b!\37\2")
        buf.write("\u0174B\3\2\2\2\u0175\u0176\7#\2\2\u0176\u0177\b\" \2")
        buf.write("\u0177D\3\2\2\2\u0178\u0179\7-\2\2\u0179\u017a\7?\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017c\b#!\2\u017cF\3\2\2\2")
        buf.write("\u017d\u017e\7/\2\2\u017e\u017f\7?\2\2\u017f\u0180\3\2")
        buf.write("\2\2\u0180\u0181\b$\"\2\u0181H\3\2\2\2\u0182\u0183\7,")
        buf.write("\2\2\u0183\u0184\7?\2\2\u0184\u0185\3\2\2\2\u0185\u0186")
        buf.write("\b%#\2\u0186J\3\2\2\2\u0187\u0188\7\61\2\2\u0188\u0189")
        buf.write("\7?\2\2\u0189\u018a\3\2\2\2\u018a\u018b\b&$\2\u018bL\3")
        buf.write("\2\2\2\u018c\u018d\7\'\2\2\u018d\u018e\7?\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0190\b\'%\2\u0190N\3\2\2\2\u0191\u0192")
        buf.write("\7<\2\2\u0192\u0193\7?\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\b(&\2\u0195P\3\2\2\2\u0196\u0197\7\60\2\2\u0197\u0198")
        buf.write("\b)\'\2\u0198R\3\2\2\2\u0199\u019a\7?\2\2\u019a\u019b")
        buf.write("\b*(\2\u019bT\3\2\2\2\u019c\u019d\7-\2\2\u019d\u019e\b")
        buf.write("+)\2\u019eV\3\2\2\2\u019f\u01a0\7/\2\2\u01a0\u01a1\b,")
        buf.write("*\2\u01a1X\3\2\2\2\u01a2\u01a3\7,\2\2\u01a3\u01a4\b-+")
        buf.write("\2\u01a4Z\3\2\2\2\u01a5\u01a6\7\61\2\2\u01a6\u01a7\b.")
        buf.write(",\2\u01a7\\\3\2\2\2\u01a8\u01a9\7\'\2\2\u01a9\u01aa\b")
        buf.write("/-\2\u01aa^\3\2\2\2\u01ab\u01ac\7*\2\2\u01ac\u01ad\b\60")
        buf.write(".\2\u01ad`\3\2\2\2\u01ae\u01af\7+\2\2\u01af\u01b0\b\61")
        buf.write("/\2\u01b0b\3\2\2\2\u01b1\u01b2\7]\2\2\u01b2\u01b3\b\62")
        buf.write("\60\2\u01b3d\3\2\2\2\u01b4\u01b5\7_\2\2\u01b5\u01b6\b")
        buf.write("\63\61\2\u01b6f\3\2\2\2\u01b7\u01b8\7}\2\2\u01b8\u01b9")
        buf.write("\b\64\62\2\u01b9h\3\2\2\2\u01ba\u01bb\7\177\2\2\u01bb")
        buf.write("\u01bc\b\65\63\2\u01bcj\3\2\2\2\u01bd\u01be\7.\2\2\u01be")
        buf.write("\u01bf\b\66\64\2\u01bfl\3\2\2\2\u01c0\u01c1\7=\2\2\u01c1")
        buf.write("\u01c2\b\67\65\2\u01c2n\3\2\2\2\u01c3\u01c4\7<\2\2\u01c4")
        buf.write("\u01c5\b8\66\2\u01c5p\3\2\2\2\u01c6\u01c7\t\4\2\2\u01c7")
        buf.write("r\3\2\2\2\u01c8\u01ca\5q9\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01d3\7\60\2\2\u01ce\u01d0")
        buf.write("\5q9\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3")
        buf.write("\u01cf\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01de\3\2\2\2")
        buf.write("\u01d5\u01d7\t\5\2\2\u01d6\u01d8\t\6\2\2\u01d7\u01d6\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01db")
        buf.write("\5q9\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01d5\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e1\b:\67\2\u01e1t\3\2\2\2\u01e2\u01eb\7\62\2")
        buf.write("\2\u01e3\u01e7\t\7\2\2\u01e4\u01e6\t\4\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01ea\u01e2\3\2\2\2\u01ea\u01e3\3\2\2\2\u01ebv\3\2\2")
        buf.write("\2\u01ec\u01ed\7\62\2\2\u01ed\u01ef\t\b\2\2\u01ee\u01f0")
        buf.write("\t\t\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2x\3\2\2\2\u01f3")
        buf.write("\u01f4\7\62\2\2\u01f4\u01f6\t\n\2\2\u01f5\u01f7\t\13\2")
        buf.write("\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9z\3\2\2\2\u01fa\u01fb")
        buf.write("\7\62\2\2\u01fb\u01fd\t\f\2\2\u01fc\u01fe\t\r\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2")
        buf.write("\u01ff\u0200\3\2\2\2\u0200|\3\2\2\2\u0201\u0206\5u;\2")
        buf.write("\u0202\u0206\5w<\2\u0203\u0206\5y=\2\u0204\u0206\5{>\2")
        buf.write("\u0205\u0201\3\2\2\2\u0205\u0202\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0205\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208")
        buf.write("\b?8\2\u0208~\3\2\2\2\u0209\u020a\n\16\2\2\u020a\u0080")
        buf.write("\3\2\2\2\u020b\u020c\7^\2\2\u020c\u020d\t\17\2\2\u020d")
        buf.write("\u0082\3\2\2\2\u020e\u0213\7$\2\2\u020f\u0212\5\177@\2")
        buf.write("\u0210\u0212\5\u0081A\2\u0211\u020f\3\2\2\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0217\7$\2\2\u0217\u0218\bB9\2\u0218\u0084\3\2")
        buf.write("\2\2\u0219\u021d\t\20\2\2\u021a\u021c\t\21\2\2\u021b\u021a")
        buf.write("\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u0220\u0221\bC:\2\u0221\u0086\3\2\2\2\u0222\u0223\13")
        buf.write("\2\2\2\u0223\u0224\bD;\2\u0224\u0088\3\2\2\2\u0225\u022a")
        buf.write("\7$\2\2\u0226\u0229\5\177@\2\u0227\u0229\5\u0081A\2\u0228")
        buf.write("\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3")
        buf.write("\2\2\2\u022c\u022a\3\2\2\2\u022d\u022e\7^\2\2\u022e\u022f")
        buf.write("\n\17\2\2\u022f\u0230\bE<\2\u0230\u008a\3\2\2\2\u0231")
        buf.write("\u0236\7$\2\2\u0232\u0235\5\177@\2\u0233\u0235\5\u0081")
        buf.write("A\2\u0234\u0232\3\2\2\2\u0234\u0233\3\2\2\2\u0235\u0238")
        buf.write("\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\bF=\2\u023a")
        buf.write("\u023b\bF>\2\u023b\u008c\3\2\2\2\33\2\u0093\u009d\u009f")
        buf.write("\u00a8\u00b0\u01cb\u01d1\u01d3\u01d7\u01dc\u01de\u01e7")
        buf.write("\u01ea\u01f1\u01f8\u01ff\u0205\u0211\u0213\u021d\u0228")
        buf.write("\u022a\u0234\u0236?\b\2\2\3\4\2\3\6\3\3\7\4\3\b\5\3\t")
        buf.write("\6\3\n\7\3\13\b\3\f\t\3\r\n\3\16\13\3\17\f\3\20\r\3\21")
        buf.write("\16\3\22\17\3\23\20\3\24\21\3\25\22\3\26\23\3\27\24\3")
        buf.write("\30\25\3\31\26\3\32\27\3\33\30\3\34\31\3\35\32\3\36\33")
        buf.write("\3\37\34\3 \35\3!\36\3\"\37\3# \3$!\3%\"\3&#\3\'$\3(%")
        buf.write("\3)&\3*\'\3+(\3,)\3-*\3.+\3/,\3\60-\3\61.\3\62/\3\63\60")
        buf.write("\3\64\61\3\65\62\3\66\63\3\67\64\38\65\3:\66\3?\67\3B")
        buf.write("8\3C9\3D:\3E;\3F<\3F=")
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
    EQCOM = 25
    DIFFCOM = 26
    LESSCOM = 27
    LEQCOM = 28
    GRECOM = 29
    GEQCOM = 30
    AND = 31
    OR = 32
    NOT = 33
    ADDASSIGN = 34
    SUBASSIGN = 35
    MULASSIGN = 36
    DIVASSIGN = 37
    MODASSIGN = 38
    ASSIGN = 39
    DOT = 40
    EQUAL = 41
    ADD = 42
    SUB = 43
    MUL = 44
    DIV = 45
    MOD = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    COMMA = 53
    SEMICOLON = 54
    COLON = 55
    FLOAT = 56
    INTEGER = 57
    STRING = 58
    ID = 59
    ERROR_CHAR = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "':='", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "EQCOM", "DIFFCOM", 
            "LESSCOM", "LEQCOM", "GRECOM", "GEQCOM", "AND", "OR", "NOT", 
            "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN", "MODASSIGN", 
            "ASSIGN", "DOT", "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
            "COLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", 
                  "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                  "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                  "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", 
                  "TRUE_", "FALSE_", "EQCOM", "DIFFCOM", "LESSCOM", "LEQCOM", 
                  "GRECOM", "GEQCOM", "AND", "OR", "NOT", "ADDASSIGN", "SUBASSIGN", 
                  "MULASSIGN", "DIVASSIGN", "MODASSIGN", "ASSIGN", "DOT", 
                  "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", 
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
            actions[24] = self.EQCOM_action 
            actions[25] = self.DIFFCOM_action 
            actions[26] = self.LESSCOM_action 
            actions[27] = self.LEQCOM_action 
            actions[28] = self.GRECOM_action 
            actions[29] = self.GEQCOM_action 
            actions[30] = self.AND_action 
            actions[31] = self.OR_action 
            actions[32] = self.NOT_action 
            actions[33] = self.ADDASSIGN_action 
            actions[34] = self.SUBASSIGN_action 
            actions[35] = self.MULASSIGN_action 
            actions[36] = self.DIVASSIGN_action 
            actions[37] = self.MODASSIGN_action 
            actions[38] = self.ASSIGN_action 
            actions[39] = self.DOT_action 
            actions[40] = self.EQUAL_action 
            actions[41] = self.ADD_action 
            actions[42] = self.SUB_action 
            actions[43] = self.MUL_action 
            actions[44] = self.DIV_action 
            actions[45] = self.MOD_action 
            actions[46] = self.LP_action 
            actions[47] = self.RP_action 
            actions[48] = self.LSB_action 
            actions[49] = self.RSB_action 
            actions[50] = self.LCB_action 
            actions[51] = self.RCB_action 
            actions[52] = self.COMMA_action 
            actions[53] = self.SEMICOLON_action 
            actions[54] = self.COLON_action 
            actions[56] = self.FLOAT_action 
            actions[61] = self.INTEGER_action 
            actions[64] = self.STRING_action 
            actions[65] = self.ID_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
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
     

    def EQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 21:
            self.lastTokenType = 'EQCOM'
     

    def DIFFCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTokenType = 'DIFFCOM'
     

    def LESSCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTokenType = 'LESSCOM'
     

    def LEQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTokenType = 'LEQCOM'
     

    def GRECOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'GRECOM'
     

    def GEQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'GEQCOM'
     

    def AND_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'AND'
     

    def OR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'OR'
     

    def NOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'NOT'
     

    def ADDASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'ADDASSIGN'
     

    def SUBASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'SUBASSIGN'
     

    def MULASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'MULASSIGN'
     

    def DIVASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'DIVASSIGN'
     

    def MODASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'MODASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'DOT'
     

    def EQUAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'EQUAL'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'MOD'
     

    def LP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'LP'
     

    def RP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'RP'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 46:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 48:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 49:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 50:
            self.lastTokenType = 'SEMICOLON'
     

    def COLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 51:
            self.lastTokenType = 'COLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 52:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 53:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 54:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 55:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 56:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 57:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 58:
            self.text = self.text.replace('\r','\n').split('\n')[0]
     

        if actionIndex == 59:
            self.lastTokenType = 'UNCLOSE_STRING'
     


