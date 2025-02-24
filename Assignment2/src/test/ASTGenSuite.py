import unittest
from TestUtils import TestAST
from main.minigo.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {var x int;};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {var x int = 100;}; var x int ;"""
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),Block([
                    VarDecl("x",IntType(),IntLiteral(100))
                ])),
                VarDecl("x",IntType(),None)
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_constdecl0(self):
        """Constant declaration"""
        input = """const x int = 100;"""
        expect = str(
            Program([
                ConstDecl("x",IntType(),IntLiteral(100))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_funcdecl0(self):
        """Function declaration"""
        input = """func main (x int) int {var y int; var z int = 100;};"""
        expect = str(
            Program([
                FuncDecl("main",[ParamDecl("x",IntType())],IntType(),Block([
                    VarDecl("y",IntType(),None),
                    VarDecl("z",IntType(),IntLiteral(100))
                ]))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_structdecl0(self):
        """Struct declaration"""
        input = """type A struct {x int; y float;};"""
        expect = str(
            Program([
                StructType("A",
                [
                    ("x",IntType()),
                    ("y",FloatType())
                ],
                [])
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_interfacedecl0(self):
        """Interface declaration"""
        input = """type A interface {x(y string) int;};"""
        expect = str(
            Program([
                InterfaceType("A",
                [
                    Prototype("x",[StringType()],IntType())
                ])
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_ifstmt0(self):
        """If statement"""
        input = """func main() {
            if (x==y) {
                var z int = 100;
            }
        }"""
        expect = str(
            Program([
                FuncDecl("main",[],VoidType(),
                    Block([
                        If(
                            BinaryOp("==",Id("x"),Id("y")),
                            Block([
                                VarDecl("z",IntType(),IntLiteral(100))
                            ]),
                            None
                        )
                    ])
                ),
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
   