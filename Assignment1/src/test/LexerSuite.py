import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_seperator(self):
        """test separator"""
        self.assertTrue(TestLexer.checkLexeme(";(){}][]",";,(,),{,},],[,],<EOF>",105))
    def test_floating_point0(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("12.34","12.34,<EOF>",106))
    def test_floating_point1(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("0.3e4","0.3e4,<EOF>",107))
    def test_floating_point2(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("101.e-4","101.e-4,<EOF>",108))
    def test_floating_point3(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("-1.","-,1.,<EOF>",109))
    def test_floating_point4(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("+1.23E+12","+,1.23E+12,<EOF>",110))
    def test_integet0(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123 -90 0 +14", "123,-,90,0,+,14,<EOF>",111))
    def test_integer1(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("0b1011 0B0001 0b010?01","0b1011,0B0001,0b010,ErrorToken ?",112))
    def test_integer2(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("0O102367 +0o123456 -0o6789", "0O102367,+,0o123456,-,0o67,89,<EOF>",113))
    def test_integer3(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("0xaa90B +0XFFF9f0 -0xBCDeF 0xABCDEFIJK", "0xaa90B,+,0XFFF9f0,-,0xBCDeF,0xABCDEF,IJK,<EOF>",114))
    def test_string0(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"abcABC\" \"def123!@#$\"","\"abcABC\",\"def123!@#$\",<EOF>",115))
    def test_string1(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"\\\\\\r\\t\\r\\\"\\n\"","\"\\\\\\r\\t\\r\\\"\\n\",<EOF>",116))
    def test_string2(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"This 1s @ l0NG Str1ng wiTH different*()&* ch4r4ct3rs_+-=*\"","\"This 1s @ l0NG Str1ng wiTH different*()&* ch4r4ct3rs_+-=*\",<EOF>",117))
    def test_string3(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"Sample\"\"","\"Sample\",ErrorToken \"",118))
    def test_string4(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("\"Sample\\\"","Unclosed string: Sample\\\"",119))
    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\"Sample\\a\"","Illegal escape in string: Sample\\a",120))
    def test_illegal_escape1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\"This is a \\b sentence\"", "Illegal escape in string: This is a \\b",121))
    def test_illegal_escape2(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\"This is \\n \\\" a sentence\" 0x123ADB \"This is anoth\\rer sen\\ltence\"", "\"This is \\n \\\" a sentence\",0x123ADB,Illegal escape in string: This is anoth\\rer sen\\l",122))
    def test_illegal_escape3(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\"\\q \\l \\r\"", "Illegal escape in string: \\q",123))
    def test_illegal_escape4(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("\" \\r \\n \\~", "Illegal escape in string:  \\r \\n \\~",124))
    def test_unclosed_string0(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"This is an unclosed string", "Unclosed string: This is an unclosed string", 125))
    def test_unclosed_string1(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"asdasd \\n \" func \"asdasd \\t", "\"asdasd \\n \",func,Unclosed string: asdasd \\t", 126))
    def test_unclosed_string2(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"", "ErrorToken \"", 127))
    def test_unclosed_string3(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"asd\"asdasd\"ajsdlajsd", "\"asd\",asdasd,Unclosed string: ajsdlajsd", 128))
    def test_unclosed_string4(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"if else [", "Unclosed string: if else [", 129))
    def test_unclosed_string5(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"if else \\n if else", "Unclosed string: if else ", 130))
    def test_identifier0(self):
        """test identifier"""
        self.assertTrue(TestLexer.checkLexeme("abcABC[ 098xdef }","abcABC,[,0,98,xdef,},<EOF>",131))
    def test_floating_point5(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("0X1234.5e+7","0X1234,.,5,e,+,7,<EOF>",132))
    def test_operators0(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("== != < <= > >= && || ! := += -= *= /= %= =","==,!=,<,<=,>,>=,&&,||,!,:=,+=,-=,*=,/=,%=,=,<EOF>",133))
    def test_operators1(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("abc.def[10]","abc,.,def,[,10,],<EOF>",134))
    def test_operators2(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("abc.def[abc.def()].def[10] >= _XADC.def[0][123]","abc,.,def,[,abc,.,def,(,),],.,def,[,10,],>=,_XADC,.,def,[,0,],[,123,],<EOF>",135))
    def test_operators3(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a[0][0](1, 2, \"asdasd\", true).asd.asdasd","a,[,0,],[,0,],(,1,,,2,,,\"asdasd\",,,true,),.,asd,.,asdasd,<EOF>",136))
    def test_newline0(self):
        """test newline"""
        input = """abc = 10
        def = 20"""
        expect = "abc,=,10,\n,def,=,20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,137))
    def test_newline1(self):
        """test newline"""
        input = """a *= 2; b -= 15.6 c /= \"asdasd\""""
        expect = "a,*=,2,;,b,-=,15.6,c,/=,\"asdasd\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,138))
    def test_comment0(self):
        """test comment"""
        input = """// This is a comment"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,139))
    def test_comment1(self):
        """test comment"""
        input = """// This is a comment
        This is not a comment"""
        expect = "\n,This,is,not,a,comment,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,140))
    def test_comment2(self):
        """test comment"""
        input = """var a int = 6 // This is a comment ;"""
        expect = "var,a,int,=,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,141))
    def test_comment3(self):
        """test comment"""
        input = """/* This is
        a multi-line comment */ var a int = 6"""
        expect = "var,a,int,=,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,142))
    def test_comment4(self):
        """test comment"""
        input = """/* This is
        a /* nested */ comment */ var a int = 6 // This is a comment ;"""
        expect = "var,a,int,=,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,143))
    def test_comment5(self):
        """test comment"""
        input = """/* This is
        a /* nested comment */ var a int = 6 // This is a comment ;"""
        expect = "var,a,int,=,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,144))
    def test_ifelse0(self):
        """test ifelse"""
        input = """if (a > b) {
            a = b;
            } else if (a < b) {
            b = a;
            } else {
            a = b;
            }"""
        expect = "if,(,a,>,b,),{,\n,a,=,b,;,\n,},else,if,(,a,<,b,),{,\n,b,=,a,;,\n,},else,{,\n,a,=,b,;,\n,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,145))
    def test_ifelse1(self):
        """test ifelse"""
        input = """if (a > b || c < d) {
            a := b;
        }
        """
        expect = "if,(,a,>,b,||,c,<,d,),{,\n,a,:=,b,;,\n,},\n,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,146))
    def test_assign0(self):
        """test assign"""
        input = """a *= 2; b -= 15.6 c /= \"asdasd\""""
        expect = "a,*=,2,;,b,-=,15.6,c,/=,\"asdasd\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,147))
    
    