import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_gllobal_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_var_decl0(self):
        input = """func main() {var a float = 10;  putFloat(a);};"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_var_decl1(self):
        input = """func main() {var a [3]int = [3]int{1,2,3}; putInt(10);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_var_decl2(self):
        input = """func main() {var a [2][2]int = [2][2]int{{1,2},{3,4}}; putInt(10);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_struct_decl0(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func main() {
    var a = A{b: 2.0, c: "abc", a: 1};
    putInt(12);
};"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_func_decl0(self):
        input = """
func add(a int, b int) int {
    return a;
}
func main() {
    putInt(add(1, 2));
};"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_struct_decl1(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func main() {
    var a = A{b: 2.0, c: "abc"};
    putInt(12);
};"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_field_access0(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func main() {
    var a = A{b: 10.0, c: "abc"};
    putFloat(a.b);
};"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_method_decl0(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func (a A) add(b int) int {
    return b;
}
func main() {
    var a = A{b: 10.0, c: "abc"};
    putInt(10);
};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_method_call0(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func (a A) add(b int) int {
    putFloatLn(a.b);
    return b;
}
func (d A) getC() string {
    return d.c;
}
func main() {
    var a = A{b: 10.0, c: "abc", a: 1};
    putIntLn(a.add(10));
    putString(a.getC());
};"""
        expect = """10.0
10
abc"""
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_method_call1(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func (a A) print() {
    putInt(a.a);
    putString(" ");
    putFloat(a.b);
    putString(" ");
    putString(a.c);
}
func main() {
    var a = A{b: 10.0, c: "abc", a: 1};
    a.print();
};"""
        expect = "1 10.0 abc"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_interface_decl0(self):
        input = """
type A interface {
    print();
}
type B struct {
    a int;
}
func (b B) print() {
    putInt(b.a);
}
func main() {
    var abc A = B{a: 1};
    abc.print();
};"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_interface_decl1(self):
        input = """
type A interface {
    print();
}
type B struct {
    a int;
}
func (b B) print() {
    putInt(b.a);
}
type C struct {
    a int;
}
func (c C) print() {
    putInt(c.a);
}
func main() {
    var abc A = B{a: 1};
    abc.print();
    var def A = C{a: 2};
    def.print();
};"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_constant_decl0(self):
        input = """
const b float = 10.0
func main() {
    const a int = 10;
    putInt(a);
    putFloat(b);
};"""
        expect = "1010.0"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_assignment0(self):
        input = """
func main() {
    var a int;
    a := 10;
    putInt(a);
}"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_assignment1(self):
        input = """
func main() {
    var a [3]int;
    a := [3]int{1,2,3};
}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_assignment2(self):
        input = """
type A struct {
    a int;
}
func main() {
    var a = A{a: 10};
    a := A{a: 300};
    putInt(a.a);
    a.a := 4;
    putInt(a.a);
}"""
        expect = "3004"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_constant_decl1(self):
        input = """
type A struct {
    a int;
}
func main() {
    const a A = A{a: 1975};
    putInt(a.a);
}"""
        expect = "1975"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_array_cell0(self):
        input = """
func main() {
    var a [3]int;
    a := [3]int{30,4,1975};
    putInt(a[1]);
}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_array_cell1(self):
        input = """
func main() {
    var a [3]int;
    a := [3]int{30,3,1975};
    a[1] := 4;
    putInt(a[0]);
    putString("/");
    putInt(a[1]);
    putString("/");
    putInt(a[2]);
}"""
        expect = "30/4/1975"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_array_cell2(self):
        input = """
func main() {
    var a [2][2] int;
    a := [2][2]int{{2,2},{3,4}};
    putInt(a[0][0]);
    a[0][1] := 9;
    putString("/");
    putInt(a[0][1]);
}"""
        expect = "2/9"
        self.assertTrue(TestCodeGen.test(input,expect,526))