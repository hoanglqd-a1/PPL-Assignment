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
        input = """a *= 2; b -= 15.6 c"""        
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
        expect = "successful"
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
    def test_arraydecl0(self):
        input = """var a [10]int = [10]int{1,2,3,4,5,6,7,8,9,10};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_arraydecl1(self):
        input = """var a [3][2] int = [3][2]int{{1,2},{3,4},{5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_arraydecl2(self):
        input = """var a [2][1][1][1] float = [2][1][1][1]int{{{{1}}},{{{1}}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_arraydecl3(self):
        input = """var b [3] = [3]int{1,2,3};"""
        expect = "Error on line 1 col 11: ="
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_arraydecl4(self):
        input = """var b [3] string = [3] {1,2,3};"""
        expect = "Error on line 1 col 24: {"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_ifexpr0(self):
        input = """if (a > b || c < d) {
            a += 3 + 5
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_ifexpr1(self):
        input = """if (a > b || c < d) {
            a := b;
            c := d
        } else {
            a := b;
            c := d
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_ifexpr2(self):
        input = """if () {
            a := b;
            c := d
        } else if (a > b || c < d) {
            a := b;
            c := d
        } else {
            a := b;
            c := d
        }
        """
        expect = "Error on line 1 col 5: )"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_ifexpr3(self):
        input = """if (a > b || c < d) {
            a := b;
            c := d
        } else if (a > b || c < d) {
            a := b;
            c := d
        } else if (a > b || c < d) {
            a := b;
            c := d
        } else {
            a := b;
            c := d
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_ifexpr4(self):
        input = """if (a > b || c < d) { a := b; c := d
        }else { a := b;
            c := d
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_ifexpr5(self):
        input = """else if (a > b || c < d) { a := b; c := d
        } else { a := b;
            c := d
        }
        """
        expect = "Error on line 1 col 1: else"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_ifexpr6(self):
        input = """if (a > 0) a:= 0"""
        expect = """Error on line 1 col 12: a"""
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_forloop0(self):
        input = """for i := 0; i < 10; i += 1 {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_forloop1(self):
        input = """for i * 8 - 2 < 10 {
            a := 100;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_forloop2(self):
        input = """for index, value := range arr {
            a /= 100;
            b -= 20;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_forloop3(self):
        input = """for i < 10; i:= 10; i += 2 {}
        """
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_forloop4(self):
        input = """for i:= 10; i *= 2; i < 100 {}
        """
        expect = "Error on line 1 col 15: *="
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_forloop5(self):
        input = """for index, value := range [3]int{1,2,3} {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_break0(self):
        input = """break"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_break1(self):
        inpput = """break for i := 0; i < 10; i += 1 {
            
        }"""
        expect = "Error on line 1 col 7: for"
        self.assertTrue(TestParser.checkParser(inpput,expect,267))
    def test_continue0(self):
        input = """continue"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_continue1(self):
        input = """continue for i := 0; i < 10; i += 1 {
            
        }"""
        expect = "Error on line 1 col 10: for"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_funccall0(self):
        input = """a()"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_funccall1(self):
        input = """a(b, 10, "asc", false)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_funccall2(self):
        input = """abc.ads.ghj.xyz()"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_funccall3(self):
        input = """fun(12, 3, 4,)"""
        expect = "Error on line 1 col 14: )"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_funccall4(self):
        input = """function("duanhcomangloilam" """
        expect = "Error on line 1 col 30: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_funccall5(self):
        input = """atvncg("ngoi", "chot", "nghe" "buoc", "em", "ve")"""
        expect = "Error on line 1 col 31: \"buoc\""
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_return0(self):
        input = """return"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_return1(self):
        input = """return 10"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
