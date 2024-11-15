// 프로그래머스 보석쇼핑 카카오인턴
// 투포인터
#include <iostream>
#include <vector>
#include <unordered_map> // unordered_map<string, int> key-value를 저장하기 위해
#include <set>

using namespace std;

vector<int> solution(vector<string> gems)
{
    set<string> uniqueGems(gems.begin(), gems.end());
    int totalGems = uniqueGems.size();

    unordered_map<string, int> gemCount;
    int start = 0, end = 0;
    int minLength = gems.size() + 1;
    int minStart = 0;

    // 1. end point를 움직여! 구간을 확장하며 gemCount를 채우며 보석을 모두 포함
    while (end < gems.size())
    {
        gemCount[gems[end]]++; // key-value에 접근하기 위해 [ ]사용
        end++;

        // 2. start point를 움직어! 보석이 모두 포함됐다면 구간을 축소 시작
        while (gemCount.size() == totalGems)
        {
            if (end - start < minLength)
            {
                minLength = end - start;
                minStart = start;
            }

            // 3. start보석의 개수를 줄이다가 0이면 gemCount에서 해당 보석 제거
            gemCount[gems[start]]--;
            if (gemCount[gems[start]] == 0)
            {
                gemCount.erase(gems[start]);
            }
            start++; // start를 오른쪽으로 움직이며 구간을 축소해야하기에 ++
        }
    }
    return {minStart + 1, minStart + minLength};
}

int main()
{
    int n;
    cin >> n;
    vector<string> gems(n);

    for (int i = 0; i < n; i++)
    {
        cin >> gems[i];
    }
    vector<int> result = solution(gems);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}