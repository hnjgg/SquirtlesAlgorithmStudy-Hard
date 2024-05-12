
//
//
///*
//첫째 줄에는 가수의 수 N과 보조 PD의 수 M
//둘째 줄부터 각 보조 PD가 정한 순서들이 한 줄에 하나씩
//각 줄의 맨 앞에는 보조 PD가 담당한 가수의 수가 나오고, 그 뒤로는 그 가수들의 순서
//
//출력은 N 개의 줄, 한 줄에 하나의 번호를 출력
//답이 여럿일 경우에는 아무거나 하나를 출력
//만약 순서를 정하는 것이 불가능할 경우에는 첫째 줄에 0을 출력
//
//입력
//
//6 3
//3 1 4 3
//4 6 2 5 4
//2 2 3
//
//출력
//
//6
//2
//1
//5
//4
//3
// */
//
//import java.util.*
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val (n , m) = readLine().split(" ").map { it.toInt() }
//    val graph = Array(n + 1) { mutableListOf<Int>() }
//    val inDegree = IntArray(n + 1) { 0 }
//    val singer = mutableListOf<Int>()
//
//    repeat(m) {
//        val pdPick = readLine().split(" ").map { it.toInt() }
//        for (i in 1 until pdPick.size - 1) {
//            val from = pdPick[i]
//            val to = pdPick[i + 1]
//            graph[from].add(to)
//            inDegree[to]++
//        }
//    }
//
//    val queue = LinkedList<Int>()
//    for (i in 1..n) {
//        if (inDegree[i] == 0) {
//            queue.offer(i)
//        }
//    }
//
//    while (queue.isNotEmpty()) {
//        val cur = queue.poll()
//        singer.add(cur)
//        for (next in graph[cur]) {
//            inDegree[next]--
//            if (inDegree[next] == 0) {
//                queue.offer(next)
//            }
//        }
//    }
//
//    if (singer.size == n) {
//        singer.forEach { println(it) }
//    } else {
//        println(0)
//    }
//}