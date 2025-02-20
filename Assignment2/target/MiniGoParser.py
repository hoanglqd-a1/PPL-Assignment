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
        buf.write("\u0265\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u0098\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00a0\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5\u00a8\n\5\f\5\16\5\u00ab\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00b3\n\6\f\6\16\6\u00b6")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00bf\n\7\f\7\16")
        buf.write("\7\u00c2\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b")
        buf.write("\u00cd\n\b\f\b\16\b\u00d0\13\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00de\n\t\f\t\16\t\u00e1")
        buf.write("\13\t\3\n\3\n\3\n\3\n\3\n\5\n\u00e8\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\7\13\u00ef\n\13\f\13\16\13\u00f2\13\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00fa\n\f\3\r\3\r\3\r\5\r\u00ff")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\5\21\u010e\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u0115\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u0123\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u0137\n\25\3\26\3\26\3")
        buf.write("\26\5\26\u013c\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0150\n\27\3\30\3\30\3\30\3\30\5\30\u0156\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\32\3\32\5\32\u015e\n\32\3\32\3\32")
        buf.write("\3\32\5\32\u0163\n\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\5\34\u016e\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0175\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u017e\n\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\5#\u0193\n#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\5&\u01a0\n&\3\'\3\'\3\'\3\'\3\'\5\'\u01a7")
        buf.write("\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\5+\u01bb\n+\3,\3,\3,\5,\u01c0\n,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\5.\u01cd\n.\3/\3/\3/\3/\3/\5/\u01d4\n")
        buf.write("/\3\60\3\60\3\60\3\60\5\60\u01da\n\60\3\61\3\61\3\61\5")
        buf.write("\61\u01df\n\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01fd")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\5\66\u0209\n\66\3\67\3\67\3\67\38\38\38\39\39\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\5:\u021b\n:\3;\3;\5;\u021f\n;\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\5=\u0229\n=\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\5>\u0235\n>\3?\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3")
        buf.write("A\5A\u0244\nA\3B\3B\5B\u0248\nB\3C\5C\u024b\nC\3C\3C\5")
        buf.write("C\u024f\nC\3C\5C\u0252\nC\3D\3D\3E\3E\3E\3E\3E\3E\3E\5")
        buf.write("E\u025d\nE\3F\3F\3G\3G\3H\3H\3H\2\b\b\n\f\16\20\24I\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\2\6\3\2\17\22\3\2$(\3\2")
        buf.write("\33 \3\388\2\u0263\2\u0090\3\2\2\2\4\u0097\3\2\2\2\6\u009f")
        buf.write("\3\2\2\2\b\u00a1\3\2\2\2\n\u00ac\3\2\2\2\f\u00b7\3\2\2")
        buf.write("\2\16\u00c3\3\2\2\2\20\u00d1\3\2\2\2\22\u00e7\3\2\2\2")
        buf.write("\24\u00e9\3\2\2\2\26\u00f9\3\2\2\2\30\u00fe\3\2\2\2\32")
        buf.write("\u0100\3\2\2\2\34\u0103\3\2\2\2\36\u0107\3\2\2\2 \u010d")
        buf.write("\3\2\2\2\"\u0114\3\2\2\2$\u0116\3\2\2\2&\u0122\3\2\2\2")
        buf.write("(\u0136\3\2\2\2*\u0138\3\2\2\2,\u014f\3\2\2\2.\u0155\3")
        buf.write("\2\2\2\60\u0157\3\2\2\2\62\u015b\3\2\2\2\64\u0167\3\2")
        buf.write("\2\2\66\u016d\3\2\2\28\u0174\3\2\2\2:\u0176\3\2\2\2<\u017d")
        buf.write("\3\2\2\2>\u017f\3\2\2\2@\u0184\3\2\2\2B\u018a\3\2\2\2")
        buf.write("D\u0192\3\2\2\2F\u0194\3\2\2\2H\u0198\3\2\2\2J\u019f\3")
        buf.write("\2\2\2L\u01a6\3\2\2\2N\u01a8\3\2\2\2P\u01ac\3\2\2\2R\u01b2")
        buf.write("\3\2\2\2T\u01ba\3\2\2\2V\u01bc\3\2\2\2X\u01c3\3\2\2\2")
        buf.write("Z\u01c8\3\2\2\2\\\u01ce\3\2\2\2^\u01d9\3\2\2\2`\u01de")
        buf.write("\3\2\2\2b\u01e0\3\2\2\2d\u01fc\3\2\2\2f\u01fe\3\2\2\2")
        buf.write("h\u0202\3\2\2\2j\u0208\3\2\2\2l\u020a\3\2\2\2n\u020d\3")
        buf.write("\2\2\2p\u0210\3\2\2\2r\u021a\3\2\2\2t\u021e\3\2\2\2v\u0220")
        buf.write("\3\2\2\2x\u0228\3\2\2\2z\u0234\3\2\2\2|\u0236\3\2\2\2")
        buf.write("~\u023a\3\2\2\2\u0080\u0243\3\2\2\2\u0082\u0247\3\2\2")
        buf.write("\2\u0084\u0251\3\2\2\2\u0086\u0253\3\2\2\2\u0088\u025c")
        buf.write("\3\2\2\2\u008a\u025e\3\2\2\2\u008c\u0260\3\2\2\2\u008e")
        buf.write("\u0262\3\2\2\2\u0090\u0091\5\4\3\2\u0091\u0092\7\2\2\3")
        buf.write("\u0092\3\3\2\2\2\u0093\u0094\5\6\4\2\u0094\u0095\5\4\3")
        buf.write("\2\u0095\u0098\3\2\2\2\u0096\u0098\5\6\4\2\u0097\u0093")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\5\3\2\2\2\u0099\u00a0")
        buf.write("\5(\25\2\u009a\u00a0\5,\27\2\u009b\u00a0\5*\26\2\u009c")
        buf.write("\u00a0\5\62\32\2\u009d\u00a0\5@!\2\u009e\u00a0\5P)\2\u009f")
        buf.write("\u0099\3\2\2\2\u009f\u009a\3\2\2\2\u009f\u009b\3\2\2\2")
        buf.write("\u009f\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3")
        buf.write("\2\2\2\u00a0\7\3\2\2\2\u00a1\u00a2\b\5\1\2\u00a2\u00a3")
        buf.write("\5\n\6\2\u00a3\u00a9\3\2\2\2\u00a4\u00a5\f\4\2\2\u00a5")
        buf.write("\u00a6\7\"\2\2\u00a6\u00a8\5\n\6\2\u00a7\u00a4\3\2\2\2")
        buf.write("\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\t\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad")
        buf.write("\b\6\1\2\u00ad\u00ae\5\f\7\2\u00ae\u00b4\3\2\2\2\u00af")
        buf.write("\u00b0\f\4\2\2\u00b0\u00b1\7!\2\2\u00b1\u00b3\5\f\7\2")
        buf.write("\u00b2\u00af\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3")
        buf.write("\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\13\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b7\u00b8\b\7\1\2\u00b8\u00b9\5\16\b\2\u00b9")
        buf.write("\u00c0\3\2\2\2\u00ba\u00bb\f\4\2\2\u00bb\u00bc\5\u008c")
        buf.write("G\2\u00bc\u00bd\5\16\b\2\u00bd\u00bf\3\2\2\2\u00be\u00ba")
        buf.write("\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\r\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3")
        buf.write("\u00c4\b\b\1\2\u00c4\u00c5\5\20\t\2\u00c5\u00ce\3\2\2")
        buf.write("\2\u00c6\u00c7\f\5\2\2\u00c7\u00c8\7,\2\2\u00c8\u00cd")
        buf.write("\5\20\t\2\u00c9\u00ca\f\4\2\2\u00ca\u00cb\7-\2\2\u00cb")
        buf.write("\u00cd\5\20\t\2\u00cc\u00c6\3\2\2\2\u00cc\u00c9\3\2\2")
        buf.write("\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\17\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2")
        buf.write("\b\t\1\2\u00d2\u00d3\5\22\n\2\u00d3\u00df\3\2\2\2\u00d4")
        buf.write("\u00d5\f\6\2\2\u00d5\u00d6\7.\2\2\u00d6\u00de\5\22\n\2")
        buf.write("\u00d7\u00d8\f\5\2\2\u00d8\u00d9\7/\2\2\u00d9\u00de\5")
        buf.write("\22\n\2\u00da\u00db\f\4\2\2\u00db\u00dc\7\60\2\2\u00dc")
        buf.write("\u00de\5\22\n\2\u00dd\u00d4\3\2\2\2\u00dd\u00d7\3\2\2")
        buf.write("\2\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\21\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e3\7#\2\2\u00e3\u00e8\5\22\n\2\u00e4")
        buf.write("\u00e5\7-\2\2\u00e5\u00e8\5\22\n\2\u00e6\u00e8\5\24\13")
        buf.write("\2\u00e7\u00e2\3\2\2\2\u00e7\u00e4\3\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\23\3\2\2\2\u00e9\u00ea\b\13\1\2\u00ea\u00eb")
        buf.write("\5\26\f\2\u00eb\u00f0\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed")
        buf.write("\u00ef\5\30\r\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2\3\2\2")
        buf.write("\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\25\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7\61\2\2\u00f4")
        buf.write("\u00f5\5\b\5\2\u00f5\u00f6\7\62\2\2\u00f6\u00fa\3\2\2")
        buf.write("\2\u00f7\u00fa\5\u0088E\2\u00f8\u00fa\7=\2\2\u00f9\u00f3")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa")
        buf.write("\27\3\2\2\2\u00fb\u00ff\5\32\16\2\u00fc\u00ff\5\34\17")
        buf.write("\2\u00fd\u00ff\5\36\20\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\31\3\2\2\2\u0100\u0101")
        buf.write("\7*\2\2\u0101\u0102\7=\2\2\u0102\33\3\2\2\2\u0103\u0104")
        buf.write("\7\63\2\2\u0104\u0105\5\b\5\2\u0105\u0106\7\64\2\2\u0106")
        buf.write("\35\3\2\2\2\u0107\u0108\7\61\2\2\u0108\u0109\5 \21\2\u0109")
        buf.write("\u010a\7\62\2\2\u010a\37\3\2\2\2\u010b\u010e\5\"\22\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c\3")
        buf.write("\2\2\2\u010e!\3\2\2\2\u010f\u0110\5\b\5\2\u0110\u0111")
        buf.write("\7\67\2\2\u0111\u0112\5\"\22\2\u0112\u0115\3\2\2\2\u0113")
        buf.write("\u0115\5\b\5\2\u0114\u010f\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115#\3\2\2\2\u0116\u0117\5&\24\2\u0117\u0118\5t;\2")
        buf.write("\u0118\u0119\5\b\5\2\u0119\u011a\5\u008eH\2\u011a%\3\2")
        buf.write("\2\2\u011b\u011c\5\24\13\2\u011c\u011d\5\32\16\2\u011d")
        buf.write("\u0123\3\2\2\2\u011e\u011f\5\24\13\2\u011f\u0120\5\34")
        buf.write("\17\2\u0120\u0123\3\2\2\2\u0121\u0123\7=\2\2\u0122\u011b")
        buf.write("\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\'\3\2\2\2\u0124\u0125\7\24\2\2\u0125\u0126\7=\2\2\u0126")
        buf.write("\u0127\5\u0084C\2\u0127\u0128\5\u008eH\2\u0128\u0137\3")
        buf.write("\2\2\2\u0129\u012a\7\24\2\2\u012a\u012b\7=\2\2\u012b\u012c")
        buf.write("\7+\2\2\u012c\u012d\5\b\5\2\u012d\u012e\5\u008eH\2\u012e")
        buf.write("\u0137\3\2\2\2\u012f\u0130\7\24\2\2\u0130\u0131\7=\2\2")
        buf.write("\u0131\u0132\5\u0084C\2\u0132\u0133\7+\2\2\u0133\u0134")
        buf.write("\5\b\5\2\u0134\u0135\5\u008eH\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0124\3\2\2\2\u0136\u0129\3\2\2\2\u0136\u012f\3\2\2\2")
        buf.write("\u0137)\3\2\2\2\u0138\u0139\7\23\2\2\u0139\u013b\7=\2")
        buf.write("\2\u013a\u013c\5\u0084C\2\u013b\u013a\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\7+\2\2\u013e")
        buf.write("\u013f\5\b\5\2\u013f\u0140\5\u008eH\2\u0140+\3\2\2\2\u0141")
        buf.write("\u0142\7\24\2\2\u0142\u0143\7=\2\2\u0143\u0144\5.\30\2")
        buf.write("\u0144\u0145\5\u0084C\2\u0145\u0146\5\u008eH\2\u0146\u0150")
        buf.write("\3\2\2\2\u0147\u0148\7\24\2\2\u0148\u0149\7=\2\2\u0149")
        buf.write("\u014a\5.\30\2\u014a\u014b\5\u0084C\2\u014b\u014c\7+\2")
        buf.write("\2\u014c\u014d\5|?\2\u014d\u014e\5\u008eH\2\u014e\u0150")
        buf.write("\3\2\2\2\u014f\u0141\3\2\2\2\u014f\u0147\3\2\2\2\u0150")
        buf.write("-\3\2\2\2\u0151\u0152\5\60\31\2\u0152\u0153\5.\30\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0156\5\60\31\2\u0155\u0151\3\2\2")
        buf.write("\2\u0155\u0154\3\2\2\2\u0156/\3\2\2\2\u0157\u0158\7\63")
        buf.write("\2\2\u0158\u0159\5\b\5\2\u0159\u015a\7\64\2\2\u015a\61")
        buf.write("\3\2\2\2\u015b\u015d\7\13\2\2\u015c\u015e\5> \2\u015d")
        buf.write("\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\7=\2\2\u0160\u0162\5\64\33\2\u0161\u0163")
        buf.write("\5\u0084C\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\5v<\2\u0165\u0166\5\u008eH")
        buf.write("\2\u0166\63\3\2\2\2\u0167\u0168\7\61\2\2\u0168\u0169\5")
        buf.write("\66\34\2\u0169\u016a\7\62\2\2\u016a\65\3\2\2\2\u016b\u016e")
        buf.write("\58\35\2\u016c\u016e\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016e\67\3\2\2\2\u016f\u0170\5:\36\2\u0170")
        buf.write("\u0171\7\67\2\2\u0171\u0172\58\35\2\u0172\u0175\3\2\2")
        buf.write("\2\u0173\u0175\5:\36\2\u0174\u016f\3\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u01759\3\2\2\2\u0176\u0177\5<\37\2\u0177\u0178")
        buf.write("\5\u0084C\2\u0178;\3\2\2\2\u0179\u017a\7=\2\2\u017a\u017b")
        buf.write("\7\67\2\2\u017b\u017e\5<\37\2\u017c\u017e\7=\2\2\u017d")
        buf.write("\u0179\3\2\2\2\u017d\u017c\3\2\2\2\u017e=\3\2\2\2\u017f")
        buf.write("\u0180\7\61\2\2\u0180\u0181\7=\2\2\u0181\u0182\7=\2\2")
        buf.write("\u0182\u0183\7\62\2\2\u0183?\3\2\2\2\u0184\u0185\7\f\2")
        buf.write("\2\u0185\u0186\7=\2\2\u0186\u0187\7\r\2\2\u0187\u0188")
        buf.write("\5B\"\2\u0188\u0189\5\u008eH\2\u0189A\3\2\2\2\u018a\u018b")
        buf.write("\7\65\2\2\u018b\u018c\5D#\2\u018c\u018d\7\66\2\2\u018d")
        buf.write("C\3\2\2\2\u018e\u018f\5F$\2\u018f\u0190\5D#\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u0193\5F$\2\u0192\u018e\3\2\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193E\3\2\2\2\u0194\u0195\7=\2\2\u0195\u0196")
        buf.write("\5\u0084C\2\u0196\u0197\5\u008eH\2\u0197G\3\2\2\2\u0198")
        buf.write("\u0199\7=\2\2\u0199\u019a\7\65\2\2\u019a\u019b\5J&\2\u019b")
        buf.write("\u019c\7\66\2\2\u019cI\3\2\2\2\u019d\u01a0\5L\'\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0K\3\2\2\2\u01a1\u01a2\5N(\2\u01a2\u01a3\7\67\2\2")
        buf.write("\u01a3\u01a4\5L\'\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\5")
        buf.write("N(\2\u01a6\u01a1\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7M\3")
        buf.write("\2\2\2\u01a8\u01a9\7=\2\2\u01a9\u01aa\79\2\2\u01aa\u01ab")
        buf.write("\5\b\5\2\u01abO\3\2\2\2\u01ac\u01ad\7\f\2\2\u01ad\u01ae")
        buf.write("\7=\2\2\u01ae\u01af\7\16\2\2\u01af\u01b0\5R*\2\u01b0\u01b1")
        buf.write("\5\u008eH\2\u01b1Q\3\2\2\2\u01b2\u01b3\7\65\2\2\u01b3")
        buf.write("\u01b4\5T+\2\u01b4\u01b5\7\66\2\2\u01b5S\3\2\2\2\u01b6")
        buf.write("\u01b7\5V,\2\u01b7\u01b8\5T+\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01bb\5V,\2\u01ba\u01b6\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("U\3\2\2\2\u01bc\u01bd\7=\2\2\u01bd\u01bf\5\64\33\2\u01be")
        buf.write("\u01c0\5\u0084C\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2")
        buf.write("\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\5\u008eH\2\u01c2")
        buf.write("W\3\2\2\2\u01c3\u01c4\5Z.\2\u01c4\u01c5\5^\60\2\u01c5")
        buf.write("\u01c6\5`\61\2\u01c6\u01c7\5\u008eH\2\u01c7Y\3\2\2\2\u01c8")
        buf.write("\u01c9\7\7\2\2\u01c9\u01ca\5b\62\2\u01ca\u01cc\5v<\2\u01cb")
        buf.write("\u01cd\5\u008eH\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2")
        buf.write("\2\2\u01cd[\3\2\2\2\u01ce\u01cf\7\b\2\2\u01cf\u01d0\7")
        buf.write("\7\2\2\u01d0\u01d1\5b\62\2\u01d1\u01d3\5v<\2\u01d2\u01d4")
        buf.write("\5\u008eH\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("]\3\2\2\2\u01d5\u01d6\5\\/\2\u01d6\u01d7\5^\60\2\u01d7")
        buf.write("\u01da\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d5\3\2\2\2")
        buf.write("\u01d9\u01d8\3\2\2\2\u01da_\3\2\2\2\u01db\u01dc\7\b\2")
        buf.write("\2\u01dc\u01df\5v<\2\u01dd\u01df\3\2\2\2\u01de\u01db\3")
        buf.write("\2\2\2\u01de\u01dd\3\2\2\2\u01dfa\3\2\2\2\u01e0\u01e1")
        buf.write("\7\61\2\2\u01e1\u01e2\5\b\5\2\u01e2\u01e3\7\62\2\2\u01e3")
        buf.write("c\3\2\2\2\u01e4\u01e5\7\t\2\2\u01e5\u01e6\5\b\5\2\u01e6")
        buf.write("\u01e7\5v<\2\u01e7\u01e8\5\u008eH\2\u01e8\u01fd\3\2\2")
        buf.write("\2\u01e9\u01ea\7\t\2\2\u01ea\u01eb\5f\64\2\u01eb\u01ec")
        buf.write("\78\2\2\u01ec\u01ed\5\b\5\2\u01ed\u01ee\78\2\2\u01ee\u01ef")
        buf.write("\5h\65\2\u01ef\u01f0\5v<\2\u01f0\u01f1\5\u008eH\2\u01f1")
        buf.write("\u01fd\3\2\2\2\u01f2\u01f3\7\t\2\2\u01f3\u01f4\7=\2\2")
        buf.write("\u01f4\u01f5\7\67\2\2\u01f5\u01f6\7=\2\2\u01f6\u01f7\7")
        buf.write(")\2\2\u01f7\u01f8\7\27\2\2\u01f8\u01f9\5j\66\2\u01f9\u01fa")
        buf.write("\5v<\2\u01fa\u01fb\5\u008eH\2\u01fb\u01fd\3\2\2\2\u01fc")
        buf.write("\u01e4\3\2\2\2\u01fc\u01e9\3\2\2\2\u01fc\u01f2\3\2\2\2")
        buf.write("\u01fde\3\2\2\2\u01fe\u01ff\7=\2\2\u01ff\u0200\7)\2\2")
        buf.write("\u0200\u0201\5\b\5\2\u0201g\3\2\2\2\u0202\u0203\7=\2\2")
        buf.write("\u0203\u0204\5\u008aF\2\u0204\u0205\5\b\5\2\u0205i\3\2")
        buf.write("\2\2\u0206\u0209\7=\2\2\u0207\u0209\5|?\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209k\3\2\2\2\u020a\u020b")
        buf.write("\7\26\2\2\u020b\u020c\5\u008eH\2\u020cm\3\2\2\2\u020d")
        buf.write("\u020e\7\25\2\2\u020e\u020f\5\u008eH\2\u020fo\3\2\2\2")
        buf.write("\u0210\u0211\5\24\13\2\u0211\u0212\5\36\20\2\u0212\u0213")
        buf.write("\5\u008eH\2\u0213q\3\2\2\2\u0214\u0215\7\n\2\2\u0215\u021b")
        buf.write("\5\u008eH\2\u0216\u0217\7\n\2\2\u0217\u0218\5\b\5\2\u0218")
        buf.write("\u0219\5\u008eH\2\u0219\u021b\3\2\2\2\u021a\u0214\3\2")
        buf.write("\2\2\u021a\u0216\3\2\2\2\u021bs\3\2\2\2\u021c\u021f\5")
        buf.write("\u008aF\2\u021d\u021f\7)\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021fu\3\2\2\2\u0220\u0221\7\65\2\2\u0221")
        buf.write("\u0222\5x=\2\u0222\u0223\7\66\2\2\u0223w\3\2\2\2\u0224")
        buf.write("\u0225\5z>\2\u0225\u0226\5x=\2\u0226\u0229\3\2\2\2\u0227")
        buf.write("\u0229\5z>\2\u0228\u0224\3\2\2\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("y\3\2\2\2\u022a\u0235\5$\23\2\u022b\u0235\5(\25\2\u022c")
        buf.write("\u0235\5,\27\2\u022d\u0235\5*\26\2\u022e\u0235\5X-\2\u022f")
        buf.write("\u0235\5d\63\2\u0230\u0235\5n8\2\u0231\u0235\5l\67\2\u0232")
        buf.write("\u0235\5p9\2\u0233\u0235\5r:\2\u0234\u022a\3\2\2\2\u0234")
        buf.write("\u022b\3\2\2\2\u0234\u022c\3\2\2\2\u0234\u022d\3\2\2\2")
        buf.write("\u0234\u022e\3\2\2\2\u0234\u022f\3\2\2\2\u0234\u0230\3")
        buf.write("\2\2\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235{\3\2\2\2\u0236\u0237\5.\30\2\u0237\u0238")
        buf.write("\5\u0084C\2\u0238\u0239\5~@\2\u0239}\3\2\2\2\u023a\u023b")
        buf.write("\7\65\2\2\u023b\u023c\5\u0080A\2\u023c\u023d\7\66\2\2")
        buf.write("\u023d\177\3\2\2\2\u023e\u023f\5\u0082B\2\u023f\u0240")
        buf.write("\7\67\2\2\u0240\u0241\5\u0080A\2\u0241\u0244\3\2\2\2\u0242")
        buf.write("\u0244\5\u0082B\2\u0243\u023e\3\2\2\2\u0243\u0242\3\2")
        buf.write("\2\2\u0244\u0081\3\2\2\2\u0245\u0248\5\b\5\2\u0246\u0248")
        buf.write("\5~@\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2\u0248\u0083")
        buf.write("\3\2\2\2\u0249\u024b\5.\30\2\u024a\u0249\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u0252\5\u0086")
        buf.write("D\2\u024d\u024f\5.\30\2\u024e\u024d\3\2\2\2\u024e\u024f")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\7=\2\2\u0251")
        buf.write("\u024a\3\2\2\2\u0251\u024e\3\2\2\2\u0252\u0085\3\2\2\2")
        buf.write("\u0253\u0254\t\2\2\2\u0254\u0087\3\2\2\2\u0255\u025d\7")
        buf.write(";\2\2\u0256\u025d\7:\2\2\u0257\u025d\7<\2\2\u0258\u025d")
        buf.write("\7\31\2\2\u0259\u025d\7\32\2\2\u025a\u025d\5H%\2\u025b")
        buf.write("\u025d\5|?\2\u025c\u0255\3\2\2\2\u025c\u0256\3\2\2\2\u025c")
        buf.write("\u0257\3\2\2\2\u025c\u0258\3\2\2\2\u025c\u0259\3\2\2\2")
        buf.write("\u025c\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u0089\3")
        buf.write("\2\2\2\u025e\u025f\t\3\2\2\u025f\u008b\3\2\2\2\u0260\u0261")
        buf.write("\t\4\2\2\u0261\u008d\3\2\2\2\u0262\u0263\t\5\2\2\u0263")
        buf.write("\u008f\3\2\2\2\60\u0097\u009f\u00a9\u00b4\u00c0\u00cc")
        buf.write("\u00ce\u00dd\u00df\u00e7\u00f0\u00f9\u00fe\u010d\u0114")
        buf.write("\u0122\u0136\u013b\u014f\u0155\u015d\u0162\u016d\u0174")
        buf.write("\u017d\u0192\u019f\u01a6\u01ba\u01bf\u01cc\u01d3\u01d9")
        buf.write("\u01de\u01fc\u0208\u021a\u021e\u0228\u0234\u0243\u0247")
        buf.write("\u024a\u024e\u0251\u025c")
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
    RULE_expr = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_expr3 = 6
    RULE_expr4 = 7
    RULE_expr5 = 8
    RULE_expr6 = 9
    RULE_expr7 = 10
    RULE_tail = 11
    RULE_field_access_tail = 12
    RULE_arr_elem_access = 13
    RULE_funccall_tail = 14
    RULE_expr_lst = 15
    RULE_expr_lstprime = 16
    RULE_assigning_stmt = 17
    RULE_lhs = 18
    RULE_var_decl = 19
    RULE_const_decl = 20
    RULE_array_decl = 21
    RULE_arridx_lst = 22
    RULE_arridx = 23
    RULE_func_decl = 24
    RULE_funcparam = 25
    RULE_paramlst = 26
    RULE_param_lstprime = 27
    RULE_param = 28
    RULE_id_nnlst = 29
    RULE_receiver = 30
    RULE_struct_decl = 31
    RULE_structfield = 32
    RULE_fielddecl_nnlst = 33
    RULE_fielddecl = 34
    RULE_struct_literal = 35
    RULE_structparam_lst = 36
    RULE_structparam_lstprime = 37
    RULE_structparam = 38
    RULE_interf_decl = 39
    RULE_interfmeth = 40
    RULE_interfmeth_nnlst = 41
    RULE_interfmethmem = 42
    RULE_ifelse_stmt = 43
    RULE_if_ = 44
    RULE_elseif_ = 45
    RULE_elseif_lst = 46
    RULE_else_ = 47
    RULE_condition = 48
    RULE_forloop_stmt = 49
    RULE_forloop_init = 50
    RULE_forloop_update = 51
    RULE_id__arr = 52
    RULE_break_stmt = 53
    RULE_continue_stmt = 54
    RULE_funccall_stmt = 55
    RULE_return_stmt = 56
    RULE_assign = 57
    RULE_blockcode = 58
    RULE_blockcodestmt_nnlst = 59
    RULE_blockcodestmt = 60
    RULE_arr_literal = 61
    RULE_arrvalue = 62
    RULE_arrelem_lst = 63
    RULE_arrelem = 64
    RULE_data_type = 65
    RULE_primitive_datatype = 66
    RULE_literal = 67
    RULE_uptassign = 68
    RULE_compare_op = 69
    RULE_end_stm = 70

    ruleNames =  [ "program", "decl_lst", "decl", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "tail", 
                   "field_access_tail", "arr_elem_access", "funccall_tail", 
                   "expr_lst", "expr_lstprime", "assigning_stmt", "lhs", 
                   "var_decl", "const_decl", "array_decl", "arridx_lst", 
                   "arridx", "func_decl", "funcparam", "paramlst", "param_lstprime", 
                   "param", "id_nnlst", "receiver", "struct_decl", "structfield", 
                   "fielddecl_nnlst", "fielddecl", "struct_literal", "structparam_lst", 
                   "structparam_lstprime", "structparam", "interf_decl", 
                   "interfmeth", "interfmeth_nnlst", "interfmethmem", "ifelse_stmt", 
                   "if_", "elseif_", "elseif_lst", "else_", "condition", 
                   "forloop_stmt", "forloop_init", "forloop_update", "id__arr", 
                   "break_stmt", "continue_stmt", "funccall_stmt", "return_stmt", 
                   "assign", "blockcode", "blockcodestmt_nnlst", "blockcodestmt", 
                   "arr_literal", "arrvalue", "arrelem_lst", "arrelem", 
                   "data_type", "primitive_datatype", "literal", "uptassign", 
                   "compare_op", "end_stm" ]

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
            self.state = 142
            self.decl_lst()
            self.state = 143
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
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.decl()
                self.state = 146
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
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

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interf_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interf_declContext,0)


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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.array_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.const_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.func_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.interf_decl()
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 162
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 163
                    self.match(MiniGoParser.OR)
                    self.state = 164
                    self.expr1(0) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    self.match(MiniGoParser.AND)
                    self.state = 175
                    self.expr2(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.compare_op()
                    self.state = 186
                    self.expr3(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_expr5)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.NOT)
                self.state = 225
                self.expr5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.SUB)
                self.state = 227
                self.expr5()
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


        def tail(self):
            return self.getTypedRuleContext(MiniGoParser.TailContext,0)


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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    self.tail() 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_expr7)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MiniGoParser.LP)
                self.state = 242
                self.expr(0)
                self.state = 243
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
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


        def arr_elem_access(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_accessContext,0)


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
        self.enterRule(localctx, 22, self.RULE_tail)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.field_access_tail()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.arr_elem_access()
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
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
        self.enterRule(localctx, 24, self.RULE_field_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.DOT)
            self.state = 255
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elem_accessContext(ParserRuleContext):
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
            return MiniGoParser.RULE_arr_elem_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem_access" ):
                return visitor.visitArr_elem_access(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem_access(self):

        localctx = MiniGoParser.Arr_elem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arr_elem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MiniGoParser.LSB)
            self.state = 258
            self.expr(0)
            self.state = 259
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
        self.enterRule(localctx, 28, self.RULE_funccall_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MiniGoParser.LP)
            self.state = 262
            self.expr_lst()
            self.state = 263
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
        self.enterRule(localctx, 30, self.RULE_expr_lst)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
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
        self.enterRule(localctx, 32, self.RULE_expr_lstprime)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expr(0)
                self.state = 270
                self.match(MiniGoParser.COMMA)
                self.state = 271
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr(0)
                pass


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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigning_stmt" ):
                return visitor.visitAssigning_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assigning_stmt(self):

        localctx = MiniGoParser.Assigning_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assigning_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.lhs()
            self.state = 277
            self.assign()
            self.state = 278
            self.expr(0)
            self.state = 279
            self.end_stm()
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


        def arr_elem_access(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_accessContext,0)


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
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expr6(0)
                self.state = 282
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.expr6(0)
                self.state = 285
                self.arr_elem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Type_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_Var_decl" ):
                return visitor.visitType_Var_decl(self)
            else:
                return visitor.visitChildren(self)


    class Value_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_Var_decl" ):
                return visitor.visitValue_Var_decl(self)
            else:
                return visitor.visitChildren(self)


    class TypeValue_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeValue_Var_decl" ):
                return visitor.visitTypeValue_Var_decl(self)
            else:
                return visitor.visitChildren(self)



    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.Type_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(MiniGoParser.VAR_)
                self.state = 291
                self.match(MiniGoParser.ID)
                self.state = 292
                self.data_type()
                self.state = 293
                self.end_stm()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.Value_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(MiniGoParser.VAR_)
                self.state = 296
                self.match(MiniGoParser.ID)
                self.state = 297
                self.match(MiniGoParser.EQUAL)
                self.state = 298
                self.expr(0)
                self.state = 299
                self.end_stm()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.TypeValue_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(MiniGoParser.VAR_)
                self.state = 302
                self.match(MiniGoParser.ID)
                self.state = 303
                self.data_type()
                self.state = 304
                self.match(MiniGoParser.EQUAL)
                self.state = 305
                self.expr(0)
                self.state = 306
                self.end_stm()
                pass


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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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
        self.enterRule(localctx, 40, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MiniGoParser.CONST_)
            self.state = 311
            self.match(MiniGoParser.ID)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 312
                self.data_type()


            self.state = 315
            self.match(MiniGoParser.EQUAL)
            self.state = 316
            self.expr(0)
            self.state = 317
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_decl)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.VAR_)
                self.state = 320
                self.match(MiniGoParser.ID)
                self.state = 321
                self.arridx_lst()
                self.state = 322
                self.data_type()
                self.state = 323
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(MiniGoParser.VAR_)
                self.state = 326
                self.match(MiniGoParser.ID)
                self.state = 327
                self.arridx_lst()
                self.state = 328
                self.data_type()
                self.state = 329
                self.match(MiniGoParser.EQUAL)
                self.state = 330
                self.arr_literal()
                self.state = 331
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arridx_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArridx_lst" ):
                return visitor.visitArridx_lst(self)
            else:
                return visitor.visitChildren(self)




    def arridx_lst(self):

        localctx = MiniGoParser.Arridx_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arridx_lst)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.arridx()
                self.state = 336
                self.arridx_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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
        self.enterRule(localctx, 46, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MiniGoParser.LSB)
            self.state = 342
            self.expr(0)
            self.state = 343
            self.match(MiniGoParser.RSB)
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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
            self.state = 345
            self.match(MiniGoParser.FUNC_)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LP:
                self.state = 346
                self.receiver()


            self.state = 349
            self.match(MiniGoParser.ID)
            self.state = 350
            self.funcparam()
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 351
                self.data_type()


            self.state = 354
            self.blockcode()
            self.state = 355
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
        self.enterRule(localctx, 50, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MiniGoParser.LP)
            self.state = 358
            self.paramlst()
            self.state = 359
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

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlst" ):
                return visitor.visitParamlst(self)
            else:
                return visitor.visitChildren(self)




    def paramlst(self):

        localctx = MiniGoParser.ParamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_paramlst)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
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
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.param()
                self.state = 366
                self.match(MiniGoParser.COMMA)
                self.state = 367
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
            self.state = 372
            self.id_nnlst()
            self.state = 373
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
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(MiniGoParser.ID)
                self.state = 376
                self.match(MiniGoParser.COMMA)
                self.state = 377
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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
            self.state = 381
            self.match(MiniGoParser.LP)
            self.state = 382
            self.match(MiniGoParser.ID)
            self.state = 383
            self.match(MiniGoParser.ID)
            self.state = 384
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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
            self.state = 386
            self.match(MiniGoParser.TYPE_)
            self.state = 387
            self.match(MiniGoParser.ID)
            self.state = 388
            self.match(MiniGoParser.STRUCT_)
            self.state = 389
            self.structfield()
            self.state = 390
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
            self.state = 392
            self.match(MiniGoParser.LCB)
            self.state = 393
            self.fielddecl_nnlst()
            self.state = 394
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
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.fielddecl()
                self.state = 397
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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
            self.state = 402
            self.match(MiniGoParser.ID)
            self.state = 403
            self.data_type()
            self.state = 404
            self.end_stm()
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
        self.enterRule(localctx, 70, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.ID)
            self.state = 407
            self.match(MiniGoParser.LCB)
            self.state = 408
            self.structparam_lst()
            self.state = 409
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
        self.enterRule(localctx, 72, self.RULE_structparam_lst)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
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
        self.enterRule(localctx, 74, self.RULE_structparam_lstprime)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.structparam()
                self.state = 416
                self.match(MiniGoParser.COMMA)
                self.state = 417
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
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
        self.enterRule(localctx, 76, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.ID)
            self.state = 423
            self.match(MiniGoParser.COLON)
            self.state = 424
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interf_declContext(ParserRuleContext):
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
            return MiniGoParser.RULE_interf_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterf_decl" ):
                return visitor.visitInterf_decl(self)
            else:
                return visitor.visitChildren(self)




    def interf_decl(self):

        localctx = MiniGoParser.Interf_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_interf_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.TYPE_)
            self.state = 427
            self.match(MiniGoParser.ID)
            self.state = 428
            self.match(MiniGoParser.INTERFACE_)
            self.state = 429
            self.interfmeth()
            self.state = 430
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

        def interfmeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfmeth_nnlstContext,0)


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
        self.enterRule(localctx, 80, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.LCB)
            self.state = 433
            self.interfmeth_nnlst()
            self.state = 434
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interfmeth_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfmethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethmemContext,0)


        def interfmeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfmeth_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmeth_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfmeth_nnlst" ):
                return visitor.visitInterfmeth_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def interfmeth_nnlst(self):

        localctx = MiniGoParser.Interfmeth_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_interfmeth_nnlst)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.interfmethmem()
                self.state = 437
                self.interfmeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.interfmethmem()
                pass


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
        self.enterRule(localctx, 84, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.ID)
            self.state = 443
            self.funcparam()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 444
                self.data_type()


            self.state = 447
            self.end_stm()
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse_stmt" ):
                return visitor.visitIfelse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ifelse_stmt(self):

        localctx = MiniGoParser.Ifelse_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ifelse_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.if_()
            self.state = 450
            self.elseif_lst()
            self.state = 451
            self.else_()
            self.state = 452
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
        self.enterRule(localctx, 88, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.IF_)
            self.state = 455
            self.condition()
            self.state = 456
            self.blockcode()
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 457
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
        self.enterRule(localctx, 90, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.ELSE_)
            self.state = 461
            self.match(MiniGoParser.IF_)
            self.state = 462
            self.condition()
            self.state = 463
            self.blockcode()
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 464
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
        self.enterRule(localctx, 92, self.RULE_elseif_lst)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.elseif_()
                self.state = 468
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
        self.enterRule(localctx, 94, self.RULE_else_)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(MiniGoParser.ELSE_)
                self.state = 474
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
        self.enterRule(localctx, 96, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(MiniGoParser.LP)
            self.state = 479
            self.expr(0)
            self.state = 480
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

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def forloop_init(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_initContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def forloop_update(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_updateContext,0)


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

        def id__arr(self):
            return self.getTypedRuleContext(MiniGoParser.Id__arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_stmt" ):
                return visitor.visitForloop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def forloop_stmt(self):

        localctx = MiniGoParser.Forloop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forloop_stmt)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(MiniGoParser.FOR_)
                self.state = 483
                self.expr(0)
                self.state = 484
                self.blockcode()
                self.state = 485
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(MiniGoParser.FOR_)
                self.state = 488
                self.forloop_init()
                self.state = 489
                self.match(MiniGoParser.SEMICOLON)
                self.state = 490
                self.expr(0)
                self.state = 491
                self.match(MiniGoParser.SEMICOLON)
                self.state = 492
                self.forloop_update()
                self.state = 493
                self.blockcode()
                self.state = 494
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(MiniGoParser.FOR_)
                self.state = 497
                self.match(MiniGoParser.ID)
                self.state = 498
                self.match(MiniGoParser.COMMA)
                self.state = 499
                self.match(MiniGoParser.ID)
                self.state = 500
                self.match(MiniGoParser.ASSIGN)
                self.state = 501
                self.match(MiniGoParser.RANGE_)
                self.state = 502
                self.id__arr()
                self.state = 503
                self.blockcode()
                self.state = 504
                self.end_stm()
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_init" ):
                return visitor.visitForloop_init(self)
            else:
                return visitor.visitChildren(self)




    def forloop_init(self):

        localctx = MiniGoParser.Forloop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forloop_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MiniGoParser.ID)
            self.state = 509
            self.match(MiniGoParser.ASSIGN)
            self.state = 510
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_update" ):
                return visitor.visitForloop_update(self)
            else:
                return visitor.visitChildren(self)




    def forloop_update(self):

        localctx = MiniGoParser.Forloop_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_forloop_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MiniGoParser.ID)
            self.state = 513
            self.uptassign()
            self.state = 514
            self.expr(0)
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
        self.enterRule(localctx, 104, self.RULE_id__arr)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
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


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.BREAK_)
            self.state = 521
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.CONTINUE_)
            self.state = 524
            self.end_stm()
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

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall_stmt" ):
                return visitor.visitFunccall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def funccall_stmt(self):

        localctx = MiniGoParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.expr6(0)
            self.state = 527
            self.funccall_tail()
            self.state = 528
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


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
        self.enterRule(localctx, 112, self.RULE_return_stmt)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(MiniGoParser.RETURN_)
                self.state = 531
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(MiniGoParser.RETURN_)
                self.state = 533
                self.expr(0)
                self.state = 534
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

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


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
        self.enterRule(localctx, 114, self.RULE_assign)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ADDASSIGN, MiniGoParser.SUBASSIGN, MiniGoParser.MULASSIGN, MiniGoParser.DIVASSIGN, MiniGoParser.MODASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.uptassign()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.match(MiniGoParser.ASSIGN)
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


    class BlockcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def blockcodestmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Blockcodestmt_nnlstContext,0)


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
        self.enterRule(localctx, 116, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.LCB)
            self.state = 543
            self.blockcodestmt_nnlst()
            self.state = 544
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Blockcodestmt_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockcodestmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtContext,0)


        def blockcodestmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Blockcodestmt_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmt_nnlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcodestmt_nnlst" ):
                return visitor.visitBlockcodestmt_nnlst(self)
            else:
                return visitor.visitChildren(self)




    def blockcodestmt_nnlst(self):

        localctx = MiniGoParser.Blockcodestmt_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_blockcodestmt_nnlst)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.blockcodestmt()
                self.state = 547
                self.blockcodestmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.blockcodestmt()
                pass


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

        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def ifelse_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_stmtContext,0)


        def forloop_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def funccall_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockcodestmt" ):
                return visitor.visitBlockcodestmt(self)
            else:
                return visitor.visitChildren(self)




    def blockcodestmt(self):

        localctx = MiniGoParser.BlockcodestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_blockcodestmt)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.assigning_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 554
                self.array_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 555
                self.const_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 556
                self.ifelse_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 557
                self.forloop_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 558
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 559
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 560
                self.funccall_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 561
                self.return_stmt()
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

        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


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
        self.enterRule(localctx, 122, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.arridx_lst()
            self.state = 565
            self.data_type()
            self.state = 566
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
        self.enterRule(localctx, 124, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(MiniGoParser.LCB)
            self.state = 569
            self.arrelem_lst()
            self.state = 570
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
        self.enterRule(localctx, 126, self.RULE_arrelem_lst)
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.arrelem()
                self.state = 573
                self.match(MiniGoParser.COMMA)
                self.state = 574
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
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
        self.enterRule(localctx, 128, self.RULE_arrelem)
        try:
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


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
        self.enterRule(localctx, 130, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 583
                    self.arridx_lst()


                self.state = 586
                self.primitive_datatype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 587
                    self.arridx_lst()


                self.state = 590
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 132, self.RULE_primitive_datatype)
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
        self.enterRule(localctx, 134, self.RULE_literal)
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


    class UptassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return MiniGoParser.RULE_uptassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUptassign" ):
                return visitor.visitUptassign(self)
            else:
                return visitor.visitChildren(self)




    def uptassign(self):

        localctx = MiniGoParser.UptassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_uptassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADDASSIGN) | (1 << MiniGoParser.SUBASSIGN) | (1 << MiniGoParser.MULASSIGN) | (1 << MiniGoParser.DIVASSIGN) | (1 << MiniGoParser.MODASSIGN))) != 0)):
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
        self.enterRule(localctx, 138, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
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
        self.enterRule(localctx, 140, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
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
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.expr1_sempred
        self._predicates[5] = self.expr2_sempred
        self._predicates[6] = self.expr3_sempred
        self._predicates[7] = self.expr4_sempred
        self._predicates[9] = self.expr6_sempred
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
                return self.precpred(self._ctx, 2)
         




