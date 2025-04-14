import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {var x int;};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int = 100 ;"""
        expect = str(Program([VarDecl("x",IntType(),IntLiteral(100))]))
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
        input = """const x = 100;"""
        expect = str(
            Program([
                ConstDecl("x",VoidType(),IntLiteral(100))
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

    def test_001(self):
        input = """const abc = foo(12); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[IntLiteral(12)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_002(self):
        input = """const abc = foo(2.0,nil,true,false,\"random string\" ); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[FloatLiteral(2.0),NilLiteral(),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\"random string\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_003(self):
        input = """const abc = foo(param); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[Id("param")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_004(self):
        input = """const abc = foo(3.0 * true && foo("str") || arr[1][2] + (-1) % false);"""
        expect = str(
            Program([ConstDecl("abc",None,FuncCall("foo",[BinaryOp("||",BinaryOp("&&",BinaryOp("*",FloatLiteral(3.0),BooleanLiteral(True)),FuncCall("foo",[StringLiteral("\"str\"")])),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("%",UnaryOp("-",IntLiteral(1)),BooleanLiteral(False))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_005(self):
        input = """const def = foo( a < b == c ); """
        expect = Program([ConstDecl("def",None,FuncCall("foo",[BinaryOp("==", BinaryOp("<", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))

    def test_006(self):
        input = """const ijk = function(a[2].b) + 10; """
        expect = Program([ConstDecl("ijk",None,BinaryOp("+",FuncCall("function",[FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b")]),IntLiteral(10)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))

    def test_007(self):
        input = """var variable int = foo(a.b()); """
        expect = Program([VarDecl("variable",IntType(),FuncCall("foo",[MethCall(Id("a"),"b",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 314))

    def test_008(self):
        input = """const phuchoang = goo(foo.a.b.c); """
        expect = Program([ConstDecl("phuchoang",None,FuncCall("goo",[FieldAccess(FieldAccess(FieldAccess(Id("foo"),"a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))

    def test_009(self):
        input = """var LePhucHoang float = f(a * (b+2)); """
        expect = Program([VarDecl("LePhucHoang",FloatType(),FuncCall("f",[BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))

    def test_010(self):
        input = """const PhucHoang = foo(PhucHoang{b: "string"},PhucHoang{a: 1}); """
        expect = Program([ConstDecl("PhucHoang",None,FuncCall("foo",[StructLiteral("PhucHoang",[("b",StringLiteral("\"string\""))]),StructLiteral("PhucHoang",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))
    
    def test_011(self):
        input = """
            var xyz = ID{field: [10]float{1.0}};
"""
        expect = Program([VarDecl("xyz",None,StructLiteral("ID",[("field",ArrayLiteral([IntLiteral(10)],FloatType(),[FloatLiteral(1.0)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))

    def test_012(self):
        input = """
            func foo() int {
                a.b.c[13] := 3.0;
                return 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(13)]),FloatLiteral(3.0)),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))

    def test_013(self):
        input = """
    type calculator struct {
        x int;
        y [10]button;
        z float;
    }
"""
        expect = Program([StructType("calculator",[("x",IntType()),("y",ArrayType([IntLiteral(10)],Id("button"))),("z",FloatType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))

    def test_014(self):
        input = """
        func foo () {
            for var abc int = 1; abc < 10; abc += 2 {break;}
            for xyz += 1; xyz < 10; xyz -= 1 {return 10;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("abc",IntType(),IntLiteral(1)),BinaryOp("<", Id("abc"), IntLiteral(10)),Assign(Id("abc"),BinaryOp("+", Id("abc"), IntLiteral(2))),Block([Break()])),
            ForStep(Assign(Id("xyz"),BinaryOp("+", Id("xyz"), IntLiteral(1))),BinaryOp("<", Id("xyz"), IntLiteral(10)),Assign(Id("xyz"),BinaryOp("-", Id("xyz"), IntLiteral(1))),Block([Return(IntLiteral(10))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))

    def test_015(self):
        input = """
        func foo () {
            for idx, arr := range [10]int{1,2} {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("idx"),Id("arr"),ArrayLiteral([IntLiteral(10)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))

    def test_016(self):
        input = """
        func foo () string {
            if (condition) {return 100 + 1.2;}
            if (false) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],StringType(),Block([
            If(Id("condition"),Block([Return(BinaryOp("+",IntLiteral(100),FloatLiteral(1.2)))]), None),
            If(BooleanLiteral(False),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))

    def test_017(self):
        input = """
        func foo () {
            if (true) {
                return;
            } else if (false) {
                return;
            } else if (true) {
                return;
            } else {
                return;
            }
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(BooleanLiteral(True), Block([Return(None)]), 
                If(BooleanLiteral(False), Block([Return(None)]), 
                    If(BooleanLiteral(True), Block([Return(None)]), Block([Return(None)]))))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))

    def test_018(self):
        input = """
            type PhucHoang interface {
                Add() ;
                Sub(a, b int) float;
            }
"""
        expect = Program([InterfaceType("PhucHoang",[Prototype("Add",[],VoidType()), Prototype("Sub",[IntType(),IntType()],FloatType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))

    def test_019(self):
        """Simple program: int main() {} """
        input = """func main() {var x int;};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_020(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_021(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_022(self):
        """Constant declaration"""
        input = """const x = 100;"""
        expect = str(
            Program([
                ConstDecl("x",IntType(),IntLiteral(100))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_023(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_024(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_025(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_026(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_027(self):
        input = """const abc = foo(12); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[IntLiteral(12)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_028(self):
        input = """const abc = foo(2.0,nil,true,false,\"random string\" ); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[FloatLiteral(2.0),NilLiteral(),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\"random string\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_029(self):
        input = """const abc = foo(param); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[Id("param")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_030(self):
        input = """const abc = foo(3.0 * true && foo("str") || arr[1][2] + (-1) % false);"""
        expect = str(
            Program([ConstDecl("abc",None,FuncCall("foo",[BinaryOp("||",BinaryOp("&&",BinaryOp("*",FloatLiteral(3.0),BooleanLiteral(True)),FuncCall("foo",[StringLiteral("\"str\"")])),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("%",UnaryOp("-",IntLiteral(1)),BooleanLiteral(False))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_031(self):
        input = """const def = foo( a < b == c ); """
        expect = Program([ConstDecl("def",None,FuncCall("foo",[BinaryOp("==", BinaryOp("<", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))

    def test_032(self):
        input = """const ijk = function(a[2].b) + 10; """
        expect = Program([ConstDecl("ijk",None,BinaryOp("+",FuncCall("function",[FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b")]),IntLiteral(10)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))

    def test_033(self):
        input = """var variable int = foo(a.b()); """
        expect = Program([VarDecl("variable",IntType(),FuncCall("foo",[MethCall(Id("a"),"b",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))

    def test_034(self):
        input = """const phuchoang = goo(foo.a.b.c); """
        expect = Program([ConstDecl("phuchoang",None,FuncCall("goo",[FieldAccess(FieldAccess(FieldAccess(Id("foo"),"a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))

    def test_035(self):
        input = """var LePhucHoang float = f(a * (b+2)); """
        expect = Program([VarDecl("LePhucHoang",FloatType(),FuncCall("f",[BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))

    def test_036(self):
        input = """const PhucHoang = foo(PhucHoang{b: "string"},PhucHoang{a: 1}); """
        expect = Program([ConstDecl("PhucHoang",None,FuncCall("foo",[StructLiteral("PhucHoang",[("b",StringLiteral("\"string\""))]),StructLiteral("PhucHoang",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))
    
    def test_037(self):
        input = """
            var xyz = ID{field: [10]float{1.0}};
"""
        expect = Program([VarDecl("xyz",None,StructLiteral("ID",[("field",ArrayLiteral([IntLiteral(10)],FloatType(),[FloatLiteral(1.0)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))

    def test_038(self):
        input = """
            func foo() int {
                a.b.c[13] := 3.0;
                return 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(13)]),FloatLiteral(3.0)),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))

    def test_039(self):
        input = """
    type calculator struct {
        x int;
        y [10]button;
        z float;
    }
"""
        expect = Program([StructType("calculator",[("x",IntType()),("y",ArrayType([IntLiteral(10)],Id("button"))),("z",FloatType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))

    def test_040(self):
        input = """
        func foo () {
            for var abc int = 1; abc < 10; abc += 2 {break;}
            for xyz += 1; xyz < 10; xyz -= 1 {return 10;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("abc",IntType(),IntLiteral(1)),BinaryOp("<", Id("abc"), IntLiteral(10)),Assign(Id("abc"),BinaryOp("+", Id("abc"), IntLiteral(2))),Block([Break()])),
            ForStep(Assign(Id("xyz"),BinaryOp("+", Id("xyz"), IntLiteral(1))),BinaryOp("<", Id("xyz"), IntLiteral(10)),Assign(Id("xyz"),BinaryOp("-", Id("xyz"), IntLiteral(1))),Block([Return(IntLiteral(10))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))

    def test_041(self):
        input = """
        func foo () {
            for idx, arr := range [10]int{1,2} {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("idx"),Id("arr"),ArrayLiteral([IntLiteral(10)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348))

    def test_042(self):
        input = """
        func foo () string {
            if (condition) {return 100 + 1.2;}
            if (false) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],StringType(),Block([
            If(Id("condition"),Block([Return(BinaryOp("+",IntLiteral(100),FloatLiteral(1.2)))]), None),
            If(BooleanLiteral(False),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))

    def test_043(self):
        input = """
        func foo () {
            if (true) {
                return;
            } else if (false) {
                return;
            } else if (true) {
                return;
            } else {
                return;
            }
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(BooleanLiteral(True), Block([Return(None)]), 
                If(BooleanLiteral(False), Block([Return(None)]), 
                    If(BooleanLiteral(True), Block([Return(None)]), Block([Return(None)]))))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350))

    def test_044(self):
        input = """
            type PhucHoang interface {
                Add() ;
                Sub(a, b int) float;
            }
"""
        expect = Program([InterfaceType("PhucHoang",[Prototype("Add",[],VoidType()), Prototype("Sub",[IntType(),IntType()],FloatType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351))

    def test_045(self):
        """Simple program: int main() {} """
        input = """func main() {var x int;};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_046(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_047(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_048(self):
        """Constant declaration"""
        input = """const x = 100;"""
        expect = str(
            Program([
                ConstDecl("x",IntType(),IntLiteral(100))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_049(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_050(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_051(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_052(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_053(self):
        input = """const abc = foo(12); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[IntLiteral(12)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_054(self):
        input = """const abc = foo(2.0,nil,true,false,\"random string\" ); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[FloatLiteral(2.0),NilLiteral(),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\"random string\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_055(self):
        input = """const abc = foo(param); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[Id("param")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_056(self):
        input = """const abc = foo(3.0 * true && foo("str") || arr[1][2] + (-1) % false);"""
        expect = str(
            Program([ConstDecl("abc",None,FuncCall("foo",[BinaryOp("||",BinaryOp("&&",BinaryOp("*",FloatLiteral(3.0),BooleanLiteral(True)),FuncCall("foo",[StringLiteral("\"str\"")])),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("%",UnaryOp("-",IntLiteral(1)),BooleanLiteral(False))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_057(self):
        input = """const def = foo( a < b == c ); """
        expect = Program([ConstDecl("def",None,FuncCall("foo",[BinaryOp("==", BinaryOp("<", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 364))

    def test_058(self):
        input = """const ijk = function(a[2].b) + 10; """
        expect = Program([ConstDecl("ijk",None,BinaryOp("+",FuncCall("function",[FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b")]),IntLiteral(10)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))

    def test_059(self):
        input = """var variable int = foo(a.b()); """
        expect = Program([VarDecl("variable",IntType(),FuncCall("foo",[MethCall(Id("a"),"b",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))

    def test_060(self):
        input = """const phuchoang = goo(foo.a.b.c); """
        expect = Program([ConstDecl("phuchoang",None,FuncCall("goo",[FieldAccess(FieldAccess(FieldAccess(Id("foo"),"a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))

    def test_061(self):
        input = """var LePhucHoang float = f(a * (b+2)); """
        expect = Program([VarDecl("LePhucHoang",FloatType(),FuncCall("f",[BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 368))

    def test_062(self):
        input = """const PhucHoang = foo(PhucHoang{b: "string"},PhucHoang{a: 1}); """
        expect = Program([ConstDecl("PhucHoang",None,FuncCall("foo",[StructLiteral("PhucHoang",[("b",StringLiteral("\"string\""))]),StructLiteral("PhucHoang",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 369))
    
    def test_063(self):
        input = """
            var xyz = ID{field: [10]float{1.0}};
"""
        expect = Program([VarDecl("xyz",None,StructLiteral("ID",[("field",ArrayLiteral([IntLiteral(10)],FloatType(),[FloatLiteral(1.0)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 370))

    def test_064(self):
        input = """
            func foo() int {
                a.b.c[13] := 3.0;
                return 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(13)]),FloatLiteral(3.0)),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 371))

    def test_065(self):
        input = """
    type calculator struct {
        x int;
        y [10]button;
        z float;
    }
"""
        expect = Program([StructType("calculator",[("x",IntType()),("y",ArrayType([IntLiteral(10)],Id("button"))),("z",FloatType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 372))

    def test_066(self):
        input = """
        func foo () {
            for var abc int = 1; abc < 10; abc += 2 {break;}
            for xyz += 1; xyz < 10; xyz -= 1 {return 10;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("abc",IntType(),IntLiteral(1)),BinaryOp("<", Id("abc"), IntLiteral(10)),Assign(Id("abc"),BinaryOp("+", Id("abc"), IntLiteral(2))),Block([Break()])),
            ForStep(Assign(Id("xyz"),BinaryOp("+", Id("xyz"), IntLiteral(1))),BinaryOp("<", Id("xyz"), IntLiteral(10)),Assign(Id("xyz"),BinaryOp("-", Id("xyz"), IntLiteral(1))),Block([Return(IntLiteral(10))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 373))

    def test_067(self):
        input = """
        func foo () {
            for idx, arr := range [10]int{1,2} {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("idx"),Id("arr"),ArrayLiteral([IntLiteral(10)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 374))

    def test_068(self):
        input = """
        func foo () string {
            if (condition) {return 100 + 1.2;}
            if (false) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],StringType(),Block([
            If(Id("condition"),Block([Return(BinaryOp("+",IntLiteral(100),FloatLiteral(1.2)))]), None),
            If(BooleanLiteral(False),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 375))

    def test_069(self):
        input = """
        func foo () {
            if (true) {
                return;
            } else if (false) {
                return;
            } else if (true) {
                return;
            } else {
                return;
            }
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(BooleanLiteral(True), Block([Return(None)]), 
                If(BooleanLiteral(False), Block([Return(None)]), 
                    If(BooleanLiteral(True), Block([Return(None)]), Block([Return(None)]))))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 376))

    def test_070(self):
        input = """
            type PhucHoang interface {
                Add() ;
                Sub(a, b int) float;
            }
"""
        expect = Program([InterfaceType("PhucHoang",[Prototype("Add",[],VoidType()), Prototype("Sub",[IntType(),IntType()],FloatType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 377))

    def test_071(self):
        """Simple program: int main() {} """
        input = """func main() {var x int;};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_072(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    def test_073(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_074(self):
        """Constant declaration"""
        input = """const x = 100;"""
        expect = str(
            Program([
                ConstDecl("x",IntType(),IntLiteral(100))
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_075(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_076(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    
    def test_077(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    
    def test_078(self):
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
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_079(self):
        input = """const abc = foo(12); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[IntLiteral(12)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_080(self):
        input = """const abc = foo(2.0,nil,true,false,\"random string\" ); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[FloatLiteral(2.0),NilLiteral(),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("\"random string\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_081(self):
        input = """const abc = foo(param); """
        expect = str(Program([ConstDecl("abc",None,FuncCall("foo",[Id("param")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_082(self):
        input = """const abc = foo(3.0 * true && foo("str") || arr[1][2] + (-1) % false);"""
        expect = str(
            Program([ConstDecl("abc",None,FuncCall("foo",[BinaryOp("||",BinaryOp("&&",BinaryOp("*",FloatLiteral(3.0),BooleanLiteral(True)),FuncCall("foo",[StringLiteral("\"str\"")])),BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("%",UnaryOp("-",IntLiteral(1)),BooleanLiteral(False))))]))])
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_083(self):
        input = """const def = foo( a < b == c ); """
        expect = Program([ConstDecl("def",None,FuncCall("foo",[BinaryOp("==", BinaryOp("<", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),390))

    def test_084(self):
        input = """const ijk = function(a[2].b) + 10; """
        expect = Program([ConstDecl("ijk",None,BinaryOp("+",FuncCall("function",[FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b")]),IntLiteral(10)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),391))

    def test_085(self):
        input = """var variable int = foo(a.b()); """
        expect = Program([VarDecl("variable",IntType(),FuncCall("foo",[MethCall(Id("a"),"b",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),392))

    def test_086(self):
        input = """const phuchoang = goo(foo.a.b.c); """
        expect = Program([ConstDecl("phuchoang",None,FuncCall("goo",[FieldAccess(FieldAccess(FieldAccess(Id("foo"),"a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),393))

    def test_087(self):
        input = """var LePhucHoang float = f(a * (b+2)); """
        expect = Program([VarDecl("LePhucHoang",FloatType(),FuncCall("f",[BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),394))

    def test_088(self):
        input = """const PhucHoang = foo(PhucHoang{b: "string"},PhucHoang{a: 1}); """
        expect = Program([ConstDecl("PhucHoang",None,FuncCall("foo",[StructLiteral("PhucHoang",[("b",StringLiteral("\"string\""))]),StructLiteral("PhucHoang",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),395))
    
    def test_089(self):
        input = """
            var xyz = ID{field: [10]float{1.0}};
"""
        expect = Program([VarDecl("xyz",None,StructLiteral("ID",[("field",ArrayLiteral([IntLiteral(10)],FloatType(),[FloatLiteral(1.0)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),396))

    def test_090(self):
        input = """
            func foo() int {
                a.b.c[13] := 3.0;
                return 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(13)]),FloatLiteral(3.0)),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),397))

    def test_091(self):
        input = """
    type calculator struct {
        x int;
        y [10]button;
        z float;
    }
"""
        expect = Program([StructType("calculator",[("x",IntType()),("y",ArrayType([IntLiteral(10)],Id("button"))),("z",FloatType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),398))

    def test_092(self):
        input = """
        func foo () {
            for var abc int = 1; abc < 10; abc += 2 {break;}
            for xyz += 1; xyz < 10; xyz -= 1 {return 10;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("abc",IntType(),IntLiteral(1)),BinaryOp("<", Id("abc"), IntLiteral(10)),Assign(Id("abc"),BinaryOp("+", Id("abc"), IntLiteral(2))),Block([Break()])),
            ForStep(Assign(Id("xyz"),BinaryOp("+", Id("xyz"), IntLiteral(1))),BinaryOp("<", Id("xyz"), IntLiteral(10)),Assign(Id("xyz"),BinaryOp("-", Id("xyz"), IntLiteral(1))),Block([Return(IntLiteral(10))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),399))

    def test_093(self):
        input = """
        func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                main(b.A.a, b.c, -100);
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func main(a int, b float, d int) {
            var a float;
            var c string;
            var A InterfaceA = StructA{a: 10, b: true};
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            x := a + 10;
            var y float = d * 10;
            
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10) {
                return a.b;
            }
            else if (a.a > 5) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("idx"),Id("arr"),ArrayLiteral([IntLiteral(10)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),400))