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
        input = """[[const(a,times(1,1))],[],[call(writeInt,[1])]]."""
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
    def test_simple_program4(self):
        input = """[[],[],[call(writeIntLn,[1]),call(writeRealLn,[12.0]),call(writeStrLn,["abc"]),call(writeBool,[true])]]."""
        expect = "1\n12.0\nabc\ntrue"
        self.assertTrue(TestVM.test(input, expect, 421))
    def test_assign0(self):
        input = """[
            [],
            [],
            [assign(a,10)]]."""   
        expect = "Undeclared identifier: assign(a,10)"
        self.assertTrue(TestVM.test(input, expect, 422))
    def test_assign1(self):
        input = """[
            [var(a, integer)],
            [],
            [assign(a, 10), call(writeInt,[1])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 423))
    def test_assign2(self):
        input = """[
            [var(a, integer), var(b, integer)],
            [],
            [assign(a, 10), call(writeInt,[10])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 424))
    def test_assign3(self):
        input = """[
            [const(a, 12),var(b,integer)],
            [],
            [assign(a, 10),call(writeInt,[10])]]."""
        expect = "Cannot assign to a constant: assign(a,10)"
        self.assertTrue(TestVM.test(input, expect, 425))
    def test_assign4(self):
        input = """[
            [var(a,integer),var(b,integer)],
            [],
            [assign(a,10.0)]]."""
        expect = "Type mismatch: assign(a,10.0)"
        self.assertTrue(TestVM.test(input, expect, 426))
    def test_assign5(self):
        input = """[
        [var(a,integer)],
        [],
        [assign(a,10),call(writeInt,[a])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 427))
    def test_vardecl0(self):
        input = """[
        [var(a,integer),const(b,10)],
        [],
        [var(a,integer),assign(a,12),call(writeInt,[a])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 428))
    def test_constdecl4(self):
        input = """[
        [var(a,integer),const(b,10)],
        [],
        [const(a,add(10,2)),call(writeInt,[a])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 429))
    def test_proccall0(self):
        input = """[
        [],
        [proc(foo,[par(a,integer)],[])],
        [call(foo,[10,12]),call(writeInt,[10])]]."""
        expect = "Wrong number of arguments: call(foo,[10,12])"
        self.assertTrue(TestVM.test(input, expect, 430))
    def test_proccall1(self):
        input = """[
        [],
        [],
        [call(foo,[10])]]."""
        expect = "Undeclared procedure: call(foo,[10])"
        self.assertTrue(TestVM.test(input, expect, 431))
    def test_proccall2(self):
        input = """[
        [],
        [proc(foo,[par(a,integer)],[call(writeInt,[10])])],
        [call(foo,[10])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 432))
    def test_proccall3(self):
        input = """[
        [const(b,12)],
        [proc(foo,[par(a,integer)],[call(writeIntLn,[a]),call(writeInt,[b])])],
        [call(foo,[10])]]."""
        expect = "10\n12"
        self.assertTrue(TestVM.test(input, expect, 433))
    def test_proccall4(self):
        input = """[
        [var(a,integer)],
        [proc(foo,[par(b,integer)],[assign(a,b),call(writeIntLn,[a])])],
        [assign(a,10),call(writeIntLn,[a]),call(foo,[20]),call(writeIntLn,[a])]]."""
        expect = "10\n20\n20\n"
        self.assertTrue(TestVM.test(input, expect, 434))
    def test_funccall0(self):
        input = """[
        [],
        [func(foo,[par(a,integer)],integer,[assign(foo,a)])],
        [call(writeInt,[call(foo,[10])])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 435))
    def test_funccall1(self):
        input = """[
        [],
        [],
        [call(writeInt,[call(foo,[10])])]]."""
        expect = "Undeclared function: call(foo,[10])"
        self.assertTrue(TestVM.test(input, expect, 436))
    def test_funccall2(self):
        input = """[
        [],
        [func(foo,[par(a,integer)],integer,[assign(foo,a)])],
        [call(writeInt,[call(foo,[10,12])])]]."""
        expect = "Wrong number of arguments: call(foo,[10,12])"
        self.assertTrue(TestVM.test(input, expect, 437))
    def test_funccall3(self):
        input = """[
        [],
        [func(foo,[par(a,integer)],integer,[assign(a,20),assign(foo,a)])],
        [var(a,integer),assign(a,10),call(writeIntLn,[call(foo,[20])]),call(writeIntLn,[a])]]."""
        expect = "20\n10\n"
        self.assertTrue(TestVM.test(input, expect, 438))
    def test_funccall4(self):
        input = """[
        [],
        [func(foo, [par(a, integer)], integer, [assign(foo, times(a, 2))])
        ,func(goo, [par(a, integer)], integer, [assign(goo, times(a, a))])],
        [call(writeInt, [call(foo, [call(goo, [3])])])]]."""
        expect = "18"
        self.assertTrue(TestVM.test(input, expect, 439))
    def test_funccall5(self):
        input = """[
        [var(b, integer)],
        [func(foo, [], integer, [assign(b, add(b, 1)), assign(foo, b)])
        ,func(goo, [par(a, integer), par(b, integer), par(c, integer)], integer, [assign(goo, add(add(a, b), c))])],
        [assign(b, 0), call(writeIntLn, [call(goo, [call(foo, []), call(foo, []), call(foo, [])])]), call(writeIntLn, [b])]]."""
        expect = "6\n3\n"
        self.assertTrue(TestVM.test(input, expect, 440))
    def test_expression0(self):
        input = """[
        [],
        [],
        [call(writeIntLn, [imod(10, 3)]), call(writeIntLn, [idiv(10,3)])]]."""
        expect = "1\n3\n"
        self.assertTrue(TestVM.test(input, expect, 441))
    def test_expression1(self):
        input = """[
        [var(a, boolean)],
        [],
        [assign(a, bnot(true)), call(writeBooleanLn, [a]), call(writeBooleanLn, [band(a, true)]), call(writeBooleanLn, [bor(false, bnot(a))])]]."""
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestVM.test(input, expect, 442))
    def test_shortcircuit0(self):
        input = """[
        [var(a, integer)],
        [func(foo, [], boolean, [assign(a, add(a, 1)), assign(foo, true)])],
        [assign(a, 0),
        call(writeBooleanLn, [bor(false , call(foo, []))]), call(writeIntLn, [a]),
        call(writeBooleanLn, [bor(true  , call(foo, []))]), call(writeIntLn, [a]),
        call(writeBooleanLn, [band(true , call(foo, []))]), call(writeIntLn, [a]),
        call(writeBooleanLn, [band(false, call(foo, []))]), call(writeIntLn, [a])]]."""
        expect = "true\n1\ntrue\n1\ntrue\n2\nfalse\n2\n"
        self.assertTrue(TestVM.test(input, expect, 443))