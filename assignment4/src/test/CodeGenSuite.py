import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
#     def test_int_literal(self):
#         input = """func main() {putInt(5);};"""
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,501))
#     def test_local_var(self):
#         input = """func main() {var a int = 20; putInt(a);};"""
#         expect = "20"
#         self.assertTrue(TestCodeGen.test(input,expect,502))
#     def test_gllobal_var(self):
#         input = """var a int = 10; func main() {putInt(a);};"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,503))
#     def test_int_ast(self):
#         input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
#         expect = "25"
#         self.assertTrue(TestCodeGen.test(input,expect,504))
#     def test_local_var_ast(self):
#         input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
#         expect = "500"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
#     def test_global_var_ast(self):  
#         input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
#         expect = "5000"
#         self.assertTrue(TestCodeGen.test(input,expect,506))
#     def test_var_decl0(self):
#         input = """func main() {var a float = 10;  putFloat(a);};"""
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,507))
#     def test_var_decl1(self):
#         input = """func main() {var a [3]int = [3]int{1,2,3}; putInt(10);};"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,508))
#     def test_var_decl2(self):
#         input = """func main() {var a [2][2]int = [2][2]int{{1,2},{3,4}}; putInt(10);};"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,509))
#     def test_struct_decl0(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func main() {
#     var a = A{b: 2.0, c: "abc", a: 1};
#     putInt(12);
# };"""
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,510))
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
#     def test_struct_decl1(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func main() {
#     var a = A{b: 2.0, c: "abc"};
#     putInt(12);
# };"""
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,512))
#     def test_field_access0(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func main() {
#     var a = A{b: 10.0, c: "abc"};
#     putFloat(a.b);
# };"""
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,513))
#     def test_method_decl0(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func (a A) add(b int) int {
#     return b;
# }
# func main() {
#     var a = A{b: 10.0, c: "abc"};
#     putInt(10);
# };"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,514))
    
#     def test_method_call0(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func (a A) add(b int) int {
#     putFloatLn(a.b);
#     return b;
# }
# func (d A) getC() string {
#     return d.c;
# }
# func main() {
#     var a = A{b: 10.0, c: "abc", a: 1};
#     putIntLn(a.add(10));
#     putString(a.getC());
# };"""
#         expect = """10.0
# 10
# abc"""
#         self.assertTrue(TestCodeGen.test(input,expect,515))
#     def test_method_call1(self):
#         input = """
# type A struct {
#     a int;
#     b float;
#     c string;
# }
# func (a A) print() {
#     putInt(a.a);
#     putString(" ");
#     putFloat(a.b);
#     putString(" ");
#     putString(a.c);
# }
# func main() {
#     var a = A{b: 10.0, c: "abc", a: 1};
#     a.print();
# };"""
#         expect = "1 10.0 abc"
#         self.assertTrue(TestCodeGen.test(input,expect,516))
#     def test_interface_decl0(self):
#         input = """
# type A interface {
#     print();
# }
# type B struct {
#     a int;
# }
# func (b B) print() {
#     putInt(b.a);
# }
# func main() {
#     var abc A = B{a: 1};
#     abc.print();
# };"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,517))
#     def test_interface_decl1(self):
#         input = """
# type A interface {
#     print();
# }
# type B struct {
#     a int;
# }
# func (b B) print() {
#     putInt(b.a);
# }
# type C struct {
#     a int;
# }
# func (c C) print() {
#     putInt(c.a);
# }
# func main() {
#     var abc A = B{a: 1};
#     abc.print();
#     var def A = C{a: 2};
#     def.print();
# };"""
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,518))
#     def test_constant_decl0(self):
#         input = """
# const b float = 10.0
# func main() {
#     const a int = 10;
#     putInt(a);
#     putFloat(b);
# };"""
#         expect = "1010.0"
#         self.assertTrue(TestCodeGen.test(input,expect,519))
#     def test_assignment0(self):
#         input = """
# func main() {
#     var a int;
#     a := 10;
#     putInt(a);
# }"""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,520))
#     def test_assignment1(self):
#         input = """
# func main() {
#     var a [3]int;
#     a := [3]int{1,2,3};
# }"""
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,521))
#     def test_assignment2(self):
#         input = """
# type A struct {
#     a int;
# }
# func main() {
#     var a = A{a: 10};
#     a := A{a: 300};
#     putInt(a.a);
#     a.a := 4;
#     putInt(a.a);
# }"""
#         expect = "3004"
#         self.assertTrue(TestCodeGen.test(input,expect,522))
#     def test_constant_decl1(self):
#         input = """
# type A struct {
#     a int;
# }
# func main() {
#     const a A = A{a: 1975};
#     putInt(a.a);
# }"""
#         expect = "1975"
#         self.assertTrue(TestCodeGen.test(input,expect,523))
#     def test_array_cell0(self):
#         input = """
# func main() {
#     var a [3]int;
#     a := [3]int{30,4,1975};
#     putInt(a[1]);
# }"""
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,524))
#     def test_array_cell1(self):
#         input = """
# func main() {
#     var a [3]int;
#     a := [3]int{30,3,1975};
#     a[1] := 4;
#     putInt(a[0]);
#     putString("/");
#     putInt(a[1]);
#     putString("/");
#     putInt(a[2]);
# }"""
#         expect = "30/4/1975"
#         self.assertTrue(TestCodeGen.test(input,expect,525))
#     def test_array_cell2(self):
#         input = """
# func main() {
#     var a [2][2] int;
#     a := [2][2]int{{2,2},{3,4}};
#     putInt(a[0][0]);
#     a[0][1] := 9;
#     putString("/");
#     putInt(a[0][1]);
# }"""
#         expect = "2/9"
#         self.assertTrue(TestCodeGen.test(input,expect,526))
#     def test_binary_op0(self):
#         input = """
# func main() {
#     putInt(1+2);
# }"""
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,527))
#     def test_binary_op1(self):
#         input = """
# func main() {
#     var a float = 20.04;
#     var b = a + 10;
#     putFloat(b);
# }"""
#         expect = "30.04"
#         self.assertTrue(TestCodeGen.test(input,expect,528))
#     def test_binary_op2(self):
#         input = """
# func main() {
#     var a = 11;
#     b := a * 10.0 / 2 - 32.5;
#     putFloat(b - 10);
# }"""
#         expect = "12.5"
#         self.assertTrue(TestCodeGen.test(input,expect,529))
#     def test_binary_op3(self):
#         input = """
# func printDecimals(a int) {
#     x := a % 10;
#     a := a / 10;
#     y := a % 10;
#     a := a / 10;
#     z := a % 10;
#     a := a / 10;
#     t := a % 10;
#     putInt(t);
#     putInt(z);
#     putInt(y);
#     putInt(x);
# }
# func main() {
#     printDecimals(1975);
# }"""
#         expect = "1975"
#         self.assertTrue(TestCodeGen.test(input,expect,530))
#     def test_binary_op4(self):
#         input = """
# func main() {
#     var x = (15 > 12 || "true" == "false") && 12.3 > 10.0;
#     putBool(x);
# }"""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,531))
#     def test_binary_op5(self):
#         input = """
# func main() {
#     var x  = false || 12 * 10 > 100 && false || 12.0 <= 50 / 4.0 && !false;
#     putBool(x);
# }
# """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,532))

#     def test_unary_op0(self):
#         input = """
# func main() {
#     var x = -10 * (-12.5);
#     putFloat(x);
# }"""
#         expect = "125.0"
#         self.assertTrue(TestCodeGen.test(input,expect,533))
#     def test_unary_op1(self):
#         input = """
# func main() {
#     var x = !(10 > 2 && 3.0 < -(-10.1));
#     putBool(x);
# }"""
#         expect = """false"""
#         self.assertTrue(TestCodeGen.test(input,expect,534))
#     def test_if0(self):
#         input = """
# func main() {
#     if (10 > 2) {
#         putInt(1);
#     } else {
#         putInt(2);
#     }   
# }"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,535))
#     def test_if1(self):
#         input = """
# func main() {
#     var x int;
#     if (10 > 2) {
#         x := 1;
#     }
#     else if (10 > 20) {
#         x := 2;
#     }
#     else {
#         x := 3;
#     }
#     putInt(x);
# }"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,536))
#     def test_if2(self):
#         input = """
# func main() {
#     var x int = 30/4;
#     if (x == 30 && x == 40 || x > 1975) {
#         putInt(x);
#     } else if (x < 5) {
#         putInt(x % 10);
#     }
# }"""
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,537))
#     def test_binary_op6(self):
#         input = """
# func main() {
#     var x = 12 > 5;
# }
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,538))
#     def test_if3(self):
#         input = """
# func main() {
#     if (12 > 5) {
#         putInt(1);
#     } else {
#         putInt(2);
#     }
# }
# """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,539))
#     def test_if4(self):
#         input = """
# func main () {
#     if (2 > 5 || 12 > 5){
#         putInt(1);
#     }
# }"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,540))
#     def test_forbasic0(self):
#         input = """
# func main () {
#     var i = 10;
#     for (i > 0) {
#         putInt(i);
#         i -= 1;
#     }
# }"""
#         expect = "10987654321"
#         self.assertTrue(TestCodeGen.test(input,expect,541))
#     def test_forbasic1(self):
#         input = """
# func main () {
#     var i = 10;
#     for (i > 0) {
#         i -= 1;
#         if (i == 8) {
#             continue;
#         }
#         else if (i == 3) {
#             break;
#         }
#         putInt(i);
#     }
# }"""
#         expect = "97654"
#         self.assertTrue(TestCodeGen.test(input,expect,542))
#     def test_forstep0(self):
#         input = """
# func main () {
#     for i := 0; i < 10; i += 2 {
#         putInt(i);
#     }
# }"""
#         expect = "02468"
#         self.assertTrue(TestCodeGen.test(input,expect,543))
#     def test_forstep1(self):
#         input = """
# func main () {
#     for i := 10; i > 0; i -= 2 {
#         putInt(i);
#     }
# }"""
#         expect = "108642"
#         self.assertTrue(TestCodeGen.test(input,expect,544))
#     def test_array0(self):
#         input = """
# func main() {
#     var x = [2]float{1.0, 2.0};
#     putFloat(x[0]);
# }"""
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input,expect,545))
#     def test_array1(self):
#         input = """
# func main() {
#     var x = [2][2]boolean{{true, false}, {false, true}};
#     putBool(x[0][0]);
# }"""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,546))
#     def test_array2(self):
#         input = """
# type A struct {
#     a int;
# }
# func main() {
#     var x = [2]A{A{a: 1}, A{a: 2}};
#     putInt(x[0].a);
# }"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,547))
#     def test_array3(self):
#         input = """
# func main() {
#     var x = [2][2]int{{1, 2}, {3, 4}};
#     x[0][0] += x[0][1];
#     putInt(x[0][0]);
# }
# """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,548))
#     def test_struct0(self):
#         input = """
# type Node struct {
#     a int;
#     n Node;
# }
# func main () {
#     var x = Node{a: 1, n: Node{a: 2}};
#     putInt(x.n.a);
# }
# """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,549))
#     def test_struct1(self):
#         input = """
# type Node struct {
#     a int;
#     n Node;
# }
# func main () {
#     var x = Node{a: 1, n: Node{a: 2, n: Node{a: 3, n: Node{a: 4}}}};
#     putInt(x.n.n.n.a);
# }
# """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,550))
#     def test_struct2(self):
#         input = """
# type Node struct {
#     a [2]int;
# }
# func main () {
#     var x = Node{a: [2]int{1, 2}};
#     putInt(x.a[1]);
# }
# """ 
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,551))
#     def test_array4(self):
#         input = """
# func main() {
#     var x = [2][2][3]float{{{1.0, 2.0, 30.0}, {4.0, 5.0, 6.0}}, {{7.0, 8.0, 9.0}, {10.0, 11.0, 12.0}}};
#     putFloat(x[0][0][2]);
#     putInt(4);
# }
# """
#         expect = "30.04"
#         self.assertTrue(TestCodeGen.test(input,expect,552))
#     def test_array5(self):
#         input = """
# func getArray() [2][2]int {
#     return [2][2]int{{1, 2}, {3, 4}};
# }
# func main () {
#     putInt(getArray()[0][1]);
# }"""
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,553))
#     def test_array6(self):
#         input = """
# type Node struct {
#     a int;
#     n [2]Node;
# }
# func getNode() Node {
#     return Node{a: 1, n: [2]Node{Node{a: 2}, Node{a: 3}}};
# }
# func main () {
#     putInt(getNode().n[1].a * getNode().n[0].a);
# }"""
#         expect = "6"
#         self.assertTrue(TestCodeGen.test(input,expect,554))
#     def test_func_decl2(self):
#         input = """
# func add(a [2]int, b [2]float) [2]float {
#     return [2]float{a[0] + b[0], a[1] + b[1]};
# }
# func main () {
#     var a [2]int = [2]int{1, 2};
#     var b [2]float = [2]int{3, 4};
#     var c [2]float = add(a, b);
#     putFloat(c[0]);
# }
# """
#         expect = "4.0"
#         self.assertTrue(TestCodeGen.test(input,expect,555))
#     def test_func_decl3(self):
#         input = """
# type A struct {
#     a int;
#     b float;
# }
# func add(a A, b A) A {
#     return A{a: a.a + b.a, b: a.b + b.b};
# }
# func main () {
#     var a = A{a: 1, b: 2.0};
#     var b = A{a: 3, b: 4.0};
#     var c = add(a, b);
#     putIntLn(c.a);
#     putFloat(c.b);
# }"""
#         expect = "4\n6.0"
#         self.assertTrue(TestCodeGen.test(input,expect,556))
#     def test_func_decl4(self):
#         input = """
# func printArray() {
#     var b int = 4;
#     var arr [b * 10 / 10 + 1]int = [b+1]int{1, 2, 3, 4, 5};
#     for i := 0; i < b; i += 1 {
#         putInt(arr[i]);
#     }
# }
# func main () {
#     printArray();
# }"""
#         expect = "1234"
#         self.assertTrue(TestCodeGen.test(input,expect,557))
#     def test_global_var0(self):
#         input = """
# var a = (10 + 12) / 3 - (500 * 2) % 3;
# func main () {
#     putInt(a);
# }"""
#         expect = "6"
#         self.assertTrue(TestCodeGen.test(input,expect,558))
#     def test_global_var1(self):
#         input = """
# var a [3]float = [3]float{1.0, 2.0, 3.0};
# func main () {
#     putFloat(a[0]);
# }"""
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input,expect,559))
#     def test_global_var2(self):
#         input = """
# type A struct {
#     a int;
#     b float;
# }
# var a A = A{a: 1, b: 2.0};
# func main () {
#     putInt(a.a);
# }"""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,560))
#     def test_global_var3(self):
#         input = """
# type A struct {
#     a int;
#     b float;
# }
# var a A = A{a: 1, b: 2.0};
# func Add(b A) A {
#     return A{a: a.a + b.a, b: a.b + b.b};
# }
# func main () {
#     var b = A{a: 3, b: 4.0};
#     var c = Add(b);
#     putIntLn(c.a);
#     putFloat(c.b);
# }"""
#         expect = "4\n6.0"
#         self.assertTrue(TestCodeGen.test(input,expect,561))
#     def test_global_var4(self):
#         input = """
# type A struct {
#     a int;
#     b float;
# }
# func (a A) Add(b A) A {
#     return A{a: a.a + b.a, b: a.b + b.b};
# }
# var a A = A{a: 1, b: 2.0};
# func main () {
#     var b = A{a: 3, b: 4.0};
#     var c = a.Add(b);
#     putIntLn(c.a);
#     putFloat(c.b);
# }"""
#         expect = "4\n6.0"
#         self.assertTrue(TestCodeGen.test(input,expect,562))
#     def test_global_var5(self):
#         input = """
# var a int = 10;
# var b float = a + 12.5;
# var c boolean = a > 5 || b < 20.0;
# func main () {
#     putIntLn(a);
#     putFloatLn(b);
#     putBool(c);
# }"""
#         expect = "10\n22.5\ntrue"
#         self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_add_string0(self):
        input = """
func main() {
    var a string = "Hello, ";
    var b string = "World";
    var c string = a + b;
    putString(c);
}
"""
        expect = "Hello, World"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_add_string1(self):
        input = """
var arr [2]string = [2]string{"Viet", "Nam"};
type A struct {
    a string;
}
func getStr() string {
    return "Hello, ";
}
func main () {
    var a A = A{a: "!"};
    putString(getStr() + arr[0] + " " + arr[1] + a.a);
}
"""
        expect = "Hello, Viet Nam!"
        self.assertTrue(TestCodeGen.test(input,expect,565))
#     def test_var_decl3(self):
#         input = """
# var a = 2;
# func main() {
#     var b [a][a] int;
#     putIntLn(b[0][0]);
#     b[0][0] := 20;
#     putInt(b[0][0]);
# }
# """
#         expect = "0\n20"
#         self.assertTrue(TestCodeGen.test(input,expect,566))
#     def test_array7(self):
#         input = """
# const a = 2;
# const b = a + 3;
# func increment(a int) int {
#     return a + 1;
# }
# func main () {
#     var arr [a][b][increment(2)]boolean;
#     putBoolLn(arr[0][0][0]);
#     arr[0][0][0] := true;
#     arr[0][0][1] := arr[0][0][0] || arr[0][0][1];
#     putBool(arr[0][0][1]);
# }"""
#         expect = """false\ntrue"""
#         self.assertTrue(TestCodeGen.test(input,expect,567))
#     def test_array8(self):
#         input = """
# type A struct {
#     a int;
# }
# func (a A) increment() int {
#     return a.a + 1;
# }
# const a = A{a: 3};
# var arr [2][2]int = [2][2]int{{1, 2}, {3, 4}};
# func main () {
#     var array[a.a][arr[0][1]][a.increment()]int;
#     putInt(array[0][1][2]);
# }"""
#         expect = "0"
#         self.assertTrue(TestCodeGen.test(input,expect,568))
#     def test_func_decl5(self):
#         input = """
# func main () {
#     var a = getInt();
#     putInt(a);
# }

# func getInt() int {
#     return 10;
# }
# """
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,569))
#     def test_func_decl6(self):
#         input = """
# func getInt() int {
#     return rec(5);
# }
# func main () {
#     putIntLn(getInt());
# }
# func rec(a int) int {
#     if (a == 0) {
#         return 1;
#     }
#     return a * rec(a - 1);
# }
# """
#         expect = "120\n"
#         self.assertTrue(TestCodeGen.test(input,expect,570))
#     def test_method_decl2(self):
#         input = """
# func (a A) add(b int, c int) {
#     a.a := a.sum(b, c);
# }
# type A struct {
#     a int;
# }
# func main () {
#     var a = A{a: 1};
#     putIntLn(a.sum(2, 3));
# }
# func (a A) sum(b, c int) int {
#     return b + c;
# }
# """
#         expect = "5\n"
#         self.assertTrue(TestCodeGen.test(input,expect,571))
#     def test_struct3(self):
#         input = """
# type A struct {
#     a int;
#     b float;
# }
# func main () {
#     var a = A{a: 1, b: 2.0};
#     var b = A{a: 5, b: 6.0};
#     a.a := 3;
#     a.b := 4.0;
#     putIntLn(a.a);
#     putFloatLn(a.b);
#     putIntLn(b.a);
#     putFloatLn(b.b);
# }"""
#         expect = "3\n4.0\n5\n6.0\n"
#         self.assertTrue(TestCodeGen.test(input,expect,572))
    def test_binary_op7(self):
        input = """
func main () {
    var x = 10 + (10 + (10 + (10 + (10 + (10 + (10 + 10))))));
    putIntLn(x);
}"""
        expect = "80\n"
        self.assertTrue(TestCodeGen.test(input,expect,573))