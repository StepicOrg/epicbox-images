package calculator

object Main extends App {

  // put your code here
  var loop: Boolean = true
  while(loop) {
    val line = scala.io.StdIn.readLine()
    if (line != null) {
      val parts = line.split(' ')
      println(parts(0).toInt + parts(1).toInt)
    } else {
      loop = false
    }
  }
}
