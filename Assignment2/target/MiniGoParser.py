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
        buf.write("\u024e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\5\4\u008e\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009a\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6\u00a2\n\6\f\6\16\6\u00a5\13\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00ad\n\7\f\7\16\7\u00b0")
        buf.write("\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b8\n\b\f\b\16\b\u00bb")
        buf.write("\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00c6\n")
        buf.write("\t\f\t\16\t\u00c9\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\7\n\u00d7\n\n\f\n\16\n\u00da\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00e1\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00f3")
        buf.write("\n\f\f\f\16\f\u00f6\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00fe")
        buf.write("\n\r\3\16\3\16\5\16\u0102\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u0109\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\7\20\u0116\n\20\f\20\16\20\u0119\13")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u0132\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u0148\n\24\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u014e\n\25\3\26\3\26\3\26\3\26\3\27\3\27\5\27")
        buf.write("\u0156\n\27\3\27\3\27\3\27\5\27\u015b\n\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\31\3\31\5\31\u0166\n\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u016d\n\32\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u017b")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \5 \u018b\n \3!\3!\3!\5!\u0190\n!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\5!\u019a\n!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\5$\u01aa\n$\3%\3%\3%\5%\u01af\n")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u01bc\n\'\3")
        buf.write("(\3(\3(\3(\3(\5(\u01c3\n(\3)\3)\3)\3)\5)\u01c9\n)\3*\3")
        buf.write("*\3*\5*\u01ce\n*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u01f0\n,\3-\3-\5-\u01f4\n-\3.\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0208\n\61\3\62\3\62\3\63\3\63\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u0214\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u0223")
        buf.write("\n\67\38\38\58\u0227\n8\39\39\39\39\39\3:\3:\5:\u0230")
        buf.write("\n:\3;\3;\3;\3;\3;\5;\u0237\n;\3<\3<\3<\3<\3=\3=\5=\u023f")
        buf.write("\n=\3>\3>\3?\3?\3?\3?\3?\3?\3?\5?\u024a\n?\3@\3@\3@\2")
        buf.write("\t\n\f\16\20\22\26\36A\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\2\5\3\2\37 \3\2\17\22\3\3//\2\u0251\2\u0080")
        buf.write("\3\2\2\2\4\u0087\3\2\2\2\6\u008d\3\2\2\2\b\u0099\3\2\2")
        buf.write("\2\n\u009b\3\2\2\2\f\u00a6\3\2\2\2\16\u00b1\3\2\2\2\20")
        buf.write("\u00bc\3\2\2\2\22\u00ca\3\2\2\2\24\u00e0\3\2\2\2\26\u00e2")
        buf.write("\3\2\2\2\30\u00fd\3\2\2\2\32\u0101\3\2\2\2\34\u0108\3")
        buf.write("\2\2\2\36\u010a\3\2\2\2 \u011a\3\2\2\2\"\u0131\3\2\2\2")
        buf.write("$\u0133\3\2\2\2&\u0147\3\2\2\2(\u014d\3\2\2\2*\u014f\3")
        buf.write("\2\2\2,\u0153\3\2\2\2.\u015f\3\2\2\2\60\u0165\3\2\2\2")
        buf.write("\62\u016c\3\2\2\2\64\u016e\3\2\2\2\66\u0171\3\2\2\28\u017a")
        buf.write("\3\2\2\2:\u017c\3\2\2\2<\u0182\3\2\2\2>\u018a\3\2\2\2")
        buf.write("@\u0199\3\2\2\2B\u019b\3\2\2\2D\u01a1\3\2\2\2F\u01a9\3")
        buf.write("\2\2\2H\u01ab\3\2\2\2J\u01b2\3\2\2\2L\u01b7\3\2\2\2N\u01bd")
        buf.write("\3\2\2\2P\u01c8\3\2\2\2R\u01cd\3\2\2\2T\u01cf\3\2\2\2")
        buf.write("V\u01ef\3\2\2\2X\u01f3\3\2\2\2Z\u01f5\3\2\2\2\\\u01f8")
        buf.write("\3\2\2\2^\u01fb\3\2\2\2`\u0207\3\2\2\2b\u0209\3\2\2\2")
        buf.write("d\u020b\3\2\2\2f\u0213\3\2\2\2h\u0215\3\2\2\2j\u0219\3")
        buf.write("\2\2\2l\u0222\3\2\2\2n\u0226\3\2\2\2p\u0228\3\2\2\2r\u022f")
        buf.write("\3\2\2\2t\u0236\3\2\2\2v\u0238\3\2\2\2x\u023e\3\2\2\2")
        buf.write("z\u0240\3\2\2\2|\u0249\3\2\2\2~\u024b\3\2\2\2\u0080\u0081")
        buf.write("\5\4\3\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084")
        buf.write("\5\6\4\2\u0084\u0085\5\4\3\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0088\5\6\4\2\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2")
        buf.write("\u0088\5\3\2\2\2\u0089\u008e\5\"\22\2\u008a\u008e\5,\27")
        buf.write("\2\u008b\u008e\5:\36\2\u008c\u008e\5B\"\2\u008d\u0089")
        buf.write("\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\7\3\2\2\2\u008f\u009a\5 \21\2\u0090")
        buf.write("\u009a\5\"\22\2\u0091\u009a\5&\24\2\u0092\u009a\5$\23")
        buf.write("\2\u0093\u009a\5J&\2\u0094\u009a\5V,\2\u0095\u009a\5\\")
        buf.write("/\2\u0096\u009a\5Z.\2\u0097\u009a\5^\60\2\u0098\u009a")
        buf.write("\5`\61\2\u0099\u008f\3\2\2\2\u0099\u0090\3\2\2\2\u0099")
        buf.write("\u0091\3\2\2\2\u0099\u0092\3\2\2\2\u0099\u0093\3\2\2\2")
        buf.write("\u0099\u0094\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0096\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\t")
        buf.write("\3\2\2\2\u009b\u009c\b\6\1\2\u009c\u009d\5\f\7\2\u009d")
        buf.write("\u00a3\3\2\2\2\u009e\u009f\f\4\2\2\u009f\u00a0\7\35\2")
        buf.write("\2\u00a0\u00a2\5\f\7\2\u00a1\u009e\3\2\2\2\u00a2\u00a5")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\13\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\b\7\1\2\u00a7")
        buf.write("\u00a8\5\16\b\2\u00a8\u00ae\3\2\2\2\u00a9\u00aa\f\4\2")
        buf.write("\2\u00aa\u00ab\7\34\2\2\u00ab\u00ad\5\16\b\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\r\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1")
        buf.write("\u00b2\b\b\1\2\u00b2\u00b3\5\20\t\2\u00b3\u00b9\3\2\2")
        buf.write("\2\u00b4\u00b5\f\4\2\2\u00b5\u00b6\7\33\2\2\u00b6\u00b8")
        buf.write("\5\20\t\2\u00b7\u00b4\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\17\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bc\u00bd\b\t\1\2\u00bd\u00be\5\22\n")
        buf.write("\2\u00be\u00c7\3\2\2\2\u00bf\u00c0\f\5\2\2\u00c0\u00c1")
        buf.write("\7#\2\2\u00c1\u00c6\5\22\n\2\u00c2\u00c3\f\4\2\2\u00c3")
        buf.write("\u00c4\7$\2\2\u00c4\u00c6\5\22\n\2\u00c5\u00bf\3\2\2\2")
        buf.write("\u00c5\u00c2\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3")
        buf.write("\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\21\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cb\b\n\1\2\u00cb\u00cc\5\24\13\2\u00cc")
        buf.write("\u00d8\3\2\2\2\u00cd\u00ce\f\6\2\2\u00ce\u00cf\7%\2\2")
        buf.write("\u00cf\u00d7\5\24\13\2\u00d0\u00d1\f\5\2\2\u00d1\u00d2")
        buf.write("\7&\2\2\u00d2\u00d7\5\24\13\2\u00d3\u00d4\f\4\2\2\u00d4")
        buf.write("\u00d5\7\'\2\2\u00d5\u00d7\5\24\13\2\u00d6\u00cd\3\2\2")
        buf.write("\2\u00d6\u00d0\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7\u00da")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\23\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\7\36\2\2\u00dc")
        buf.write("\u00e1\5\26\f\2\u00dd\u00de\7$\2\2\u00de\u00e1\5\26\f")
        buf.write("\2\u00df\u00e1\5\26\f\2\u00e0\u00db\3\2\2\2\u00e0\u00dd")
        buf.write("\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\25\3\2\2\2\u00e2\u00e3")
        buf.write("\b\f\1\2\u00e3\u00e4\5\30\r\2\u00e4\u00f4\3\2\2\2\u00e5")
        buf.write("\u00e6\f\6\2\2\u00e6\u00e7\7!\2\2\u00e7\u00f3\7\64\2\2")
        buf.write("\u00e8\u00e9\f\5\2\2\u00e9\u00ea\7*\2\2\u00ea\u00eb\5")
        buf.write("\n\6\2\u00eb\u00ec\7+\2\2\u00ec\u00f3\3\2\2\2\u00ed\u00ee")
        buf.write("\f\4\2\2\u00ee\u00ef\7(\2\2\u00ef\u00f0\5\32\16\2\u00f0")
        buf.write("\u00f1\7)\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00e5\3\2\2\2")
        buf.write("\u00f2\u00e8\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f3\u00f6\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\27")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7(\2\2\u00f8")
        buf.write("\u00f9\5\n\6\2\u00f9\u00fa\7)\2\2\u00fa\u00fe\3\2\2\2")
        buf.write("\u00fb\u00fe\7\64\2\2\u00fc\u00fe\5|?\2\u00fd\u00f7\3")
        buf.write("\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\31")
        buf.write("\3\2\2\2\u00ff\u0102\5\34\17\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102\33\3\2\2\2\u0103")
        buf.write("\u0104\5\n\6\2\u0104\u0105\7.\2\2\u0105\u0106\5\34\17")
        buf.write("\2\u0106\u0109\3\2\2\2\u0107\u0109\5\n\6\2\u0108\u0103")
        buf.write("\3\2\2\2\u0108\u0107\3\2\2\2\u0109\35\3\2\2\2\u010a\u010b")
        buf.write("\b\20\1\2\u010b\u010c\7\64\2\2\u010c\u0117\3\2\2\2\u010d")
        buf.write("\u010e\f\5\2\2\u010e\u010f\7!\2\2\u010f\u0116\7\64\2\2")
        buf.write("\u0110\u0111\f\4\2\2\u0111\u0112\7*\2\2\u0112\u0113\5")
        buf.write("\n\6\2\u0113\u0114\7+\2\2\u0114\u0116\3\2\2\2\u0115\u010d")
        buf.write("\3\2\2\2\u0115\u0110\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\37\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u011a\u011b\5\36\20\2\u011b\u011c\5b\62")
        buf.write("\2\u011c\u011d\5\n\6\2\u011d\u011e\5~@\2\u011e!\3\2\2")
        buf.write("\2\u011f\u0120\7\24\2\2\u0120\u0121\7\64\2\2\u0121\u0122")
        buf.write("\5x=\2\u0122\u0123\5~@\2\u0123\u0132\3\2\2\2\u0124\u0125")
        buf.write("\7\24\2\2\u0125\u0126\7\64\2\2\u0126\u0127\7\"\2\2\u0127")
        buf.write("\u0128\5\n\6\2\u0128\u0129\5~@\2\u0129\u0132\3\2\2\2\u012a")
        buf.write("\u012b\7\24\2\2\u012b\u012c\7\64\2\2\u012c\u012d\5x=\2")
        buf.write("\u012d\u012e\7\"\2\2\u012e\u012f\5\n\6\2\u012f\u0130\5")
        buf.write("~@\2\u0130\u0132\3\2\2\2\u0131\u011f\3\2\2\2\u0131\u0124")
        buf.write("\3\2\2\2\u0131\u012a\3\2\2\2\u0132#\3\2\2\2\u0133\u0134")
        buf.write("\7\23\2\2\u0134\u0135\7\64\2\2\u0135\u0136\7\"\2\2\u0136")
        buf.write("\u0137\5\n\6\2\u0137\u0138\5~@\2\u0138%\3\2\2\2\u0139")
        buf.write("\u013a\7\24\2\2\u013a\u013b\7\64\2\2\u013b\u013c\5(\25")
        buf.write("\2\u013c\u013d\5x=\2\u013d\u013e\5~@\2\u013e\u0148\3\2")
        buf.write("\2\2\u013f\u0140\7\24\2\2\u0140\u0141\7\64\2\2\u0141\u0142")
        buf.write("\5(\25\2\u0142\u0143\5x=\2\u0143\u0144\7\"\2\2\u0144\u0145")
        buf.write("\5h\65\2\u0145\u0146\5~@\2\u0146\u0148\3\2\2\2\u0147\u0139")
        buf.write("\3\2\2\2\u0147\u013f\3\2\2\2\u0148\'\3\2\2\2\u0149\u014a")
        buf.write("\5*\26\2\u014a\u014b\5(\25\2\u014b\u014e\3\2\2\2\u014c")
        buf.write("\u014e\5*\26\2\u014d\u0149\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e)\3\2\2\2\u014f\u0150\7*\2\2\u0150\u0151\5\n\6\2")
        buf.write("\u0151\u0152\7+\2\2\u0152+\3\2\2\2\u0153\u0155\7\13\2")
        buf.write("\2\u0154\u0156\5\66\34\2\u0155\u0154\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7\64\2\2\u0158")
        buf.write("\u015a\5.\30\2\u0159\u015b\5x=\2\u015a\u0159\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\5d\63\2")
        buf.write("\u015d\u015e\5~@\2\u015e-\3\2\2\2\u015f\u0160\7(\2\2\u0160")
        buf.write("\u0161\5\60\31\2\u0161\u0162\7)\2\2\u0162/\3\2\2\2\u0163")
        buf.write("\u0166\5\62\32\2\u0164\u0166\3\2\2\2\u0165\u0163\3\2\2")
        buf.write("\2\u0165\u0164\3\2\2\2\u0166\61\3\2\2\2\u0167\u0168\5")
        buf.write("\64\33\2\u0168\u0169\7.\2\2\u0169\u016a\5\62\32\2\u016a")
        buf.write("\u016d\3\2\2\2\u016b\u016d\5\64\33\2\u016c\u0167\3\2\2")
        buf.write("\2\u016c\u016b\3\2\2\2\u016d\63\3\2\2\2\u016e\u016f\5")
        buf.write("8\35\2\u016f\u0170\5x=\2\u0170\65\3\2\2\2\u0171\u0172")
        buf.write("\7(\2\2\u0172\u0173\7\64\2\2\u0173\u0174\7\64\2\2\u0174")
        buf.write("\u0175\7)\2\2\u0175\67\3\2\2\2\u0176\u0177\7\64\2\2\u0177")
        buf.write("\u0178\7.\2\2\u0178\u017b\58\35\2\u0179\u017b\7\64\2\2")
        buf.write("\u017a\u0176\3\2\2\2\u017a\u0179\3\2\2\2\u017b9\3\2\2")
        buf.write("\2\u017c\u017d\7\f\2\2\u017d\u017e\7\64\2\2\u017e\u017f")
        buf.write("\7\r\2\2\u017f\u0180\5<\37\2\u0180\u0181\5~@\2\u0181;")
        buf.write("\3\2\2\2\u0182\u0183\7,\2\2\u0183\u0184\5> \2\u0184\u0185")
        buf.write("\7-\2\2\u0185=\3\2\2\2\u0186\u0187\5@!\2\u0187\u0188\5")
        buf.write("> \2\u0188\u018b\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u0186")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018b?\3\2\2\2\u018c\u018d")
        buf.write("\7\64\2\2\u018d\u018f\5x=\2\u018e\u0190\5(\25\2\u018f")
        buf.write("\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\5~@\2\u0192\u019a\3\2\2\2\u0193\u0194\7\64")
        buf.write("\2\2\u0194\u0195\7\64\2\2\u0195\u019a\5~@\2\u0196\u0197")
        buf.write("\7\64\2\2\u0197\u0198\7\16\2\2\u0198\u019a\5~@\2\u0199")
        buf.write("\u018c\3\2\2\2\u0199\u0193\3\2\2\2\u0199\u0196\3\2\2\2")
        buf.write("\u019aA\3\2\2\2\u019b\u019c\7\f\2\2\u019c\u019d\7\64\2")
        buf.write("\2\u019d\u019e\7\16\2\2\u019e\u019f\5D#\2\u019f\u01a0")
        buf.write("\5~@\2\u01a0C\3\2\2\2\u01a1\u01a2\7,\2\2\u01a2\u01a3\5")
        buf.write("F$\2\u01a3\u01a4\7-\2\2\u01a4E\3\2\2\2\u01a5\u01a6\5H")
        buf.write("%\2\u01a6\u01a7\5F$\2\u01a7\u01aa\3\2\2\2\u01a8\u01aa")
        buf.write("\3\2\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("G\3\2\2\2\u01ab\u01ac\7\64\2\2\u01ac\u01ae\5.\30\2\u01ad")
        buf.write("\u01af\5x=\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b1\5~@\2\u01b1I\3\2\2\2\u01b2")
        buf.write("\u01b3\5L\'\2\u01b3\u01b4\5P)\2\u01b4\u01b5\5R*\2\u01b5")
        buf.write("\u01b6\5~@\2\u01b6K\3\2\2\2\u01b7\u01b8\7\7\2\2\u01b8")
        buf.write("\u01b9\5T+\2\u01b9\u01bb\5d\63\2\u01ba\u01bc\5~@\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bcM\3\2\2\2\u01bd")
        buf.write("\u01be\7\b\2\2\u01be\u01bf\7\7\2\2\u01bf\u01c0\5T+\2\u01c0")
        buf.write("\u01c2\5d\63\2\u01c1\u01c3\5~@\2\u01c2\u01c1\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3O\3\2\2\2\u01c4\u01c5\5N(\2\u01c5")
        buf.write("\u01c6\5P)\2\u01c6\u01c9\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8")
        buf.write("\u01c4\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9Q\3\2\2\2\u01ca")
        buf.write("\u01cb\7\b\2\2\u01cb\u01ce\5d\63\2\u01cc\u01ce\3\2\2\2")
        buf.write("\u01cd\u01ca\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ceS\3\2\2")
        buf.write("\2\u01cf\u01d0\7(\2\2\u01d0\u01d1\5\n\6\2\u01d1\u01d2")
        buf.write("\7)\2\2\u01d2U\3\2\2\2\u01d3\u01d4\7\t\2\2\u01d4\u01d5")
        buf.write("\5\n\6\2\u01d5\u01d6\5d\63\2\u01d6\u01d7\5~@\2\u01d7\u01f0")
        buf.write("\3\2\2\2\u01d8\u01d9\7\t\2\2\u01d9\u01da\7\64\2\2\u01da")
        buf.write("\u01db\7 \2\2\u01db\u01dc\5\n\6\2\u01dc\u01dd\7/\2\2\u01dd")
        buf.write("\u01de\5\n\6\2\u01de\u01df\7/\2\2\u01df\u01e0\7\64\2\2")
        buf.write("\u01e0\u01e1\7\37\2\2\u01e1\u01e2\5\n\6\2\u01e2\u01e3")
        buf.write("\5d\63\2\u01e3\u01e4\5~@\2\u01e4\u01f0\3\2\2\2\u01e5\u01e6")
        buf.write("\7\t\2\2\u01e6\u01e7\7\64\2\2\u01e7\u01e8\7.\2\2\u01e8")
        buf.write("\u01e9\7\64\2\2\u01e9\u01ea\7 \2\2\u01ea\u01eb\7\27\2")
        buf.write("\2\u01eb\u01ec\5X-\2\u01ec\u01ed\5d\63\2\u01ed\u01ee\5")
        buf.write("~@\2\u01ee\u01f0\3\2\2\2\u01ef\u01d3\3\2\2\2\u01ef\u01d8")
        buf.write("\3\2\2\2\u01ef\u01e5\3\2\2\2\u01f0W\3\2\2\2\u01f1\u01f4")
        buf.write("\7\64\2\2\u01f2\u01f4\5h\65\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4Y\3\2\2\2\u01f5\u01f6\7\26\2\2\u01f6")
        buf.write("\u01f7\5~@\2\u01f7[\3\2\2\2\u01f8\u01f9\7\25\2\2\u01f9")
        buf.write("\u01fa\5~@\2\u01fa]\3\2\2\2\u01fb\u01fc\5\26\f\2\u01fc")
        buf.write("\u01fd\7(\2\2\u01fd\u01fe\5\32\16\2\u01fe\u01ff\7)\2\2")
        buf.write("\u01ff\u0200\5~@\2\u0200_\3\2\2\2\u0201\u0202\7\n\2\2")
        buf.write("\u0202\u0208\5~@\2\u0203\u0204\7\n\2\2\u0204\u0205\5\n")
        buf.write("\6\2\u0205\u0206\5~@\2\u0206\u0208\3\2\2\2\u0207\u0201")
        buf.write("\3\2\2\2\u0207\u0203\3\2\2\2\u0208a\3\2\2\2\u0209\u020a")
        buf.write("\t\2\2\2\u020ac\3\2\2\2\u020b\u020c\7,\2\2\u020c\u020d")
        buf.write("\5f\64\2\u020d\u020e\7-\2\2\u020ee\3\2\2\2\u020f\u0210")
        buf.write("\5\b\5\2\u0210\u0211\5f\64\2\u0211\u0214\3\2\2\2\u0212")
        buf.write("\u0214\3\2\2\2\u0213\u020f\3\2\2\2\u0213\u0212\3\2\2\2")
        buf.write("\u0214g\3\2\2\2\u0215\u0216\5(\25\2\u0216\u0217\5x=\2")
        buf.write("\u0217\u0218\5j\66\2\u0218i\3\2\2\2\u0219\u021a\7,\2\2")
        buf.write("\u021a\u021b\5l\67\2\u021b\u021c\7-\2\2\u021ck\3\2\2\2")
        buf.write("\u021d\u021e\5n8\2\u021e\u021f\7.\2\2\u021f\u0220\5l\67")
        buf.write("\2\u0220\u0223\3\2\2\2\u0221\u0223\5n8\2\u0222\u021d\3")
        buf.write("\2\2\2\u0222\u0221\3\2\2\2\u0223m\3\2\2\2\u0224\u0227")
        buf.write("\5\n\6\2\u0225\u0227\5j\66\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0225\3\2\2\2\u0227o\3\2\2\2\u0228\u0229\7\64\2\2\u0229")
        buf.write("\u022a\7,\2\2\u022a\u022b\5r:\2\u022b\u022c\7-\2\2\u022c")
        buf.write("q\3\2\2\2\u022d\u0230\5t;\2\u022e\u0230\3\2\2\2\u022f")
        buf.write("\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230s\3\2\2\2\u0231")
        buf.write("\u0232\5v<\2\u0232\u0233\7.\2\2\u0233\u0234\5t;\2\u0234")
        buf.write("\u0237\3\2\2\2\u0235\u0237\5v<\2\u0236\u0231\3\2\2\2\u0236")
        buf.write("\u0235\3\2\2\2\u0237u\3\2\2\2\u0238\u0239\7\64\2\2\u0239")
        buf.write("\u023a\7\60\2\2\u023a\u023b\5|?\2\u023bw\3\2\2\2\u023c")
        buf.write("\u023f\5z>\2\u023d\u023f\7\64\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023e\u023d\3\2\2\2\u023fy\3\2\2\2\u0240\u0241\t\3\2")
        buf.write("\2\u0241{\3\2\2\2\u0242\u024a\7\62\2\2\u0243\u024a\7\61")
        buf.write("\2\2\u0244\u024a\7\63\2\2\u0245\u024a\7\31\2\2\u0246\u024a")
        buf.write("\7\32\2\2\u0247\u024a\5p9\2\u0248\u024a\5h\65\2\u0249")
        buf.write("\u0242\3\2\2\2\u0249\u0243\3\2\2\2\u0249\u0244\3\2\2\2")
        buf.write("\u0249\u0245\3\2\2\2\u0249\u0246\3\2\2\2\u0249\u0247\3")
        buf.write("\2\2\2\u0249\u0248\3\2\2\2\u024a}\3\2\2\2\u024b\u024c")
        buf.write("\t\4\2\2\u024c\177\3\2\2\2/\u0087\u008d\u0099\u00a3\u00ae")
        buf.write("\u00b9\u00c5\u00c7\u00d6\u00d8\u00e0\u00f2\u00f4\u00fd")
        buf.write("\u0101\u0108\u0115\u0117\u0131\u0147\u014d\u0155\u015a")
        buf.write("\u0165\u016c\u017a\u018a\u018f\u0199\u01a9\u01ae\u01bb")
        buf.write("\u01c2\u01c8\u01cd\u01ef\u01f3\u0207\u0213\u0222\u0226")
        buf.write("\u022f\u0236\u023e\u0249")
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
    RULE_decllst = 1
    RULE_decl = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_expr4 = 8
    RULE_expr5 = 9
    RULE_expr6 = 10
    RULE_expr7 = 11
    RULE_exprlst = 12
    RULE_exprlstprime = 13
    RULE_lhs = 14
    RULE_assigning = 15
    RULE_vardecl = 16
    RULE_constdecl = 17
    RULE_arraydecl = 18
    RULE_arridxlst = 19
    RULE_arridx = 20
    RULE_funcdecl = 21
    RULE_funcparam = 22
    RULE_paramlst = 23
    RULE_paramlstprime = 24
    RULE_param = 25
    RULE_receiver = 26
    RULE_idlst = 27
    RULE_structdecl = 28
    RULE_structfield = 29
    RULE_fielddecllst = 30
    RULE_fielddecl = 31
    RULE_interfdecl = 32
    RULE_interfmeth = 33
    RULE_interfmethlst = 34
    RULE_interfmethmem = 35
    RULE_ifelse_stat = 36
    RULE_if_ = 37
    RULE_elseif_ = 38
    RULE_elseif_lst = 39
    RULE_else_ = 40
    RULE_condition = 41
    RULE_forloop_stat = 42
    RULE_id__arr = 43
    RULE_break_stat = 44
    RULE_continue_stat = 45
    RULE_funccall_stat = 46
    RULE_return_stat = 47
    RULE_assign = 48
    RULE_blockcode = 49
    RULE_stmtlst = 50
    RULE_arr_literal = 51
    RULE_arrelemlst = 52
    RULE_arreleml = 53
    RULE_arrelem = 54
    RULE_struct_literal = 55
    RULE_structparamlst = 56
    RULE_structparamlstprime = 57
    RULE_structparam = 58
    RULE_data_type = 59
    RULE_primitive_datatype = 60
    RULE_literal = 61
    RULE_end_stm = 62

    ruleNames =  [ "program", "decllst", "decl", "statement", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "exprlst", "exprlstprime", "lhs", "assigning", "vardecl", 
                   "constdecl", "arraydecl", "arridxlst", "arridx", "funcdecl", 
                   "funcparam", "paramlst", "paramlstprime", "param", "receiver", 
                   "idlst", "structdecl", "structfield", "fielddecllst", 
                   "fielddecl", "interfdecl", "interfmeth", "interfmethlst", 
                   "interfmethmem", "ifelse_stat", "if_", "elseif_", "elseif_lst", 
                   "else_", "condition", "forloop_stat", "id__arr", "break_stat", 
                   "continue_stat", "funccall_stat", "return_stat", "assign", 
                   "blockcode", "stmtlst", "arr_literal", "arrelemlst", 
                   "arreleml", "arrelem", "struct_literal", "structparamlst", 
                   "structparamlstprime", "structparam", "data_type", "primitive_datatype", 
                   "literal", "end_stm" ]

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

        def decllst(self):
            return self.getTypedRuleContext(MiniGoParser.DecllstContext,0)


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
            self.state = 126
            self.decllst()
            self.state = 127
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllst(self):
            return self.getTypedRuleContext(MiniGoParser.DecllstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllst" ):
                return visitor.visitDecllst(self)
            else:
                return visitor.visitChildren(self)




    def decllst(self):

        localctx = MiniGoParser.DecllstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllst)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decl()
                self.state = 130
                self.decllst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.decl()
                pass


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
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.structdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.interfdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
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
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 149
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 150
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 156
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 157
                    self.match(MiniGoParser.OR)
                    self.state = 158
                    self.expr1(0) 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 167
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 168
                    self.match(MiniGoParser.AND)
                    self.state = 169
                    self.expr2(0) 
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 178
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 179
                    self.match(MiniGoParser.COMPARISON_OP)
                    self.state = 180
                    self.expr3(0) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 189
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 190
                        self.match(MiniGoParser.ADD)
                        self.state = 191
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 192
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 193
                        self.match(MiniGoParser.SUB)
                        self.state = 194
                        self.expr4(0)
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 203
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 204
                        self.match(MiniGoParser.MUL)
                        self.state = 205
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 206
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 207
                        self.match(MiniGoParser.DIV)
                        self.state = 208
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 209
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 210
                        self.match(MiniGoParser.MOD)
                        self.state = 211
                        self.expr5()
                        pass

             
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_expr5)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(MiniGoParser.NOT)
                self.state = 218
                self.expr6(0)
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(MiniGoParser.SUB)
                self.state = 220
                self.expr6(0)
                pass
            elif token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 240
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 227
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 228
                        self.match(MiniGoParser.DOT)
                        self.state = 229
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 230
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 231
                        self.match(MiniGoParser.LSB)
                        self.state = 232
                        self.expr(0)
                        self.state = 233
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 235
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 236
                        self.match(MiniGoParser.LP)
                        self.state = 237
                        self.exprlst()
                        self.state = 238
                        self.match(MiniGoParser.RP)
                        pass

             
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_expr7)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(MiniGoParser.LP)
                self.state = 246
                self.expr(0)
                self.state = 247
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
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
        self.enterRule(localctx, 24, self.RULE_exprlst)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
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
        self.enterRule(localctx, 26, self.RULE_exprlstprime)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.expr(0)
                self.state = 258
                self.match(MiniGoParser.COMMA)
                self.state = 259
                self.exprlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 275
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 267
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 268
                        self.match(MiniGoParser.DOT)
                        self.state = 269
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 270
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 271
                        self.match(MiniGoParser.LSB)
                        self.state = 272
                        self.expr(0)
                        self.state = 273
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.lhs(0)
            self.state = 281
            self.assign()
            self.state = 282
            self.expr(0)
            self.state = 283
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
        self.enterRule(localctx, 32, self.RULE_vardecl)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(MiniGoParser.VAR_)
                self.state = 286
                self.match(MiniGoParser.ID)
                self.state = 287
                self.data_type()
                self.state = 288
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(MiniGoParser.VAR_)
                self.state = 291
                self.match(MiniGoParser.ID)
                self.state = 292
                self.match(MiniGoParser.EQUAL)
                self.state = 293
                self.expr(0)
                self.state = 294
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(MiniGoParser.VAR_)
                self.state = 297
                self.match(MiniGoParser.ID)
                self.state = 298
                self.data_type()
                self.state = 299
                self.match(MiniGoParser.EQUAL)
                self.state = 300
                self.expr(0)
                self.state = 301
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
        self.enterRule(localctx, 34, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.CONST_)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 307
            self.match(MiniGoParser.EQUAL)
            self.state = 308
            self.expr(0)
            self.state = 309
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
        self.enterRule(localctx, 36, self.RULE_arraydecl)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(MiniGoParser.VAR_)
                self.state = 312
                self.match(MiniGoParser.ID)
                self.state = 313
                self.arridxlst()
                self.state = 314
                self.data_type()
                self.state = 315
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(MiniGoParser.VAR_)
                self.state = 318
                self.match(MiniGoParser.ID)
                self.state = 319
                self.arridxlst()
                self.state = 320
                self.data_type()
                self.state = 321
                self.match(MiniGoParser.EQUAL)
                self.state = 322
                self.arr_literal()
                self.state = 323
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
        self.enterRule(localctx, 38, self.RULE_arridxlst)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.arridx()
                self.state = 328
                self.arridxlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
        self.enterRule(localctx, 40, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.LSB)
            self.state = 334
            self.expr(0)
            self.state = 335
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
        self.enterRule(localctx, 42, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.FUNC_)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LP:
                self.state = 338
                self.receiver()


            self.state = 341
            self.match(MiniGoParser.ID)
            self.state = 342
            self.funcparam()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 343
                self.data_type()


            self.state = 346
            self.blockcode()
            self.state = 347
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
        self.enterRule(localctx, 44, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MiniGoParser.LP)
            self.state = 350
            self.paramlst()
            self.state = 351
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
        self.enterRule(localctx, 46, self.RULE_paramlst)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
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
        self.enterRule(localctx, 48, self.RULE_paramlstprime)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.param()
                self.state = 358
                self.match(MiniGoParser.COMMA)
                self.state = 359
                self.paramlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
        self.enterRule(localctx, 50, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.idlst()
            self.state = 365
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
        self.enterRule(localctx, 52, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MiniGoParser.LP)
            self.state = 368
            self.match(MiniGoParser.ID)
            self.state = 369
            self.match(MiniGoParser.ID)
            self.state = 370
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
        self.enterRule(localctx, 54, self.RULE_idlst)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(MiniGoParser.ID)
                self.state = 373
                self.match(MiniGoParser.COMMA)
                self.state = 374
                self.idlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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
        self.enterRule(localctx, 56, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.TYPE_)
            self.state = 379
            self.match(MiniGoParser.ID)
            self.state = 380
            self.match(MiniGoParser.STRUCT_)
            self.state = 381
            self.structfield()
            self.state = 382
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
        self.enterRule(localctx, 58, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.LCB)
            self.state = 385
            self.fielddecllst()
            self.state = 386
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
        self.enterRule(localctx, 60, self.RULE_fielddecllst)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.fielddecl()
                self.state = 389
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
        self.enterRule(localctx, 62, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(MiniGoParser.ID)
                self.state = 395
                self.data_type()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 396
                    self.arridxlst()


                self.state = 399
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(MiniGoParser.ID)
                self.state = 402
                self.match(MiniGoParser.ID)
                self.state = 403
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 404
                self.match(MiniGoParser.ID)
                self.state = 405
                self.match(MiniGoParser.INTERFACE_)
                self.state = 406
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
        self.enterRule(localctx, 64, self.RULE_interfdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.TYPE_)
            self.state = 410
            self.match(MiniGoParser.ID)
            self.state = 411
            self.match(MiniGoParser.INTERFACE_)
            self.state = 412
            self.interfmeth()
            self.state = 413
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
        self.enterRule(localctx, 66, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.LCB)
            self.state = 416
            self.interfmethlst()
            self.state = 417
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
        self.enterRule(localctx, 68, self.RULE_interfmethlst)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.interfmethmem()
                self.state = 420
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
        self.enterRule(localctx, 70, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(MiniGoParser.ID)
            self.state = 426
            self.funcparam()
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.ID))) != 0):
                self.state = 427
                self.data_type()


            self.state = 430
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
        self.enterRule(localctx, 72, self.RULE_ifelse_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.if_()
            self.state = 433
            self.elseif_lst()
            self.state = 434
            self.else_()
            self.state = 435
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
        self.enterRule(localctx, 74, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.IF_)
            self.state = 438
            self.condition()
            self.state = 439
            self.blockcode()
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 440
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
        self.enterRule(localctx, 76, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.ELSE_)
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
        self.enterRule(localctx, 78, self.RULE_elseif_lst)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.elseif_()
                self.state = 451
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
        self.enterRule(localctx, 80, self.RULE_else_)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(MiniGoParser.ELSE_)
                self.state = 457
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
        self.enterRule(localctx, 82, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MiniGoParser.LP)
            self.state = 462
            self.expr(0)
            self.state = 463
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
        self.enterRule(localctx, 84, self.RULE_forloop_stat)
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(MiniGoParser.FOR_)
                self.state = 466
                self.expr(0)
                self.state = 467
                self.blockcode()
                self.state = 468
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(MiniGoParser.FOR_)
                self.state = 471
                self.match(MiniGoParser.ID)
                self.state = 472
                self.match(MiniGoParser.ASSIGN)
                self.state = 473
                self.expr(0)
                self.state = 474
                self.match(MiniGoParser.SEMICOLON)
                self.state = 475
                self.expr(0)
                self.state = 476
                self.match(MiniGoParser.SEMICOLON)
                self.state = 477
                self.match(MiniGoParser.ID)
                self.state = 478
                self.match(MiniGoParser.UPT_ASSIGN)
                self.state = 479
                self.expr(0)
                self.state = 480
                self.blockcode()
                self.state = 481
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(MiniGoParser.FOR_)
                self.state = 484
                self.match(MiniGoParser.ID)
                self.state = 485
                self.match(MiniGoParser.COMMA)
                self.state = 486
                self.match(MiniGoParser.ID)
                self.state = 487
                self.match(MiniGoParser.ASSIGN)
                self.state = 488
                self.match(MiniGoParser.RANGE_)
                self.state = 489
                self.id__arr()
                self.state = 490
                self.blockcode()
                self.state = 491
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
        self.enterRule(localctx, 86, self.RULE_id__arr)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self.enterRule(localctx, 88, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MiniGoParser.BREAK_)
            self.state = 500
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
        self.enterRule(localctx, 90, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.CONTINUE_)
            self.state = 503
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
        self.enterRule(localctx, 92, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.expr6(0)
            self.state = 506
            self.match(MiniGoParser.LP)
            self.state = 507
            self.exprlst()
            self.state = 508
            self.match(MiniGoParser.RP)
            self.state = 509
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
        self.enterRule(localctx, 94, self.RULE_return_stat)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(MiniGoParser.RETURN_)
                self.state = 512
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.match(MiniGoParser.RETURN_)
                self.state = 514
                self.expr(0)
                self.state = 515
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
        self.enterRule(localctx, 96, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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

        def stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlstContext,0)


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
        self.enterRule(localctx, 98, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.LCB)
            self.state = 522
            self.stmtlst()
            self.state = 523
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlst" ):
                return visitor.visitStmtlst(self)
            else:
                return visitor.visitChildren(self)




    def stmtlst(self):

        localctx = MiniGoParser.StmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmtlst)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF_, MiniGoParser.FOR_, MiniGoParser.RETURN_, MiniGoParser.CONST_, MiniGoParser.VAR_, MiniGoParser.CONTINUE_, MiniGoParser.BREAK_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.statement()
                self.state = 526
                self.stmtlst()
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
        self.enterRule(localctx, 102, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.arridxlst()
            self.state = 532
            self.data_type()
            self.state = 533
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
        self.enterRule(localctx, 104, self.RULE_arrelemlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(MiniGoParser.LCB)
            self.state = 536
            self.arreleml()
            self.state = 537
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
        self.enterRule(localctx, 106, self.RULE_arreleml)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.arrelem()
                self.state = 540
                self.match(MiniGoParser.COMMA)
                self.state = 541
                self.arreleml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
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
        self.enterRule(localctx, 108, self.RULE_arrelem)
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
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
        self.enterRule(localctx, 110, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(MiniGoParser.ID)
            self.state = 551
            self.match(MiniGoParser.LCB)
            self.state = 552
            self.structparamlst()
            self.state = 553
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
        self.enterRule(localctx, 112, self.RULE_structparamlst)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
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
        self.enterRule(localctx, 114, self.RULE_structparamlstprime)
        try:
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.structparam()
                self.state = 560
                self.match(MiniGoParser.COMMA)
                self.state = 561
                self.structparamlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
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
        self.enterRule(localctx, 116, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.ID)
            self.state = 567
            self.match(MiniGoParser.COLON)
            self.state = 568
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
        self.enterRule(localctx, 118, self.RULE_data_type)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.primitive_datatype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 571
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
        self.enterRule(localctx, 120, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
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
        self.enterRule(localctx, 122, self.RULE_literal)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 578
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 579
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 580
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 581
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 582
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
        self.enterRule(localctx, 124, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
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
        self._predicates[4] = self.expr_sempred
        self._predicates[5] = self.expr1_sempred
        self._predicates[6] = self.expr2_sempred
        self._predicates[7] = self.expr3_sempred
        self._predicates[8] = self.expr4_sempred
        self._predicates[10] = self.expr6_sempred
        self._predicates[14] = self.lhs_sempred
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
         




