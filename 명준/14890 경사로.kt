


/*
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2

3

 */


fun main() = with(System.`in`.bufferedReader()) {
    val (n, l) = readLine().split(" ").map { it.toInt() }
    val map = Array(n){IntArray(n)}
    var answer = 0

//지도 입력받기
    for (i in 0 until n) {
        val input = readLine().split(" ").map { it.toInt() }
        for (j in 0 until n) {
            map[i][j] = input[j]
        }
    }
//x체크
    for (x in 0 until n) {
        var count = 1
        var prevHeight = map[x][0]

        for (y in 1 until n) {
            if (map[x][y] == prevHeight) {
                count++
            } else if (map[x][y] == prevHeight + 1 && count >= l) {
                count = 1
                prevHeight++
            } else if (map[x][y] == prevHeight - 1 && count >= 0) {
                count = -l + 1
                prevHeight--
            } else break

            if (y == n-1 && count >= 0) answer++

        }
    }
//y체크
    for (y in 0 until n) {
        var count = 1
        var prevHeight = map[0][y]

        for (x in 1 until n) {
            if (map[x][y] == prevHeight) {
                count++
            } else if (map[x][y] == prevHeight + 1 && count >= l) {
                count = 1
                prevHeight++
            } else if (map[x][y] == prevHeight - 1 && count >= 0) {
                count = -l + 1
                prevHeight--
            } else break

            if (x == n - 1 && count >= 0) answer++
        }
    }

    println(answer)
}