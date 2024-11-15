// 프로그래머스 코딩 테스트 공부

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // INT_MAX: 2147483647, INT_MIN: -2147483648

using namespace std;

int solution(int alp, int cop, vector<vector<int>> problems)
{
    // 문제 해결을 위해 필요한 최대 alp, cop
    int maxalp = 0;
    int maxcop = 0;

    for (const auto &problem : problems)
    {
        maxalp = max(maxalp, problem[0]); // alp_req, . . . .
        maxcop = max(maxcop, problem[1]); // . cop_req, . . .
    }

    // 최대 alp, cop나오면 종로
    alp = min(alp, maxalp);
    cop = min(cop, maxcop);

    vector<vector<int>> dp


}

int main()
{
    int alp, cop, n; // 문제 갯수
    cin >> alp >> cop >> n;

    vector<vector<int>> problems(n, vector<int>(5)); // alp_req, cop_req, alp_rwd, cop_rwd, cost

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cin >> problems[i][j]; // problem[0][0] problem[0][1] problem[0][2] problem[0][3] problem[0][4]
        }
    }

    cout << solution(alp, cop, problems) << endl;
    return 0;
}

