import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readLine().toInt()
    var arr = readLine().split(" ").map { it.toInt() }.toIntArray()

    var sum = 0
    var count: Int

    /**
     * i 공장에서는 몇 개를 사든 어차피 3원, 그러니 최대한 많이 사둔다
     * i+1, i+2 공장에서는 몇 개를 사든 2원씩이다
     * i+1에서 i에서 산 라면 수 vs i+1에서 살 수 있는 라면의 수 중에서 작은 수만큼 구매
     * i+2에서는 i+1에서 구매하지 못한 라면만큼 남기고 구매
     */

    for (i in 0 until n) {
        if (arr[i] > 0) {
            count = arr[i]
            sum += 3 * count

            if (i + 1 < n) {
                count = min(count, arr[i + 1])
                sum += 2 * count
                arr[i + 1] -= count
            }

            if (i + 2 < n) {
                count = min(count, arr[i + 2] - min(arr[i + 1], arr[i + 2]))
                sum += 2 * count
                arr[i + 2] -= count
            }
        }
    }

    println(sum)
}
