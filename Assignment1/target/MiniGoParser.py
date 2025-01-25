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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u0164\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\6\2D\n\2\r\2\16\2E\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3R\n\3\3\4\3\4\3\4")
        buf.write("\7\4W\n\4\f\4\16\4Z\13\4\3\5\3\5\3\5\7\5_\n\5\f\5\16\5")
        buf.write("b\13\5\3\6\3\6\3\6\7\6g\n\6\f\6\16\6j\13\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7p\n\7\3\7\7\7s\n\7\f\7\16\7v\13\7\3\b\3\b\3\b")
        buf.write("\7\b{\n\b\f\b\16\b~\13\b\3\t\5\t\u0081\n\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0090\n\n")
        buf.write("\f\n\16\n\u0093\13\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u009b\n\13\3\f\3\f\3\f\7\f\u00a0\n\f\f\f\16\f\u00a3\13")
        buf.write("\f\5\f\u00a5\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00b2\n\17\3\17\3\17\5\17\u00b6\n")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\6\21\u00c6\n\21\r\21\16\21\u00c7")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\7\23\u00d5\n\23\f\23\16\23\u00d8\13\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u00e2\n\25\3\25\3\25\3")
        buf.write("\25\5\25\u00e7\n\25\3\25\3\25\5\25\u00eb\n\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00fa\n\27\3\27\7\27\u00fd\n\27\f\27\16\27\u0100")
        buf.write("\13\27\3\27\3\27\3\27\3\30\3\30\5\30\u0107\n\30\3\30\3")
        buf.write("\30\3\30\5\30\u010c\n\30\7\30\u010e\n\30\f\30\16\30\u0111")
        buf.write("\13\30\3\31\3\31\3\31\5\31\u0116\n\31\3\31\3\31\5\31\u011a")
        buf.write("\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0123\n")
        buf.write("\32\3\32\7\32\u0126\n\32\f\32\16\32\u0129\13\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\5\33\u0130\n\33\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u0136\n\34\f\34\16\34\u0139\13\34\5\34\u013b\n\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\6\35\u0143\n\35\r\35\16")
        buf.write("\35\u0144\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u014d\n\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 \u015a\n ")
        buf.write("\3!\6!\u015d\n!\r!\16!\u015e\3!\5!\u0162\n!\3!\2\2\"\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@\2\6\3\2%\'\4\2\5\5$$\3\2\22\25\4\2\6\6//\2\u0177")
        buf.write("\2C\3\2\2\2\4Q\3\2\2\2\6S\3\2\2\2\b[\3\2\2\2\nc\3\2\2")
        buf.write("\2\fk\3\2\2\2\16w\3\2\2\2\20\u0080\3\2\2\2\22\u0084\3")
        buf.write("\2\2\2\24\u009a\3\2\2\2\26\u00a4\3\2\2\2\30\u00a6\3\2")
        buf.write("\2\2\32\u00a8\3\2\2\2\34\u00ad\3\2\2\2\36\u00b9\3\2\2")
        buf.write("\2 \u00bf\3\2\2\2\"\u00ce\3\2\2\2$\u00d1\3\2\2\2&\u00d9")
        buf.write("\3\2\2\2(\u00dc\3\2\2\2*\u00f0\3\2\2\2,\u00f4\3\2\2\2")
        buf.write(".\u0104\3\2\2\2\60\u0112\3\2\2\2\62\u011d\3\2\2\2\64\u012f")
        buf.write("\3\2\2\2\66\u0131\3\2\2\28\u0142\3\2\2\2:\u0149\3\2\2")
        buf.write("\2<\u0150\3\2\2\2>\u0159\3\2\2\2@\u0161\3\2\2\2BD\5\4")
        buf.write("\3\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2")
        buf.write("GH\7\2\2\3H\3\3\2\2\2IR\5\6\4\2JR\5\32\16\2KR\5\34\17")
        buf.write("\2LR\5\36\20\2MR\5(\25\2NR\5,\27\2OR\5\62\32\2PR\5 \21")
        buf.write("\2QI\3\2\2\2QJ\3\2\2\2QK\3\2\2\2QL\3\2\2\2QM\3\2\2\2Q")
        buf.write("N\3\2\2\2QO\3\2\2\2QP\3\2\2\2R\5\3\2\2\2SX\5\b\5\2TU\7")
        buf.write("\3\2\2UW\5\b\5\2VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2")
        buf.write("\2Y\7\3\2\2\2ZX\3\2\2\2[`\5\n\6\2\\]\7\4\2\2]_\5\n\6\2")
        buf.write("^\\\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\t\3\2\2\2b")
        buf.write("`\3\2\2\2ch\5\f\7\2de\7\36\2\2eg\5\f\7\2fd\3\2\2\2gj\3")
        buf.write("\2\2\2hf\3\2\2\2hi\3\2\2\2i\13\3\2\2\2jh\3\2\2\2kt\5\16")
        buf.write("\b\2lp\7#\2\2mp\3\2\2\2np\7$\2\2ol\3\2\2\2om\3\2\2\2o")
        buf.write("n\3\2\2\2pq\3\2\2\2qs\5\16\b\2ro\3\2\2\2sv\3\2\2\2tr\3")
        buf.write("\2\2\2tu\3\2\2\2u\r\3\2\2\2vt\3\2\2\2w|\5\20\t\2xy\t\2")
        buf.write("\2\2y{\5\20\t\2zx\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2")
        buf.write("\2}\17\3\2\2\2~|\3\2\2\2\177\u0081\t\3\2\2\u0080\177\3")
        buf.write("\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\5\22\n\2\u0083\21\3\2\2\2\u0084\u0091\5\24\13\2\u0085")
        buf.write("\u0086\7!\2\2\u0086\u0090\7\63\2\2\u0087\u0088\7*\2\2")
        buf.write("\u0088\u0089\5\6\4\2\u0089\u008a\7+\2\2\u008a\u0090\3")
        buf.write("\2\2\2\u008b\u008c\7(\2\2\u008c\u008d\5\26\f\2\u008d\u008e")
        buf.write("\7)\2\2\u008e\u0090\3\2\2\2\u008f\u0085\3\2\2\2\u008f")
        buf.write("\u0087\3\2\2\2\u008f\u008b\3\2\2\2\u0090\u0093\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\23\3\2")
        buf.write("\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7(\2\2\u0095\u0096")
        buf.write("\5\6\4\2\u0096\u0097\7)\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009b\7\63\2\2\u0099\u009b\5> \2\u009a\u0094\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\25\3\2")
        buf.write("\2\2\u009c\u00a1\5\6\4\2\u009d\u009e\7.\2\2\u009e\u00a0")
        buf.write("\5\6\4\2\u009f\u009d\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u009c\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a7\5\22\n\2\u00a7\31")
        buf.write("\3\2\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00aa\7 \2\2\u00aa")
        buf.write("\u00ab\5\6\4\2\u00ab\u00ac\5@!\2\u00ac\33\3\2\2\2\u00ad")
        buf.write("\u00ae\7\27\2\2\u00ae\u00b5\7\63\2\2\u00af\u00b6\5<\37")
        buf.write("\2\u00b0\u00b2\5<\37\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7\"\2\2\u00b4")
        buf.write("\u00b6\5\6\4\2\u00b5\u00af\3\2\2\2\u00b5\u00b1\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b8\5@!\2\u00b8\35\3\2\2")
        buf.write("\2\u00b9\u00ba\7\26\2\2\u00ba\u00bb\7\63\2\2\u00bb\u00bc")
        buf.write("\7\"\2\2\u00bc\u00bd\5\6\4\2\u00bd\u00be\5@!\2\u00be\37")
        buf.write("\3\2\2\2\u00bf\u00c0\7\27\2\2\u00c0\u00c5\7\63\2\2\u00c1")
        buf.write("\u00c2\7*\2\2\u00c2\u00c3\5\6\4\2\u00c3\u00c4\7+\2\2\u00c4")
        buf.write("\u00c6\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3")
        buf.write("\2\2\2\u00c9\u00ca\5<\37\2\u00ca\u00cb\7\"\2\2\u00cb\u00cc")
        buf.write("\58\35\2\u00cc\u00cd\5@!\2\u00cd!\3\2\2\2\u00ce\u00cf")
        buf.write("\7\63\2\2\u00cf\u00d0\5<\37\2\u00d0#\3\2\2\2\u00d1\u00d6")
        buf.write("\5\"\22\2\u00d2\u00d3\7.\2\2\u00d3\u00d5\5\"\22\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7%\3\2\2\2\u00d8\u00d6\3\2\2")
        buf.write("\2\u00d9\u00da\7\63\2\2\u00da\u00db\7\63\2\2\u00db\'\3")
        buf.write("\2\2\2\u00dc\u00e1\7\16\2\2\u00dd\u00de\7(\2\2\u00de\u00df")
        buf.write("\5&\24\2\u00df\u00e0\7)\2\2\u00e0\u00e2\3\2\2\2\u00e1")
        buf.write("\u00dd\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e4\7\63\2\2\u00e4\u00e6\7(\2\2\u00e5\u00e7\5")
        buf.write("$\23\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00ea\7)\2\2\u00e9\u00eb\5<\37\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ed\7,\2\2\u00ed\u00ee\7-\2\2\u00ee\u00ef\5@")
        buf.write("!\2\u00ef)\3\2\2\2\u00f0\u00f1\7\63\2\2\u00f1\u00f2\5")
        buf.write("<\37\2\u00f2\u00f3\5@!\2\u00f3+\3\2\2\2\u00f4\u00f5\7")
        buf.write("\17\2\2\u00f5\u00f6\7\63\2\2\u00f6\u00f7\7\20\2\2\u00f7")
        buf.write("\u00f9\7,\2\2\u00f8\u00fa\5@!\2\u00f9\u00f8\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fe\3\2\2\2\u00fb\u00fd\5*\26\2")
        buf.write("\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0102\7-\2\2\u0102\u0103\5@!\2\u0103-\3")
        buf.write("\2\2\2\u0104\u0106\7\63\2\2\u0105\u0107\5<\37\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u010f\3\2\2\2")
        buf.write("\u0108\u0109\7.\2\2\u0109\u010b\7\63\2\2\u010a\u010c\5")
        buf.write("<\37\2\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u0108\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110/\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u0113\7\63\2\2\u0113\u0115\7(\2\2")
        buf.write("\u0114\u0116\5.\30\2\u0115\u0114\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119\7)\2\2\u0118\u011a")
        buf.write("\5<\37\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011c\5@!\2\u011c\61\3\2\2\2\u011d")
        buf.write("\u011e\7\17\2\2\u011e\u011f\7\63\2\2\u011f\u0120\7\21")
        buf.write("\2\2\u0120\u0122\7,\2\2\u0121\u0123\5@!\2\u0122\u0121")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0127\3\2\2\2\u0124")
        buf.write("\u0126\5\60\31\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2")
        buf.write("\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7-\2\2\u012b")
        buf.write("\u012c\5@!\2\u012c\63\3\2\2\2\u012d\u0130\5\6\4\2\u012e")
        buf.write("\u0130\5\66\34\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2")
        buf.write("\2\u0130\65\3\2\2\2\u0131\u013a\7,\2\2\u0132\u0137\5\64")
        buf.write("\33\2\u0133\u0134\7.\2\2\u0134\u0136\5\64\33\2\u0135\u0133")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u013a\u0132\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013d\7-\2\2\u013d\67\3\2\2\2\u013e\u013f")
        buf.write("\7*\2\2\u013f\u0140\5\6\4\2\u0140\u0141\7+\2\2\u0141\u0143")
        buf.write("\3\2\2\2\u0142\u013e\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0147\5<\37\2\u0147\u0148\5\66\34\2\u01489\3\2")
        buf.write("\2\2\u0149\u014a\7\63\2\2\u014a\u014c\7,\2\2\u014b\u014d")
        buf.write("\5$\23\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u014f\7-\2\2\u014f;\3\2\2\2\u0150")
        buf.write("\u0151\t\4\2\2\u0151=\3\2\2\2\u0152\u015a\7\61\2\2\u0153")
        buf.write("\u015a\7\60\2\2\u0154\u015a\7\62\2\2\u0155\u015a\7\34")
        buf.write("\2\2\u0156\u015a\7\35\2\2\u0157\u015a\58\35\2\u0158\u015a")
        buf.write("\5:\36\2\u0159\u0152\3\2\2\2\u0159\u0153\3\2\2\2\u0159")
        buf.write("\u0154\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0156\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a?\3\2\2")
        buf.write("\2\u015b\u015d\t\5\2\2\u015c\u015b\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0162\3\2\2\2\u0160\u0162\7\2\2\3\u0161\u015c\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162A\3\2\2\2(EQX`hot|\u0080\u008f")
        buf.write("\u0091\u009a\u00a1\u00a4\u00b1\u00b5\u00c7\u00d6\u00e1")
        buf.write("\u00e6\u00ea\u00f9\u00fe\u0106\u010b\u010f\u0115\u0119")
        buf.write("\u0122\u0127\u012f\u0137\u013a\u0144\u014c\u0159\u015e")
        buf.write("\u0161")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'||'", "'&&'", "'!'", "'\n'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "'nil'", 
                     "'true'", "'false'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NL", "WS", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "IF_", 
                      "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                      "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                      "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                      "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "OP3", 
                      "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", 
                      "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
                      "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_expr0 = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_expr3 = 5
    RULE_expr4 = 6
    RULE_expr5 = 7
    RULE_expr6 = 8
    RULE_expr7 = 9
    RULE_expr_list = 10
    RULE_lhs = 11
    RULE_assigning = 12
    RULE_vardecl = 13
    RULE_constdecl = 14
    RULE_arraydecl = 15
    RULE_parameter = 16
    RULE_parameterlst = 17
    RULE_receiver = 18
    RULE_funcdecl = 19
    RULE_fielddecl = 20
    RULE_structdecl = 21
    RULE_method_para_list = 22
    RULE_methoddecl = 23
    RULE_interfacedecl = 24
    RULE_arr_elem = 25
    RULE_arr_elem_list = 26
    RULE_arr_literal = 27
    RULE_struct_literal = 28
    RULE_data_type = 29
    RULE_literal = 30
    RULE_end_stm = 31

    ruleNames =  [ "program", "decl", "expr0", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr_list", "lhs", 
                   "assigning", "vardecl", "constdecl", "arraydecl", "parameter", 
                   "parameterlst", "receiver", "funcdecl", "fielddecl", 
                   "structdecl", "method_para_list", "methoddecl", "interfacedecl", 
                   "arr_elem", "arr_elem_list", "arr_literal", "struct_literal", 
                   "data_type", "literal", "end_stm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NL=4
    WS=5
    SINGLE_LINE_CMT=6
    MULTI_LINE_CMT=7
    IF_=8
    ELSE_=9
    FOR_=10
    RETURN_=11
    FUNC_=12
    TYPE_=13
    STRUCT_=14
    INTERFACE_=15
    STRING_=16
    INT_=17
    FLOAT_=18
    BOOLEAN_=19
    CONST_=20
    VAR_=21
    CONTINUE_=22
    BREAK_=23
    RANGE_=24
    NIL_=25
    TRUE_=26
    FALSE_=27
    COMPARISON_OP=28
    OP3=29
    ASSIGN1=30
    OP5=31
    ASSIGN=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    LPAREN=38
    RPAREN=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    COMMA=44
    SEMICOLON=45
    FLOAT=46
    INTEGER=47
    STRING=48
    ID=49
    ERROR_CHAR=50
    ILLEGAL_ESCAPE=51
    UNCLOSE_STRING=52

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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.decl()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.FUNC_) | (1 << MiniGoParser.TYPE_) | (1 << MiniGoParser.CONST_) | (1 << MiniGoParser.VAR_) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 69
            self.match(MiniGoParser.EOF)
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

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.expr0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.assigning()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.vardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.funcdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.structdecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.interfacedecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 78
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr1Context,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)




    def expr0(self):

        localctx = MiniGoParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expr1()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 82
                self.match(MiniGoParser.T__0)
                self.state = 83
                self.expr1()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr2Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr2Context,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MiniGoParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expr2()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__1:
                self.state = 90
                self.match(MiniGoParser.T__1)
                self.state = 91
                self.expr2()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr3Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr3Context,i)


        def COMPARISON_OP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMPARISON_OP)
            else:
                return self.getToken(MiniGoParser.COMPARISON_OP, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = MiniGoParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expr3()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMPARISON_OP:
                self.state = 98
                self.match(MiniGoParser.COMPARISON_OP)
                self.state = 99
                self.expr3()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr4Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr4Context,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ADD)
            else:
                return self.getToken(MiniGoParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SUB)
            else:
                return self.getToken(MiniGoParser.SUB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = MiniGoParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expr4()
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 106
                        self.match(MiniGoParser.ADD)
                        pass

                    elif la_ == 2:
                        pass

                    elif la_ == 3:
                        self.state = 108
                        self.match(MiniGoParser.SUB)
                        pass


                    self.state = 111
                    self.expr4() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr5Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr5Context,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MUL)
            else:
                return self.getToken(MiniGoParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DIV)
            else:
                return self.getToken(MiniGoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MOD)
            else:
                return self.getToken(MiniGoParser.MOD, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MiniGoParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expr5()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 118
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.expr5()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 14, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__2 or _la==MiniGoParser.SUB:
                self.state = 125
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 128
            self.expr6()
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


        def OP5(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OP5)
            else:
                return self.getToken(MiniGoParser.OP5, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr_listContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expr7()
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.OP5]:
                        self.state = 131
                        self.match(MiniGoParser.OP5)
                        self.state = 132
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LSB]:
                        self.state = 133
                        self.match(MiniGoParser.LSB)
                        self.state = 134
                        self.expr0()
                        self.state = 135
                        self.match(MiniGoParser.RSB)
                        pass
                    elif token in [MiniGoParser.LPAREN]:
                        self.state = 137
                        self.match(MiniGoParser.LPAREN)
                        self.state = 138
                        self.expr_list()
                        self.state = 139
                        self.match(MiniGoParser.RPAREN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 18, self.RULE_expr7)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MiniGoParser.LPAREN)
                self.state = 147
                self.expr0()
                self.state = 148
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 154
                self.expr0()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 155
                    self.match(MiniGoParser.COMMA)
                    self.state = 156
                    self.expr0()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.expr6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


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
        self.enterRule(localctx, 24, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.lhs()
            self.state = 167
            self.match(MiniGoParser.ASSIGN1)
            self.state = 168
            self.expr0()
            self.state = 169
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MiniGoParser.VAR_)
            self.state = 172
            self.match(MiniGoParser.ID)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 173
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 174
                    self.data_type()


                self.state = 177
                self.match(MiniGoParser.ASSIGN)
                self.state = 178
                self.expr0()
                pass


            self.state = 181
            self.end_stm()
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


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
        self.enterRule(localctx, 28, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.CONST_)
            self.state = 184
            self.match(MiniGoParser.ID)
            self.state = 185
            self.match(MiniGoParser.ASSIGN)
            self.state = 186
            self.expr0()
            self.state = 187
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

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.VAR_)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 191
                self.match(MiniGoParser.LSB)
                self.state = 192
                self.expr0()
                self.state = 193
                self.match(MiniGoParser.RSB)
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 199
            self.data_type()
            self.state = 200
            self.match(MiniGoParser.ASSIGN)
            self.state = 201
            self.arr_literal()
            self.state = 202
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.ID)
            self.state = 205
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlst" ):
                return visitor.visitParameterlst(self)
            else:
                return visitor.visitChildren(self)




    def parameterlst(self):

        localctx = MiniGoParser.ParameterlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameterlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.parameter()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 208
                self.match(MiniGoParser.COMMA)
                self.state = 209
                self.parameter()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 216
            self.match(MiniGoParser.ID)
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


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
        self.enterRule(localctx, 38, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MiniGoParser.FUNC_)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 219
                self.match(MiniGoParser.LPAREN)
                self.state = 220
                self.receiver()
                self.state = 221
                self.match(MiniGoParser.RPAREN)


            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 226
            self.match(MiniGoParser.LPAREN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 227
                self.parameterlst()


            self.state = 230
            self.match(MiniGoParser.RPAREN)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 231
                self.data_type()


            self.state = 234
            self.match(MiniGoParser.LCB)
            self.state = 235
            self.match(MiniGoParser.RCB)
            self.state = 236
            self.end_stm()
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
        self.enterRule(localctx, 40, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 239
            self.data_type()
            self.state = 240
            self.end_stm()
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

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_stmContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_stmContext,i)


        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.TYPE_)
            self.state = 243
            self.match(MiniGoParser.ID)
            self.state = 244
            self.match(MiniGoParser.STRUCT_)
            self.state = 245
            self.match(MiniGoParser.LCB)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 246
                self.end_stm()


            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 249
                self.fielddecl()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
            self.match(MiniGoParser.RCB)
            self.state = 256
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def data_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Data_typeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Data_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_para_list" ):
                return visitor.visitMethod_para_list(self)
            else:
                return visitor.visitChildren(self)




    def method_para_list(self):

        localctx = MiniGoParser.Method_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.ID)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 259
                self.data_type()


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 262
                self.match(MiniGoParser.COMMA)
                self.state = 263
                self.match(MiniGoParser.ID)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                    self.state = 264
                    self.data_type()


                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def method_para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Method_para_listContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.ID)
            self.state = 273
            self.match(MiniGoParser.LPAREN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 274
                self.method_para_list()


            self.state = 277
            self.match(MiniGoParser.RPAREN)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING_) | (1 << MiniGoParser.INT_) | (1 << MiniGoParser.FLOAT_) | (1 << MiniGoParser.BOOLEAN_))) != 0):
                self.state = 278
                self.data_type()


            self.state = 281
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
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

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def end_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.End_stmContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.End_stmContext,i)


        def methoddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethoddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.TYPE_)
            self.state = 284
            self.match(MiniGoParser.ID)
            self.state = 285
            self.match(MiniGoParser.INTERFACE_)
            self.state = 286
            self.match(MiniGoParser.LCB)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.NL - -1)) | (1 << (MiniGoParser.SEMICOLON - -1)))) != 0):
                self.state = 287
                self.end_stm()


            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 290
                self.methoddecl()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.match(MiniGoParser.RCB)
            self.state = 297
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def arr_elem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem" ):
                return visitor.visitArr_elem(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem(self):

        localctx = MiniGoParser.Arr_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arr_elem)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__2, MiniGoParser.TRUE_, MiniGoParser.FALSE_, MiniGoParser.SUB, MiniGoParser.LPAREN, MiniGoParser.LSB, MiniGoParser.FLOAT, MiniGoParser.INTEGER, MiniGoParser.STRING, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.expr0()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.arr_elem_list()
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


    class Arr_elem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def arr_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_elemContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_elemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_elem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem_list" ):
                return visitor.visitArr_elem_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem_list(self):

        localctx = MiniGoParser.Arr_elem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arr_elem_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.LCB)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.TRUE_) | (1 << MiniGoParser.FALSE_) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 304
                self.arr_elem()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 305
                    self.match(MiniGoParser.COMMA)
                    self.state = 306
                    self.arr_elem()
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 314
            self.match(MiniGoParser.RCB)
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

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def arr_elem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_listContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr0Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr0Context,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_literal" ):
                return visitor.visitArr_literal(self)
            else:
                return visitor.visitChildren(self)




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arr_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 316
                self.match(MiniGoParser.LSB)
                self.state = 317
                self.expr0()
                self.state = 318
                self.match(MiniGoParser.RSB)
                self.state = 322 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 324
            self.data_type()
            self.state = 325
            self.arr_elem_list()
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

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def parameterlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.match(MiniGoParser.LCB)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 329
                self.parameterlst()


            self.state = 332
            self.match(MiniGoParser.RCB)
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

        def INT_(self):
            return self.getToken(MiniGoParser.INT_, 0)

        def FLOAT_(self):
            return self.getToken(MiniGoParser.FLOAT_, 0)

        def STRING_(self):
            return self.getToken(MiniGoParser.STRING_, 0)

        def BOOLEAN_(self):
            return self.getToken(MiniGoParser.BOOLEAN_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
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

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literal)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.TRUE_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [MiniGoParser.FALSE_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.arr_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 342
                self.struct_literal()
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

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NL)
            else:
                return self.getToken(MiniGoParser.NL, i)

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
        self.enterRule(localctx, 62, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NL, MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 345
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.NL or _la==MiniGoParser.SEMICOLON):
                        break

                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(MiniGoParser.EOF)
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





