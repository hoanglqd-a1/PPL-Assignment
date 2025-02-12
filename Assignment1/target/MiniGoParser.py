# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u0261\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\4\3\4\5\4\u0090\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00a1\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7")
        buf.write("\u00a9\n\7\f\7\16\7\u00ac\13\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\b\u00b4\n\b\f\b\16\b\u00b7\13\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\7\t\u00bf\n\t\f\t\16\t\u00c2\13\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\n\u00cd\n\n\f\n\16\n\u00d0\13\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u00de\n\13\f\13\16\13\u00e1\13\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00e8\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00fa\n\r\f\r\16")
        buf.write("\r\u00fd\13\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0105")
        buf.write("\n\16\3\17\3\17\5\17\u0109\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u0110\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\7\21\u011d\n\21\f\21\16\21\u0120")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0139\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u014f\n\25\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0155\n\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u015d\n\30\3\30\3\30\3\30\5\30\u0162\n\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u016d\n\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u0174\n\33\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0182\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\5!\u0192\n!\3\"\3\"\3\"\5\"\u0197\n\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01a1\n\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\5%\u01b1\n%\3&\3&\3&\5")
        buf.write("&\u01b6\n&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u01c3")
        buf.write("\n(\3)\3)\3)\3)\3)\5)\u01ca\n)\3*\3*\3*\3*\5*\u01d0\n")
        buf.write("*\3+\3+\3+\5+\u01d5\n+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u01f7\n-\3.\3.\5.\u01fb\n.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\5\62\u020f\n\62\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\64\3\65\3\65\3\65\3\65\5\65\u021b\n\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0227\n")
        buf.write("\66\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\39\59")
        buf.write("\u0236\n9\3:\3:\5:\u023a\n:\3;\3;\3;\3;\3;\3<\3<\5<\u0243")
        buf.write("\n<\3=\3=\3=\3=\3=\5=\u024a\n=\3>\3>\3>\3>\3?\3?\5?\u0252")
        buf.write("\n?\3@\3@\3A\3A\3A\3A\3A\3A\3A\5A\u025d\nA\3B\3B\3B\2")
        buf.write("\t\f\16\20\22\24\30 C\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\u0080\u0082\2\5\3\2\37 \3\2\17\22\3\3//\2")
        buf.write("\u026b\2\u0084\3\2\2\2\4\u008b\3\2\2\2\6\u008f\3\2\2\2")
        buf.write("\b\u0097\3\2\2\2\n\u00a0\3\2\2\2\f\u00a2\3\2\2\2\16\u00ad")
        buf.write("\3\2\2\2\20\u00b8\3\2\2\2\22\u00c3\3\2\2\2\24\u00d1\3")
        buf.write("\2\2\2\26\u00e7\3\2\2\2\30\u00e9\3\2\2\2\32\u0104\3\2")
        buf.write("\2\2\34\u0108\3\2\2\2\36\u010f\3\2\2\2 \u0111\3\2\2\2")
        buf.write("\"\u0121\3\2\2\2$\u0138\3\2\2\2&\u013a\3\2\2\2(\u014e")
        buf.write("\3\2\2\2*\u0154\3\2\2\2,\u0156\3\2\2\2.\u015a\3\2\2\2")
        buf.write("\60\u0166\3\2\2\2\62\u016c\3\2\2\2\64\u0173\3\2\2\2\66")
        buf.write("\u0175\3\2\2\28\u0178\3\2\2\2:\u0181\3\2\2\2<\u0183\3")
        buf.write("\2\2\2>\u0189\3\2\2\2@\u0191\3\2\2\2B\u01a0\3\2\2\2D\u01a2")
        buf.write("\3\2\2\2F\u01a8\3\2\2\2H\u01b0\3\2\2\2J\u01b2\3\2\2\2")
        buf.write("L\u01b9\3\2\2\2N\u01be\3\2\2\2P\u01c4\3\2\2\2R\u01cf\3")
        buf.write("\2\2\2T\u01d4\3\2\2\2V\u01d6\3\2\2\2X\u01f6\3\2\2\2Z\u01fa")
        buf.write("\3\2\2\2\\\u01fc\3\2\2\2^\u01ff\3\2\2\2`\u0202\3\2\2\2")
        buf.write("b\u020e\3\2\2\2d\u0210\3\2\2\2f\u0212\3\2\2\2h\u021a\3")
        buf.write("\2\2\2j\u0226\3\2\2\2l\u0228\3\2\2\2n\u022c\3\2\2\2p\u0235")
        buf.write("\3\2\2\2r\u0239\3\2\2\2t\u023b\3\2\2\2v\u0242\3\2\2\2")
        buf.write("x\u0249\3\2\2\2z\u024b\3\2\2\2|\u0251\3\2\2\2~\u0253\3")
        buf.write("\2\2\2\u0080\u025c\3\2\2\2\u0082\u025e\3\2\2\2\u0084\u0085")
        buf.write("\5\4\3\2\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u0088")
        buf.write("\5\6\4\2\u0088\u0089\5\4\3\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u008c\5\6\4\2\u008b\u0087\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\5\3\2\2\2\u008d\u0090\5\b\5\2\u008e\u0090\5\n\6")
        buf.write("\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\7\3\2")
        buf.write("\2\2\u0091\u0098\5$\23\2\u0092\u0098\5(\25\2\u0093\u0098")
        buf.write("\5&\24\2\u0094\u0098\5.\30\2\u0095\u0098\5<\37\2\u0096")
        buf.write("\u0098\5D#\2\u0097\u0091\3\2\2\2\u0097\u0092\3\2\2\2\u0097")
        buf.write("\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\t\3\2\2\2\u0099\u00a1\5\"\22")
        buf.write("\2\u009a\u00a1\5L\'\2\u009b\u00a1\5X-\2\u009c\u00a1\5")
        buf.write("^\60\2\u009d\u00a1\5\\/\2\u009e\u00a1\5`\61\2\u009f\u00a1")
        buf.write("\5b\62\2\u00a0\u0099\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0")
        buf.write("\u009b\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0\u009d\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\13\3\2")
        buf.write("\2\2\u00a2\u00a3\b\7\1\2\u00a3\u00a4\5\16\b\2\u00a4\u00aa")
        buf.write("\3\2\2\2\u00a5\u00a6\f\4\2\2\u00a6\u00a7\7\35\2\2\u00a7")
        buf.write("\u00a9\5\16\b\2\u00a8\u00a5\3\2\2\2\u00a9\u00ac\3\2\2")
        buf.write("\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\r\3\2")
        buf.write("\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\b\1\2\u00ae\u00af")
        buf.write("\5\20\t\2\u00af\u00b5\3\2\2\2\u00b0\u00b1\f\4\2\2\u00b1")
        buf.write("\u00b2\7\34\2\2\u00b2\u00b4\5\20\t\2\u00b3\u00b0\3\2\2")
        buf.write("\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\17\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9")
        buf.write("\b\t\1\2\u00b9\u00ba\5\22\n\2\u00ba\u00c0\3\2\2\2\u00bb")
        buf.write("\u00bc\f\4\2\2\u00bc\u00bd\7\33\2\2\u00bd\u00bf\5\22\n")
        buf.write("\2\u00be\u00bb\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\21\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c3\u00c4\b\n\1\2\u00c4\u00c5\5\24\13\2\u00c5")
        buf.write("\u00ce\3\2\2\2\u00c6\u00c7\f\5\2\2\u00c7\u00c8\7#\2\2")
        buf.write("\u00c8\u00cd\5\24\13\2\u00c9\u00ca\f\4\2\2\u00ca\u00cb")
        buf.write("\7$\2\2\u00cb\u00cd\5\24\13\2\u00cc\u00c6\3\2\2\2\u00cc")
        buf.write("\u00c9\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\23\3\2\2\2\u00d0\u00ce\3\2")
        buf.write("\2\2\u00d1\u00d2\b\13\1\2\u00d2\u00d3\5\26\f\2\u00d3\u00df")
        buf.write("\3\2\2\2\u00d4\u00d5\f\6\2\2\u00d5\u00d6\7%\2\2\u00d6")
        buf.write("\u00de\5\26\f\2\u00d7\u00d8\f\5\2\2\u00d8\u00d9\7&\2\2")
        buf.write("\u00d9\u00de\5\26\f\2\u00da\u00db\f\4\2\2\u00db\u00dc")
        buf.write("\7\'\2\2\u00dc\u00de\5\26\f\2\u00dd\u00d4\3\2\2\2\u00dd")
        buf.write("\u00d7\3\2\2\2\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\25\3\2")
        buf.write("\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7\36\2\2\u00e3\u00e8")
        buf.write("\5\30\r\2\u00e4\u00e5\7$\2\2\u00e5\u00e8\5\30\r\2\u00e6")
        buf.write("\u00e8\5\30\r\2\u00e7\u00e2\3\2\2\2\u00e7\u00e4\3\2\2")
        buf.write("\2\u00e7\u00e6\3\2\2\2\u00e8\27\3\2\2\2\u00e9\u00ea\b")
        buf.write("\r\1\2\u00ea\u00eb\5\32\16\2\u00eb\u00fb\3\2\2\2\u00ec")
        buf.write("\u00ed\f\6\2\2\u00ed\u00ee\7!\2\2\u00ee\u00fa\7\64\2\2")
        buf.write("\u00ef\u00f0\f\5\2\2\u00f0\u00f1\7*\2\2\u00f1\u00f2\5")
        buf.write("\f\7\2\u00f2\u00f3\7+\2\2\u00f3\u00fa\3\2\2\2\u00f4\u00f5")
        buf.write("\f\4\2\2\u00f5\u00f6\7(\2\2\u00f6\u00f7\5\34\17\2\u00f7")
        buf.write("\u00f8\7)\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00ec\3\2\2\2")
        buf.write("\u00f9\u00ef\3\2\2\2\u00f9\u00f4\3\2\2\2\u00fa\u00fd\3")
        buf.write("\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\31")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7(\2\2\u00ff")
        buf.write("\u0100\5\f\7\2\u0100\u0101\7)\2\2\u0101\u0105\3\2\2\2")
        buf.write("\u0102\u0105\7\64\2\2\u0103\u0105\5\u0080A\2\u0104\u00fe")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105")
        buf.write("\33\3\2\2\2\u0106\u0109\5\36\20\2\u0107\u0109\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\35\3\2")
        buf.write("\2\2\u010a\u010b\5\f\7\2\u010b\u010c\7.\2\2\u010c\u010d")
        buf.write("\5\36\20\2\u010d\u0110\3\2\2\2\u010e\u0110\5\f\7\2\u010f")
        buf.write("\u010a\3\2\2\2\u010f\u010e\3\2\2\2\u0110\37\3\2\2\2\u0111")
        buf.write("\u0112\b\21\1\2\u0112\u0113\7\64\2\2\u0113\u011e\3\2\2")
        buf.write("\2\u0114\u0115\f\5\2\2\u0115\u0116\7!\2\2\u0116\u011d")
        buf.write("\7\64\2\2\u0117\u0118\f\4\2\2\u0118\u0119\7*\2\2\u0119")
        buf.write("\u011a\5\f\7\2\u011a\u011b\7+\2\2\u011b\u011d\3\2\2\2")
        buf.write("\u011c\u0114\3\2\2\2\u011c\u0117\3\2\2\2\u011d\u0120\3")
        buf.write("\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f!")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\5 \21\2\u0122")
        buf.write("\u0123\5d\63\2\u0123\u0124\5\f\7\2\u0124\u0125\5\u0082")
        buf.write("B\2\u0125#\3\2\2\2\u0126\u0127\7\24\2\2\u0127\u0128\7")
        buf.write("\64\2\2\u0128\u0129\5|?\2\u0129\u012a\5\u0082B\2\u012a")
        buf.write("\u0139\3\2\2\2\u012b\u012c\7\24\2\2\u012c\u012d\7\64\2")
        buf.write("\2\u012d\u012e\7\"\2\2\u012e\u012f\5\f\7\2\u012f\u0130")
        buf.write("\5\u0082B\2\u0130\u0139\3\2\2\2\u0131\u0132\7\24\2\2\u0132")
        buf.write("\u0133\7\64\2\2\u0133\u0134\5|?\2\u0134\u0135\7\"\2\2")
        buf.write("\u0135\u0136\5\f\7\2\u0136\u0137\5\u0082B\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u0126\3\2\2\2\u0138\u012b\3\2\2\2\u0138")
        buf.write("\u0131\3\2\2\2\u0139%\3\2\2\2\u013a\u013b\7\23\2\2\u013b")
        buf.write("\u013c\7\64\2\2\u013c\u013d\7\"\2\2\u013d\u013e\5\f\7")
        buf.write("\2\u013e\u013f\5\u0082B\2\u013f\'\3\2\2\2\u0140\u0141")
        buf.write("\7\24\2\2\u0141\u0142\7\64\2\2\u0142\u0143\5*\26\2\u0143")
        buf.write("\u0144\5|?\2\u0144\u0145\5\u0082B\2\u0145\u014f\3\2\2")
        buf.write("\2\u0146\u0147\7\24\2\2\u0147\u0148\7\64\2\2\u0148\u0149")
        buf.write("\5*\26\2\u0149\u014a\5|?\2\u014a\u014b\7\"\2\2\u014b\u014c")
        buf.write("\5l\67\2\u014c\u014d\5\u0082B\2\u014d\u014f\3\2\2\2\u014e")
        buf.write("\u0140\3\2\2\2\u014e\u0146\3\2\2\2\u014f)\3\2\2\2\u0150")
        buf.write("\u0151\5,\27\2\u0151\u0152\5*\26\2\u0152\u0155\3\2\2\2")
        buf.write("\u0153\u0155\5,\27\2\u0154\u0150\3\2\2\2\u0154\u0153\3")
        buf.write("\2\2\2\u0155+\3\2\2\2\u0156\u0157\7*\2\2\u0157\u0158\5")
        buf.write("\f\7\2\u0158\u0159\7+\2\2\u0159-\3\2\2\2\u015a\u015c\7")
        buf.write("\13\2\2\u015b\u015d\58\35\2\u015c\u015b\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\7\64\2")
        buf.write("\2\u015f\u0161\5\60\31\2\u0160\u0162\5|?\2\u0161\u0160")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0164\5f\64\2\u0164\u0165\5\u0082B\2\u0165/\3\2\2\2\u0166")
        buf.write("\u0167\7(\2\2\u0167\u0168\5\62\32\2\u0168\u0169\7)\2\2")
        buf.write("\u0169\61\3\2\2\2\u016a\u016d\5\64\33\2\u016b\u016d\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d\63")
        buf.write("\3\2\2\2\u016e\u016f\5\66\34\2\u016f\u0170\7.\2\2\u0170")
        buf.write("\u0171\5\64\33\2\u0171\u0174\3\2\2\2\u0172\u0174\5\66")
        buf.write("\34\2\u0173\u016e\3\2\2\2\u0173\u0172\3\2\2\2\u0174\65")
        buf.write("\3\2\2\2\u0175\u0176\5:\36\2\u0176\u0177\5|?\2\u0177\67")
        buf.write("\3\2\2\2\u0178\u0179\7(\2\2\u0179\u017a\7\64\2\2\u017a")
        buf.write("\u017b\7\64\2\2\u017b\u017c\7)\2\2\u017c9\3\2\2\2\u017d")
        buf.write("\u017e\7\64\2\2\u017e\u017f\7.\2\2\u017f\u0182\5:\36\2")
        buf.write("\u0180\u0182\7\64\2\2\u0181\u017d\3\2\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182;\3\2\2\2\u0183\u0184\7\f\2\2\u0184\u0185")
        buf.write("\7\64\2\2\u0185\u0186\7\r\2\2\u0186\u0187\5> \2\u0187")
        buf.write("\u0188\5\u0082B\2\u0188=\3\2\2\2\u0189\u018a\7,\2\2\u018a")
        buf.write("\u018b\5@!\2\u018b\u018c\7-\2\2\u018c?\3\2\2\2\u018d\u018e")
        buf.write("\5B\"\2\u018e\u018f\5@!\2\u018f\u0192\3\2\2\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("A\3\2\2\2\u0193\u0194\7\64\2\2\u0194\u0196\5|?\2\u0195")
        buf.write("\u0197\5*\26\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u0199\5\u0082B\2\u0199\u01a1")
        buf.write("\3\2\2\2\u019a\u019b\7\64\2\2\u019b\u019c\7\64\2\2\u019c")
        buf.write("\u01a1\5\u0082B\2\u019d\u019e\7\64\2\2\u019e\u019f\7\16")
        buf.write("\2\2\u019f\u01a1\5\u0082B\2\u01a0\u0193\3\2\2\2\u01a0")
        buf.write("\u019a\3\2\2\2\u01a0\u019d\3\2\2\2\u01a1C\3\2\2\2\u01a2")
        buf.write("\u01a3\7\f\2\2\u01a3\u01a4\7\64\2\2\u01a4\u01a5\7\16\2")
        buf.write("\2\u01a5\u01a6\5F$\2\u01a6\u01a7\5\u0082B\2\u01a7E\3\2")
        buf.write("\2\2\u01a8\u01a9\7,\2\2\u01a9\u01aa\5H%\2\u01aa\u01ab")
        buf.write("\7-\2\2\u01abG\3\2\2\2\u01ac\u01ad\5J&\2\u01ad\u01ae\5")
        buf.write("H%\2\u01ae\u01b1\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ac")
        buf.write("\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1I\3\2\2\2\u01b2\u01b3")
        buf.write("\7\64\2\2\u01b3\u01b5\5\60\31\2\u01b4\u01b6\5|?\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\5\u0082B\2\u01b8K\3\2\2\2\u01b9\u01ba\5N")
        buf.write("(\2\u01ba\u01bb\5R*\2\u01bb\u01bc\5T+\2\u01bc\u01bd\5")
        buf.write("\u0082B\2\u01bdM\3\2\2\2\u01be\u01bf\7\7\2\2\u01bf\u01c0")
        buf.write("\5V,\2\u01c0\u01c2\5f\64\2\u01c1\u01c3\5\u0082B\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3O\3\2\2\2\u01c4")
        buf.write("\u01c5\7\b\2\2\u01c5\u01c6\7\7\2\2\u01c6\u01c7\5V,\2\u01c7")
        buf.write("\u01c9\5f\64\2\u01c8\u01ca\5\u0082B\2\u01c9\u01c8\3\2")
        buf.write("\2\2\u01c9\u01ca\3\2\2\2\u01caQ\3\2\2\2\u01cb\u01cc\5")
        buf.write("P)\2\u01cc\u01cd\5R*\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0")
        buf.write("\3\2\2\2\u01cf\u01cb\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0")
        buf.write("S\3\2\2\2\u01d1\u01d2\7\b\2\2\u01d2\u01d5\5f\64\2\u01d3")
        buf.write("\u01d5\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5U\3\2\2\2\u01d6\u01d7\7(\2\2\u01d7\u01d8\5\f\7\2")
        buf.write("\u01d8\u01d9\7)\2\2\u01d9W\3\2\2\2\u01da\u01db\7\t\2\2")
        buf.write("\u01db\u01dc\5\f\7\2\u01dc\u01dd\5f\64\2\u01dd\u01de\5")
        buf.write("\u0082B\2\u01de\u01f7\3\2\2\2\u01df\u01e0\7\t\2\2\u01e0")
        buf.write("\u01e1\7\64\2\2\u01e1\u01e2\7 \2\2\u01e2\u01e3\5\f\7\2")
        buf.write("\u01e3\u01e4\7/\2\2\u01e4\u01e5\5\f\7\2\u01e5\u01e6\7")
        buf.write("/\2\2\u01e6\u01e7\7\64\2\2\u01e7\u01e8\7\37\2\2\u01e8")
        buf.write("\u01e9\5\f\7\2\u01e9\u01ea\5f\64\2\u01ea\u01eb\5\u0082")
        buf.write("B\2\u01eb\u01f7\3\2\2\2\u01ec\u01ed\7\t\2\2\u01ed\u01ee")
        buf.write("\7\64\2\2\u01ee\u01ef\7.\2\2\u01ef\u01f0\7\64\2\2\u01f0")
        buf.write("\u01f1\7 \2\2\u01f1\u01f2\7\27\2\2\u01f2\u01f3\5Z.\2\u01f3")
        buf.write("\u01f4\5f\64\2\u01f4\u01f5\5\u0082B\2\u01f5\u01f7\3\2")
        buf.write("\2\2\u01f6\u01da\3\2\2\2\u01f6\u01df\3\2\2\2\u01f6\u01ec")
        buf.write("\3\2\2\2\u01f7Y\3\2\2\2\u01f8\u01fb\7\64\2\2\u01f9\u01fb")
        buf.write("\5l\67\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb")
        buf.write("[\3\2\2\2\u01fc\u01fd\7\26\2\2\u01fd\u01fe\5\u0082B\2")
        buf.write("\u01fe]\3\2\2\2\u01ff\u0200\7\25\2\2\u0200\u0201\5\u0082")
        buf.write("B\2\u0201_\3\2\2\2\u0202\u0203\5\30\r\2\u0203\u0204\7")
        buf.write("(\2\2\u0204\u0205\5\34\17\2\u0205\u0206\7)\2\2\u0206\u0207")
        buf.write("\5\u0082B\2\u0207a\3\2\2\2\u0208\u0209\7\n\2\2\u0209\u020f")
        buf.write("\5\u0082B\2\u020a\u020b\7\n\2\2\u020b\u020c\5\f\7\2\u020c")
        buf.write("\u020d\5\u0082B\2\u020d\u020f\3\2\2\2\u020e\u0208\3\2")
        buf.write("\2\2\u020e\u020a\3\2\2\2\u020fc\3\2\2\2\u0210\u0211\t")
        buf.write("\2\2\2\u0211e\3\2\2\2\u0212\u0213\7,\2\2\u0213\u0214\5")
        buf.write("h\65\2\u0214\u0215\7-\2\2\u0215g\3\2\2\2\u0216\u0217\5")
        buf.write("j\66\2\u0217\u0218\5h\65\2\u0218\u021b\3\2\2\2\u0219\u021b")
        buf.write("\3\2\2\2\u021a\u0216\3\2\2\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("i\3\2\2\2\u021c\u0227\5\"\22\2\u021d\u0227\5$\23\2\u021e")
        buf.write("\u0227\5(\25\2\u021f\u0227\5&\24\2\u0220\u0227\5L\'\2")
        buf.write("\u0221\u0227\5X-\2\u0222\u0227\5^\60\2\u0223\u0227\5\\")
        buf.write("/\2\u0224\u0227\5`\61\2\u0225\u0227\5b\62\2\u0226\u021c")
        buf.write("\3\2\2\2\u0226\u021d\3\2\2\2\u0226\u021e\3\2\2\2\u0226")
        buf.write("\u021f\3\2\2\2\u0226\u0220\3\2\2\2\u0226\u0221\3\2\2\2")
        buf.write("\u0226\u0222\3\2\2\2\u0226\u0223\3\2\2\2\u0226\u0224\3")
        buf.write("\2\2\2\u0226\u0225\3\2\2\2\u0227k\3\2\2\2\u0228\u0229")
        buf.write("\5*\26\2\u0229\u022a\5|?\2\u022a\u022b\5n8\2\u022bm\3")
        buf.write("\2\2\2\u022c\u022d\7,\2\2\u022d\u022e\5p9\2\u022e\u022f")
        buf.write("\7-\2\2\u022fo\3\2\2\2\u0230\u0231\5r:\2\u0231\u0232\7")
        buf.write(".\2\2\u0232\u0233\5p9\2\u0233\u0236\3\2\2\2\u0234\u0236")
        buf.write("\5r:\2\u0235\u0230\3\2\2\2\u0235\u0234\3\2\2\2\u0236q")
        buf.write("\3\2\2\2\u0237\u023a\5\f\7\2\u0238\u023a\5n8\2\u0239\u0237")
        buf.write("\3\2\2\2\u0239\u0238\3\2\2\2\u023as\3\2\2\2\u023b\u023c")
        buf.write("\7\64\2\2\u023c\u023d\7,\2\2\u023d\u023e\5v<\2\u023e\u023f")
        buf.write("\7-\2\2\u023fu\3\2\2\2\u0240\u0243\5x=\2\u0241\u0243\3")
        buf.write("\2\2\2\u0242\u0240\3\2\2\2\u0242\u0241\3\2\2\2\u0243w")
        buf.write("\3\2\2\2\u0244\u0245\5z>\2\u0245\u0246\7.\2\2\u0246\u0247")
        buf.write("\5x=\2\u0247\u024a\3\2\2\2\u0248\u024a\5z>\2\u0249\u0244")
        buf.write("\3\2\2\2\u0249\u0248\3\2\2\2\u024ay\3\2\2\2\u024b\u024c")
        buf.write("\7\64\2\2\u024c\u024d\7\60\2\2\u024d\u024e\5\u0080A\2")
        buf.write("\u024e{\3\2\2\2\u024f\u0252\5~@\2\u0250\u0252\7\64\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252}\3\2\2")
        buf.write("\2\u0253\u0254\t\3\2\2\u0254\177\3\2\2\2\u0255\u025d\7")
        buf.write("\62\2\2\u0256\u025d\7\61\2\2\u0257\u025d\7\63\2\2\u0258")
        buf.write("\u025d\7\31\2\2\u0259\u025d\7\32\2\2\u025a\u025d\5t;\2")
        buf.write("\u025b\u025d\5l\67\2\u025c\u0255\3\2\2\2\u025c\u0256\3")
        buf.write("\2\2\2\u025c\u0257\3\2\2\2\u025c\u0258\3\2\2\2\u025c\u0259")
        buf.write("\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d")
        buf.write("\u0081\3\2\2\2\u025e\u025f\t\4\2\2\u025f\u0083\3\2\2\2")
        buf.write("\61\u008b\u008f\u0097\u00a0\u00aa\u00b5\u00c0\u00cc\u00ce")
        buf.write("\u00dd\u00df\u00e7\u00f9\u00fb\u0104\u0108\u010f\u011c")
        buf.write("\u011e\u0138\u014e\u0154\u015c\u0161\u016c\u0173\u0181")
        buf.write("\u0191\u0196\u01a0\u01b0\u01b5\u01c2\u01c9\u01cf\u01d4")
        buf.write("\u01f6\u01fa\u020e\u021a\u0226\u0235\u0239\u0242\u0249")
        buf.write("\u0251\u025c")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "'&&'", "'||'", "'!'", "<INVALID>", 
                     "':='", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
                      "AND", "OR", "NOT", "UPT_ASSIGN", "ASSIGN", "DOT", 
                      "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", "LP", 
                      "RP", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                      "COLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl_stmtlst = 1
    RULE_decl_stmt = 2
    RULE_decl = 3
    RULE_stmt = 4
    RULE_expr = 5
    RULE_expr1 = 6
    RULE_expr2 = 7
    RULE_expr3 = 8
    RULE_expr4 = 9
    RULE_expr5 = 10
    RULE_expr6 = 11
    RULE_expr7 = 12
    RULE_exprlst = 13
    RULE_exprlstprime = 14
    RULE_lhs = 15
    RULE_assigning = 16
    RULE_vardecl = 17
    RULE_constdecl = 18
    RULE_arraydecl = 19
    RULE_arridxlst = 20
    RULE_arridx = 21
    RULE_funcdecl = 22
    RULE_funcparam = 23
    RULE_paramlst = 24
    RULE_paramlstprime = 25
    RULE_param = 26
    RULE_receiver = 27
    RULE_idlst = 28
    RULE_structdecl = 29
    RULE_structfield = 30
    RULE_fielddecllst = 31
    RULE_fielddecl = 32
    RULE_interfdecl = 33
    RULE_interfmeth = 34
    RULE_interfmethlst = 35
    RULE_interfmethmem = 36
    RULE_ifelse_stat = 37
    RULE_if_ = 38
    RULE_elseif_ = 39
    RULE_elseif_lst = 40
    RULE_else_ = 41
    RULE_condition = 42
    RULE_forloop_stat = 43
    RULE_id__arr = 44
    RULE_break_stat = 45
    RULE_continue_stat = 46
    RULE_funccall_stat = 47
    RULE_return_stat = 48
    RULE_assign = 49
    RULE_blockcode = 50
    RULE_blockcodestmtlst = 51
    RULE_blockcodestmt = 52
    RULE_arr_literal = 53
    RULE_arrelemlst = 54
    RULE_arreleml = 55
    RULE_arrelem = 56
    RULE_struct_literal = 57
    RULE_structparamlst = 58
    RULE_structparamlstprime = 59
    RULE_structparam = 60
    RULE_data_type = 61
    RULE_primitive_datatype = 62
    RULE_literal = 63
    RULE_end_stm = 64

    ruleNames =  [ "program", "decl_stmtlst", "decl_stmt", "decl", "stmt", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "exprlst", "exprlstprime", "lhs", "assigning", 
                   "vardecl", "constdecl", "arraydecl", "arridxlst", "arridx", 
                   "funcdecl", "funcparam", "paramlst", "paramlstprime", 
                   "param", "receiver", "idlst", "structdecl", "structfield", 
                   "fielddecllst", "fielddecl", "interfdecl", "interfmeth", 
                   "interfmethlst", "interfmethmem", "ifelse_stat", "if_", 
                   "elseif_", "elseif_lst", "else_", "condition", "forloop_stat", 
                   "id__arr", "break_stat", "continue_stat", "funccall_stat", 
                   "return_stat", "assign", "blockcode", "blockcodestmtlst", 
                   "blockcodestmt", "arr_literal", "arrelemlst", "arreleml", 
                   "arrelem", "struct_literal", "structparamlst", "structparamlstprime", 
                   "structparam", "data_type", "primitive_datatype", "literal", 
                   "end_stm" ]

    EOF = Token.EOF
    SINGLE_LINE_CMT=1
    MULTI_LINE_CMT=2
    NL=3
    WS=4
    IF_=5
    ELSE_=6
    FOR_=7
    RETURN_=8
    FUNC_=9
    TYPE_=10
    STRUCT_=11
    INTERFACE_=12
    STRING_=13
    INT_=14
    FLOAT_=15
    BOOLEAN_=16
    CONST_=17
    VAR_=18
    CONTINUE_=19
    BREAK_=20
    RANGE_=21
    NIL_=22
    TRUE_=23
    FALSE_=24
    COMPARISON_OP=25
    AND=26
    OR=27
    NOT=28
    UPT_ASSIGN=29
    ASSIGN=30
    DOT=31
    EQUAL=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    LP=38
    RP=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    COMMA=44
    SEMICOLON=45
    COLON=46
    FLOAT=47
    INTEGER=48
    STRING=49
    ID=50
    ERROR_CHAR=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtlstContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.decl_stmtlst()
            self.state = 131
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtContext,0)


        def decl_stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmtlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmtlst" ):
                return visitor.visitDecl_stmtlst(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmtlst(self):

        localctx = MiniGoParser.Decl_stmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_stmtlst)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.decl_stmt()
                self.state = 134
                self.decl_stmtlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.decl_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_stmt)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC_, MiniGoParser.TYPE_, MiniGoParser.CONST_, MiniGoParser.VAR_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.decl()
                pass
            elif token in [MiniGoParser.IF_, MiniGoParser.FOR_, MiniGoParser.RETURN_, MiniGoParser.CONTINUE_, MiniGoParser.BREAK_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfdecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.arraydecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.constdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.funcdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.structdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.interfdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def ifelse_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_statContext,0)


        def forloop_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statContext,0)


        def funccall_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.ifelse_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.forloop_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.continue_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.break_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.funccall_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 157
                self.return_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    self.match(MiniGoParser.OR)
                    self.state = 165
                    self.expr1(0) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    self.match(MiniGoParser.AND)
                    self.state = 176
                    self.expr2(0) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def COMPARISON_OP(self):
            return self.getToken(MiniGoParser.COMPARISON_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    self.match(MiniGoParser.COMPARISON_OP)
                    self.state = 187
                    self.expr3(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 196
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 197
                        self.match(MiniGoParser.ADD)
                        self.state = 198
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        self.match(MiniGoParser.SUB)
                        self.state = 201
                        self.expr4(0)
                        pass

             
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 210
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 211
                        self.match(MiniGoParser.MUL)
                        self.state = 212
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 213
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 214
                        self.match(MiniGoParser.DIV)
                        self.state = 215
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 216
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 217
                        self.match(MiniGoParser.MOD)
                        self.state = 218
                        self.expr5()
                        pass

             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr5)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.NOT)
                self.state = 225
                self.expr6(0)
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.SUB)
                self.state = 227
                self.expr6(0)
                pass
            elif token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 247
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 234
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 235
                        self.match(MiniGoParser.DOT)
                        self.state = 236
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 237
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 238
                        self.match(MiniGoParser.LSB)
                        self.state = 239
                        self.expr(0)
                        self.state = 240
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 242
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 243
                        self.match(MiniGoParser.LP)
                        self.state = 244
                        self.exprlst()
                        self.state = 245
                        self.match(MiniGoParser.RP)
                        pass

             
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr7)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MiniGoParser.LP)
                self.state = 253
                self.expr(0)
                self.state = 254
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlst" ):
                return visitor.visitExprlst(self)
            else:
                return visitor.visitChildren(self)




    def exprlst(self):

        localctx = MiniGoParser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprlst)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.exprlstprime()
                pass
            elif token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def exprlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlstprime" ):
                return visitor.visitExprlstprime(self)
            else:
                return visitor.visitChildren(self)




    def exprlstprime(self):

        localctx = MiniGoParser.ExprlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprlstprime)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expr(0)
                self.state = 265
                self.match(MiniGoParser.COMMA)
                self.state = 266
                self.exprlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 282
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 274
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 275
                        self.match(MiniGoParser.DOT)
                        self.state = 276
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 277
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 278
                        self.match(MiniGoParser.LSB)
                        self.state = 279
                        self.expr(0)
                        self.state = 280
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssigningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigning" ):
                return visitor.visitAssigning(self)
            else:
                return visitor.visitChildren(self)




    def assigning(self):

        localctx = MiniGoParser.AssigningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.lhs(0)
            self.state = 288
            self.assign()
            self.state = 289
            self.expr(0)
            self.state = 290
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vardecl)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(MiniGoParser.VAR_)
                self.state = 293
                self.match(MiniGoParser.ID)
                self.state = 294
                self.data_type()
                self.state = 295
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(MiniGoParser.VAR_)
                self.state = 298
                self.match(MiniGoParser.ID)
                self.state = 299
                self.match(MiniGoParser.EQUAL)
                self.state = 300
                self.expr(0)
                self.state = 301
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(MiniGoParser.VAR_)
                self.state = 304
                self.match(MiniGoParser.ID)
                self.state = 305
                self.data_type()
                self.state = 306
                self.match(MiniGoParser.EQUAL)
                self.state = 307
                self.expr(0)
                self.state = 308
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_(self):
            return self.getToken(MiniGoParser.CONST_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MiniGoParser.CONST_)
            self.state = 313
            self.match(MiniGoParser.ID)
            self.state = 314
            self.match(MiniGoParser.EQUAL)
            self.state = 315
            self.expr(0)
            self.state = 316
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(MiniGoParser.VAR_)
                self.state = 319
                self.match(MiniGoParser.ID)
                self.state = 320
                self.arridxlst()
                self.state = 321
                self.data_type()
                self.state = 322
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.VAR_)
                self.state = 325
                self.match(MiniGoParser.ID)
                self.state = 326
                self.arridxlst()
                self.state = 327
                self.data_type()
                self.state = 328
                self.match(MiniGoParser.EQUAL)
                self.state = 329
                self.arr_literal()
                self.state = 330
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArridxlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridxlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArridxlst" ):
                return visitor.visitArridxlst(self)
            else:
                return visitor.visitChildren(self)




    def arridxlst(self):

        localctx = MiniGoParser.ArridxlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arridxlst)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.arridx()
                self.state = 335
                self.arridxlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.arridx()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArridxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArridx" ):
                return visitor.visitArridx(self)
            else:
                return visitor.visitChildren(self)




    def arridx(self):

        localctx = MiniGoParser.ArridxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.LSB)
            self.state = 341
            self.expr(0)
            self.state = 342
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_(self):
            return self.getToken(MiniGoParser.FUNC_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcparam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncparamContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.FUNC_)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LP:
                self.state = 345
                self.receiver()


            self.state = 348
            self.match(MiniGoParser.ID)
            self.state = 349
            self.funcparam()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 350
                self.data_type()


            self.state = 353
            self.blockcode()
            self.state = 354
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def paramlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcparam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncparam" ):
                return visitor.visitFuncparam(self)
            else:
                return visitor.visitChildren(self)




    def funcparam(self):

        localctx = MiniGoParser.FuncparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(MiniGoParser.LP)
            self.state = 357
            self.paramlst()
            self.state = 358
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlst" ):
                return visitor.visitParamlst(self)
            else:
                return visitor.visitChildren(self)




    def paramlst(self):

        localctx = MiniGoParser.ParamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_paramlst)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.paramlstprime()
                pass
            elif token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlstprime" ):
                return visitor.visitParamlstprime(self)
            else:
                return visitor.visitChildren(self)




    def paramlstprime(self):

        localctx = MiniGoParser.ParamlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_paramlstprime)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.param()
                self.state = 365
                self.match(MiniGoParser.COMMA)
                self.state = 366
                self.paramlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlst(self):
            return self.getTypedRuleContext(MiniGoParser.IdlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.idlst()
            self.state = 372
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MiniGoParser.LP)
            self.state = 375
            self.match(MiniGoParser.ID)
            self.state = 376
            self.match(MiniGoParser.ID)
            self.state = 377
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def idlst(self):
            return self.getTypedRuleContext(MiniGoParser.IdlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlst" ):
                return visitor.visitIdlst(self)
            else:
                return visitor.visitChildren(self)




    def idlst(self):

        localctx = MiniGoParser.IdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_idlst)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(MiniGoParser.ID)
                self.state = 380
                self.match(MiniGoParser.COMMA)
                self.state = 381
                self.idlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT_(self):
            return self.getToken(MiniGoParser.STRUCT_, 0)

        def structfield(self):
            return self.getTypedRuleContext(MiniGoParser.StructfieldContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.TYPE_)
            self.state = 386
            self.match(MiniGoParser.ID)
            self.state = 387
            self.match(MiniGoParser.STRUCT_)
            self.state = 388
            self.structfield()
            self.state = 389
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def fielddecllst(self):
            return self.getTypedRuleContext(MiniGoParser.FielddecllstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structfield

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfield" ):
                return visitor.visitStructfield(self)
            else:
                return visitor.visitChildren(self)




    def structfield(self):

        localctx = MiniGoParser.StructfieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MiniGoParser.LCB)
            self.state = 392
            self.fielddecllst()
            self.state = 393
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddecllstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self):
            return self.getTypedRuleContext(MiniGoParser.FielddeclContext,0)


        def fielddecllst(self):
            return self.getTypedRuleContext(MiniGoParser.FielddecllstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecllst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecllst" ):
                return visitor.visitFielddecllst(self)
            else:
                return visitor.visitChildren(self)




    def fielddecllst(self):

        localctx = MiniGoParser.FielddecllstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_fielddecllst)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.fielddecl()
                self.state = 396
                self.fielddecllst()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.ID)
                self.state = 402
                self.data_type()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 403
                    self.arridxlst()


                self.state = 406
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(MiniGoParser.ID)
                self.state = 409
                self.match(MiniGoParser.ID)
                self.state = 410
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.match(MiniGoParser.ID)
                self.state = 412
                self.match(MiniGoParser.INTERFACE_)
                self.state = 413
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

        def interfmeth(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfdecl" ):
                return visitor.visitInterfdecl(self)
            else:
                return visitor.visitChildren(self)




    def interfdecl(self):

        localctx = MiniGoParser.InterfdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_interfdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.TYPE_)
            self.state = 417
            self.match(MiniGoParser.ID)
            self.state = 418
            self.match(MiniGoParser.INTERFACE_)
            self.state = 419
            self.interfmeth()
            self.state = 420
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfmethContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def interfmethlst(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmeth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfmeth" ):
                return visitor.visitInterfmeth(self)
            else:
                return visitor.visitChildren(self)




    def interfmeth(self):

        localctx = MiniGoParser.InterfmethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.LCB)
            self.state = 423
            self.interfmethlst()
            self.state = 424
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfmethlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfmethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethmemContext,0)


        def interfmethlst(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmethlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfmethlst" ):
                return visitor.visitInterfmethlst(self)
            else:
                return visitor.visitChildren(self)




    def interfmethlst(self):

        localctx = MiniGoParser.InterfmethlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_interfmethlst)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.interfmethmem()
                self.state = 427
                self.interfmethlst()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfmethmemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcparam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncparamContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmethmem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfmethmem" ):
                return visitor.visitInterfmethmem(self)
            else:
                return visitor.visitChildren(self)




    def interfmethmem(self):

        localctx = MiniGoParser.InterfmethmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.ID)
            self.state = 433
            self.funcparam()
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 434
                self.data_type()


            self.state = 437
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelse_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(MiniGoParser.If_Context,0)


        def elseif_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_lstContext,0)


        def else_(self):
            return self.getTypedRuleContext(MiniGoParser.Else_Context,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse_stat" ):
                return visitor.visitIfelse_stat(self)
            else:
                return visitor.visitChildren(self)




    def ifelse_stat(self):

        localctx = MiniGoParser.Ifelse_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ifelse_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.if_()
            self.state = 440
            self.elseif_lst()
            self.state = 441
            self.else_()
            self.state = 442
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_" ):
                return visitor.visitIf_(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = MiniGoParser.If_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.IF_)
            self.state = 445
            self.condition()
            self.state = 446
            self.blockcode()
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 447
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_" ):
                return visitor.visitElseif_(self)
            else:
                return visitor.visitChildren(self)




    def elseif_(self):

        localctx = MiniGoParser.Elseif_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.ELSE_)
            self.state = 451
            self.match(MiniGoParser.IF_)
            self.state = 452
            self.condition()
            self.state = 453
            self.blockcode()
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 454
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_Context,0)


        def elseif_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_lst" ):
                return visitor.visitElseif_lst(self)
            else:
                return visitor.visitChildren(self)




    def elseif_lst(self):

        localctx = MiniGoParser.Elseif_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elseif_lst)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.elseif_()
                self.state = 458
                self.elseif_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_" ):
                return visitor.visitElse_(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = MiniGoParser.Else_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_else_)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(MiniGoParser.ELSE_)
                self.state = 464
                self.blockcode()
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.LP)
            self.state = 469
            self.expr(0)
            self.state = 470
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)

        def id__arr(self):
            return self.getTypedRuleContext(MiniGoParser.Id__arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_stat" ):
                return visitor.visitForloop_stat(self)
            else:
                return visitor.visitChildren(self)




    def forloop_stat(self):

        localctx = MiniGoParser.Forloop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_forloop_stat)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(MiniGoParser.FOR_)
                self.state = 473
                self.expr(0)
                self.state = 474
                self.blockcode()
                self.state = 475
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(MiniGoParser.FOR_)
                self.state = 478
                self.match(MiniGoParser.ID)
                self.state = 479
                self.match(MiniGoParser.ASSIGN)
                self.state = 480
                self.expr(0)
                self.state = 481
                self.match(MiniGoParser.SEMICOLON)
                self.state = 482
                self.expr(0)
                self.state = 483
                self.match(MiniGoParser.SEMICOLON)
                self.state = 484
                self.match(MiniGoParser.ID)
                self.state = 485
                self.match(MiniGoParser.UPT_ASSIGN)
                self.state = 486
                self.expr(0)
                self.state = 487
                self.blockcode()
                self.state = 488
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.match(MiniGoParser.FOR_)
                self.state = 491
                self.match(MiniGoParser.ID)
                self.state = 492
                self.match(MiniGoParser.COMMA)
                self.state = 493
                self.match(MiniGoParser.ID)
                self.state = 494
                self.match(MiniGoParser.ASSIGN)
                self.state = 495
                self.match(MiniGoParser.RANGE_)
                self.state = 496
                self.id__arr()
                self.state = 497
                self.blockcode()
                self.state = 498
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id__arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id__arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId__arr" ):
                return visitor.visitId__arr(self)
            else:
                return visitor.visitChildren(self)




    def id__arr(self):

        localctx = MiniGoParser.Id__arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_id__arr)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.arr_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stat" ):
                return visitor.visitBreak_stat(self)
            else:
                return visitor.visitChildren(self)




    def break_stat(self):

        localctx = MiniGoParser.Break_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.BREAK_)
            self.state = 507
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(MiniGoParser.CONTINUE_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stat" ):
                return visitor.visitContinue_stat(self)
            else:
                return visitor.visitChildren(self)




    def continue_stat(self):

        localctx = MiniGoParser.Continue_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(MiniGoParser.CONTINUE_)
            self.state = 510
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_stat" ):
                return visitor.visitFunccall_stat(self)
            else:
                return visitor.visitChildren(self)




    def funccall_stat(self):

        localctx = MiniGoParser.Funccall_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.expr6(0)
            self.state = 513
            self.match(MiniGoParser.LP)
            self.state = 514
            self.exprlst()
            self.state = 515
            self.match(MiniGoParser.RP)
            self.state = 516
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(MiniGoParser.RETURN_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




    def return_stat(self):

        localctx = MiniGoParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_return_stat)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(MiniGoParser.RETURN_)
                self.state = 519
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(MiniGoParser.RETURN_)
                self.state = 521
                self.expr(0)
                self.state = 522
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UPT_ASSIGN or _la==MiniGoParser.ASSIGN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcodestmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcode" ):
                return visitor.visitBlockcode(self)
            else:
                return visitor.visitChildren(self)




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MiniGoParser.LCB)
            self.state = 529
            self.blockcodestmtlst()
            self.state = 530
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodestmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockcodestmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtContext,0)


        def blockcodestmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmtlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcodestmtlst" ):
                return visitor.visitBlockcodestmtlst(self)
            else:
                return visitor.visitChildren(self)




    def blockcodestmtlst(self):

        localctx = MiniGoParser.BlockcodestmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blockcodestmtlst)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF_, MiniGoParser.FOR_, MiniGoParser.RETURN_, MiniGoParser.CONST_, MiniGoParser.VAR_, MiniGoParser.CONTINUE_, MiniGoParser.BREAK_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.blockcodestmt()
                self.state = 533
                self.blockcodestmtlst()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def ifelse_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_statContext,0)


        def forloop_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statContext,0)


        def funccall_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcodestmt" ):
                return visitor.visitBlockcodestmt(self)
            else:
                return visitor.visitChildren(self)




    def blockcodestmt(self):

        localctx = MiniGoParser.BlockcodestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_blockcodestmt)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 541
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 542
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 544
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 545
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 546
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 547
                self.return_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def arrelemlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_literal" ):
                return visitor.visitArr_literal(self)
            else:
                return visitor.visitChildren(self)




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.arridxlst()
            self.state = 551
            self.data_type()
            self.state = 552
            self.arrelemlst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def arreleml(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelemlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrelemlst" ):
                return visitor.visitArrelemlst(self)
            else:
                return visitor.visitChildren(self)




    def arrelemlst(self):

        localctx = MiniGoParser.ArrelemlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arrelemlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(MiniGoParser.LCB)
            self.state = 555
            self.arreleml()
            self.state = 556
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrelem(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arreleml(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arreleml

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArreleml" ):
                return visitor.visitArreleml(self)
            else:
                return visitor.visitChildren(self)




    def arreleml(self):

        localctx = MiniGoParser.ArrelemlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_arreleml)
        try:
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.arrelem()
                self.state = 559
                self.match(MiniGoParser.COMMA)
                self.state = 560
                self.arreleml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.arrelem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrelemlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrelem" ):
                return visitor.visitArrelem(self)
            else:
                return visitor.visitChildren(self)




    def arrelem(self):

        localctx = MiniGoParser.ArrelemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arrelem)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.arrelemlst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def structparamlst(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.ID)
            self.state = 570
            self.match(MiniGoParser.LCB)
            self.state = 571
            self.structparamlst()
            self.state = 572
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructparamlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparamlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparamlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparamlst" ):
                return visitor.visitStructparamlst(self)
            else:
                return visitor.visitChildren(self)




    def structparamlst(self):

        localctx = MiniGoParser.StructparamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_structparamlst)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.structparamlstprime()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructparamlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structparamlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparamlstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparamlstprime" ):
                return visitor.visitStructparamlstprime(self)
            else:
                return visitor.visitChildren(self)




    def structparamlstprime(self):

        localctx = MiniGoParser.StructparamlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_structparamlstprime)
        try:
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.structparam()
                self.state = 579
                self.match(MiniGoParser.COMMA)
                self.state = 580
                self.structparamlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.structparam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparam" ):
                return visitor.visitStructparam(self)
            else:
                return visitor.visitChildren(self)




    def structparam(self):

        localctx = MiniGoParser.StructparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(MiniGoParser.ID)
            self.state = 586
            self.match(MiniGoParser.COLON)
            self.state = 587
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_data_type)
        try:
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.primitive_datatype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_datatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_(self):
            return self.getToken(MiniGoParser.INT_, 0)

        def FLOAT_(self):
            return self.getToken(MiniGoParser.FLOAT_, 0)

        def STRING_(self):
            return self.getToken(MiniGoParser.STRING_, 0)

        def BOOLEAN_(self):
            return self.getToken(MiniGoParser.BOOLEAN_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_datatype" ):
                return visitor.visitPrimitive_datatype(self)
            else:
                return visitor.visitChildren(self)




    def primitive_datatype(self):

        localctx = MiniGoParser.Primitive_datatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def TRUE_(self):
            return self.getToken(MiniGoParser.TRUE_, 0)

        def FALSE_(self):
            return self.getToken(MiniGoParser.FALSE_, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_literal)
        try:
            self.state = 602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 597
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 598
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 599
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 600
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 601
                self.arr_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_stm" ):
                return visitor.visitEnd_stm(self)
            else:
                return visitor.visitChildren(self)




    def end_stm(self):

        localctx = MiniGoParser.End_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.EOF or _la==MiniGoParser.SEMICOLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        self._predicates[6] = self.expr1_sempred
        self._predicates[7] = self.expr2_sempred
        self._predicates[8] = self.expr3_sempred
        self._predicates[9] = self.expr4_sempred
        self._predicates[11] = self.expr6_sempred
        self._predicates[15] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




