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
    def test_integer0(self):
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
        self.assertTrue(TestLexer.checkLexeme("\"if else \\n if else", "Unclosed string: if else \\n if else", 130))
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
        expect = "abc,=,10,;,def,=,20,<EOF>"
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
        expect = "This,is,not,a,comment,<EOF>"
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
        expect = "if,(,a,>,b,),{,a,=,b,;,},else,if,(,a,<,b,),{,b,=,a,;,},else,{,a,=,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,145))
    def test_ifelse1(self):
        """test ifelse"""
        input = """if (a > b || c < d) {
            a := b;
        }
        """
        expect = "if,(,a,>,b,||,c,<,d,),{,a,:=,b,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,146))
    def test_assignment6(self):
        """test assign"""
        input = """a *= 2; b -= 15.6 c /= \"asdasd\""""
        expect = "a,*=,2,;,b,-=,15.6,c,/=,\"asdasd\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,147))
    def test_ID0(self):
        """test ID"""
        input = """abc = 10"""
        expect = "abc,=,10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,148))
    def test_ID1(self):
        """test ID"""
        input = """___abc = 10"""
        expect = "___abc,=,10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,149))
    def test_ID2(self):
        input = """AHJH_asdasd__asd_asd = ____"""
        expect = "AHJH_asdasd__asd_asd,=,____,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,150))
    def test_ID3(self):
        input = """10abcd_edf"""
        expect = "10,abcd_edf,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,151))
    def test_ID4(self):
        input = """10__asda123anlj"""
        expect = "10,__asda123anlj,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,152))
    def test_ID5(self):
        input = """_ addda_aaaa%tyda!sd"""
        expect = "_,addda_aaaa,%,tyda,!,sd,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,153))
    def test_string5(self):
        input = """\"asdasd\\g \\h \\l \\n \\r \\t \\\" \\\" \\\" \\\" \\\""""
        expect = "Illegal escape in string: asdasd\\g"
        self.assertTrue(TestLexer.checkLexeme(input,expect,154))
    def test_string6(self):
        input = """\"asdasd\" \\l"""
        expect = "\"asdasd\",ErrorToken \\"
        self.assertTrue(TestLexer.checkLexeme(input,expect,155))
    def test_string7(self):
        input = """\"Va bau troi dem ngan sao toa sang
        var x int = 10;"""
        expect = "Unclosed string: Va bau troi dem ngan sao toa sang"
        self.assertTrue(TestLexer.checkLexeme(input,expect,156))
    def test_string8(self):
        input = """var x = 10;
        var str string = \"Tieng toi vang rung nui, sao khong ai tra loi
        """
        expect = "var,x,=,10,;,var,str,string,=,Unclosed string: Tieng toi vang rung nui, sao khong ai tra loi"
        self.assertTrue(TestLexer.checkLexeme(input,expect,157))
    def test_string9(self):
        input = """var x = \"Nhan tin theo cung gio \" khan con \"day doi nguoi"""
        expect = "var,x,=,\"Nhan tin theo cung gio \",khan,con,Unclosed string: day doi nguoi"
        self.assertTrue(TestLexer.checkLexeme(input,expect,158))
    def test_floating_point6(self):
        input = """09e101"""
        expect = "0,9,e101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,159))
    def test_floating_point7(self):
        input = """129e-101"""
        expect = "129,e,-,101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,160))
    def test_floating_point8(self):
        input = """.129e+101"""
        expect = ".,129,e,+,101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,161))
    def test_floating_point9(self):
        input = """-00.E-101"""
        expect = "-,00.E-101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,162))
    def test_floating_point10(self):
        input = """+11.11e+10e-10"""
        expect = "+,11.11e+10,e,-,10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,163))
    def test_floating_point11(self):
        input = """+123.45e-10.01934+E111"""
        expect = "+,123.45e-10,.,0,1934,+,E111,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,164))
    def test_vardeclare0(self):
        input = """var a = 0x1234ABCD;"""
        expect = "var,a,=,0x1234ABCD,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,165))
    def test_vardeclare1(self):
        input = """var a = "Hello World \\n [] \\\\ \\\"";"""
        expect = """var,a,=,"Hello World \\n [] \\\\ \\\"",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,166))
    def test_vardeclare2(self):
        input = """var string a = "Hello World \\n [] \\\\ \\\"";"""
        expect = """var,string,a,=,"Hello World \\n [] \\\\ \\\"",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,167))
    def test_funcdecl0(self):
        input = """func main (xyz int) int {}
        """
        expect = """func,main,(,xyz,int,),int,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,168))
    def test_funcdecl1(self):
        input = """func main (xyz int, str string, f float, b boolean) float { };"""
        expect = """func,main,(,xyz,int,,,str,string,,,f,float,,,b,boolean,),float,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,169))
    def test_funcdecl2(self):
        input = """func (c Calculator) main (xyz int, str string) { };"""
        expect = """func,(,c,Calculator,),main,(,xyz,int,,,str,string,),{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,170))
    def test_funcdecl3(self):
        input = """func Fibonacci(n int) int {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    } else {
        return Fibonacci(n-1) + Fibonacci(n-2)
    }
}
        """
        expect = "func,Fibonacci,(,n,int,),int,{,if,(,n,==,0,),{,return,0,;,},else,if,(,n,==,1,),{,return,1,;,},else,{,return,Fibonacci,(,n,-,1,),+,Fibonacci,(,n,-,2,),;,},;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,171))
    def test_assignment0(self):
        input = """a *= 2; b -= 15.6; c /= \"asdasd\";"""
        expect = """a,*=,2,;,b,-=,15.6,;,c,/=,"asdasd",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,172))
    def test_assignment1(self):
        input = """a *= 2; b -= 15.6 c"""  
        expect = """a,*=,2,;,b,-=,15.6,c,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,173))
    def test_structdecl0(self):
        input = """type A struct{ a int 
        }"""
        expect = """type,A,struct,{,a,int,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,174))
    def test_structdecl1(self):
        input = """type A struct { 
        a int
        c string
        }"""
        expect = """type,A,struct,{,a,int,;,c,string,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,175))
    def test_structdecl2(self):
        input = """type A struct { 
        if int; 
        else float ;}
        """
        expect = """type,A,struct,{,if,int,;,else,float,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,176))
    def test_interface0(self):
        input = """type A interface{ 
        a() int;
        b(c int) float;
        C()
        D(a, b string)
        };"""
        expect = """type,A,interface,{,a,(,),int,;,b,(,c,int,),float,;,C,(,),;,D,(,a,,,b,string,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,177))
    def test_interface1(self):
        input = """type A interface  { 
        function(a, b, c, d int, e, f string, g, h, i float, j, k, l, m, n boolean); func0() boolean
        };"""
        expect = """type,A,interface,{,function,(,a,,,b,,,c,,,d,int,,,e,,,f,string,,,g,,,h,,,i,float,,,j,,,k,,,l,,,m,,,n,boolean,),;,func0,(,),boolean,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,178))
    def test_assignment2(self):
        input = """a[1][2][b(1)] %= n[2] * func0(1)"""
        expect = """a,[,1,],[,2,],[,b,(,1,),],%=,n,[,2,],*,func0,(,1,),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,179))
    def test_assignment3(self):
        input = """a[1][3] += 1.0 * 2 || true && false;"""
        expect = """a,[,1,],[,3,],+=,1.0,*,2,||,true,&&,false,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,180))
    def test_assignment4(self):
        input = """var a = \"string\" + \"string\" * 2 / 34;"""
        expect = """var,a,=,\"string\",+,\"string\",*,2,/,34,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,181))
    def test_assignment5(self):
        input = """const a = 2.0 * (4 * 0.5)"""
        expect = """const,a,=,2.0,*,(,4,*,0.5,),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,182))
    def test_arraydecl0(self):
        input = """var a [10]int = [10]int{1,2,3,4,5,6,7};"""
        expect = """var,a,[,10,],int,=,[,10,],int,{,1,,,2,,,3,,,4,,,5,,,6,,,7,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,183))
    def test_arraydecl1(self):
        input = """var b [3] string = [3] {1,2,3};"""
        expect = """var,b,[,3,],string,=,[,3,],{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,184))
    def test_integer4(self):
        input = """b101000232341"""
        expect = """b101000232341,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,185))
    def test_integer5(self):
        input = """0B1011010001201"""
        expect = "0B1011010001,201,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,186))
    def test_integer6(self):
        input = """00b0100011010"""
        expect = """0,0b0100011010,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,187))
    def test_integer7(self):
        input = """0O371239908"""
        expect = "0O37123,9908,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,188))
    def test_integer8(self):
        input = """0O13110o9099"""
        expect = "0O13110,o9099,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,189))
    def test_integer9(self):
        input = """0987765"""
        expect = "0,987765,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,190))
    def test_integer10(self):
        input = """0xAB980FEDGHJK900X111"""
        expect = """0xAB980FED,GHJK900X111,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,191))
    def test_integer11(self):
        input = """0x018394AbcdeF"""
        expect = "0x018394AbcdeF,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,192))
    def test_forloop0(self):
        input = """for i := 0; i < 10; i += 1 {
        }
        """
        expect = "for,i,:=,0,;,i,<,10,;,i,+=,1,{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,193))
    def test_forloop1(self):
        input = """for index, value := range arr {
            a /= 100;
            b -= 20;
        }"""
        expect = """for,index,,,value,:=,range,arr,{,a,/=,100,;,b,-=,20,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,194))
    def test_forloop2(self):
        input = """for i < 10; i:= 10; i += 2 {}
        """
        expect = """for,i,<,10,;,i,:=,10,;,i,+=,2,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,195))
    def test_forloop3(self):
        input = """for index, value := range [3]int{1,2,3} {}"""
        expect = """for,index,,,value,:=,range,[,3,],int,{,1,,,2,,,3,},{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,196))
    def test_funccall0(self):
        input = """abc.ads.ghj.xyz()"""
        expect = """abc,.,ads,.,ghj,.,xyz,(,),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,197))
    def test_funccall1(self):
        input = """function("duanhcomangloilam\""""
        expect = """function,(,"duanhcomangloilam",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,198))
    def test_funccall2(self):
        input = """atvncg("ngoi", "chot", "nghe" "buoc", "em", "ve")"""
        expect = """atvncg,(,"ngoi",,,"chot",,,"nghe","buoc",,,"em",,,"ve",),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,199))
    def test_statement0(self):
        input = """return 10; break; continue;"""
        expect = """return,10,;,break,;,continue,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,200))
    def test_newline2(self):
        input = """break
        """
        expect = """break,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,2001))
    def test_newline3(self):
        input = """var
        a int =
        0b100101
        """
        expect = """var,a,int,=,0b100101,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,2002))