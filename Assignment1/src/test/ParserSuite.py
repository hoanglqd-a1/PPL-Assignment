import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_vardecl0(self):
        input = """var a ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_vardecl1(self):
        input = """var a int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_vardecl2(self):
        input = """var a float = 1.0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_vardecl3(self):
        input = """var a boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_vardecl4(self):
        input = """var a string = "Hello World";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_vardecl5(self):
        input = """var a int = 12.5 + 12 * -3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_vardecl6(self):
        input = """var a int = 6;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_vardecl7(self):
        input = """var a int 6;"""
        expect = "Error on line 1 col 11: 6"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_vardecl8(self):
        input = """var int = 6;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_vardecl9(self):
        input = """a int = 6;"""
        expect = "Error on line 1 col 3: int"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_vardecl10(self):
        input = """var a = 0x1234ABCD;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_vardecl11(self):
        input = """var a = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_vardecl12(self):
        input = """var a = "Hello World \\n [] \\\\ \\\"";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_vardecl13(self):
        input = """var string a = "Hello World \\n [] \\\\ \\\"";"""
        expect = "Error on line 1 col 5: string"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_vardecl14(self):
        input = """var a float;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_constdecl0(self):
        input = """const a = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_constdecl1(self):
        input = """const a = ;"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_funcdecl0(self):
        input = """func main () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_funcdecl1(self):
        input = """func main (xyz int) int {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_funcdecl2(self):
        input = """func main (xyz int, str string, f float, b boolean) float { };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_funcdecl3(self):
        input = """func (c Calculator) main (xyz int, str string) { };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_funcdecl4(self):
        input = """func (xyz int) float { }"""
        expect = "Error on line 1 col 11: int"        
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_funcdecl5(self):
        input = """func () float { }"""
        expect = "Error on line 1 col 7: )"        
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_funcdecl6(self):
        input = """func main int {}"""
        expect = "Error on line 1 col 11: int"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_assign0(self):
        input = """a := 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_assign1(self):
        input = """a += 1.0
b := 1.0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_assign2(self):
        input = """a *= 2; b -= 15.6; c /= \"asdasd\";"""        
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_assign3(self):
        input = """a *= 2; b -= 15.6 c /= \"asdasd\""""        
        expect = "Error on line 1 col 19: c"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_struct_decl0(self):
        input = """type A struct{ a int 
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_struct_decl1(self):
        input = """type A struct {a int; b float ;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_struct_decl2(self):
        input = """type A struct { 
        a int
        c string
        }"""
        expect = "Error on line 4 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_struct_decl3(self):
        input = """type A struct { 
        if int; 
        else float ;}
        """
        expect = "Error on line 2 col 9: if"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_interface_decl0(self):
        input = """type A interface{ 
        a() int;
        b(c int) float;
        C()
        D(a, b string)
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_interface_decl1(self):
        input = """type A interface  { 
        function(a, b, c, d int, e, f string, g, h, i float, j, k, l, m, n boolean); func0() boolean
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_interface_decl2(self):
        input = """type A interface{ 
        a() int b() float
        };"""
        expect = "Error on line 2 col 17: b"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_interface_decl3(self):
        input = """type A interface{
        a int 
        b() float
        };"""
        expect = "Error on line 2 col 11: int"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_assign4(self):
        input = """a += -1.0 * 2 || true && false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_assign5(self):
        input = """a[1][2][b(1)] %= n[2] * func0(1)
        a[1][3] += 1.0 * 2 || true && false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_vardecl15(self):
        input = """var a = \"string\" + \"string\" * 2 / 34;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_vardecl16(self):
        input = """var func = 2.0 * (4 * 0.5)
        """
        expect = "Error on line 1 col 5: func"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_constdecl2(self):
        input = """const a = 2.0 * (4 * 0.5)
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_constdecl3(self):
        input = """const a = abc[ref[1][2]] * 90 - ero % 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_expr_syntax0(self):
        input = """a.b"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21030))
    def test_expr_syntax1(self):
        input = """abc[asda.asd[1]][ghj(12.3).ref(false)].lo(lqd)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21031))
    def test_expr_syntax2(self):
        input = """abc[asda.asd"""
        expect = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,21032))
    def test_expr_syntax3(self):
        input = """10 + abc || efd >= 10 && 123 % 10 + ARE.xyz[123] || !(true && false)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21033))
    def test_expr_syntax4(self):
        input = """- FUNC.abc(\"asda\", 10)[123][12] / 10.0 * (abc() + 10) || 12 % 23 - 5.5 < 0"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21034))
    def test_expr_syntax5(self):
        input = """abcasd && (true || false && !(var1 == var2.ref()) ) || !(def && !ahg)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21035))
    def test_expr_syntax6(self):
        input = """acv[123][(abc.def.efd[0][0b101] + efg) * 10].get(123, 10.0, true)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21036))
    def test_expr_syntax7(self):
        input = """\"Hello World\".upper()"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21037))