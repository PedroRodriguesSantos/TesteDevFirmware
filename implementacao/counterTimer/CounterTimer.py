import time

timer_routine_light_sensor = 0
timer_routine_distance_sensor = 0
timer_routine_battery_sensor = 0

max_timer_sensors = 50

def counterTimerProcess(ID):
    global timer_routine_light_sensor
    global timer_routine_distance_sensor
    global timer_routine_battery_sensor

    if ID == 0:
        return timer_routine_light_sensor
    
    elif ID == 1:
        return timer_routine_distance_sensor
    
    elif ID == 2:
        return timer_routine_battery_sensor
    
    else:
        timer_routine_light_sensor += 1
        timer_routine_distance_sensor += 1
        timer_routine_battery_sensor += 1
        time.sleep(0.1)

    

    

    
    


