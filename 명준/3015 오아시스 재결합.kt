//
//
//import java.util.Stack
//
//
///*
//첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다
//둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 2^31 나노미터 보다 작다
//
//입력
//
//7
//2
//4
//1
//2
//2
//5
//1
//
//출력 : 10
//
// */
//
//
//
//
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val n = readLine().toInt()
//    var answer = 0L
//    val stack = Stack<Pair<Long,Long>>()  // (그사람의키, 그사람과 마주볼 수 있는사람의 숫자를 저장)
//
//    repeat(n) {
//        var nowHeight = readLine().toLong() // 현재들어온 높이
//        var nextHeight = Pair(nowHeight, 1L) //
//
//        while (stack.isNotEmpty() && stack.peek().first <= nowHeight) {
//            val top = stack.pop()
//            answer += top.second
//
//            if (top.first == nowHeight) nextHeight = Pair(top.first, top.second +1)
//            // 키가 같다면
//        }
//        if (stack.isNotEmpty()) answer++
//        stack.push(nextHeight)
//
//    }
//
//    println(answer)
//
//}