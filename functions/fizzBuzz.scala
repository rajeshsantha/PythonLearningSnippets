/*
def isDivideByn(number, n):
    return number % n == 0


def fizzBuzz(input):
    result = ""

    if isDivideByn(input, 3) and isDivideByn(input, 5):
        print("fizzBuzz")
    elif isDivideByn(input, 3):
        print("fizz")
    elif isDivideByn(input, 5):
        print("buzz")
    else:
        print("invalid input ", input)

*/

/*
# if number divided by both 3,5 => print("fizzBuzz")
# if number divided by 5 => print("buzz")
# if number divided by 3 => print("fizz")
*/
object FizzBuzz extends App{

def fizzBuzzFunc(input:Int):Unit = {

    input match {
        case x if x%5==0 && x%3==0 => print("fizzbuzz")
        case x if x%5==0 => print("buzz")
        case x if x%3==0 => print("fizz")
        case _ => println("invalid input ") 
    }

}

fizzBuzzFunc(11351)

 //0 to 10 by 2 foreach println

  def add1(a:Int,b:Int):Int =  a+b

 def add2(a:Int)(b:Int):Int =   a+b
 
 // println(add1(1,2))
  val addNumber5 =add2(5) _
  println(addNumber5(2))

}


