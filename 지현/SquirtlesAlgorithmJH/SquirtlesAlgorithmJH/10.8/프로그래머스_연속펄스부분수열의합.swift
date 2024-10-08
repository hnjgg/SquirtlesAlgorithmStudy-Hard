import Foundation

func solution(_ sequence:[Int]) -> Int64 {
    var negativePulse = [Int64]()
    var positivePulse = [Int64]()
    for (idx, num) in sequence.enumerated() {
        if idx % 2 == 0 {
            negativePulse.append(Int64(num * -1))
            positivePulse.append(Int64(num))
        } else {
            negativePulse.append(Int64(num))
            positivePulse.append(Int64(num * -1))
        }
    }

    let nPulseMax: Int64 = maxSubArray(negativePulse)
    let pPulseMax: Int64 = maxSubArray(positivePulse)
    return max(nPulseMax, pPulseMax)
}

// 카데인 알고리즘
func maxSubArray(_ nums: [Int64]) -> Int64 {
    guard !nums.isEmpty else { return 0 }

    var currentSum = nums[0]
    var maxSum = nums[0]

    for i in 1..<nums.count {
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)
    }

    return maxSum
}
