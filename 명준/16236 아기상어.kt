//
///*
//거리가 가까운 물고기가 많다면,
//가장 위에 있는 물고기,여러마리라면, 가장 왼쪽에 있는 물고기
//
//입력
//
//첫째 줄에 공간의 크기 N
//둘째 줄부터 N개의 줄에 공간의 상태
//0 : 빈칸
//1,2,3,4,5,6 : 칸에 있는 물고기 크기
//9 : 아기 상어의 위치
//
//출력
//
//3
//0 0 0
//0 0 0
//0 9 0
//
//0
//---
//4
//4 3 2 1
//0 0 0 0
//0 0 9 0
//1 2 3 4
//
//14
//
//---
//????
//
//6
//5 4 3 2 3 4
//4 3 2 3 4 5
//3 2 9 5 6 6
//2 1 2 3 4 5
//3 2 1 6 5 4
//6 6 6 6 6 6
//
//60
//
//---
//????
//6
//6 0 6 0 6 1
//0 0 0 0 0 2
//2 3 4 5 6 6
//0 0 0 0 0 2
//0 2 0 0 0 0
//3 9 3 0 0 1
//
//48
//
//---
//
//6
//1 1 1 1 1 1
//2 2 6 2 2 3
//2 2 5 2 2 3
//2 2 2 4 6 3
//0 0 0 0 0 6
//0 0 0 0 0 9
//
//39
//
// */
//
//import java.util.LinkedList
//import java.util.Queue
//
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val n = readLine().toInt()
//    val map = Array(n) {IntArray(n)}
//    var size = 2
//    var answer = 0
//    var eatFish = 0
//    var (x,y) = Pair(0,0)
//    val dx = intArrayOf(1,-1,0,0)
//    val dy = intArrayOf(0,0,1,-1)
//
//    //맵과 초기 위치 저장
//    for (i in 0 until n) {
//        val input = readLine().split(" ").map { it.toInt() }
//        for (j in 0 until n) {
//            map[i][j] = input[j]
//            if (map[i][j] == 9 ) {
//                x = i
//                y = j
//                map[i][j] = 0
//            }
//        }
//    }
//
//
//
//
//    while (true) {
//        val q : Queue<Triple<Int,Int,Int>> = LinkedList()
//        val visited = Array(n) {BooleanArray(n)}
//        q.add(Triple(x,y,0))
//
//        var minDistance = Int.MAX_VALUE
//        //먹을수 있는 물고기 저장용
//        val temp = mutableListOf<Pair<Int,Int>>()
//
//
//        while (q.isNotEmpty()) {
//            val (curX , curY, distance) = q.poll()
//
//            //경우 나누기 현재 위치에 먹을수 있는 물고기가 있을 때
//            if (map[curX][curY] in 1 until size && distance <= minDistance) {
//                minDistance = distance
//                temp.add(Pair(curX,curY))
//            }
//            //방문하지 않았고, 최소거리 이하인 경우
//            if (!visited[curX][curY] && distance <= minDistance) {
//                visited[curX][curY] = true
//                for (i in 0 until 4) {
//                    val newX = curX + dx[i]
//                    val newY = curY + dy[i]
//
//                    //먹을수 있는 물고기가 범위 안에 있고, 상어가 지나갈수 있음
//                    if (newX in 0 until n && newY in 0 until n && map[newX][newY] <= size) {
//                        q.add(Triple(newX,newY,distance+1))
//                    }
//                }
//            }
//
//
//        }
//
//        if (temp.isEmpty()) break
//        else {
//            //가장 우선순위 높은 물고기 먹기  가장위 -> 가장 오른쪽
//            temp.sortBy { it.second }
//            temp.sortBy { it.first }
//
//            val (newX,newY) = temp[0]
//            x = newX
//            y = newY
//            answer += minDistance
//            eatFish++
//
//            if (eatFish == size) {
//                size++
//                eatFish = 0
//            }
//            map[x][y] = 0
//        }
//    }
//
//    println(answer)
//
//}