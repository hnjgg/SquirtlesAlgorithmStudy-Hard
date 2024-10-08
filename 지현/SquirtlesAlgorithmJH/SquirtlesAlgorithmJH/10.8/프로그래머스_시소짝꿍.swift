import Foundation

func solution(_ weights:[Int]) -> Int64 {
  var answer: Int64 = 0

  var dict: [Int: Int64] = [:]
  for weight in weights {
    dict[weight, default: 0] += 1
  }
  for i in dict where i.value >= 2 {
    answer += i.value * (i.value - 1) / 2
  }

  let setWeights = Set(weights)
  for weight in setWeights {
    // ^^ .. 소수점 처리 때문인 것을 발견 못하고 테케4~11 계속 통과 못해서 헤맨 부분
    if (weight*2) % 3 == 0 && weights.contains(weight * 2/3) {
      answer += dict[weight]! * dict[weight * 2/3]!
    }
    if weight % 2 == 0 && weights.contains(weight * 1/2) {
      answer += dict[weight]! * dict[weight * 1/2]!
    }
    if (weight*3) % 4 == 0 && weights.contains(weight * 3/4) {
      answer += dict[weight]! * dict[weight * 3/4]!
    }
  }
  return answer
}
