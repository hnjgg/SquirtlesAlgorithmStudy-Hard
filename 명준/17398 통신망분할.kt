//
///*
//입력
//첫번째 줄에는 통신탑의 갯수 N , 통신탑 사이의 연결갯수 M , 통신망 연결 분할 횟수 Q
//두번째 ~ M개 줄에 두개의 자연수 (X,Y) , X와Y가 연결됨을 뜻함 --중복된 연결 없음 모든 통신탑은 하나의 통신망에 속함
//그다음줄 부터 Q개의 줄에 걸쳐 제거될 연결의 번호 자연수 A -> A번째로 입력된 (X,Y)의 연결이 제거됐음을 의미
//
//(1 <= N <= 100,000, 1 <= M <= 100,000, 1 <= Q <= M)
//출력
//첫 번째 줄에 Q개의 연결을 순서대로 제거하는데 드는 비용의 합을 출력한다.
//
//
//4 4 3
//1 2
//2 3
//3 4
//1 4
//4
//2
//3
//
//5
//
// */
//
//
//fun find(a: Int, parent: IntArray): Int {
//    if (parent[a] != a) {
//        parent[a] = find(parent[a], parent)
//    }
//    return parent[a]
//}
//
//fun union(a: Int, b: Int, parent: IntArray, size: IntArray): Boolean {
//    val rootA = find(a, parent)
//    val rootB = find(b, parent)
//    if (rootA != rootB) {
//        if (size[rootA] < size[rootB]) {
//            parent[rootA] = rootB
//            size[rootB] += size[rootA]
//        } else {
//            parent[rootB] = rootA
//            size[rootA] += size[rootB]
//        }
//        return true
//    }
//    return false
//}
//
//fun main() = with(System.`in`.bufferedReader()) {
//
//    val (n, m, q) = readLine().split(" ").map { it.toInt() }
//    val edge = mutableListOf<Pair<Int, Int>>()
//    val remove = IntArray(q)
//    val parent = IntArray(n + 1) { it }
//    val size = IntArray(n + 1) { 1 }
//    var answer = 0L
//
//    repeat(m) {
//        val (x, y) = readLine().split(" ").map { it.toInt() }
//        edge.add(Pair(x, y))
//    }
//
//    repeat(q) {
//        remove[it] = readLine().toInt() - 1
//    }
//
//    val removedSet = remove.toSet()
//    for (i in edge.indices) {
//        if (i !in removedSet) {
//            union(edge[i].first, edge[i].second, parent, size)
//        }
//    }
//
//    for (j in remove.indices.reversed()) {
//        val (x, y) = edge[remove[j]]
//        val rootX = find(x, parent)
//        val rootY = find(y, parent)
//
//        if (rootX != rootY) {
//            val cost = size[rootX].toLong() * size[rootY].toLong()
//            answer += cost
//            union(x, y, parent, size)
//        }
//    }
//
//    println(answer)
//}