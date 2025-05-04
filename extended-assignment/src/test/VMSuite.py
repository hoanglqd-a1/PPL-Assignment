import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    def test_simple_program(self):        
        input = """[[],[],[call(writeInt,[3])]]."""
        expect = "3"    
        self.assertTrue(TestVM.test(input, expect, 401))

    def test_simple_expression(self):        
        input = """[[],[],[call(writeInt,[add(3,1)])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 402))

    def test_redeclaration(self):        
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 403))

    def test_minus_expression(self):        
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 404))

    def test_nested_expression(self):        
        input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
        expect = "6"
        self.assertTrue(TestVM.test(input, expect, 405))
    def test_0(self):
        input = """[[],[],[call(writeInt,[times(add(1,2),3)])]]."""
        expect = "9"
        self.assertTrue(TestVM.test(input, expect, 406))
    def test_simple_program1(self):        
        input = """[[],[],[call(writeReal,[3.0])]]."""
        expect = "3.0"    
        self.assertTrue(TestVM.test(input, expect, 407))
    def test_simple_program2(self):
        input = """[[],[],[call(writeStr,["abc"])]]."""
        expect = "abc"
        self.assertTrue(TestVM.test(input, expect, 408))
    def test_simple_program3(self):
        input = """[[],[],[call(writeBool,[true])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 409))
    def test_simple_expression0(self):
        input = """[[],[],[call(writeInt,[times(add(3,1),sub(2))])]]."""
        expect = "-8"
        self.assertTrue(TestVM.test(input, expect, 410))
    def test_simple_expression1(self):
        input = """[[],[],[call(writeReal,[sub(add(rdiv(5,2),3.6))])]]."""
        expect = "-6.1"
        self.assertTrue(TestVM.test(input, expect, 411))
    def test_constdecl0(self):
        input = """[[const(a,1)],[],[call(writeInt,[1])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 412))
    def test_constdecl1(self):
        input = """[[const(a,1),const(a,2)],[],[call(writeInt,[add(a,b)])]]."""
        expect = "Redeclared identifier: const(a,2)"
        self.assertTrue(TestVM.test(input, expect, 413))
    def test_constdecl3(self):
        input = """[[const(writeInt,1)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(writeInt,1)"
        self.assertTrue(TestVM.test(input, expect, 414))
    def test_funcdecl0(self):
        input = """[[],[func(foo,[par(a,integer)],integer,[])],[]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 415))
    def test_funcdecl1(self):
        input = """[[const(foo,12)],[func(foo,[par(a,integer)],integer,[])],[]]."""
        expect = "Redeclared function: func(foo,[par(a,integer)],integer,[])"
        self.assertTrue(TestVM.test(input, expect, 416))
    def test_funcdecl2(self):
        input = """[[],[func(foo,[par(a,integer),par(a,float)],integer,[])],[]]."""
        expect = "Redeclared identifier: par(a,float)"
        self.assertTrue(TestVM.test(input, expect, 417))
    def test_procdecl0(self):
        input = """[[],[proc(foo,[par(a,integer)],[])],[]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 418))
    def test_procdecl1(self):
        input = """[[const(foo,12)],[proc(foo,[par(a,integer)],[])],[]]."""
        expect = "Redeclared procedure: proc(foo,[par(a,integer)],[])"
        self.assertTrue(TestVM.test(input, expect, 419))
    def test_procdecl2(self):
        input = """[[],[proc(foo,[par(a,integer),par(a,float)],[])],[]]."""
        expect = "Redeclared identifier: par(a,float)"
        self.assertTrue(TestVM.test(input, expect, 420))

