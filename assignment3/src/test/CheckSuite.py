import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_no_error(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
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
    def test0(self):
        input = """func foo(a int) {

      foo(1);

      var foo = 1;

      foo(2); // error

 }"""
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test1(self):
        input = """const x = 5;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))
    def test2(self):
        input = """const x = 4;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = "Type Mismatch: VarDecl(y,ArrayType(IntType,[BinaryOp(Id(x),+,IntLiteral(3))]),ArrayLiteral([IntLiteral(8)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test3(self):
        input = """const x = 4;
        var y [5][2][3]int = [x+1][x-2][2*x-5]int{{1,2},{2,3}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))
    def test4(self):
        input = """const x = 4;
        const y = x + 2;
        var z [10][2][3]string = [x+1][x-2][2*x-5]string{{"a","b"},{"c","d"}}"""
        expect = """Type Mismatch: VarDecl(z,ArrayType(StringType,[IntLiteral(10),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([BinaryOp(Id(x),+,IntLiteral(1)),BinaryOp(Id(x),-,IntLiteral(2)),BinaryOp(BinaryOp(IntLiteral(2),*,Id(x)),-,IntLiteral(5))],StringType,[[StringLiteral("a"),StringLiteral("b")],[StringLiteral("c"),StringLiteral("d")]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,408))
    def test5(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a + 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a)) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: BinaryOp(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(10)),||,BinaryOp(StringLiteral("abc"),>,StringLiteral("cd")))
"""
        self.assertTrue(TestChecker.test(input,expect,409))
    def test6(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a < 10 || "abc" > "cd") {
                return a.b;
            }
            else if (12) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: If(IntLiteral(12),Block([Return(BinaryOp(IntLiteral(10),==,IntLiteral(5)))]),Block([Return(BinaryOp(FieldAccess(Id(a),a),>,IntLiteral(0)))]))
"""
        self.assertTrue(TestChecker.test(input,expect,410))
    def test7(self):
        input = """func (a StructA) Add (a int, b int) int {
            return a + b
        }
        """
        expect = """Undeclared Identifier: StructA
"""
        self.assertTrue(TestChecker.test(input,expect,411))
    def test8(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a + 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Type Mismatch: Return(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(0)))
"""
        self.assertTrue(TestChecker.test(input,expect,412))
    def test9(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Sub(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Undeclared Method: Sub\n"""
        self.assertTrue(TestChecker.test(input,expect,413))
    def test10(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return a + b
        }
        """
        expect = """Type Mismatch: Return(BinaryOp(Id(a),+,Id(b)))\n"""
        self.assertTrue(TestChecker.test(input,expect,414))
    def test11(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
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
        """
        expect = """Undeclared Identifier: StructB\n"""
        self.assertTrue(TestChecker.test(input,expect,415))
    def test12(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(10, 10 * b.c));
            d.A.Sub(d, b);
            x := 10 + b.a;
        }
        type StructB struct {
            A StructA;
            c float;
        }
        """
        expect = """Undeclared Field: c\n"""
        self.assertTrue(TestChecker.test(input,expect,416))
    def test13(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
            a.Add(1, 2);
        }
        """
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])\n"""
        self.assertTrue(TestChecker.test(input,expect,417))
    def test14(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return
            var a int;
            a += a.Add(1, 2);
        }
"""
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])
"""
        self.assertTrue(TestChecker.test(input,expect,418))
    def test15(self):
        input = """
        var x int
        func x() {
            return
        }"""
        expect = """Redeclared Function: x\n"""
        self.assertTrue(TestChecker.test(input,expect,419))
    def test16(self):
        input = """
        func f1() int {
            return 10
        }
        func main() {
            f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,420))
    def test17(self):
        input = """
        func f1() {
            return
        }
        func main() {
            var x int = 10
            x += 1 + f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])
"""
        self.assertTrue(TestChecker.test(input,expect,421))
    def test18(self):
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
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA, d int) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: d
"""
        self.assertTrue(TestChecker.test(input,expect,422))
    def test19(self):
        input = """
func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                main(b.A.a, b.c, -100, StructB{A: StructA{a: 10, b: true}, c: 1.0});
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func main(a int, b float, d int, b StructB) {
            var a float;
            var c string;
            var A InterfaceA = StructA{a: 10, b: true};
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: b\n"""
        self.assertTrue(TestChecker.test(input,expect,423))
    def test20(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
            Div(a float, b float)
        }
        """
        expect = """Type Mismatch: VarDecl(A,Id(InterfaceA),StructLiteral(StructA,[(a,IntLiteral(10)),(b,BooleanLiteral(true))]))
"""
        self.assertTrue(TestChecker.test(input,expect,424))
    def test21(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
            x := a + b.a + b.efg;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Field: efg\n"""
        self.assertTrue(TestChecker.test(input,expect,425))
    def test22(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            value()
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        
        """
        expect = """Undeclared Function: value
"""
        self.assertTrue(TestChecker.test(input,expect,426))
    def test23(self):
        input = """
        func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                return
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            c.Sub(d, b.Div(a, b));
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        type StructA struct {
            a int;
            b boolean;
        }
        """
        expect = """Undeclared Method: Div
"""
        self.assertTrue(TestChecker.test(input,expect,427))
    def test24(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            return
                        }
                        return
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Identifier: value
"""
        self.assertTrue(TestChecker.test(input,expect,428))
    def test25(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for d {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: For(Id(d),Block([Assign(Id(a),BinaryOp(Id(a),&&,FuncCall(func0,[FieldAccess(Id(B),A)])))]))
"""
        self.assertTrue(TestChecker.test(input,expect,429))
    def test26(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range "asdasd" {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: ForEach(Id(idx),Id(value),StringLiteral("asdasd"),Block([Break()]))
"""
        self.assertTrue(TestChecker.test(input,expect,430))
    def test27(self):
        input = """
        func getArray() [12]int {
            return [12]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))
    def test28(self):
        input = """
        func getArray() [12]int {
            return [11]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = """Type Mismatch: Return(ArrayLiteral([IntLiteral(11)],IntType,[IntLiteral(0),IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10),IntLiteral(11)]))
"""
        self.assertTrue(TestChecker.test(input,expect,432))
    def test29(self):
        input = """type InterfaceA interface {
            Add(a int, b int) int
            Add(b StructB, c StructA)
        }"""
        expect = """Redeclared Prototype: Add
"""
        self.assertTrue(TestChecker.test(input,expect,433))
    def test30(self):
        input = """
        func main(){
            for i := 0; i < 10; i += 2 {
                putLn()
            }
        }
        """
        expect = """Undeclared Identifier: i
"""
        self.assertTrue(TestChecker.test(input,expect,434))
    def test31(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test32(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test33(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test34(self):
        input = """func foo(a int) {

      foo(1);

      var foo = 1;

      foo(2); // error

 }"""
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test35(self):
        input = """const x = 5;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
    def test36(self):
        input = """const x = 4;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = "Type Mismatch: VarDecl(y,ArrayType(IntType,[BinaryOp(Id(x),+,IntLiteral(3))]),ArrayLiteral([IntLiteral(8)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test37(self):
        input = """const x = 4;
        var y [5][2][3]int = [x+1][x-2][2*x-5]int{{1,2},{2,3}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))
    def test38(self):
        input = """const x = 4;
        const y = x + 2;
        var z [10][2][3]string = [x+1][x-2][2*x-5]string{{"a","b"},{"c","d"}}"""
        expect = """Type Mismatch: VarDecl(z,ArrayType(StringType,[IntLiteral(10),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([BinaryOp(Id(x),+,IntLiteral(1)),BinaryOp(Id(x),-,IntLiteral(2)),BinaryOp(BinaryOp(IntLiteral(2),*,Id(x)),-,IntLiteral(5))],StringType,[[StringLiteral("a"),StringLiteral("b")],[StringLiteral("c"),StringLiteral("d")]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,442))
    def test39(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a + 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a)) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: BinaryOp(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(10)),||,BinaryOp(StringLiteral("abc"),>,StringLiteral("cd")))
"""
        self.assertTrue(TestChecker.test(input,expect,443))
    def test40(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a < 10 || "abc" > "cd") {
                return a.b;
            }
            else if (12) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: If(IntLiteral(12),Block([Return(BinaryOp(IntLiteral(10),==,IntLiteral(5)))]),Block([Return(BinaryOp(FieldAccess(Id(a),a),>,IntLiteral(0)))]))
"""
        self.assertTrue(TestChecker.test(input,expect,444))
    def test41(self):
        input = """func (a StructA) Add (a int, b int) int {
            return a + b
        }
        """
        expect = """Undeclared Identifier: StructA
"""
        self.assertTrue(TestChecker.test(input,expect,445))
    def test42(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a + 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Type Mismatch: Return(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(0)))
"""
        self.assertTrue(TestChecker.test(input,expect,446))
    def test43(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Sub(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Undeclared Method: Sub\n"""
        self.assertTrue(TestChecker.test(input,expect,447))
    def test44(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return a + b
        }
        """
        expect = """Type Mismatch: Return(BinaryOp(Id(a),+,Id(b)))\n"""
        self.assertTrue(TestChecker.test(input,expect,448))
    def test45(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
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
        """
        expect = """Undeclared Identifier: StructB\n"""
        self.assertTrue(TestChecker.test(input,expect,449))
    def test46(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(10, 10 * b.c));
            d.A.Sub(d, b);
            x := 10 + b.a;
        }
        type StructB struct {
            A StructA;
            c float;
        }
        """
        expect = """Undeclared Field: c\n"""
        self.assertTrue(TestChecker.test(input,expect,450))
    def test47(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
            a.Add(1, 2);
        }
        """
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])\n"""
        self.assertTrue(TestChecker.test(input,expect,451))
    def test48(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return
            var a int;
            a += a.Add(1, 2);
        }
"""
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])
"""
        self.assertTrue(TestChecker.test(input,expect,452))
    def test49(self):
        input = """
        var x int
        func x() {
            return
        }"""
        expect = """Redeclared Function: x\n"""
        self.assertTrue(TestChecker.test(input,expect,453))
    def test50(self):
        input = """
        func f1() int {
            return 10
        }
        func main() {
            f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,454))
    def test51(self):
        input = """
        func f1() {
            return
        }
        func main() {
            var x int = 10
            x += 1 + f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])
"""
        self.assertTrue(TestChecker.test(input,expect,455))
    def test52(self):
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
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA, d int) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: d
"""
        self.assertTrue(TestChecker.test(input,expect,456))
    def test53(self):
        input = """
func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                main(b.A.a, b.c, -100, StructB{A: StructA{a: 10, b: true}, c: 1.0});
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func main(a int, b float, d int, b StructB) {
            var a float;
            var c string;
            var A InterfaceA = StructA{a: 10, b: true};
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: b\n"""
        self.assertTrue(TestChecker.test(input,expect,457))
    def test54(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
            Div(a float, b float)
        }
        """
        expect = """Type Mismatch: VarDecl(A,Id(InterfaceA),StructLiteral(StructA,[(a,IntLiteral(10)),(b,BooleanLiteral(true))]))
"""
        self.assertTrue(TestChecker.test(input,expect,458))
    def test55(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
            x := a + b.a + b.efg;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Field: efg\n"""
        self.assertTrue(TestChecker.test(input,expect,459))
    def test56(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            value()
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        
        """
        expect = """Undeclared Function: value
"""
        self.assertTrue(TestChecker.test(input,expect,460))
    def test57(self):
        input = """
        func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                return
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            c.Sub(d, b.Div(a, b));
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        type StructA struct {
            a int;
            b boolean;
        }
        """
        expect = """Undeclared Method: Div
"""
        self.assertTrue(TestChecker.test(input,expect,461))
    def test58(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            return
                        }
                        return
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Identifier: value
"""
        self.assertTrue(TestChecker.test(input,expect,462))
    def test59(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for d {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: For(Id(d),Block([Assign(Id(a),BinaryOp(Id(a),&&,FuncCall(func0,[FieldAccess(Id(B),A)])))]))
"""
        self.assertTrue(TestChecker.test(input,expect,463))
    def test60(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range "asdasd" {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: ForEach(Id(idx),Id(value),StringLiteral("asdasd"),Block([Break()]))
"""
        self.assertTrue(TestChecker.test(input,expect,464))
    def test61(self):
        input = """
        func getArray() [12]int {
            return [12]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))
    def test62(self):
        input = """
        func getArray() [12]int {
            return [11]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = """Type Mismatch: Return(ArrayLiteral([IntLiteral(11)],IntType,[IntLiteral(0),IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10),IntLiteral(11)]))
"""
        self.assertTrue(TestChecker.test(input,expect,466))
    def test63(self):
        input = """type InterfaceA interface {
            Add(a int, b int) int
            Add(b StructB, c StructA)
        }"""
        expect = """Redeclared Prototype: Add
"""
        self.assertTrue(TestChecker.test(input,expect,467))
    def test64(self):
        input = """
        func main(){
            for i := 0; i < 10; i += 2 {
                putLn()
            }
        }
        """
        expect = """Undeclared Identifier: i
"""
        self.assertTrue(TestChecker.test(input,expect,468))
    def test65(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test66(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test67(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test68(self):
        input = """func foo(a int) {

      foo(1);

      var foo = 1;

      foo(2); // error

 }"""
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test69(self):
        input = """const x = 5;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))
    def test70(self):
        input = """const x = 4;
        var y [x+3]int = [8]int{1,2,3}"""
        expect = "Type Mismatch: VarDecl(y,ArrayType(IntType,[BinaryOp(Id(x),+,IntLiteral(3))]),ArrayLiteral([IntLiteral(8)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test71(self):
        input = """const x = 4;
        var y [5][2][3]int = [x+1][x-2][2*x-5]int{{1,2},{2,3}}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))
    def test72(self):
        input = """const x = 4;
        const y = x + 2;
        var z [10][2][3]string = [x+1][x-2][2*x-5]string{{"a","b"},{"c","d"}}"""
        expect = """Type Mismatch: VarDecl(z,ArrayType(StringType,[IntLiteral(10),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([BinaryOp(Id(x),+,IntLiteral(1)),BinaryOp(Id(x),-,IntLiteral(2)),BinaryOp(BinaryOp(IntLiteral(2),*,Id(x)),-,IntLiteral(5))],StringType,[[StringLiteral("a"),StringLiteral("b")],[StringLiteral("c"),StringLiteral("d")]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,476))
    def test73(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a + 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a)) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: BinaryOp(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(10)),||,BinaryOp(StringLiteral("abc"),>,StringLiteral("cd")))
"""
        self.assertTrue(TestChecker.test(input,expect,477))
    def test74(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a < 10 || "abc" > "cd") {
                return a.b;
            }
            else if (12) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        """
        expect = """Type Mismatch: If(IntLiteral(12),Block([Return(BinaryOp(IntLiteral(10),==,IntLiteral(5)))]),Block([Return(BinaryOp(FieldAccess(Id(a),a),>,IntLiteral(0)))]))
"""
        self.assertTrue(TestChecker.test(input,expect,478))
    def test75(self):
        input = """func (a StructA) Add (a int, b int) int {
            return a + b
        }
        """
        expect = """Undeclared Identifier: StructA
"""
        self.assertTrue(TestChecker.test(input,expect,479))
    def test76(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a + 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Type Mismatch: Return(BinaryOp(FieldAccess(Id(a),a),+,IntLiteral(0)))
"""
        self.assertTrue(TestChecker.test(input,expect,480))
    def test77(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Sub(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return a + b
        }"""
        expect = """Undeclared Method: Sub\n"""
        self.assertTrue(TestChecker.test(input,expect,481))
    def test78(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return a + b
        }
        """
        expect = """Type Mismatch: Return(BinaryOp(Id(a),+,Id(b)))\n"""
        self.assertTrue(TestChecker.test(input,expect,482))
    def test79(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
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
        """
        expect = """Undeclared Identifier: StructB\n"""
        self.assertTrue(TestChecker.test(input,expect,483))
    def test80(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(10, 10 * b.c));
            d.A.Sub(d, b);
            x := 10 + b.a;
        }
        type StructB struct {
            A StructA;
            c float;
        }
        """
        expect = """Undeclared Field: c\n"""
        self.assertTrue(TestChecker.test(input,expect,484))
    def test81(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
            a.Add(1, 2);
        }
        """
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])\n"""
        self.assertTrue(TestChecker.test(input,expect,485))
    def test82(self):
        input = """
        type StructA struct {
            a int;
            b boolean;
        }
        func (a StructA) Add(a int, b int) {
            return
            var a int;
            a += a.Add(1, 2);
        }
"""
        expect = """Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])
"""
        self.assertTrue(TestChecker.test(input,expect,486))
    def test83(self):
        input = """
        var x int
        func x() {
            return
        }"""
        expect = """Redeclared Function: x\n"""
        self.assertTrue(TestChecker.test(input,expect,487))
    def test84(self):
        input = """
        func f1() int {
            return 10
        }
        func main() {
            f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test85(self):
        input = """
        func f1() {
            return
        }
        func main() {
            var x int = 10
            x += 1 + f1();
        }"""
        expect = """Type Mismatch: FuncCall(f1,[])
"""
        self.assertTrue(TestChecker.test(input,expect,489))
    def test86(self):
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
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
                return 10 == 5;
            }
            else {
                return a.a > 0;
            }
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA, d int) {
            c.Sub(d, b);
            b.Sub(d, c);
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: d
"""
        self.assertTrue(TestChecker.test(input,expect,490))
    def test87(self):
        input = """
func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                main(b.A.a, b.c, -100, StructB{A: StructA{a: 10, b: true}, c: 1.0});
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func main(a int, b float, d int, b StructB) {
            var a float;
            var c string;
            var A InterfaceA = StructA{a: 10, b: true};
            const B StructB = StructB{A: StructA{a: 10, b: true}, c: 1.0};
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Redeclared Parameter: b\n"""
        self.assertTrue(TestChecker.test(input,expect,491))
    def test88(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
            Div(a float, b float)
        }
        """
        expect = """Type Mismatch: VarDecl(A,Id(InterfaceA),StructLiteral(StructA,[(a,IntLiteral(10)),(b,BooleanLiteral(true))]))
"""
        self.assertTrue(TestChecker.test(input,expect,492))
    def test89(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
            x := a + b.a + b.efg;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Field: efg\n"""
        self.assertTrue(TestChecker.test(input,expect,493))
    def test90(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            value()
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        
        """
        expect = """Undeclared Function: value
"""
        self.assertTrue(TestChecker.test(input,expect,494))
    def test91(self):
        input = """
        func (b StructB) a (d int, e int) {
            putInt(b.A.a);
            putInt(d + e);
            if (b.A.b) {
                return
            }
            return
        }
        var a int; 
        const b float = 1.0;
        type StructB struct {
            A StructA;
            c float;
        }
        func (a StructA) Add(a int, b int) int {
            return 10
        }
        func (b StructA) Sub (d StructB, c StructA) {
            c.Sub(d, b);
            b.Sub(d, c);
            c.Sub(d, b.Div(a, b));
            return
            putInt(d.A.Add(a, 10 * b.a));
            d.A.Sub(d, b);
            x := a + b.a;
        }
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        type StructA struct {
            a int;
            b boolean;
        }
        """
        expect = """Undeclared Method: Div
"""
        self.assertTrue(TestChecker.test(input,expect,495))
    def test92(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            return
                        }
                        return
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Undeclared Identifier: value
"""
        self.assertTrue(TestChecker.test(input,expect,496))
    def test93(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for d {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range [10]float {1.0, 1.0 + 2, -2.3} {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: For(Id(d),Block([Assign(Id(a),BinaryOp(Id(a),&&,FuncCall(func0,[FieldAccess(Id(B),A)])))]))
"""
        self.assertTrue(TestChecker.test(input,expect,497))
    def test94(self):
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
            x := a + A.a;
            var y float = d * 10;
            const d = 10;
            var C = [d]StructA {StructA{a: 10, b: true}, StructA{a: 10, b: true}};
            z := C[0].Add(10, 10) + C[1].Add(10, 20 * 3 % 3) / 3.0;
            C[1 + 3].Sub(B, A);
            if (A.Add(10, 10) == 20) {
                if (true) {
                    var a = true || false;
                    for func0(B.A) {
                        a := a && func0(B.A);
                    }
                } else if (!func0(StructA{})) {
                    idx := 0;
                    var value StructA;
                    for idx, value := range C {
                        putInt(idx);
                        putInt(value.Add(1, 2));
                        var value float = 10.0
                        for idx, value := range "asdasd" {
                            break;
                        }
                    }
                    var B StructB = StructB{A: value, c: 0.0};
                } else {
                    i := 0
                    for i := 0; i < 10; i += 2 {
                        x := C[i].Add(1, 2) + 3
                        var y float = 1 + 2
                    }
                    return
                }
            } else {
                var a string = "" + C[9].Mul(10);
                break;
                continue;
                return;
            }
            return
        }
        type StructA struct {
            a int;
            b boolean;
        }
        func func0(a StructA) boolean {
            if (a.a > 10 || "abc" > "cd") {
                return a.b;
            }
            else if (!func0(a) && a.Add(1, 3) == 4) {
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
        func (a StructA) Mul (a int) string {
            var a string = "abc";
            return a + "asdas";
        }
        type InterfaceA interface {
            Add(a int, b int) int
            Sub(b StructB, c StructA)
        }
        """
        expect = """Type Mismatch: ForEach(Id(idx),Id(value),StringLiteral("asdasd"),Block([Break()]))
"""
        self.assertTrue(TestChecker.test(input,expect,498))
    def test95(self):
        input = """
        func getArray() [12]int {
            return [12]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))
    def test96(self):
        input = """
        func getArray() [12]int {
            return [11]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
        }
        func main() {
            var idx int
            var value = 0
            for idx, value := range getArray() {
                return
            }
        }
"""     
        expect = """Type Mismatch: Return(ArrayLiteral([IntLiteral(11)],IntType,[IntLiteral(0),IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10),IntLiteral(11)]))
"""
        self.assertTrue(TestChecker.test(input,expect,500))