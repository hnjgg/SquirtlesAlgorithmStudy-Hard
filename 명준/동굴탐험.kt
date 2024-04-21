


import java.util.*

class Solution {
   fun solution(n: Int, path: Array<IntArray>, order: Array<IntArray>): Boolean {
       val mapList = ArrayList<ArrayList<Int>>()
       val orderList = IntArray(n)
       repeat(n) { mapList.add(ArrayList()) }

       path.forEach { i ->
           mapList[i[0]].add(i[1])
           mapList[i[1]].add(i[0])
       }

       order.forEach { i ->
           orderList[i[1]] = i[0]
       }

       val next = IntArray(n)
       val visit = BooleanArray(n)
       val q: Queue<Int> = LinkedList()
       q.add(0)
       var count = 0


       while (!q.isEmpty()) {
           val now = q.poll()
           if (!visit[orderList[now]] && now != orderList[now]) {
               next[orderList[now]] = now
               continue
           }
           visit[now] = true
           count++

           if (next[now] != 0) q.add(next[now])
           mapList[now].forEach { i ->
               if (!visit[i]) q.add(i)
           }
       }
       return count == n
   }
}