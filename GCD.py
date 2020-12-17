#no tail recursive
	def gcd(a: Int, b: Int): Int =
  		if (b == 0) a else gcd(b, a % b)


#tail recursive
import scala.annotation.tailrec
object Main
{
    def GCD(n: Int, m: Int): Int =
    {
      @tailrec def gcd(x:Int, y:Int): Int=
      {
        if (y == 0) x
        else gcd(y, x % y)
      }
      gcd(n, m)
    }

    def main(args:Array[String])
    {
      println(GCD(12, 18))
    }
}
