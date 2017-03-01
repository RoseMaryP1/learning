Scala Basics
============

Good 1hr overview video: https://www.youtube.com/watch?v=DzFt0YkZo8M

* Can use named arguments (like python)
* `object` to define a singleton, `class` to define a class and `def` to define a function
* Typed, so you define parameters like so `def myFn(args: Array[String]) ReturnType = {..`
* If you use `var` before the argument, it will be mutable.
* Still uses brackets, but they are somewhat optional?
* Calling functions without parameters just uses the `fnName` not `fnName()`
* `return` is optional, can just use the value to be returned (uses last line executed by default)
* functions that don't return values are called "proceedures" and return type is `def myFn(): Unit = { doStuff }`
* variable number of inputs can be handled by `def myFn(args: Int*)`
* Recursion is a little odd, .. probably want to review this later
* Arrays and ArrayBuffers <- (~python lists):
    * `Array[Type](Size)` is a static size vs `ArrayBuffer[Type](InitSize)` which can be added/appended to.
    * Get or set a specific element `myArray(i) = Item`
    * Add items to beginning `myArrayBuff.insert(0, Item1, Item2)`
    * Add items to end `myArrayBuff += NewItem`
    * Add multiple items to end `myArrayBuff ++= Array(1, 2, 3)`
    * Remove 2 items starting at the 2nd index `myArrayBuff.remove(1, 2)`
    * Multi-dimentional arrays with `myArray = Array.ofDim[Int](10,10)` and reference with `myArray(0, 0)`
    * Can use `.sum`, `.min`, and `.max` on arrays. (no parenthesis)
    * Sort (not in place) using `.sort(_<_)` for ascending and `.sort(_>_)` for descending
* Maps (keyval storage ~ python dicts):
    * To create: `items = Map(somekey -> someval, ...)`, by default is NOT mutable
    * To check key exists: `items.contains(somekey)`
    * To reference a value: `items(somekey)`
    * For a mutable Map: `items = collection.mutable.Map(..)`
    * To add to a mutable map: `items(newkey) = Item`
    * To loop: `for()(k,v) <- items){}`
* Tuple: immutable collection of various types (~python tuple)
    * Literal: `items = (100, "Item _2", "Item _3")`
    * Loop: `items.productIterator.foreach{ i => println(i)}` << (similar to TypeScript)
* Loops:
    * `for (i <- beginVal to (myArray.length - 1){}`
    * `for (item <- Items) {}`
    * `myArray.foreach(println)`
* Output:
    * `println("print to command line: %s", "someString")`
    * `printf("print a decimal: %f.1 \n", 5.0 )`
    * `printf(s"Embed a string: $myVal\n")`
    * `println(s"Embed a string: ${myVal.attribute}")`

    
* Filters? (~python generators):
    * `numsX2 = for(num <- Array(1,2,3,4) yield num * 2`

Classes:
------
* Are placed within objects?
* Default constructor is defined by class itself, (no `__constructor`). `class MyClass(var arg1: int) {}`
* Constructors for other signatures are possible to define using `def this(..new signature..)`
* Custom constructors call `this(arg1, arg2)` to trigger the actual constructor.. kinda like `.super()`
* Reference attributes with `this.arg1`
* NO static vars or methods allowed, but you can basically do the same thing by creating a companion object (singleton) using `object mySameClassName { ..static vars and functions}`
* Constructor attributes are initialized by default, but to initialize attributes or check inputs, use `this.someFn()` or `var myId = MyClass.newIdNum` or just `var item = "A"`
* `protected`, `public`, and `private` still work the same. `public` by default?
* To override methods, use `override def toString(...`
* to create an instance: `var instance = new MyClass` or `var instance = new MyClass(args)`
* Can declare `final` on a class to ensure it's not inherited from.
* Inherit with: `class Child(name: String) extends Person(name) {..`
* abstract classes can be defined with `abstract class myAbsClass(..` and can define abstract classes with `def absFn: ReturnType`
* traits can be used for multiple inheritance: `trait Flyable { ..` and can set abstract or actual methods and vars like abstract classes.
* Inherit traits using `class myClass() extends Trait1 with Trait2 with ..{`

Higher order functions:
--------
* Can be set to variables. `val newFn = someOtherFn _` (note the underscore)
* using map: `List(1000, 1000).map(newFn).foreach(println)`
* also map: `List(1000, 1000).map(x: Int => x * 50).foreach(println)`
* using filter: `List(1, 2, 3).filter(_ % 2 == 0).foreach(println)`
* Can pass functions into other functions using `def outerFn(innterFn: (Int) => (Int)) = { innerFn }`
* Closures are values that depend on external values. `val myClosure = (num: Double) => num / otherNum` and called like Function.

Writing and reading files
---------
* use `java.io.PrintWriter` to write and `scala.io.Source` to read files.
* Reading:
```
  val writer = new PrintWriter("filename.txt")
  writer.write("Some Text")
  writer.close()
```
* Writing:
```
  val text = Source.fromFile("filename.txt", "UTF-8")
  val lineIterator = text.getLines
  for(line <- lineIterator)
    println(line)
  text.close()
```
Exceptions
--------
* use try, catch and finally like so: 
```
def myFn(n1: Int, n2 Int) = try {
  (n1 / n2)
} catch {
  case ex: Java.lang.ArithmaticException => "Can't Divide by zero"
} finally {
  // Clean up after exception.
}
```
