import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int_literal(self):
    #     input = """func main() {putInt(5);};"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_local_var(self):
    #     input = """func main() {var a int = 20;  putInt(a);};"""
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_gllobal_var(self):
    #     input = """var a int = 10; func main() { putInt(a);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_int_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_local_var_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
    #     expect = "500"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_global_var_ast(self):  
    #     input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
    #     expect = "5000"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
    # def test_var_decl0(self):
    #     input = """func main() {var a float = 10;  putFloat(a);};"""
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_var_decl1(self):
    #     input = """func main() {var a [3]int = [3]int{1,2,3}; putInt(10);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_var_decl1(self):
    #     input = """func main() {var a [2][2]int = [2][2]int{{1,2},{3,4}}; putInt(10);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_struct_decl0(self):
        input = """
type A struct {
    a int;
    b float;
    c string;
}
func main() {
    var a = A{a: 1, b: 2.0, c: "abc"};
    putInt(12);
};"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,510))
#     def test_func_decl0(self):
#         input = """
# func add(a int, b int) int {
#     return a;
# }
# func main() {
#     putInt(add(1, 2));
# };"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,511))