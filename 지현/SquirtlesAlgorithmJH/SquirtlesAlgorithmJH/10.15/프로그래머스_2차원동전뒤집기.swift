//
//  main.swift
//  SquirtlesAlgorithmJH
//
//  Created by 김지현 on 10/14/24.
//

// ** 미해결 **
import Foundation
// beg + target을 xor 연산을 한 결과 배열을 모두 0으로 바꾸기

// 첫번째 시도 -> row, 또는 col의 첫번째 원소가 1일 때만 그 행/열을 바꿈
// 결과: 테케 4개 실패

// 두번째 시도 -> 해당 row에 1이 반 이상 차지할 때에만 그 열을 flip + 해당 col에 1이 존재하면 그 행을 flip
// 결과: 테케 2개 실패
// 고려한 예시 -> beg: [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0]], tar: [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1]]

// 세번째 시도 -> row 1이 반 이상 차지할 때 flip할 배열, 반 미만 차지할 때 flip할 배열 두개를 두고 결과가 더 작은 것 return
// 결과: 테케 1개 실패

func solution(_ beginning:[[Int]], _ target:[[Int]]) -> Int {
    var xorArray = xor(beginning, target)
    var xorArray2 = xorArray

    let rows = beginning.count
    let cols = beginning[0].count
    var cnt: Int = 0
    var cnt2: Int = 0

    for row in 0 ..< rows {
        // 첫번째 시도 -> if xorArray[row][0] == 1 {
      if xorArray[row].filter({ $0 == 1 }).count > cols / 2 {
            flipRow(&xorArray, row)
            cnt += 1
        } else {
            flipRow(&xorArray2, row)
            cnt2 += 1
        }
    }
    for col in 0 ..< cols {
        for row in 0 ..< rows {
            if xorArray[row][col] == 1 || xorArray2[row][col] == 1 {
                if xorArray[row][col] == 1 {
                    flipCol(&xorArray, col)
                    cnt += 1
                }
                if xorArray2[row][col] == 1 {
                    flipCol(&xorArray2, col)
                    cnt2 += 1
                }
                break
            }
        }
    }

    for row in 0 ..< rows {
        for col in 0 ..< cols {
            if xorArray[row][col] != 0 { cnt = -1 }
            if xorArray2[row][col] != 0 { cnt2 = -1}
        }
    }

    if cnt == -1 && cnt2 == -1 {
        return -1
    }  else if min(cnt, cnt2) == -1 {
        return max(cnt, cnt2)
    } else {
        return min(cnt, cnt2)
    }
}

private func xor(_ beginning:[[Int]], _ target:[[Int]]) -> [[Int]] {

    var xorArray = [[Int]]()
    for i in 0 ..< beginning.count {
        var row = [Int]()
        for j in 0 ..< beginning[0].count {
            row.append(beginning[i][j] ^ target[i][j])
        }
        xorArray.append(row)
    }
    return xorArray
}

private func flipRow(_ array: inout [[Int]], _ row: Int) {
    for i in 0 ..< array[row].count {
        array[row][i] = array[row][i] == 0 ? 1 : 0
    }
}

private func flipCol(_ array: inout [[Int]], _ col: Int) {
    for i in 0 ..< array.count {
        array[i][col] = array[i][col] == 0 ? 1: 0
    }
}
