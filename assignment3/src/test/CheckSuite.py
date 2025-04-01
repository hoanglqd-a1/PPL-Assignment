import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_no_error(self):
        input = """
        var a int; 
        const b float = 1.0;
        struct StructB{
            A StructA;
            c float;
        }
        func main(a int, b float){
            var x float;
            var y string;
            var A StructA;
        }
        struct StructA{
            a int;
            b bool;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,403))
  