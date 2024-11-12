def solution(storey):
    answer = 0
    while(storey>0) :
        btn = storey %10
        if(btn > 5) :
            answer += (10-btn)
            storey += (10-btn)
        elif(btn < 5) :
            answer += btn
            storey -= btn
        else:
            tmp = storey // 10
            if(tmp%10 >= 5) :
                answer += (10-btn)
                storey += (10-btn)
            else:
                answer += btn
                storey -= btn
        storey //= 10
    return answer
