import sys

def solution(m, n, startX, startY, balls):

    answer = []


    for ball in balls:
        distance = sys.maxsize
        if startX != ball[0]:
            distance = min(distance, (startX - ball[0]) ** 2 + (startY+ball[1]) ** 2)
            distance = min(distance, (startX - ball[0]) ** 2 + (startY - 2*n + ball[1]) ** 2)
        else:
            if startY < ball[1]:
                distance = min(distance, (startX - ball[0]) ** 2 + (startY+ball[1]) ** 2)
            else:
                distance = min(distance, (startX - ball[0]) ** 2 + (startY - 2*n + ball[1]) ** 2)

        if startY != ball[1]:
            distance = min(distance, (startX + ball[0]) ** 2 + (startY-ball[1]) ** 2)
            distance = min(distance, (startX -2*m + ball[0]) ** 2 + (startY-ball[1]) ** 2)
        else:
            if startX < ball[0]:
                distance = min(distance, (startX + ball[0]) ** 2 + (startY-ball[1]) ** 2)
            else:
                distance = min(distance, (startX -2*m + ball[0]) ** 2 + (startY-ball[1]) ** 2)
        
        answer.append(distance)

        
    return answer