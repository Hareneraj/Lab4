

import time
from hal import hal_input_switch as SWITCH
from hal import hal_led as LED

def main():
    LED.init()
    SWITCH.init()
    level = 0 #LED Blinking starts with turn on
    start_time = time.time()  # Record the start time
    while(True):
        switch_pos = SWITCH.read_slide_switch()
        if (switch_pos==0): #Slide switch at right position
            if (time.time() - start_time) > 5:
                LED.set_output(24, 0)  # Turn off the LED after 5 seconds
                break  # Exit the loop 
            LED.set_output(24, level)
            level = not level #Toggle level for next loop
            time.sleep(0.05)
        else:
            LED.set_output(24,0) #Off the LED
            time.sleep(0.05) #Add a delay to reduce frequency of checking slide switch
    return 1

if __name__ == "__main__":
    main()