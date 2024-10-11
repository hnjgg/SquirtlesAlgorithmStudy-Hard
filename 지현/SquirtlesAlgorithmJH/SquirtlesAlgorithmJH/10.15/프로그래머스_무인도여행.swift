//
//  main.swift
//  SquirtlesAlgorithmJH
//
//  Created by 김지현 on 10/11/24.
//

import Foundation

func solution(_ maps:[String]) -> [Int] {
  // x == 바다
  // 숫자 == 식량이 있는 무인도
  // 무인도의 숫자를 모두 합하면 최대 며칠 머물 수 있는지를 나타냄
  // 머물 수 있는 날 수를 오름차순 배열로 return
  // 무인도가 없으면 [-1] 리턴

  // R최대 100 C최대 100 : 10000
  let maps2 = maps.map { Array($0) }
  let R = maps.count
  let C = maps[0].count

  var visited = Array(
    repeating: Array(repeating: false, count: C),
    count: R
  )

  var answer: [Int] = []
  var day: Int = 0
  func dfs(x: Int, y: Int) {
    if x < 0 || y < 0 || x >= R || y >= C || visited[x][y] || maps2[x][y] == "X"
    { return }
    visited[x][y] = true
    day += Int(String(maps2[x][y]))!

    dfs(x: x, y: y+1)
    dfs(x: x, y: y-1)
    dfs(x: x+1, y: y)
    dfs(x: x-1, y: y)
  }

  for r in 0 ..< R {
    for c in 0 ..< C {
      dfs(x: r, y: c)
      if day != 0 {
        answer.append(day)
        day = 0
      }
    }
  }

  if answer.isEmpty {
    return [-1]
  } else {
    return answer.sorted(by: <)
  }
}

// 점수 +3
//solution(["X591X", "X1X5X", "X231X", "1XXX1"])
