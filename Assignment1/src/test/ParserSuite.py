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
    def test_multipletest0(self):
        input = """return 10; break; continue;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_multipletest1(self):
        input = """var a int = 10;
        const b = 10.0 / 5.0;
        p := Person{name: \"abc\", age: 10, address: \"abc\"}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_multipletest2(self):
        input = """var y string = "abc";
        var z = 10.24; var x int;
        var arr [3]int = [3]int{1,2,3};
        var arr1 [4]float ;
        var arr2 [4][5]boolean ;
        const a = "heo may con gio thu vuong trong mat em khi chieu nang tan";
        d := 10 || 20 * (15 + 5 - abc.xyz) / 12;
        // tung nu hon ngat moi mem tan vao trong gio menh mang
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_multipletest3(self):
        input = """type Person struct {
    name string
    age int
    address string
}

func main() {
    var p Person
    p.name := "abc"
    p.age := 10
    p.address := "abc"

    var p1 Person = Person{name: "abc", age: 10, address: "abc"}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_multipletest4(self):
        input = """type Person struct {
    name string
    age int
    address Address
}
type Address struct {
    city string
    country string
}

func main() {
    var p Person
    p.name := "abc"
    p.age := 10
    p.address := Address{city: "abc", country: "abc"}

    var p1 Person = Person{name: "abc", age:10, address: Address{city: "abc", country: "abc"}}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_multipletest5(self):
        input = """type Calculator interface {
    Add(x, y) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}

type CalculatorImpl struct {
    name string
    age int
    address Address
}

func main() {
    var p Calculator
    p.name := "abc"
    p.age := 10
    p.address := Address{city: "abc", country: "abc"}

    var p1 Calculator = CalculatorImpl{name: "abc", age: 10, address: Address{city: "abc", country: "abc"}}
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_multipletest6(self):
        input = """type Calculator interface {
    Add(x, y) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}

type CalculatorImpl struct {
    name string
    age int
    address Address
}

func myFunc(){
    var p Calculator
    p.name := "abc"
    p.age := 10
    p.address := Address{city: "abc", country: "abc"}

    var p1 Calculator = CalculatorImpl{name: "abc", age: 10, address: Address{city: "abc", country: "abc"}}

    return 100 * 20 - 13.567
}

func sayHello(name string){
    print("Hello " + name)
    return
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_multipletest7(self):
        input = """func Fibonacci(n int) int {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    } else {
        return Fibonacci(n-1) + Fibonacci(n-2)
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_multipletest8(self):
        input = """func Greeting() {
    for i := 0; i < 1000; i+=1 {
        print("Hello World")
        str := input()
        if (str == "exit") {
            break
        } else if (str == "continue") {
            continue    
        } else if (str == "tell me a joke") {
            for _, value := range [3]int{1,2,3} {
                tellMeAJoke()
            }
        } else {
            print("I don't understand")
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_multipletest9(self):
        input = """for index, value := range arr{
        print(value)
        if (value > 100) {
            i := 0
            for arr1[i] != value {
                for j:= 0; j < 10; j += 1 {
                    print(arr1[j])
                }
                i += 1
            }
        } else if (value < 100) {
            print("less than 100")
            continue
        } else {
            print("dau phai yeu het tam, nguoi de tam, nguoi de tam")
            break
        }
    } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_multipletest10(self):
        input = """type Calculator struct {
        name string
        value int
}
func (c Calculator) Add(x int, y int) int {
    return x + y
}

func (c Calculator) Subtract(a float, b float, c int) float {
    return a - b
}

func (c Calculator) Reset() {
    c.name := "abc"
    c.value := 10
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_multipletest11(self):
        input = """// addNumbers takes two integers and returns their sum.
func addNumbers(a int, b int) int {
    sum := a + b // Implicit return variable usage
    return sum
}

func main() {
    // Declare and initialize two numbers using shorthand assignment
    x := 5
    y := 10
    
    // Call the function and store the result
    result := addNumbers(x, y)
    
    // A no-op statement to use result and avoid unused variable error (normally we'd print it)
    _ := result
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_multipletest12(self):
        input = """
// Person represents an individual with a name and age.
type Person struct {
    Name string
    Age  int
}

/*
   Greet generates a greeting message for the person.
   It returns a string formatted with the person's name and age.
*/
func (p Person) Greet() string {
    return "Hello, my name is " + p.Name + " and I am " + stringify(rune(p.Age)) + " years old."
}

func main() {
    // Create a new Person instance
    p := Person{Name: "Alice", Age: 30}
    
    // Call the method
    message := p.Greet()
    
    // Avoid unused variable warning
    _ := message
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    
    def test_multipletest13(self):
        input = """// Person represents an individual with a name and age.
type Person struct {
    Name string
    Age  int
}

/*
   Greet generates a greeting message for the person.
   It returns a string formatted with the person's name and age.
*/
func (p Person) Greet() string {
    return "Hello, my name is " + p.Name + " and I am " + stringify(rune(p.Age)) + " years old."
}

/*
   ComputeFactorial calculates the factorial of the person's age.
   It uses a recursive approach.
*/
func (p Person) ComputeFactorial(n int) int {
    if (n <= 1) {
        return 1
    }
    return n * p.ComputeFactorial(n-1)
}

/*
   IsAdult checks if the person is considered an adult.
   It returns true if the age is 18 or older.
*/
func (p Person) IsAdult() bool {
    return p.Age >= 18 && (p.Age%2 == 0 || p.ComputeFactorial(p.Age%5) > 10)
}

func main() {
    // Create a new Person instance
    p := Person{Name: "Alice", Age: 30}
    
    // Call the methods
    message := p.Greet()
    factorial := p.ComputeFactorial(p.Age)
    isAdult := p.IsAdult()
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_multipletest14(self):
        input = """// Rectangle represents a geometric shape with width and height.
type Rectangle struct {
    Width  float64
    Height float64
}

/*
   Area calculates and returns the area of the rectangle.
*/
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

/*
   Perimeter calculates and returns the perimeter of the rectangle.
*/
func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}

/*
   FindMax finds the maximum number in an array.
*/
func FindMax(numbers int) int {
    if (len(numbers) == 0) {
        return 0
    }
    max := numbers[0]
    for _, num := range numbers {
        if (num > max) {
            max := num
        }
    }
    return max
}

func main() {
    // Create a new Rectangle instance
    rect := Rectangle{Width: 5.0, Height: 10.0}
    
    // Call the methods
    area := rect.Area()
    perimeter := rect.Perimeter()
    
    // Declare and initialize an array
    numbers := [5]int{3, 7, 2, 9, 5}
    maxNumber := FindMax(numbers)
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_multipletest15(self):
        input = """func main() {
    // Declare and initialize an array
    numbers := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    // Iterate over the array using a for loop
    for _, num := range numbers {
        // Check if the number is even or odd using parenthesized boolean expressions
        if (num%2 == 0) {
            // Even number case
            _ := "Even"
        } else {
            // Odd number case
            _ := "Odd"
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_multipletest16(self):
        input = """
func main() {
    // Example using a for loop and if/else with parenthesized boolean expressions

    for i := 0; i < 10; i+=1 {
        if (i%2 == 0) { // Parentheses around the boolean expression
            fmt.Printf("%d is even\n", i)
        } else if (i > 5 && (i < 9 || i == 9)) { // Parentheses around compound boolean expression
            fmt.Printf("%d is greater than 5 and less than 9 or equal to 9\n", i)
        } else {
            fmt.Printf("%d is odd\n", i)
        }
    }

    names := [23]string{"Alice", "Bob", "Charlie", "David", "Eve"} // Another Example demonstrating different boolean conditions

    for _, name := range names {
        if (name == "Alice" || name == "Eve") { // Parentheses around the OR condition
            fmt.Println(name, "is a popular name.")
        } else if (name != "Bob" && (len(name) > 3)) { // Parentheses around the AND and length conditions
            fmt.Println(name, "is a less common name with more than 3 characters.")
        } else {
            fmt.Println(name, "is a common name.")
        }
    }


    // Example with a nested if

    for j := 1; j <= 5; j+=2 {
        fmt.Println("Outer loop:", j)
        if (j > 2) {
            if (j < 5) { // Nested if with parentheses
                fmt.Println("  Inner loop: j is between 3 and 4")
            } else {
                fmt.Println("  Inner loop: j is 5")
            }
        }
    }

}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_constdecl4(self):
        input = """const x int = 10;"""
        expect = "Error on line 1 col 9: int"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_funccall6(self):
        input = """foo(2 + x, 4 / y - 1);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_funccall7(self):
        input = """m.goo(2 + foo(), 4 / bar() - arr[2][3]);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_funccall8(self):
        input = """foo("asdasd" xyz + 6);"""
        expect = "Error on line 1 col 14: xyz"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_assign7(self):
        input = """a := foo := bar := 5;"""
        expect = """Error on line 1 col 10: :="""
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_ifexpr7(self):
        input = """if (A) {
            a := b;
        }
        else {
            a := b;
        }
        else {
            a := b;
        }"""
        expect = "Error on line 7 col 9: else"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    