//package com.example.myapplication
//
//import java.util.Stack
//
//
///*
//크기가 n인 arr
//어떤 i,j 에 대한 점수는 (arr[i]+...+arr[j]) * min{arr[i],...arr[j]}가 된다.
//즉, left = i 부터 right = j 까지의 합에 i부터 j 까지의 최솟값을 곱한것이 점수임
//
//6
//3 1 6 4 5 2
//
//left 0
//right
//
//60
//
//
//시간초과 해결하기
//
//
//한방향으로 풀어보기
// */
//
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val n = readLine().toInt()
//    val arr = readLine().split(" ").map { it.toInt() }
//    val left = IntArray(n)
//    val right = IntArray(n)
//    val preSum = LongArray(n + 1)
//    val list = Stack<Int>()
//    var answer = 0L
//
//    for (i in 1..n) {
//        preSum[i] = preSum[i - 1] + arr[i - 1]
//    }
//
//    for (j in 0 until n){
//        while (list.isNotEmpty() &&arr[list.last()] >= arr[j]) {
//            list.removeAt(list.size - 1)
//        }
//        left[j] = if (list.isEmpty()) 0 else list.last() + 1
//        list.add(j)
//    }
//
//    list.clear()
//
//    for (k in n - 1 downTo 0) {
//        while (list.isNotEmpty() && arr[list.last()] >= arr[k]){
//            list.removeAt(list.size - 1)
//        }
//        right[k] = if (list.isEmpty()) n - 1 else list.last() - 1
//        list.add(k)
//    }
//
//    for (l in 0 until n){
//        val totalScore = preSum[right[l] + 1] - preSum[left[l]]
//        val score = totalScore * arr[l]
//        if (score > answer) {
//            answer = score
//        }
//    }
//
//    println(answer)
//
//}