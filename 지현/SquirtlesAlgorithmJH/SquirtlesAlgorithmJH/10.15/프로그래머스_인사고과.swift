//
//  main.swift
//  SquirtlesAlgorithmJH
//
//  Created by 김지현 on 10/11/24.
//

import Foundation

/*
1. 근태 + 동료 높은순으로 인센티브 차등 지급
2. 합이 동일하면 동석차, 동석차 만큼 다음 석차는 건너뜀 1등 두명, 바로 다음은 3등
3. 두 점수 모두 다른 임의의 사람보다 낮으면 인센 못받음
4. 완호는 첫번째 점수, 완호가 인센 못받으면 -1
*/

func solution(_ scores:[[Int]]) -> Int {
    let myScore = scores[0]

  // 1. 인센 받을 수 있는 사람 골라내기
    let sortedScores = scores.sorted {
        $0[0] > $1[0] || ($0[0] == $1[0] && $0[1] < $1[1])
      //  x, y 둘 다 내림차순으로 정렬
      // -> x 제일 큰 것, y 제일 큰 것을 max에서 가지게 되므로
      // 점점 항상 작을 수 밖에 없게 됨

      // x 내림차순으로 하되, x가 같을 때 y를 오름차순
      // -> [[4, 1], [3, 5], [2, 4]]
    }
    var secondMax = sortedScores[0][1]

    var passedScores: [Int] = []
    for score in sortedScores {
        if secondMax > score[1] {
            if score == myScore { return -1 }
        } else {
            passedScores.append(score[0] + score[1])
        }
        secondMax = max(secondMax, score[1])
    }

  // 2. 석차 매기기
    passedScores = passedScores.sorted(by: >)
    let rank = passedScores.firstIndex(where: { $0 == myScore.reduce(0,+) })!
    return rank + 1
}
