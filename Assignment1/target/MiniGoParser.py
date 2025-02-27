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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0241\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0094\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\5\4\u009b\n\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a8\n\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6\u00b2\n\6\f\6\16\6\u00b5\13\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\7\7\u00bd\n\7\f\7\16\7\u00c0\13")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00c9\n\b\f\b\16\b")
        buf.write("\u00cc\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00d7")
        buf.write("\n\t\f\t\16\t\u00da\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\7\n\u00e8\n\n\f\n\16\n\u00eb\13\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u00f2\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00f9\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\7\f\u0107\n\f\f\f\16\f\u010a\13\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u0112\n\r\3\16\3\16\5\16\u0116")
        buf.write("\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u011f\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\5\23\u012b\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u0132\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u013b\n\25")
        buf.write("\3\26\3\26\5\26\u013f\n\26\3\27\3\27\3\27\5\27\u0144\n")
        buf.write("\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\5\31\u0150\n\31\3\31\3\31\3\31\3\32\3\32\5\32\u0157\n")
        buf.write("\32\3\32\3\32\3\32\5\32\u015c\n\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\5\34\u0166\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u016d\n\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0176\n\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\5#\u018a\n#\3$\3$\3$\3$\3%")
        buf.write("\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u019d\n\'")
        buf.write("\3(\3(\3(\5(\u01a2\n(\3(\3(\3)\3)\3)\3)\3*\3*\3*\5*\u01ad")
        buf.write("\n*\3+\3+\3+\3+\5+\u01b3\n+\3,\3,\3,\3,\3,\5,\u01ba\n")
        buf.write(",\3-\3-\3-\3-\5-\u01c0\n-\3.\3.\3.\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01de")
        buf.write("\n\60\3\61\3\61\5\61\u01e2\n\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01ef\n\64\3\65")
        buf.write("\3\65\5\65\u01f3\n\65\3\66\3\66\3\67\3\67\3\67\3\67\3")
        buf.write("8\38\38\38\58\u01ff\n8\39\39\39\39\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\5;\u020e\n;\3<\3<\5<\u0212\n<\3=\3=\3=\3=\3=\3")
        buf.write(">\3>\5>\u021b\n>\3?\3?\3?\3?\3?\5?\u0222\n?\3@\3@\3@\3")
        buf.write("@\3A\5A\u0229\nA\3A\3A\3B\3B\5B\u022f\nB\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\5D\u023b\nD\3E\3E\3F\3F\3F\2\b\n\f\16")
        buf.write("\20\22\26G\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|")
        buf.write("~\u0080\u0082\u0084\u0086\u0088\u008a\2\6\3\2$)\3\2\17")
        buf.write("\22\3\2\33 \3\388\2\u0241\2\u008c\3\2\2\2\4\u0093\3\2")
        buf.write("\2\2\6\u009a\3\2\2\2\b\u00a7\3\2\2\2\n\u00ab\3\2\2\2\f")
        buf.write("\u00b6\3\2\2\2\16\u00c1\3\2\2\2\20\u00cd\3\2\2\2\22\u00db")
        buf.write("\3\2\2\2\24\u00f1\3\2\2\2\26\u00f8\3\2\2\2\30\u0111\3")
        buf.write("\2\2\2\32\u0115\3\2\2\2\34\u0117\3\2\2\2\36\u011e\3\2")
        buf.write("\2\2 \u0120\3\2\2\2\"\u0124\3\2\2\2$\u012a\3\2\2\2&\u0131")
        buf.write("\3\2\2\2(\u013a\3\2\2\2*\u013e\3\2\2\2,\u0140\3\2\2\2")
        buf.write(".\u0148\3\2\2\2\60\u014c\3\2\2\2\62\u0154\3\2\2\2\64\u015f")
        buf.write("\3\2\2\2\66\u0165\3\2\2\28\u016c\3\2\2\2:\u016e\3\2\2")
        buf.write("\2<\u0175\3\2\2\2>\u0177\3\2\2\2@\u017c\3\2\2\2B\u0181")
        buf.write("\3\2\2\2D\u0189\3\2\2\2F\u018b\3\2\2\2H\u018f\3\2\2\2")
        buf.write("J\u0194\3\2\2\2L\u019c\3\2\2\2N\u019e\3\2\2\2P\u01a5\3")
        buf.write("\2\2\2R\u01a9\3\2\2\2T\u01ae\3\2\2\2V\u01b4\3\2\2\2X\u01bf")
        buf.write("\3\2\2\2Z\u01c1\3\2\2\2\\\u01c4\3\2\2\2^\u01dd\3\2\2\2")
        buf.write("`\u01e1\3\2\2\2b\u01e3\3\2\2\2d\u01e5\3\2\2\2f\u01ee\3")
        buf.write("\2\2\2h\u01f0\3\2\2\2j\u01f4\3\2\2\2l\u01f6\3\2\2\2n\u01fe")
        buf.write("\3\2\2\2p\u0200\3\2\2\2r\u0204\3\2\2\2t\u020d\3\2\2\2")
        buf.write("v\u0211\3\2\2\2x\u0213\3\2\2\2z\u021a\3\2\2\2|\u0221\3")
        buf.write("\2\2\2~\u0223\3\2\2\2\u0080\u0228\3\2\2\2\u0082\u022e")
        buf.write("\3\2\2\2\u0084\u0230\3\2\2\2\u0086\u023a\3\2\2\2\u0088")
        buf.write("\u023c\3\2\2\2\u008a\u023e\3\2\2\2\u008c\u008d\5\4\3\2")
        buf.write("\u008d\u008e\7\2\2\3\u008e\3\3\2\2\2\u008f\u0090\5\6\4")
        buf.write("\2\u0090\u0091\5\4\3\2\u0091\u0094\3\2\2\2\u0092\u0094")
        buf.write("\5\6\4\2\u0093\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\5\3\2\2\2\u0095\u009b\5*\26\2\u0096\u009b\5\60\31\2\u0097")
        buf.write("\u009b\5\62\32\2\u0098\u009b\5@!\2\u0099\u009b\5H%\2\u009a")
        buf.write("\u0095\3\2\2\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009d\5\u008aF\2\u009d\7\3\2\2\2\u009e\u00a8")
        buf.write("\5*\26\2\u009f\u00a8\5\60\31\2\u00a0\u00a8\5P)\2\u00a1")
        buf.write("\u00a8\5R*\2\u00a2\u00a8\5^\60\2\u00a3\u00a8\5b\62\2\u00a4")
        buf.write("\u00a8\5d\63\2\u00a5\u00a8\5f\64\2\u00a6\u00a8\5h\65\2")
        buf.write("\u00a7\u009e\3\2\2\2\u00a7\u009f\3\2\2\2\u00a7\u00a0\3")
        buf.write("\2\2\2\u00a7\u00a1\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3")
        buf.write("\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\5\u008a")
        buf.write("F\2\u00aa\t\3\2\2\2\u00ab\u00ac\b\6\1\2\u00ac\u00ad\5")
        buf.write("\f\7\2\u00ad\u00b3\3\2\2\2\u00ae\u00af\f\4\2\2\u00af\u00b0")
        buf.write("\7\"\2\2\u00b0\u00b2\5\f\7\2\u00b1\u00ae\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\13\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\b\7")
        buf.write("\1\2\u00b7\u00b8\5\16\b\2\u00b8\u00be\3\2\2\2\u00b9\u00ba")
        buf.write("\f\4\2\2\u00ba\u00bb\7!\2\2\u00bb\u00bd\5\16\b\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\r\3\2\2\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c1\u00c2\b\b\1\2\u00c2\u00c3\5\20\t\2\u00c3\u00ca")
        buf.write("\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5\u00c6\5\u0088E\2\u00c6")
        buf.write("\u00c7\5\20\t\2\u00c7\u00c9\3\2\2\2\u00c8\u00c4\3\2\2")
        buf.write("\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb\17\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce")
        buf.write("\b\t\1\2\u00ce\u00cf\5\22\n\2\u00cf\u00d8\3\2\2\2\u00d0")
        buf.write("\u00d1\f\5\2\2\u00d1\u00d2\7,\2\2\u00d2\u00d7\5\22\n\2")
        buf.write("\u00d3\u00d4\f\4\2\2\u00d4\u00d5\7-\2\2\u00d5\u00d7\5")
        buf.write("\22\n\2\u00d6\u00d0\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\21\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\b\n")
        buf.write("\1\2\u00dc\u00dd\5\24\13\2\u00dd\u00e9\3\2\2\2\u00de\u00df")
        buf.write("\f\6\2\2\u00df\u00e0\7.\2\2\u00e0\u00e8\5\24\13\2\u00e1")
        buf.write("\u00e2\f\5\2\2\u00e2\u00e3\7/\2\2\u00e3\u00e8\5\24\13")
        buf.write("\2\u00e4\u00e5\f\4\2\2\u00e5\u00e6\7\60\2\2\u00e6\u00e8")
        buf.write("\5\24\13\2\u00e7\u00de\3\2\2\2\u00e7\u00e1\3\2\2\2\u00e7")
        buf.write("\u00e4\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\23\3\2\2\2\u00eb\u00e9\3\2")
        buf.write("\2\2\u00ec\u00ed\7#\2\2\u00ed\u00f2\5\24\13\2\u00ee\u00ef")
        buf.write("\7-\2\2\u00ef\u00f2\5\24\13\2\u00f0\u00f2\5\26\f\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2\25\3\2\2\2\u00f3\u00f4\b\f\1\2\u00f4\u00f9\5\30")
        buf.write("\r\2\u00f5\u00f6\5\30\r\2\u00f6\u00f7\5\36\20\2\u00f7")
        buf.write("\u00f9\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f8\u00f5\3\2\2\2")
        buf.write("\u00f9\u0108\3\2\2\2\u00fa\u00fb\f\b\2\2\u00fb\u0107\5")
        buf.write("\34\17\2\u00fc\u00fd\f\7\2\2\u00fd\u0107\5\"\22\2\u00fe")
        buf.write("\u00ff\f\5\2\2\u00ff\u0100\5\34\17\2\u0100\u0101\5\36")
        buf.write("\20\2\u0101\u0107\3\2\2\2\u0102\u0103\f\4\2\2\u0103\u0104")
        buf.write("\5\"\22\2\u0104\u0105\5\36\20\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u00fa\3\2\2\2\u0106\u00fc\3\2\2\2\u0106\u00fe\3\2\2\2")
        buf.write("\u0106\u0102\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3")
        buf.write("\2\2\2\u0108\u0109\3\2\2\2\u0109\27\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010b\u010c\7\61\2\2\u010c\u010d\5\n\6\2\u010d")
        buf.write("\u010e\7\62\2\2\u010e\u0112\3\2\2\2\u010f\u0112\5\u0086")
        buf.write("D\2\u0110\u0112\7=\2\2\u0111\u010b\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0110\3\2\2\2\u0112\31\3\2\2\2\u0113\u0116")
        buf.write("\5\34\17\2\u0114\u0116\5\"\22\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\33\3\2\2\2\u0117\u0118\7*\2\2\u0118")
        buf.write("\u0119\7=\2\2\u0119\35\3\2\2\2\u011a\u011b\5 \21\2\u011b")
        buf.write("\u011c\5\36\20\2\u011c\u011f\3\2\2\2\u011d\u011f\5 \21")
        buf.write("\2\u011e\u011a\3\2\2\2\u011e\u011d\3\2\2\2\u011f\37\3")
        buf.write("\2\2\2\u0120\u0121\7\63\2\2\u0121\u0122\5\n\6\2\u0122")
        buf.write("\u0123\7\64\2\2\u0123!\3\2\2\2\u0124\u0125\7\61\2\2\u0125")
        buf.write("\u0126\5$\23\2\u0126\u0127\7\62\2\2\u0127#\3\2\2\2\u0128")
        buf.write("\u012b\5&\24\2\u0129\u012b\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u0129\3\2\2\2\u012b%\3\2\2\2\u012c\u012d\5\n\6")
        buf.write("\2\u012d\u012e\7\67\2\2\u012e\u012f\5&\24\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u0132\5\n\6\2\u0131\u012c\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\'\3\2\2\2\u0133\u0134\5\26\f\2\u0134")
        buf.write("\u0135\5\34\17\2\u0135\u013b\3\2\2\2\u0136\u0137\5\26")
        buf.write("\f\2\u0137\u0138\5\36\20\2\u0138\u013b\3\2\2\2\u0139\u013b")
        buf.write("\7=\2\2\u013a\u0133\3\2\2\2\u013a\u0136\3\2\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b)\3\2\2\2\u013c\u013f\5,\27\2\u013d")
        buf.write("\u013f\5.\30\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f+\3\2\2\2\u0140\u0141\7\24\2\2\u0141\u0143\7=\2")
        buf.write("\2\u0142\u0144\5\u0080A\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\7+\2\2\u0146")
        buf.write("\u0147\5\n\6\2\u0147-\3\2\2\2\u0148\u0149\7\24\2\2\u0149")
        buf.write("\u014a\7=\2\2\u014a\u014b\5\u0080A\2\u014b/\3\2\2\2\u014c")
        buf.write("\u014d\7\23\2\2\u014d\u014f\7=\2\2\u014e\u0150\5\u0080")
        buf.write("A\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0152\7+\2\2\u0152\u0153\5\n\6\2\u0153")
        buf.write("\61\3\2\2\2\u0154\u0156\7\13\2\2\u0155\u0157\5> \2\u0156")
        buf.write("\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\7=\2\2\u0159\u015b\5\64\33\2\u015a\u015c")
        buf.write("\5\u0080A\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\5l\67\2\u015e\63\3\2\2\2\u015f")
        buf.write("\u0160\7\61\2\2\u0160\u0161\5\66\34\2\u0161\u0162\7\62")
        buf.write("\2\2\u0162\65\3\2\2\2\u0163\u0166\58\35\2\u0164\u0166")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\67\3\2\2\2\u0167\u0168\5:\36\2\u0168\u0169\7\67\2\2\u0169")
        buf.write("\u016a\58\35\2\u016a\u016d\3\2\2\2\u016b\u016d\5:\36\2")
        buf.write("\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016d9\3\2\2")
        buf.write("\2\u016e\u016f\5<\37\2\u016f\u0170\5\u0080A\2\u0170;\3")
        buf.write("\2\2\2\u0171\u0172\7=\2\2\u0172\u0173\7\67\2\2\u0173\u0176")
        buf.write("\5<\37\2\u0174\u0176\7=\2\2\u0175\u0171\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176=\3\2\2\2\u0177\u0178\7\61\2\2\u0178")
        buf.write("\u0179\7=\2\2\u0179\u017a\7=\2\2\u017a\u017b\7\62\2\2")
        buf.write("\u017b?\3\2\2\2\u017c\u017d\7\f\2\2\u017d\u017e\7=\2\2")
        buf.write("\u017e\u017f\7\r\2\2\u017f\u0180\5B\"\2\u0180A\3\2\2\2")
        buf.write("\u0181\u0182\7\65\2\2\u0182\u0183\5D#\2\u0183\u0184\7")
        buf.write("\66\2\2\u0184C\3\2\2\2\u0185\u0186\5F$\2\u0186\u0187\5")
        buf.write("D#\2\u0187\u018a\3\2\2\2\u0188\u018a\5F$\2\u0189\u0185")
        buf.write("\3\2\2\2\u0189\u0188\3\2\2\2\u018aE\3\2\2\2\u018b\u018c")
        buf.write("\7=\2\2\u018c\u018d\5\u0080A\2\u018d\u018e\5\u008aF\2")
        buf.write("\u018eG\3\2\2\2\u018f\u0190\7\f\2\2\u0190\u0191\7=\2\2")
        buf.write("\u0191\u0192\7\16\2\2\u0192\u0193\5J&\2\u0193I\3\2\2\2")
        buf.write("\u0194\u0195\7\65\2\2\u0195\u0196\5L\'\2\u0196\u0197\7")
        buf.write("\66\2\2\u0197K\3\2\2\2\u0198\u0199\5N(\2\u0199\u019a\5")
        buf.write("L\'\2\u019a\u019d\3\2\2\2\u019b\u019d\5N(\2\u019c\u0198")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019dM\3\2\2\2\u019e\u019f")
        buf.write("\7=\2\2\u019f\u01a1\5\64\33\2\u01a0\u01a2\5\u0080A\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a4\5\u008aF\2\u01a4O\3\2\2\2\u01a5\u01a6\5(")
        buf.write("\25\2\u01a6\u01a7\5j\66\2\u01a7\u01a8\5\n\6\2\u01a8Q\3")
        buf.write("\2\2\2\u01a9\u01aa\5T+\2\u01aa\u01ac\5X-\2\u01ab\u01ad")
        buf.write("\5Z.\2\u01ac\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01adS")
        buf.write("\3\2\2\2\u01ae\u01af\7\7\2\2\u01af\u01b0\5\\/\2\u01b0")
        buf.write("\u01b2\5l\67\2\u01b1\u01b3\5\u008aF\2\u01b2\u01b1\3\2")
        buf.write("\2\2\u01b2\u01b3\3\2\2\2\u01b3U\3\2\2\2\u01b4\u01b5\7")
        buf.write("\b\2\2\u01b5\u01b6\7\7\2\2\u01b6\u01b7\5\\/\2\u01b7\u01b9")
        buf.write("\5l\67\2\u01b8\u01ba\5\u008aF\2\u01b9\u01b8\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01baW\3\2\2\2\u01bb\u01bc\5V,\2\u01bc")
        buf.write("\u01bd\5X-\2\u01bd\u01c0\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf")
        buf.write("\u01bb\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0Y\3\2\2\2\u01c1")
        buf.write("\u01c2\7\b\2\2\u01c2\u01c3\5l\67\2\u01c3[\3\2\2\2\u01c4")
        buf.write("\u01c5\7\61\2\2\u01c5\u01c6\5\n\6\2\u01c6\u01c7\7\62\2")
        buf.write("\2\u01c7]\3\2\2\2\u01c8\u01c9\7\t\2\2\u01c9\u01ca\5\n")
        buf.write("\6\2\u01ca\u01cb\5l\67\2\u01cb\u01de\3\2\2\2\u01cc\u01cd")
        buf.write("\7\t\2\2\u01cd\u01ce\5`\61\2\u01ce\u01cf\78\2\2\u01cf")
        buf.write("\u01d0\5\n\6\2\u01d0\u01d1\78\2\2\u01d1\u01d2\5P)\2\u01d2")
        buf.write("\u01d3\5l\67\2\u01d3\u01de\3\2\2\2\u01d4\u01d5\7\t\2\2")
        buf.write("\u01d5\u01d6\7=\2\2\u01d6\u01d7\7\67\2\2\u01d7\u01d8\7")
        buf.write("=\2\2\u01d8\u01d9\7)\2\2\u01d9\u01da\7\27\2\2\u01da\u01db")
        buf.write("\5\n\6\2\u01db\u01dc\5l\67\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01c8\3\2\2\2\u01dd\u01cc\3\2\2\2\u01dd\u01d4\3\2\2\2")
        buf.write("\u01de_\3\2\2\2\u01df\u01e2\5,\27\2\u01e0\u01e2\5P)\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2a\3\2\2")
        buf.write("\2\u01e3\u01e4\7\26\2\2\u01e4c\3\2\2\2\u01e5\u01e6\7\25")
        buf.write("\2\2\u01e6e\3\2\2\2\u01e7\u01e8\7=\2\2\u01e8\u01ef\5\"")
        buf.write("\22\2\u01e9\u01ea\5\26\f\2\u01ea\u01eb\7*\2\2\u01eb\u01ec")
        buf.write("\7=\2\2\u01ec\u01ed\5\"\22\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write("\u01e7\3\2\2\2\u01ee\u01e9\3\2\2\2\u01efg\3\2\2\2\u01f0")
        buf.write("\u01f2\7\n\2\2\u01f1\u01f3\5\n\6\2\u01f2\u01f1\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3i\3\2\2\2\u01f4\u01f5\t\2\2")
        buf.write("\2\u01f5k\3\2\2\2\u01f6\u01f7\7\65\2\2\u01f7\u01f8\5n")
        buf.write("8\2\u01f8\u01f9\7\66\2\2\u01f9m\3\2\2\2\u01fa\u01fb\5")
        buf.write("\b\5\2\u01fb\u01fc\5n8\2\u01fc\u01ff\3\2\2\2\u01fd\u01ff")
        buf.write("\5\b\5\2\u01fe\u01fa\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("o\3\2\2\2\u0200\u0201\5\36\20\2\u0201\u0202\5\u0082B\2")
        buf.write("\u0202\u0203\5r:\2\u0203q\3\2\2\2\u0204\u0205\7\65\2\2")
        buf.write("\u0205\u0206\5t;\2\u0206\u0207\7\66\2\2\u0207s\3\2\2\2")
        buf.write("\u0208\u0209\5v<\2\u0209\u020a\7\67\2\2\u020a\u020b\5")
        buf.write("t;\2\u020b\u020e\3\2\2\2\u020c\u020e\5v<\2\u020d\u0208")
        buf.write("\3\2\2\2\u020d\u020c\3\2\2\2\u020eu\3\2\2\2\u020f\u0212")
        buf.write("\5\n\6\2\u0210\u0212\5r:\2\u0211\u020f\3\2\2\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212w\3\2\2\2\u0213\u0214\7=\2\2\u0214\u0215")
        buf.write("\7\65\2\2\u0215\u0216\5z>\2\u0216\u0217\7\66\2\2\u0217")
        buf.write("y\3\2\2\2\u0218\u021b\5|?\2\u0219\u021b\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021a\u0219\3\2\2\2\u021b{\3\2\2\2\u021c")
        buf.write("\u021d\5~@\2\u021d\u021e\7\67\2\2\u021e\u021f\5|?\2\u021f")
        buf.write("\u0222\3\2\2\2\u0220\u0222\5~@\2\u0221\u021c\3\2\2\2\u0221")
        buf.write("\u0220\3\2\2\2\u0222}\3\2\2\2\u0223\u0224\7=\2\2\u0224")
        buf.write("\u0225\79\2\2\u0225\u0226\5\n\6\2\u0226\177\3\2\2\2\u0227")
        buf.write("\u0229\5\36\20\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2")
        buf.write("\2\u0229\u022a\3\2\2\2\u022a\u022b\5\u0082B\2\u022b\u0081")
        buf.write("\3\2\2\2\u022c\u022f\5\u0084C\2\u022d\u022f\7=\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f\u0083\3\2\2\2")
        buf.write("\u0230\u0231\t\3\2\2\u0231\u0085\3\2\2\2\u0232\u023b\7")
        buf.write(";\2\2\u0233\u023b\7:\2\2\u0234\u023b\7<\2\2\u0235\u023b")
        buf.write("\7\31\2\2\u0236\u023b\7\32\2\2\u0237\u023b\7\30\2\2\u0238")
        buf.write("\u023b\5x=\2\u0239\u023b\5p9\2\u023a\u0232\3\2\2\2\u023a")
        buf.write("\u0233\3\2\2\2\u023a\u0234\3\2\2\2\u023a\u0235\3\2\2\2")
        buf.write("\u023a\u0236\3\2\2\2\u023a\u0237\3\2\2\2\u023a\u0238\3")
        buf.write("\2\2\2\u023a\u0239\3\2\2\2\u023b\u0087\3\2\2\2\u023c\u023d")
        buf.write("\t\4\2\2\u023d\u0089\3\2\2\2\u023e\u023f\t\5\2\2\u023f")
        buf.write("\u008b\3\2\2\2\61\u0093\u009a\u00a7\u00b3\u00be\u00ca")
        buf.write("\u00d6\u00d8\u00e7\u00e9\u00f1\u00f8\u0106\u0108\u0111")
        buf.write("\u0115\u011e\u012a\u0131\u013a\u013e\u0143\u014f\u0156")
        buf.write("\u015b\u0165\u016c\u0175\u0189\u019c\u01a1\u01ac\u01b2")
        buf.write("\u01b9\u01bf\u01dd\u01e1\u01ee\u01f2\u01fe\u020d\u0211")
        buf.write("\u021a\u0221\u0228\u022e\u023a")
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
                     "'false'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "':='", "'.'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "EQCOM", 
                      "DIFFCOM", "LESSCOM", "LEQCOM", "GRECOM", "GEQCOM", 
                      "AND", "OR", "NOT", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", 
                      "DIVASSIGN", "MODASSIGN", "ASSIGN", "DOT", "EQUAL", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", "LSB", 
                      "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", 
                      "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl_lst = 1
    RULE_decl = 2
    RULE_stmt = 3
    RULE_expr = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_expr4 = 8
    RULE_expr5 = 9
    RULE_expr6 = 10
    RULE_expr7 = 11
    RULE_tail = 12
    RULE_field_access_tail = 13
    RULE_arridx_nnlst = 14
    RULE_arridx = 15
    RULE_funccall_tail = 16
    RULE_expr_lst = 17
    RULE_expr_lstprime = 18
    RULE_lhs = 19
    RULE_var_decl = 20
    RULE_withInit_var_decl = 21
    RULE_withoutInit_var_decl = 22
    RULE_const_decl = 23
    RULE_func_decl = 24
    RULE_funcparam = 25
    RULE_param_lst = 26
    RULE_param_lstprime = 27
    RULE_param = 28
    RULE_id_nnlst = 29
    RULE_receiver = 30
    RULE_struct_decl = 31
    RULE_structfield = 32
    RULE_fielddecl_nnlst = 33
    RULE_fielddecl = 34
    RULE_interface_decl = 35
    RULE_interfacemeth = 36
    RULE_interfacemeth_nnlst = 37
    RULE_interfacemethmem = 38
    RULE_assigning_stmt = 39
    RULE_ifelse_stmt = 40
    RULE_if_ = 41
    RULE_elseif_ = 42
    RULE_elseif_lst = 43
    RULE_else_ = 44
    RULE_condition = 45
    RULE_forloop_stmt = 46
    RULE_forloop_init = 47
    RULE_break_stmt = 48
    RULE_continue_stmt = 49
    RULE_funccall_stmt = 50
    RULE_return_stmt = 51
    RULE_assign = 52
    RULE_blockcode = 53
    RULE_stmt_nnlst = 54
    RULE_arr_literal = 55
    RULE_arrvalue = 56
    RULE_arrelem_lst = 57
    RULE_arrelem = 58
    RULE_struct_literal = 59
    RULE_structparam_lst = 60
    RULE_structparam_lstprime = 61
    RULE_structparam = 62
    RULE_data_type = 63
    RULE_prime_datatype = 64
    RULE_primitive_datatype = 65
    RULE_literal = 66
    RULE_compare_op = 67
    RULE_end_stm = 68

    ruleNames =  [ "program", "decl_lst", "decl", "stmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "tail", "field_access_tail", "arridx_nnlst", "arridx", 
                   "funccall_tail", "expr_lst", "expr_lstprime", "lhs", 
                   "var_decl", "withInit_var_decl", "withoutInit_var_decl", 
                   "const_decl", "func_decl", "funcparam", "param_lst", 
                   "param_lstprime", "param", "id_nnlst", "receiver", "struct_decl", 
                   "structfield", "fielddecl_nnlst", "fielddecl", "interface_decl", 
                   "interfacemeth", "interfacemeth_nnlst", "interfacemethmem", 
                   "assigning_stmt", "ifelse_stmt", "if_", "elseif_", "elseif_lst", 
                   "else_", "condition", "forloop_stmt", "forloop_init", 
                   "break_stmt", "continue_stmt", "funccall_stmt", "return_stmt", 
                   "assign", "blockcode", "stmt_nnlst", "arr_literal", "arrvalue", 
                   "arrelem_lst", "arrelem", "struct_literal", "structparam_lst", 
                   "structparam_lstprime", "structparam", "data_type", "prime_datatype", 
                   "primitive_datatype", "literal", "compare_op", "end_stm" ]

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
    EQCOM=25
    DIFFCOM=26
    LESSCOM=27
    LEQCOM=28
    GRECOM=29
    GEQCOM=30
    AND=31
    OR=32
    NOT=33
    ADDASSIGN=34
    SUBASSIGN=35
    MULASSIGN=36
    DIVASSIGN=37
    MODASSIGN=38
    ASSIGN=39
    DOT=40
    EQUAL=41
    ADD=42
    SUB=43
    MUL=44
    DIV=45
    MOD=46
    LP=47
    RP=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    COMMA=53
    SEMICOLON=54
    COLON=55
    FLOAT=56
    INTEGER=57
    STRING=58
    ID=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62

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

        def decl_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_lstContext,0)


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
            self.state = 138
            self.decl_lst()
            self.state = 139
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_lst" ):
                return visitor.visitDecl_lst(self)
            else:
                return visitor.visitChildren(self)




    def decl_lst(self):

        localctx = MiniGoParser.Decl_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_lst)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.decl()
                self.state = 142
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 147
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 148
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 149
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 150
                self.struct_decl()
                pass

            elif la_ == 5:
                self.state = 151
                self.interface_decl()
                pass


            self.state = 154
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def ifelse_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_stmtContext,0)


        def forloop_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def funccall_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 156
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 157
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 158
                self.assigning_stmt()
                pass

            elif la_ == 4:
                self.state = 159
                self.ifelse_stmt()
                pass

            elif la_ == 5:
                self.state = 160
                self.forloop_stmt()
                pass

            elif la_ == 6:
                self.state = 161
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 162
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 163
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.state = 164
                self.return_stmt()
                pass


            self.state = 167
            self.end_stm()
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
            self.state = 170
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    self.match(MiniGoParser.OR)
                    self.state = 174
                    self.expr1(0) 
                self.state = 179
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
            self.state = 181
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    self.match(MiniGoParser.AND)
                    self.state = 185
                    self.expr2(0) 
                self.state = 190
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


        def compare_op(self):
            return self.getTypedRuleContext(MiniGoParser.Compare_opContext,0)


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
            self.state = 192
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    self.compare_op()
                    self.state = 196
                    self.expr3(0) 
                self.state = 202
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
            self.state = 204
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 206
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 207
                        self.match(MiniGoParser.ADD)
                        self.state = 208
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 209
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 210
                        self.match(MiniGoParser.SUB)
                        self.state = 211
                        self.expr4(0)
                        pass

             
                self.state = 216
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
            self.state = 218
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 229
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 220
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 221
                        self.match(MiniGoParser.MUL)
                        self.state = 222
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 223
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 224
                        self.match(MiniGoParser.DIV)
                        self.state = 225
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 226
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 227
                        self.match(MiniGoParser.MOD)
                        self.state = 228
                        self.expr5()
                        pass

             
                self.state = 233
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

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


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
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(MiniGoParser.NOT)
                self.state = 235
                self.expr5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(MiniGoParser.SUB)
                self.state = 237
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
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


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 242
                self.expr7()
                pass

            elif la_ == 2:
                self.state = 243
                self.expr7()
                self.state = 244
                self.arridx_nnlst()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 248
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 249
                        self.field_access_tail()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 250
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 251
                        self.funccall_tail()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 252
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 253
                        self.field_access_tail()
                        self.state = 254
                        self.arridx_nnlst()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 256
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 257
                        self.funccall_tail()
                        self.state = 258
                        self.arridx_nnlst()
                        pass

             
                self.state = 264
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

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(MiniGoParser.LP)
                self.state = 266
                self.expr(0)
                self.state = 267
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail" ):
                return visitor.visitTail(self)
            else:
                return visitor.visitChildren(self)




    def tail(self):

        localctx = MiniGoParser.TailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tail)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.field_access_tail()
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.funccall_tail()
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


    class Field_access_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access_tail" ):
                return visitor.visitField_access_tail(self)
            else:
                return visitor.visitChildren(self)




    def field_access_tail(self):

        localctx = MiniGoParser.Field_access_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_field_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.DOT)
            self.state = 278
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arridx_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArridx_nnlst" ):
                return visitor.visitArridx_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def arridx_nnlst(self):

        localctx = MiniGoParser.Arridx_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arridx_nnlst)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.arridx()
                self.state = 281
                self.arridx_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
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
        self.enterRule(localctx, 30, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MiniGoParser.LSB)
            self.state = 287
            self.expr(0)
            self.state = 288
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_tail" ):
                return visitor.visitFunccall_tail(self)
            else:
                return visitor.visitChildren(self)




    def funccall_tail(self):

        localctx = MiniGoParser.Funccall_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funccall_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.LP)
            self.state = 291
            self.expr_lst()
            self.state = 292
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst" ):
                return visitor.visitExpr_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr_lst(self):

        localctx = MiniGoParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_lst)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expr_lstprime()
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


    class Expr_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_lstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lstprime" ):
                return visitor.visitExpr_lstprime(self)
            else:
                return visitor.visitChildren(self)




    def expr_lstprime(self):

        localctx = MiniGoParser.Expr_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr_lstprime)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.expr(0)
                self.state = 299
                self.match(MiniGoParser.COMMA)
                self.state = 300
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
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

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lhs)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.expr6(0)
                self.state = 306
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.expr6(0)
                self.state = 309
                self.arridx_nnlst()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithInit_var_declContext,0)


        def withoutInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithoutInit_var_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_decl)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.withInit_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.withoutInit_var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithInit_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_withInit_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithInit_var_decl" ):
                return visitor.visitWithInit_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def withInit_var_decl(self):

        localctx = MiniGoParser.WithInit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_withInit_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MiniGoParser.VAR_)
            self.state = 319
            self.match(MiniGoParser.ID)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 320
                self.data_type()


            self.state = 323
            self.match(MiniGoParser.EQUAL)
            self.state = 324
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithoutInit_var_declContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_withoutInit_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithoutInit_var_decl" ):
                return visitor.visitWithoutInit_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def withoutInit_var_decl(self):

        localctx = MiniGoParser.WithoutInit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_withoutInit_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MiniGoParser.VAR_)
            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
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


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MiniGoParser.CONST_)
            self.state = 331
            self.match(MiniGoParser.ID)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 332
                self.data_type()


            self.state = 335
            self.match(MiniGoParser.EQUAL)
            self.state = 336
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
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


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MiniGoParser.FUNC_)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LP:
                self.state = 339
                self.receiver()


            self.state = 342
            self.match(MiniGoParser.ID)
            self.state = 343
            self.funcparam()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 344
                self.data_type()


            self.state = 347
            self.blockcode()
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

        def param_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstContext,0)


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
        self.enterRule(localctx, 50, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MiniGoParser.LP)
            self.state = 350
            self.param_lst()
            self.state = 351
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = MiniGoParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param_lst)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.param_lstprime()
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


    class Param_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_lstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lstprime" ):
                return visitor.visitParam_lstprime(self)
            else:
                return visitor.visitChildren(self)




    def param_lstprime(self):

        localctx = MiniGoParser.Param_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param_lstprime)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.param()
                self.state = 358
                self.match(MiniGoParser.COMMA)
                self.state = 359
                self.param_lstprime()
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

        def id_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_nnlstContext,0)


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
        self.enterRule(localctx, 56, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.id_nnlst()
            self.state = 365
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_nnlst" ):
                return visitor.visitId_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def id_nnlst(self):

        localctx = MiniGoParser.Id_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_id_nnlst)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(MiniGoParser.ID)
                self.state = 368
                self.match(MiniGoParser.COMMA)
                self.state = 369
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 60, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(MiniGoParser.LP)
            self.state = 374
            self.match(MiniGoParser.ID)
            self.state = 375
            self.match(MiniGoParser.ID)
            self.state = 376
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_struct_decl)
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

        def fielddecl_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Fielddecl_nnlstContext,0)


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
        self.enterRule(localctx, 64, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MiniGoParser.LCB)
            self.state = 384
            self.fielddecl_nnlst()
            self.state = 385
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fielddecl_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self):
            return self.getTypedRuleContext(MiniGoParser.FielddeclContext,0)


        def fielddecl_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Fielddecl_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl_nnlst" ):
                return visitor.visitFielddecl_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl_nnlst(self):

        localctx = MiniGoParser.Fielddecl_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fielddecl_nnlst)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.fielddecl()
                self.state = 388
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.fielddecl()
                pass


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.ID)
            self.state = 394
            self.data_type()
            self.state = 395
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
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

        def interfacemeth(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacemethContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(MiniGoParser.TYPE_)
            self.state = 398
            self.match(MiniGoParser.ID)
            self.state = 399
            self.match(MiniGoParser.INTERFACE_)
            self.state = 400
            self.interfacemeth()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacemethContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def interfacemeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfacemeth_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacemeth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacemeth" ):
                return visitor.visitInterfacemeth(self)
            else:
                return visitor.visitChildren(self)




    def interfacemeth(self):

        localctx = MiniGoParser.InterfacemethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_interfacemeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MiniGoParser.LCB)
            self.state = 403
            self.interfacemeth_nnlst()
            self.state = 404
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interfacemeth_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfacemethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacemethmemContext,0)


        def interfacemeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfacemeth_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacemeth_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacemeth_nnlst" ):
                return visitor.visitInterfacemeth_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def interfacemeth_nnlst(self):

        localctx = MiniGoParser.Interfacemeth_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_interfacemeth_nnlst)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.interfacemethmem()
                self.state = 407
                self.interfacemeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.interfacemethmem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacemethmemContext(ParserRuleContext):
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
            return MiniGoParser.RULE_interfacemethmem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacemethmem" ):
                return visitor.visitInterfacemethmem(self)
            else:
                return visitor.visitChildren(self)




    def interfacemethmem(self):

        localctx = MiniGoParser.InterfacemethmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_interfacemethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MiniGoParser.ID)
            self.state = 413
            self.funcparam()
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 414
                self.data_type()


            self.state = 417
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assigning_stmtContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigning_stmt" ):
                return visitor.visitAssigning_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assigning_stmt(self):

        localctx = MiniGoParser.Assigning_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_assigning_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.lhs()
            self.state = 420
            self.assign()
            self.state = 421
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelse_stmtContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse_stmt" ):
                return visitor.visitIfelse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ifelse_stmt(self):

        localctx = MiniGoParser.Ifelse_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_ifelse_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.if_()
            self.state = 424
            self.elseif_lst()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE_:
                self.state = 425
                self.else_()


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
        self.enterRule(localctx, 82, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(MiniGoParser.IF_)
            self.state = 429
            self.condition()
            self.state = 430
            self.blockcode()
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 431
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
        self.enterRule(localctx, 84, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.ELSE_)
            self.state = 435
            self.match(MiniGoParser.IF_)
            self.state = 436
            self.condition()
            self.state = 437
            self.blockcode()
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 438
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
        self.enterRule(localctx, 86, self.RULE_elseif_lst)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.elseif_()
                self.state = 442
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
        self.enterRule(localctx, 88, self.RULE_else_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(MiniGoParser.ELSE_)
            self.state = 448
            self.blockcode()
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
        self.enterRule(localctx, 90, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.LP)
            self.state = 451
            self.expr(0)
            self.state = 452
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStepContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def forloop_init(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_initContext,0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStep" ):
                return visitor.visitForStep(self)
            else:
                return visitor.visitChildren(self)


    class ForBasicContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBasic" ):
                return visitor.visitForBasic(self)
            else:
                return visitor.visitChildren(self)


    class ForEachContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)
        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)
        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)
        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForEach" ):
                return visitor.visitForEach(self)
            else:
                return visitor.visitChildren(self)



    def forloop_stmt(self):

        localctx = MiniGoParser.Forloop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forloop_stmt)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ForBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(MiniGoParser.FOR_)
                self.state = 455
                self.expr(0)
                self.state = 456
                self.blockcode()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.ForStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.match(MiniGoParser.FOR_)
                self.state = 459
                self.forloop_init()
                self.state = 460
                self.match(MiniGoParser.SEMICOLON)
                self.state = 461
                self.expr(0)
                self.state = 462
                self.match(MiniGoParser.SEMICOLON)
                self.state = 463
                self.assigning_stmt()
                self.state = 464
                self.blockcode()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.match(MiniGoParser.FOR_)
                self.state = 467
                self.match(MiniGoParser.ID)
                self.state = 468
                self.match(MiniGoParser.COMMA)
                self.state = 469
                self.match(MiniGoParser.ID)
                self.state = 470
                self.match(MiniGoParser.ASSIGN)
                self.state = 471
                self.match(MiniGoParser.RANGE_)
                self.state = 472
                self.expr(0)
                self.state = 473
                self.blockcode()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithInit_var_declContext,0)


        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_init" ):
                return visitor.visitForloop_init(self)
            else:
                return visitor.visitChildren(self)




    def forloop_init(self):

        localctx = MiniGoParser.Forloop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forloop_init)
        try:
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.withInit_var_decl()
                pass
            elif token in [MiniGoParser.NIL_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.assigning_stmt()
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


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.BREAK_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(MiniGoParser.CONTINUE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.CONTINUE_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_stmt" ):
                return visitor.visitFunccall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def funccall_stmt(self):

        localctx = MiniGoParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_funccall_stmt)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(MiniGoParser.ID)
                self.state = 486
                self.funccall_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.expr6(0)
                self.state = 488
                self.match(MiniGoParser.DOT)
                self.state = 489
                self.match(MiniGoParser.ID)
                self.state = 490
                self.funccall_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(MiniGoParser.RETURN_, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.RETURN_)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 495
                self.expr(0)


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADDASSIGN(self):
            return self.getToken(MiniGoParser.ADDASSIGN, 0)

        def SUBASSIGN(self):
            return self.getToken(MiniGoParser.SUBASSIGN, 0)

        def MULASSIGN(self):
            return self.getToken(MiniGoParser.MULASSIGN, 0)

        def DIVASSIGN(self):
            return self.getToken(MiniGoParser.DIVASSIGN, 0)

        def MODASSIGN(self):
            return self.getToken(MiniGoParser.MODASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADDASSIGN) | (1 << MiniGoParser.SUBASSIGN) | (1 << MiniGoParser.MULASSIGN) | (1 << MiniGoParser.DIVASSIGN) | (1 << MiniGoParser.MODASSIGN) | (1 << MiniGoParser.ASSIGN))) != 0)):
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

        def stmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_nnlstContext,0)


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
        self.enterRule(localctx, 106, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.LCB)
            self.state = 501
            self.stmt_nnlst()
            self.state = 502
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_nnlst" ):
                return visitor.visitStmt_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def stmt_nnlst(self):

        localctx = MiniGoParser.Stmt_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_nnlst)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.stmt()
                self.state = 505
                self.stmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.stmt()
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

        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def prime_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Prime_datatypeContext,0)


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_literal" ):
                return visitor.visitArr_literal(self)
            else:
                return visitor.visitChildren(self)




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.arridx_nnlst()
            self.state = 511
            self.prime_datatype()
            self.state = 512
            self.arrvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def arrelem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arrelem_lstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrvalue" ):
                return visitor.visitArrvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrvalue(self):

        localctx = MiniGoParser.ArrvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LCB)
            self.state = 515
            self.arrelem_lst()
            self.state = 516
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrelem_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrelem(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrelem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arrelem_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrelem_lst" ):
                return visitor.visitArrelem_lst(self)
            else:
                return visitor.visitChildren(self)




    def arrelem_lst(self):

        localctx = MiniGoParser.Arrelem_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arrelem_lst)
        try:
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.arrelem()
                self.state = 519
                self.match(MiniGoParser.COMMA)
                self.state = 520
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
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


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrelem" ):
                return visitor.visitArrelem(self)
            else:
                return visitor.visitChildren(self)




    def arrelem(self):

        localctx = MiniGoParser.ArrelemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arrelem)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL_, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.arrvalue()
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

        def structparam_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstContext,0)


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
        self.enterRule(localctx, 118, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(MiniGoParser.ID)
            self.state = 530
            self.match(MiniGoParser.LCB)
            self.state = 531
            self.structparam_lst()
            self.state = 532
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structparam_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparam_lst" ):
                return visitor.visitStructparam_lst(self)
            else:
                return visitor.visitChildren(self)




    def structparam_lst(self):

        localctx = MiniGoParser.Structparam_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_structparam_lst)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.structparam_lstprime()
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


    class Structparam_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structparam_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam_lstprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparam_lstprime" ):
                return visitor.visitStructparam_lstprime(self)
            else:
                return visitor.visitChildren(self)




    def structparam_lstprime(self):

        localctx = MiniGoParser.Structparam_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_structparam_lstprime)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.structparam()
                self.state = 539
                self.match(MiniGoParser.COMMA)
                self.state = 540
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructparam" ):
                return visitor.visitStructparam(self)
            else:
                return visitor.visitChildren(self)




    def structparam(self):

        localctx = MiniGoParser.StructparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(MiniGoParser.ID)
            self.state = 546
            self.match(MiniGoParser.COLON)
            self.state = 547
            self.expr(0)
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

        def prime_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Prime_datatypeContext,0)


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LSB:
                self.state = 549
                self.arridx_nnlst()


            self.state = 552
            self.prime_datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prime_datatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prime_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrime_datatype" ):
                return visitor.visitPrime_datatype(self)
            else:
                return visitor.visitChildren(self)




    def prime_datatype(self):

        localctx = MiniGoParser.Prime_datatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_prime_datatype)
        try:
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING_, MiniGoParser.INT_, MiniGoParser.FLOAT_, MiniGoParser.BOOLEAN_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.primitive_datatype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
        self.enterRule(localctx, 130, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
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

        def NIL_(self):
            return self.getToken(MiniGoParser.NIL_, 0)

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
        self.enterRule(localctx, 132, self.RULE_literal)
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 562
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 563
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 564
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.NIL_]:
                self.enterOuterAlt(localctx, 6)
                self.state = 565
                self.match(MiniGoParser.NIL_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 566
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 8)
                self.state = 567
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


    class Compare_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQCOM(self):
            return self.getToken(MiniGoParser.EQCOM, 0)

        def DIFFCOM(self):
            return self.getToken(MiniGoParser.DIFFCOM, 0)

        def LESSCOM(self):
            return self.getToken(MiniGoParser.LESSCOM, 0)

        def LEQCOM(self):
            return self.getToken(MiniGoParser.LEQCOM, 0)

        def GRECOM(self):
            return self.getToken(MiniGoParser.GRECOM, 0)

        def GEQCOM(self):
            return self.getToken(MiniGoParser.GEQCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_op" ):
                return visitor.visitCompare_op(self)
            else:
                return visitor.visitChildren(self)




    def compare_op(self):

        localctx = MiniGoParser.Compare_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQCOM) | (1 << MiniGoParser.DIFFCOM) | (1 << MiniGoParser.LESSCOM) | (1 << MiniGoParser.LEQCOM) | (1 << MiniGoParser.GRECOM) | (1 << MiniGoParser.GEQCOM))) != 0)):
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
        self.enterRule(localctx, 136, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         




