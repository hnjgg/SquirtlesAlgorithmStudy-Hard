// 프로그래머스 마법의 엘리베이터

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int storey)
{
    int answer = 0;

    while (storey != 0)
    {
        int digit = storey % 10; 
        storey /= 10;            

        if (digit > 5)
        {
            answer += 10 - digit;
            storey++;  
        }
        else if (digit < 5)
        {
            answer += digit;
        }
        else
        { 
            if (storey % 10 >= 5)
            {
                answer += 10 - digit;
                storey++;
            }
            else
            {
                answer += digit;
            }
        }
    }
    return answer;
}

int main()
{
    int storey;
    cin >> storey;
    cout << solution(storey) << endl;
    return 0;
}
