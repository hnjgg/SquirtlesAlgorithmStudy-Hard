Todo : Trie 자료구조 공부해서 해설 안보고 풀어보기
///*
//
//1.trieNode data class 만들기
//2.단어를 트라이에 삽입해 각 문자에 대한 rest값 갱신
//3. checkCount 함수는 단어를 검색할 때 필요한 최소 문자 수를 계산
//4. solution 함수는 주어진 단어 리스트를 트라이에 삽입한 후, 각 단어를 검색하여 필요한 최소 문자 수를 합산
//
//입력
//검색에 사용되는 중복없는 단어 N개
//모든 단어는 소문자, 단어의 수 N과 단어들의 길이의 총합 L의 범위는
//2 <= N <= 100,000
//2 <= L <= 1,000,000
//
//"go","gone","guild"
//
//7
//
//"abc","def","ghi","jklm"
//4
//
//
//출력
//단어를 찾을 때 입력해야할 총 문자수를 return
// */
//
//
//class Trie {
//    data class TrieNode(var rest: Int = 0, var isWord: Boolean = false, val children: MutableMap<Char, TrieNode> = mutableMapOf())
//    //rest: 해당 노드를 지나가는 단어의 수 , isWord: 현재 노드가 단어의 끝인지 여부, children: 현재 노드의 자식 노드를 저장하는 맵
//    private val root = TrieNode()
//
//    fun insert(word: String) {
//        var curr = root
//
//        for (i in word) {
//            if (!curr.children.containsKey(i)) {
//                curr.children[i] = TrieNode(1)
//            } else {
//                curr.children[i]!!.rest++
//            }
//            curr = curr.children[i]!!
//        }
//        curr.isWord = true
//    }
//
//    fun checkCount(word: String): Int {
//        //각 문자를 순회하며, 현재 노드의 rest 값이 1이면 curCount를 반환
//        //그렇지 않으면, 현재 문자의 자식 노드로 이동하고 curCount를 증가
//        //모든 문자를 순회하면 단어의 길이를 반환
//        var curChar = root
//        var curCount = 0
//
//        for (c in word) {
//            if (curChar.rest == 1) return curCount
//            curChar = curChar.children[c]!!
//            curCount++
//        }
//
//        return word.length
//    }
//}
//
//fun solution(words: List<String>): Int {
//    val trie = Trie()
//    words.forEach { word -> trie.insert(word) }
//    return words.fold(0) { pre, cur -> pre + trie.checkCount(cur) }
//}
//
//fun main() = with(System.`in`.bufferedReader()) {
//    val words = readLine().split(",")
//    val answer = solution(words)
//    println(answer)
//}