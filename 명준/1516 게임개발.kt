//package com.example.myapplication
//
//
//
///*
//
//첫번째 줄 건물의 종류 수 N
//다음 N개줄에 각 건물을 짓는데 걸리는 시간 그 건물을 짓는데 먼저 필요한 건물의 번호
//각 줄은 -1로 끝남
//
//입력
//5
//10 -1
//10 1 -1
//4 1 -1
//4 3 1 -1
//3 3 -1
//
//출력
//    10
//    20
//    14
//    18
//    17
// */
//
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val n = readLine().toInt()
//    val buildingTime = mutableMapOf<Int, Int>()
//    val answer = mutableListOf<Int>()
//
//    for (i in 1..n) {
//        buildingTime[i] = 0
//    }
//
//    repeat(n) {
//        val buildingInfo = readLine().split(" ").map { it.toInt() }
//        var buildTime = buildingInfo[0]
//        if (buildingInfo.size > 1) {
//            for (j in 1 until buildingInfo.size) {
//                val preBuilding = buildingInfo[j]
//                if (buildingTime.containsKey(preBuilding)) {
//                    val preTime = buildingTime[preBuilding] ?: 0
//                    if (preTime != 0) {
//                        buildTime += preTime
//                    }
//                }
//            }
//        }
//        buildingTime[it + 1] = buildTime
//        println(buildTime)
//    }
//}