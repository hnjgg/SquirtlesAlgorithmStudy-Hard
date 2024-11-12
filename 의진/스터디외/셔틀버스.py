from collections import deque

def time2min(time):
    h, m = map(int, time.split(":"))
    minute = h * 60 + m
    return minute

def min2time(minute):
    h = minute // 60
    m = minute % 60

    h = str(h).zfill(2)
    m = str(m).zfill(2)
    return f"{h}:{m}"


def solution(n, t, m, timetable):
    timetable = deque(sorted(list(map(time2min, timetable))))
    bus_time = [540 + i * t for i in range(n)]

    
    for i, bus in enumerate(bus_time):
        cur_m = m
        while True:
            if not timetable: # 모두 다 타버렸다.
                break
            time = timetable.popleft()
            if time <= bus:
                cur_m -= 1
                if cur_m == 0 and i == len(bus_time) -1: # 마지막 자리를 앉았는데 그게 마지막 버스다 -> -1
                    return min2time(time-1)

                if cur_m == -1:
                    timetable.appendleft(time) # 버스에 가봤더니 자리가 없다. -> 다음 버스로
                    break
            else:
                timetable.appendleft(time) # 이 버스를 못 탄다. 다음 버스를 따져본다.
                break
            
        
    return min2time(bus_time[-1]) # 버스가 이미 다 태웠다.


        