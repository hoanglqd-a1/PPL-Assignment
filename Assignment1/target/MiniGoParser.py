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
        buf.write("\u0251\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u0096\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u009e")
        buf.write("\n\5\f\5\16\5\u00a1\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a9")
        buf.write("\n\6\f\6\16\6\u00ac\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7\u00b5\n\7\f\7\16\7\u00b8\13\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\7\b\u00c3\n\b\f\b\16\b\u00c6\13\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00d4\n")
        buf.write("\t\f\t\16\t\u00d7\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00e3\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00f5\n\13\f\13\16\13\u00f8\13\13\3\f\3\f\5\f\u00fc\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u0103\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u0114\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u011e\n\20\3\20\3\20\3\20\3\20\5\20\u0124")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u013a\n\22\3\23\3\23\3\23\3\23\5\23\u0140\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\5\25\u0148\n\25\3\25\3\25\3\25")
        buf.write("\5\25\u014d\n\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\5\27\u0158\n\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u015f\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u0168")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u017d")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\5!\u018a")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0191\n\"\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\5&\u01a5\n&\3\'")
        buf.write("\3\'\3\'\5\'\u01aa\n\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\5)\u01b7\n)\3*\3*\3*\3*\3*\5*\u01be\n*\3+\3+\3+\3")
        buf.write("+\5+\u01c4\n+\3,\3,\3,\5,\u01c9\n,\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01e7\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\5\61\u01f3\n\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\5\65\u0207\n\65\3\66\3\66\5\66\u020b\n\66\3")
        buf.write("\67\3\67\3\67\3\67\38\38\38\38\58\u0215\n8\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\59\u0221\n9\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\5<\u0230\n<\3=\3=\5=\u0234\n=\3>\5>\u0237")
        buf.write("\n>\3>\3>\5>\u023b\n>\3>\5>\u023e\n>\3?\3?\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\5@\u0249\n@\3A\3A\3B\3B\3C\3C\3C\2\b\b\n\f")
        buf.write("\16\20\24D\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|")
        buf.write("~\u0080\u0082\u0084\2\6\3\2\17\22\3\2$(\3\2\33 \3\388")
        buf.write("\2\u0253\2\u0086\3\2\2\2\4\u008d\3\2\2\2\6\u0095\3\2\2")
        buf.write("\2\b\u0097\3\2\2\2\n\u00a2\3\2\2\2\f\u00ad\3\2\2\2\16")
        buf.write("\u00b9\3\2\2\2\20\u00c7\3\2\2\2\22\u00e2\3\2\2\2\24\u00e4")
        buf.write("\3\2\2\2\26\u00fb\3\2\2\2\30\u0102\3\2\2\2\32\u0104\3")
        buf.write("\2\2\2\34\u0113\3\2\2\2\36\u0123\3\2\2\2 \u0125\3\2\2")
        buf.write("\2\"\u0139\3\2\2\2$\u013f\3\2\2\2&\u0141\3\2\2\2(\u0145")
        buf.write("\3\2\2\2*\u0151\3\2\2\2,\u0157\3\2\2\2.\u015e\3\2\2\2")
        buf.write("\60\u0160\3\2\2\2\62\u0167\3\2\2\2\64\u0169\3\2\2\2\66")
        buf.write("\u016e\3\2\2\28\u0174\3\2\2\2:\u017c\3\2\2\2<\u017e\3")
        buf.write("\2\2\2>\u0182\3\2\2\2@\u0189\3\2\2\2B\u0190\3\2\2\2D\u0192")
        buf.write("\3\2\2\2F\u0196\3\2\2\2H\u019c\3\2\2\2J\u01a4\3\2\2\2")
        buf.write("L\u01a6\3\2\2\2N\u01ad\3\2\2\2P\u01b2\3\2\2\2R\u01b8\3")
        buf.write("\2\2\2T\u01c3\3\2\2\2V\u01c8\3\2\2\2X\u01ca\3\2\2\2Z\u01e6")
        buf.write("\3\2\2\2\\\u01e8\3\2\2\2^\u01ec\3\2\2\2`\u01f2\3\2\2\2")
        buf.write("b\u01f4\3\2\2\2d\u01f7\3\2\2\2f\u01fa\3\2\2\2h\u0206\3")
        buf.write("\2\2\2j\u020a\3\2\2\2l\u020c\3\2\2\2n\u0214\3\2\2\2p\u0220")
        buf.write("\3\2\2\2r\u0222\3\2\2\2t\u0226\3\2\2\2v\u022f\3\2\2\2")
        buf.write("x\u0233\3\2\2\2z\u023d\3\2\2\2|\u023f\3\2\2\2~\u0248\3")
        buf.write("\2\2\2\u0080\u024a\3\2\2\2\u0082\u024c\3\2\2\2\u0084\u024e")
        buf.write("\3\2\2\2\u0086\u0087\5\4\3\2\u0087\u0088\7\2\2\3\u0088")
        buf.write("\3\3\2\2\2\u0089\u008a\5\6\4\2\u008a\u008b\5\4\3\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008e\5\6\4\2\u008d\u0089\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\5\3\2\2\2\u008f\u0096\5\36")
        buf.write("\20\2\u0090\u0096\5\"\22\2\u0091\u0096\5 \21\2\u0092\u0096")
        buf.write("\5(\25\2\u0093\u0096\5\66\34\2\u0094\u0096\5F$\2\u0095")
        buf.write("\u008f\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2")
        buf.write("\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3")
        buf.write("\2\2\2\u0096\7\3\2\2\2\u0097\u0098\b\5\1\2\u0098\u0099")
        buf.write("\5\n\6\2\u0099\u009f\3\2\2\2\u009a\u009b\f\4\2\2\u009b")
        buf.write("\u009c\7\"\2\2\u009c\u009e\5\n\6\2\u009d\u009a\3\2\2\2")
        buf.write("\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\t\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3")
        buf.write("\b\6\1\2\u00a3\u00a4\5\f\7\2\u00a4\u00aa\3\2\2\2\u00a5")
        buf.write("\u00a6\f\4\2\2\u00a6\u00a7\7!\2\2\u00a7\u00a9\5\f\7\2")
        buf.write("\u00a8\u00a5\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\13\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ad\u00ae\b\7\1\2\u00ae\u00af\5\16\b\2\u00af")
        buf.write("\u00b6\3\2\2\2\u00b0\u00b1\f\4\2\2\u00b1\u00b2\5\u0082")
        buf.write("B\2\u00b2\u00b3\5\16\b\2\u00b3\u00b5\3\2\2\2\u00b4\u00b0")
        buf.write("\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\r\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9")
        buf.write("\u00ba\b\b\1\2\u00ba\u00bb\5\20\t\2\u00bb\u00c4\3\2\2")
        buf.write("\2\u00bc\u00bd\f\5\2\2\u00bd\u00be\7,\2\2\u00be\u00c3")
        buf.write("\5\20\t\2\u00bf\u00c0\f\4\2\2\u00c0\u00c1\7-\2\2\u00c1")
        buf.write("\u00c3\5\20\t\2\u00c2\u00bc\3\2\2\2\u00c2\u00bf\3\2\2")
        buf.write("\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\17\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8")
        buf.write("\b\t\1\2\u00c8\u00c9\5\22\n\2\u00c9\u00d5\3\2\2\2\u00ca")
        buf.write("\u00cb\f\6\2\2\u00cb\u00cc\7.\2\2\u00cc\u00d4\5\22\n\2")
        buf.write("\u00cd\u00ce\f\5\2\2\u00ce\u00cf\7/\2\2\u00cf\u00d4\5")
        buf.write("\22\n\2\u00d0\u00d1\f\4\2\2\u00d1\u00d2\7\60\2\2\u00d2")
        buf.write("\u00d4\5\22\n\2\u00d3\u00ca\3\2\2\2\u00d3\u00cd\3\2\2")
        buf.write("\2\u00d3\u00d0\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\21\3\2\2\2\u00d7\u00d5")
        buf.write("\3\2\2\2\u00d8\u00d9\7#\2\2\u00d9\u00e3\5\22\n\2\u00da")
        buf.write("\u00db\7-\2\2\u00db\u00e3\5\22\n\2\u00dc\u00e3\5\24\13")
        buf.write("\2\u00dd\u00de\7\61\2\2\u00de\u00df\5\b\5\2\u00df\u00e0")
        buf.write("\7\62\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5~@\2\u00e2")
        buf.write("\u00d8\3\2\2\2\u00e2\u00da\3\2\2\2\u00e2\u00dc\3\2\2\2")
        buf.write("\u00e2\u00dd\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\23\3\2")
        buf.write("\2\2\u00e4\u00e5\b\13\1\2\u00e5\u00e6\7=\2\2\u00e6\u00f6")
        buf.write("\3\2\2\2\u00e7\u00e8\f\6\2\2\u00e8\u00e9\7*\2\2\u00e9")
        buf.write("\u00f5\7=\2\2\u00ea\u00eb\f\5\2\2\u00eb\u00ec\7\63\2\2")
        buf.write("\u00ec\u00ed\5\b\5\2\u00ed\u00ee\7\64\2\2\u00ee\u00f5")
        buf.write("\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1\7\61\2\2\u00f1")
        buf.write("\u00f2\5\26\f\2\u00f2\u00f3\7\62\2\2\u00f3\u00f5\3\2\2")
        buf.write("\2\u00f4\u00e7\3\2\2\2\u00f4\u00ea\3\2\2\2\u00f4\u00ef")
        buf.write("\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\25\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9")
        buf.write("\u00fc\5\30\r\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc\27\3\2\2\2\u00fd\u00fe\5")
        buf.write("\b\5\2\u00fe\u00ff\7\67\2\2\u00ff\u0100\5\30\r\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u0103\5\b\5\2\u0102\u00fd\3\2\2\2")
        buf.write("\u0102\u0101\3\2\2\2\u0103\31\3\2\2\2\u0104\u0105\5\34")
        buf.write("\17\2\u0105\u0106\5j\66\2\u0106\u0107\5\b\5\2\u0107\u0108")
        buf.write("\5\u0084C\2\u0108\33\3\2\2\2\u0109\u010a\5\24\13\2\u010a")
        buf.write("\u010b\7*\2\2\u010b\u010c\7=\2\2\u010c\u0114\3\2\2\2\u010d")
        buf.write("\u010e\5\24\13\2\u010e\u010f\7\63\2\2\u010f\u0110\5\b")
        buf.write("\5\2\u0110\u0111\7\64\2\2\u0111\u0114\3\2\2\2\u0112\u0114")
        buf.write("\7=\2\2\u0113\u0109\3\2\2\2\u0113\u010d\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\35\3\2\2\2\u0115\u0116\7\24\2\2\u0116")
        buf.write("\u0117\7=\2\2\u0117\u0118\5z>\2\u0118\u0119\5\u0084C\2")
        buf.write("\u0119\u0124\3\2\2\2\u011a\u011b\7\24\2\2\u011b\u011d")
        buf.write("\7=\2\2\u011c\u011e\5z>\2\u011d\u011c\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7+\2\2\u0120")
        buf.write("\u0121\5\b\5\2\u0121\u0122\5\u0084C\2\u0122\u0124\3\2")
        buf.write("\2\2\u0123\u0115\3\2\2\2\u0123\u011a\3\2\2\2\u0124\37")
        buf.write("\3\2\2\2\u0125\u0126\7\23\2\2\u0126\u0127\7=\2\2\u0127")
        buf.write("\u0128\7+\2\2\u0128\u0129\5\b\5\2\u0129\u012a\5\u0084")
        buf.write("C\2\u012a!\3\2\2\2\u012b\u012c\7\24\2\2\u012c\u012d\7")
        buf.write("=\2\2\u012d\u012e\5$\23\2\u012e\u012f\5z>\2\u012f\u0130")
        buf.write("\5\u0084C\2\u0130\u013a\3\2\2\2\u0131\u0132\7\24\2\2\u0132")
        buf.write("\u0133\7=\2\2\u0133\u0134\5$\23\2\u0134\u0135\5z>\2\u0135")
        buf.write("\u0136\7+\2\2\u0136\u0137\5r:\2\u0137\u0138\5\u0084C\2")
        buf.write("\u0138\u013a\3\2\2\2\u0139\u012b\3\2\2\2\u0139\u0131\3")
        buf.write("\2\2\2\u013a#\3\2\2\2\u013b\u013c\5&\24\2\u013c\u013d")
        buf.write("\5$\23\2\u013d\u0140\3\2\2\2\u013e\u0140\5&\24\2\u013f")
        buf.write("\u013b\3\2\2\2\u013f\u013e\3\2\2\2\u0140%\3\2\2\2\u0141")
        buf.write("\u0142\7\63\2\2\u0142\u0143\5\b\5\2\u0143\u0144\7\64\2")
        buf.write("\2\u0144\'\3\2\2\2\u0145\u0147\7\13\2\2\u0146\u0148\5")
        buf.write("\64\33\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\7=\2\2\u014a\u014c\5*\26\2")
        buf.write("\u014b\u014d\5z>\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2")
        buf.write("\2\2\u014d\u014e\3\2\2\2\u014e\u014f\5l\67\2\u014f\u0150")
        buf.write("\5\u0084C\2\u0150)\3\2\2\2\u0151\u0152\7\61\2\2\u0152")
        buf.write("\u0153\5,\27\2\u0153\u0154\7\62\2\2\u0154+\3\2\2\2\u0155")
        buf.write("\u0158\5.\30\2\u0156\u0158\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0156\3\2\2\2\u0158-\3\2\2\2\u0159\u015a\5\60\31")
        buf.write("\2\u015a\u015b\7\67\2\2\u015b\u015c\5.\30\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015f\5\60\31\2\u015e\u0159\3\2\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f/\3\2\2\2\u0160\u0161\5\62\32\2\u0161")
        buf.write("\u0162\5z>\2\u0162\61\3\2\2\2\u0163\u0164\7=\2\2\u0164")
        buf.write("\u0165\7\67\2\2\u0165\u0168\5\62\32\2\u0166\u0168\7=\2")
        buf.write("\2\u0167\u0163\3\2\2\2\u0167\u0166\3\2\2\2\u0168\63\3")
        buf.write("\2\2\2\u0169\u016a\7\61\2\2\u016a\u016b\7=\2\2\u016b\u016c")
        buf.write("\7=\2\2\u016c\u016d\7\62\2\2\u016d\65\3\2\2\2\u016e\u016f")
        buf.write("\7\f\2\2\u016f\u0170\7=\2\2\u0170\u0171\7\r\2\2\u0171")
        buf.write("\u0172\58\35\2\u0172\u0173\5\u0084C\2\u0173\67\3\2\2\2")
        buf.write("\u0174\u0175\7\65\2\2\u0175\u0176\5:\36\2\u0176\u0177")
        buf.write("\7\66\2\2\u01779\3\2\2\2\u0178\u0179\5<\37\2\u0179\u017a")
        buf.write("\5:\36\2\u017a\u017d\3\2\2\2\u017b\u017d\5<\37\2\u017c")
        buf.write("\u0178\3\2\2\2\u017c\u017b\3\2\2\2\u017d;\3\2\2\2\u017e")
        buf.write("\u017f\7=\2\2\u017f\u0180\5z>\2\u0180\u0181\5\u0084C\2")
        buf.write("\u0181=\3\2\2\2\u0182\u0183\7=\2\2\u0183\u0184\7\65\2")
        buf.write("\2\u0184\u0185\5@!\2\u0185\u0186\7\66\2\2\u0186?\3\2\2")
        buf.write("\2\u0187\u018a\5B\"\2\u0188\u018a\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u0188\3\2\2\2\u018aA\3\2\2\2\u018b\u018c")
        buf.write("\5D#\2\u018c\u018d\7\67\2\2\u018d\u018e\5B\"\2\u018e\u0191")
        buf.write("\3\2\2\2\u018f\u0191\5D#\2\u0190\u018b\3\2\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191C\3\2\2\2\u0192\u0193\7=\2\2\u0193\u0194")
        buf.write("\79\2\2\u0194\u0195\5\b\5\2\u0195E\3\2\2\2\u0196\u0197")
        buf.write("\7\f\2\2\u0197\u0198\7=\2\2\u0198\u0199\7\16\2\2\u0199")
        buf.write("\u019a\5H%\2\u019a\u019b\5\u0084C\2\u019bG\3\2\2\2\u019c")
        buf.write("\u019d\7\65\2\2\u019d\u019e\5J&\2\u019e\u019f\7\66\2\2")
        buf.write("\u019fI\3\2\2\2\u01a0\u01a1\5L\'\2\u01a1\u01a2\5J&\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a5\5L\'\2\u01a4\u01a0\3\2\2\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5K\3\2\2\2\u01a6\u01a7\7=\2\2")
        buf.write("\u01a7\u01a9\5*\26\2\u01a8\u01aa\5z>\2\u01a9\u01a8\3\2")
        buf.write("\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac")
        buf.write("\5\u0084C\2\u01acM\3\2\2\2\u01ad\u01ae\5P)\2\u01ae\u01af")
        buf.write("\5T+\2\u01af\u01b0\5V,\2\u01b0\u01b1\5\u0084C\2\u01b1")
        buf.write("O\3\2\2\2\u01b2\u01b3\7\7\2\2\u01b3\u01b4\5X-\2\u01b4")
        buf.write("\u01b6\5l\67\2\u01b5\u01b7\5\u0084C\2\u01b6\u01b5\3\2")
        buf.write("\2\2\u01b6\u01b7\3\2\2\2\u01b7Q\3\2\2\2\u01b8\u01b9\7")
        buf.write("\b\2\2\u01b9\u01ba\7\7\2\2\u01ba\u01bb\5X-\2\u01bb\u01bd")
        buf.write("\5l\67\2\u01bc\u01be\5\u0084C\2\u01bd\u01bc\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01beS\3\2\2\2\u01bf\u01c0\5R*\2\u01c0")
        buf.write("\u01c1\5T+\2\u01c1\u01c4\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3")
        buf.write("\u01bf\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4U\3\2\2\2\u01c5")
        buf.write("\u01c6\7\b\2\2\u01c6\u01c9\5l\67\2\u01c7\u01c9\3\2\2\2")
        buf.write("\u01c8\u01c5\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9W\3\2\2")
        buf.write("\2\u01ca\u01cb\7\61\2\2\u01cb\u01cc\5\b\5\2\u01cc\u01cd")
        buf.write("\7\62\2\2\u01cdY\3\2\2\2\u01ce\u01cf\7\t\2\2\u01cf\u01d0")
        buf.write("\5\b\5\2\u01d0\u01d1\5l\67\2\u01d1\u01d2\5\u0084C\2\u01d2")
        buf.write("\u01e7\3\2\2\2\u01d3\u01d4\7\t\2\2\u01d4\u01d5\5\\/\2")
        buf.write("\u01d5\u01d6\78\2\2\u01d6\u01d7\5\b\5\2\u01d7\u01d8\7")
        buf.write("8\2\2\u01d8\u01d9\5^\60\2\u01d9\u01da\5l\67\2\u01da\u01db")
        buf.write("\5\u0084C\2\u01db\u01e7\3\2\2\2\u01dc\u01dd\7\t\2\2\u01dd")
        buf.write("\u01de\7=\2\2\u01de\u01df\7\67\2\2\u01df\u01e0\7=\2\2")
        buf.write("\u01e0\u01e1\7)\2\2\u01e1\u01e2\7\27\2\2\u01e2\u01e3\5")
        buf.write("`\61\2\u01e3\u01e4\5l\67\2\u01e4\u01e5\5\u0084C\2\u01e5")
        buf.write("\u01e7\3\2\2\2\u01e6\u01ce\3\2\2\2\u01e6\u01d3\3\2\2\2")
        buf.write("\u01e6\u01dc\3\2\2\2\u01e7[\3\2\2\2\u01e8\u01e9\7=\2\2")
        buf.write("\u01e9\u01ea\7)\2\2\u01ea\u01eb\5\b\5\2\u01eb]\3\2\2\2")
        buf.write("\u01ec\u01ed\7=\2\2\u01ed\u01ee\5\u0080A\2\u01ee\u01ef")
        buf.write("\5\b\5\2\u01ef_\3\2\2\2\u01f0\u01f3\7=\2\2\u01f1\u01f3")
        buf.write("\5r:\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3a")
        buf.write("\3\2\2\2\u01f4\u01f5\7\26\2\2\u01f5\u01f6\5\u0084C\2\u01f6")
        buf.write("c\3\2\2\2\u01f7\u01f8\7\25\2\2\u01f8\u01f9\5\u0084C\2")
        buf.write("\u01f9e\3\2\2\2\u01fa\u01fb\5\24\13\2\u01fb\u01fc\7\61")
        buf.write("\2\2\u01fc\u01fd\5\26\f\2\u01fd\u01fe\7\62\2\2\u01fe\u01ff")
        buf.write("\5\u0084C\2\u01ffg\3\2\2\2\u0200\u0201\7\n\2\2\u0201\u0207")
        buf.write("\5\u0084C\2\u0202\u0203\7\n\2\2\u0203\u0204\5\b\5\2\u0204")
        buf.write("\u0205\5\u0084C\2\u0205\u0207\3\2\2\2\u0206\u0200\3\2")
        buf.write("\2\2\u0206\u0202\3\2\2\2\u0207i\3\2\2\2\u0208\u020b\5")
        buf.write("\u0080A\2\u0209\u020b\7)\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020bk\3\2\2\2\u020c\u020d\7\65\2\2\u020d")
        buf.write("\u020e\5n8\2\u020e\u020f\7\66\2\2\u020fm\3\2\2\2\u0210")
        buf.write("\u0211\5p9\2\u0211\u0212\5n8\2\u0212\u0215\3\2\2\2\u0213")
        buf.write("\u0215\5p9\2\u0214\u0210\3\2\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("o\3\2\2\2\u0216\u0221\5\32\16\2\u0217\u0221\5\36\20\2")
        buf.write("\u0218\u0221\5\"\22\2\u0219\u0221\5 \21\2\u021a\u0221")
        buf.write("\5N(\2\u021b\u0221\5Z.\2\u021c\u0221\5d\63\2\u021d\u0221")
        buf.write("\5b\62\2\u021e\u0221\5f\64\2\u021f\u0221\5h\65\2\u0220")
        buf.write("\u0216\3\2\2\2\u0220\u0217\3\2\2\2\u0220\u0218\3\2\2\2")
        buf.write("\u0220\u0219\3\2\2\2\u0220\u021a\3\2\2\2\u0220\u021b\3")
        buf.write("\2\2\2\u0220\u021c\3\2\2\2\u0220\u021d\3\2\2\2\u0220\u021e")
        buf.write("\3\2\2\2\u0220\u021f\3\2\2\2\u0221q\3\2\2\2\u0222\u0223")
        buf.write("\5$\23\2\u0223\u0224\5z>\2\u0224\u0225\5t;\2\u0225s\3")
        buf.write("\2\2\2\u0226\u0227\7\65\2\2\u0227\u0228\5v<\2\u0228\u0229")
        buf.write("\7\66\2\2\u0229u\3\2\2\2\u022a\u022b\5x=\2\u022b\u022c")
        buf.write("\7\67\2\2\u022c\u022d\5v<\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u0230\5x=\2\u022f\u022a\3\2\2\2\u022f\u022e\3\2\2\2\u0230")
        buf.write("w\3\2\2\2\u0231\u0234\5\b\5\2\u0232\u0234\5t;\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0232\3\2\2\2\u0234y\3\2\2\2\u0235")
        buf.write("\u0237\5$\23\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u023e\5|?\2\u0239\u023b\5$")
        buf.write("\23\2\u023a\u0239\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023e\7=\2\2\u023d\u0236\3\2\2\2\u023d")
        buf.write("\u023a\3\2\2\2\u023e{\3\2\2\2\u023f\u0240\t\2\2\2\u0240")
        buf.write("}\3\2\2\2\u0241\u0249\7;\2\2\u0242\u0249\7:\2\2\u0243")
        buf.write("\u0249\7<\2\2\u0244\u0249\7\31\2\2\u0245\u0249\7\32\2")
        buf.write("\2\u0246\u0249\5> \2\u0247\u0249\5r:\2\u0248\u0241\3\2")
        buf.write("\2\2\u0248\u0242\3\2\2\2\u0248\u0243\3\2\2\2\u0248\u0244")
        buf.write("\3\2\2\2\u0248\u0245\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\177\3\2\2\2\u024a\u024b\t\3\2\2\u024b")
        buf.write("\u0081\3\2\2\2\u024c\u024d\t\4\2\2\u024d\u0083\3\2\2\2")
        buf.write("\u024e\u024f\t\5\2\2\u024f\u0085\3\2\2\2/\u008d\u0095")
        buf.write("\u009f\u00aa\u00b6\u00c2\u00c4\u00d3\u00d5\u00e2\u00f4")
        buf.write("\u00f6\u00fb\u0102\u0113\u011d\u0123\u0139\u013f\u0147")
        buf.write("\u014c\u0157\u015e\u0167\u017c\u0189\u0190\u01a4\u01a9")
        buf.write("\u01b6\u01bd\u01c3\u01c8\u01e6\u01f2\u0206\u020a\u0214")
        buf.write("\u0220\u022f\u0233\u0236\u023a\u023d\u0248")
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
    RULE_exprlst = 10
    RULE_expr_lstprime = 11
    RULE_assigning_stmt = 12
    RULE_lhs = 13
    RULE_var_decl = 14
    RULE_const_decl = 15
    RULE_arraydecl = 16
    RULE_arridx_lst = 17
    RULE_arridx = 18
    RULE_func_decl = 19
    RULE_funcparam = 20
    RULE_paramlst = 21
    RULE_param_lstprime = 22
    RULE_param = 23
    RULE_id_nnlst = 24
    RULE_receiver = 25
    RULE_struct_decl = 26
    RULE_structfield = 27
    RULE_fielddecl_nnlst = 28
    RULE_fielddecl = 29
    RULE_struct_literal = 30
    RULE_structparam_lst = 31
    RULE_structparam_lstprime = 32
    RULE_structparam = 33
    RULE_interf_decl = 34
    RULE_interfmeth = 35
    RULE_interfmeth_nnlst = 36
    RULE_interfmethmem = 37
    RULE_ifelse_stmt = 38
    RULE_if_ = 39
    RULE_elseif_ = 40
    RULE_elseif_lst = 41
    RULE_else_ = 42
    RULE_condition = 43
    RULE_forloop_stmt = 44
    RULE_forloop_init = 45
    RULE_forloop_update = 46
    RULE_id__arr = 47
    RULE_break_stmt = 48
    RULE_continue_stmt = 49
    RULE_funccall_stmt = 50
    RULE_return_stmt = 51
    RULE_assign = 52
    RULE_blockcode = 53
    RULE_blockcodestmt_nnlst = 54
    RULE_blockcodestmt = 55
    RULE_arr_literal = 56
    RULE_arrvalue = 57
    RULE_arrelem_lst = 58
    RULE_arrelem = 59
    RULE_data_type = 60
    RULE_primitive_datatype = 61
    RULE_literal = 62
    RULE_uptassign = 63
    RULE_compare_op = 64
    RULE_end_stm = 65

    ruleNames =  [ "program", "decl_lst", "decl", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "exprlst", "expr_lstprime", 
                   "assigning_stmt", "lhs", "var_decl", "const_decl", "arraydecl", 
                   "arridx_lst", "arridx", "func_decl", "funcparam", "paramlst", 
                   "param_lstprime", "param", "id_nnlst", "receiver", "struct_decl", 
                   "structfield", "fielddecl_nnlst", "fielddecl", "struct_literal", 
                   "structparam_lst", "structparam_lstprime", "structparam", 
                   "interf_decl", "interfmeth", "interfmeth_nnlst", "interfmethmem", 
                   "ifelse_stmt", "if_", "elseif_", "elseif_lst", "else_", 
                   "condition", "forloop_stmt", "forloop_init", "forloop_update", 
                   "id__arr", "break_stmt", "continue_stmt", "funccall_stmt", 
                   "return_stmt", "assign", "blockcode", "blockcodestmt_nnlst", 
                   "blockcodestmt", "arr_literal", "arrvalue", "arrelem_lst", 
                   "arrelem", "data_type", "primitive_datatype", "literal", 
                   "uptassign", "compare_op", "end_stm" ]

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
            self.state = 132
            self.decl_lst()
            self.state = 133
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.decl()
                self.state = 136
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.arraydecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.const_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.func_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
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
            self.state = 150
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    self.match(MiniGoParser.OR)
                    self.state = 154
                    self.expr1(0) 
                self.state = 159
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
            self.state = 161
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    self.match(MiniGoParser.AND)
                    self.state = 165
                    self.expr2(0) 
                self.state = 170
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
            self.state = 172
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    self.compare_op()
                    self.state = 176
                    self.expr3(0) 
                self.state = 182
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
            self.state = 184
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 186
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 187
                        self.match(MiniGoParser.ADD)
                        self.state = 188
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 189
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 190
                        self.match(MiniGoParser.SUB)
                        self.state = 191
                        self.expr4(0)
                        pass

             
                self.state = 196
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
            self.state = 198
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 209
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 200
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 201
                        self.match(MiniGoParser.MUL)
                        self.state = 202
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 203
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 204
                        self.match(MiniGoParser.DIV)
                        self.state = 205
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 206
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 207
                        self.match(MiniGoParser.MOD)
                        self.state = 208
                        self.expr5()
                        pass

             
                self.state = 213
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


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(MiniGoParser.NOT)
                self.state = 215
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(MiniGoParser.SUB)
                self.state = 217
                self.expr5()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.expr6(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.match(MiniGoParser.LP)
                self.state = 220
                self.expr(0)
                self.state = 221
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.literal()
                pass


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 242
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 229
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 230
                        self.match(MiniGoParser.DOT)
                        self.state = 231
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 232
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 233
                        self.match(MiniGoParser.LSB)
                        self.state = 234
                        self.expr(0)
                        self.state = 235
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 237
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 238
                        self.match(MiniGoParser.LP)
                        self.state = 239
                        self.exprlst()
                        self.state = 240
                        self.match(MiniGoParser.RP)
                        pass

             
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlst" ):
                return visitor.visitExprlst(self)
            else:
                return visitor.visitChildren(self)




    def exprlst(self):

        localctx = MiniGoParser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprlst)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
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
        self.enterRule(localctx, 22, self.RULE_expr_lstprime)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.expr(0)
                self.state = 252
                self.match(MiniGoParser.COMMA)
                self.state = 253
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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
        self.enterRule(localctx, 24, self.RULE_assigning_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.lhs()
            self.state = 259
            self.assign()
            self.state = 260
            self.expr(0)
            self.state = 261
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lhs)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.expr6(0)
                self.state = 264
                self.match(MiniGoParser.DOT)
                self.state = 265
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.expr6(0)
                self.state = 268
                self.match(MiniGoParser.LSB)
                self.state = 269
                self.expr(0)
                self.state = 270
                self.match(MiniGoParser.RSB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
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
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(MiniGoParser.VAR_)
                self.state = 276
                self.match(MiniGoParser.ID)
                self.state = 277
                self.data_type()
                self.state = 278
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(MiniGoParser.VAR_)
                self.state = 281
                self.match(MiniGoParser.ID)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 282
                    self.data_type()


                self.state = 285
                self.match(MiniGoParser.EQUAL)
                self.state = 286
                self.expr(0)
                self.state = 287
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MiniGoParser.CONST_)
            self.state = 292
            self.match(MiniGoParser.ID)
            self.state = 293
            self.match(MiniGoParser.EQUAL)
            self.state = 294
            self.expr(0)
            self.state = 295
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
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arraydecl)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(MiniGoParser.VAR_)
                self.state = 298
                self.match(MiniGoParser.ID)
                self.state = 299
                self.arridx_lst()
                self.state = 300
                self.data_type()
                self.state = 301
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.VAR_)
                self.state = 304
                self.match(MiniGoParser.ID)
                self.state = 305
                self.arridx_lst()
                self.state = 306
                self.data_type()
                self.state = 307
                self.match(MiniGoParser.EQUAL)
                self.state = 308
                self.arr_literal()
                self.state = 309
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
        self.enterRule(localctx, 34, self.RULE_arridx_lst)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.arridx()
                self.state = 314
                self.arridx_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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
        self.enterRule(localctx, 36, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.LSB)
            self.state = 320
            self.expr(0)
            self.state = 321
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
        self.enterRule(localctx, 38, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.FUNC_)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LP:
                self.state = 324
                self.receiver()


            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.funcparam()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 329
                self.data_type()


            self.state = 332
            self.blockcode()
            self.state = 333
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
        self.enterRule(localctx, 40, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.LP)
            self.state = 336
            self.paramlst()
            self.state = 337
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
        self.enterRule(localctx, 42, self.RULE_paramlst)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
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
        self.enterRule(localctx, 44, self.RULE_param_lstprime)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.param()
                self.state = 344
                self.match(MiniGoParser.COMMA)
                self.state = 345
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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
        self.enterRule(localctx, 46, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.id_nnlst()
            self.state = 351
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
        self.enterRule(localctx, 48, self.RULE_id_nnlst)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(MiniGoParser.ID)
                self.state = 354
                self.match(MiniGoParser.COMMA)
                self.state = 355
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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
        self.enterRule(localctx, 50, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.LP)
            self.state = 360
            self.match(MiniGoParser.ID)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
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
        self.enterRule(localctx, 52, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.TYPE_)
            self.state = 365
            self.match(MiniGoParser.ID)
            self.state = 366
            self.match(MiniGoParser.STRUCT_)
            self.state = 367
            self.structfield()
            self.state = 368
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
        self.enterRule(localctx, 54, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.LCB)
            self.state = 371
            self.fielddecl_nnlst()
            self.state = 372
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
        self.enterRule(localctx, 56, self.RULE_fielddecl_nnlst)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.fielddecl()
                self.state = 375
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
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
        self.enterRule(localctx, 58, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MiniGoParser.ID)
            self.state = 381
            self.data_type()
            self.state = 382
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
        self.enterRule(localctx, 60, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.ID)
            self.state = 385
            self.match(MiniGoParser.LCB)
            self.state = 386
            self.structparam_lst()
            self.state = 387
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
        self.enterRule(localctx, 62, self.RULE_structparam_lst)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
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
        self.enterRule(localctx, 64, self.RULE_structparam_lstprime)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.structparam()
                self.state = 394
                self.match(MiniGoParser.COMMA)
                self.state = 395
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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
        self.enterRule(localctx, 66, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MiniGoParser.ID)
            self.state = 401
            self.match(MiniGoParser.COLON)
            self.state = 402
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
        self.enterRule(localctx, 68, self.RULE_interf_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MiniGoParser.TYPE_)
            self.state = 405
            self.match(MiniGoParser.ID)
            self.state = 406
            self.match(MiniGoParser.INTERFACE_)
            self.state = 407
            self.interfmeth()
            self.state = 408
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
        self.enterRule(localctx, 70, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(MiniGoParser.LCB)
            self.state = 411
            self.interfmeth_nnlst()
            self.state = 412
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
        self.enterRule(localctx, 72, self.RULE_interfmeth_nnlst)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.interfmethmem()
                self.state = 415
                self.interfmeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
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
        self.enterRule(localctx, 74, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.ID)
            self.state = 421
            self.funcparam()
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 422
                self.data_type()


            self.state = 425
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
        self.enterRule(localctx, 76, self.RULE_ifelse_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.if_()
            self.state = 428
            self.elseif_lst()
            self.state = 429
            self.else_()
            self.state = 430
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
        self.enterRule(localctx, 78, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.IF_)
            self.state = 433
            self.condition()
            self.state = 434
            self.blockcode()
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 435
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
        self.enterRule(localctx, 80, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.ELSE_)
            self.state = 439
            self.match(MiniGoParser.IF_)
            self.state = 440
            self.condition()
            self.state = 441
            self.blockcode()
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 442
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
        self.enterRule(localctx, 82, self.RULE_elseif_lst)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.elseif_()
                self.state = 446
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
        self.enterRule(localctx, 84, self.RULE_else_)
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(MiniGoParser.ELSE_)
                self.state = 452
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
        self.enterRule(localctx, 86, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.LP)
            self.state = 457
            self.expr(0)
            self.state = 458
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
        self.enterRule(localctx, 88, self.RULE_forloop_stmt)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(MiniGoParser.FOR_)
                self.state = 461
                self.expr(0)
                self.state = 462
                self.blockcode()
                self.state = 463
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.match(MiniGoParser.FOR_)
                self.state = 466
                self.forloop_init()
                self.state = 467
                self.match(MiniGoParser.SEMICOLON)
                self.state = 468
                self.expr(0)
                self.state = 469
                self.match(MiniGoParser.SEMICOLON)
                self.state = 470
                self.forloop_update()
                self.state = 471
                self.blockcode()
                self.state = 472
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 474
                self.match(MiniGoParser.FOR_)
                self.state = 475
                self.match(MiniGoParser.ID)
                self.state = 476
                self.match(MiniGoParser.COMMA)
                self.state = 477
                self.match(MiniGoParser.ID)
                self.state = 478
                self.match(MiniGoParser.ASSIGN)
                self.state = 479
                self.match(MiniGoParser.RANGE_)
                self.state = 480
                self.id__arr()
                self.state = 481
                self.blockcode()
                self.state = 482
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
        self.enterRule(localctx, 90, self.RULE_forloop_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(MiniGoParser.ID)
            self.state = 487
            self.match(MiniGoParser.ASSIGN)
            self.state = 488
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
        self.enterRule(localctx, 92, self.RULE_forloop_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(MiniGoParser.ID)
            self.state = 491
            self.uptassign()
            self.state = 492
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
        self.enterRule(localctx, 94, self.RULE_id__arr)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
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
        self.enterRule(localctx, 96, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.BREAK_)
            self.state = 499
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
        self.enterRule(localctx, 98, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.CONTINUE_)
            self.state = 502
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


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

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
        self.enterRule(localctx, 100, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.expr6(0)
            self.state = 505
            self.match(MiniGoParser.LP)
            self.state = 506
            self.exprlst()
            self.state = 507
            self.match(MiniGoParser.RP)
            self.state = 508
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
        self.enterRule(localctx, 102, self.RULE_return_stmt)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(MiniGoParser.RETURN_)
                self.state = 511
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(MiniGoParser.RETURN_)
                self.state = 513
                self.expr(0)
                self.state = 514
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
        self.enterRule(localctx, 104, self.RULE_assign)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ADDASSIGN, MiniGoParser.SUBASSIGN, MiniGoParser.MULASSIGN, MiniGoParser.DIVASSIGN, MiniGoParser.MODASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.uptassign()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
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
        self.enterRule(localctx, 106, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.LCB)
            self.state = 523
            self.blockcodestmt_nnlst()
            self.state = 524
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
        self.enterRule(localctx, 108, self.RULE_blockcodestmt_nnlst)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.blockcodestmt()
                self.state = 527
                self.blockcodestmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
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


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


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
        self.enterRule(localctx, 110, self.RULE_blockcodestmt)
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.assigning_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 534
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 535
                self.const_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 536
                self.ifelse_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 537
                self.forloop_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 538
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 539
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 540
                self.funccall_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 541
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
        self.enterRule(localctx, 112, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.arridx_lst()
            self.state = 545
            self.data_type()
            self.state = 546
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
        self.enterRule(localctx, 114, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(MiniGoParser.LCB)
            self.state = 549
            self.arrelem_lst()
            self.state = 550
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
        self.enterRule(localctx, 116, self.RULE_arrelem_lst)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.arrelem()
                self.state = 553
                self.match(MiniGoParser.COMMA)
                self.state = 554
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
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
        self.enterRule(localctx, 118, self.RULE_arrelem)
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.NOT, MiniGoParser.SUB, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
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
        self.enterRule(localctx, 120, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 563
                    self.arridx_lst()


                self.state = 566
                self.primitive_datatype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 567
                    self.arridx_lst()


                self.state = 570
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
        self.enterRule(localctx, 122, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
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
        self.enterRule(localctx, 124, self.RULE_literal)
        try:
            self.state = 582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 575
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 577
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 578
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 579
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 580
                self.struct_literal()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 581
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
        self.enterRule(localctx, 126, self.RULE_uptassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
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
        self.enterRule(localctx, 128, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
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
        self.enterRule(localctx, 130, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




